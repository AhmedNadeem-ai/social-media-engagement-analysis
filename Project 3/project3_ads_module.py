"""Adds Project 2 ad-performance data (cleaned_data.csv) to the Project 3 engine.
Run: python project3_ads_module.py -> ads_results.json (read by build_dashboard.py)"""
import json, numpy as np, pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("cleaned_data.csv", parse_dates=["date"])
def kpis(g):
    s = g[["impressions", "clicks", "spend", "conversions", "revenue"]].sum()
    return pd.Series(dict(rows=len(g), impressions=s.impressions, spend=s.spend, revenue=s.revenue,
        ctr=s.clicks / s.impressions * 100, cpc=s.spend / max(s.clicks, 1), cvr=s.conversions / max(s.clicks, 1) * 100,
        roas=s.revenue / max(s.spend, 1), cpa=s.spend / s.conversions if s.conversions else np.nan))
def by(col): return df.groupby(col).apply(kpis, include_groups=False).round(2).reset_index().to_dict("records")
overall = kpis(df).round(2).to_dict()

# Audience-need clusters: campaign x city x age segments, clustered on performance profile
seg = df.groupby(["campaign", "city", "age"]).apply(kpis, include_groups=False).reset_index()
seg = seg[seg.rows >= 20].copy()
F = np.log1p(seg[["ctr", "cvr", "roas", "cpc"]].clip(lower=0))
km = KMeans(n_clusters=4, n_init=10, random_state=7).fit(StandardScaler().fit_transform(F))
seg["cluster"] = km.labels_
prof = seg.groupby("cluster")[["ctr", "cvr", "roas", "cpc"]].mean()
ranked = prof.roas.sort_values(ascending=False).index.tolist()
names = dict(zip(ranked, ["Top performers", "Solid core", "Underperformers", "Budget drains"]))
clusters = []
for c in prof.index:
    s = seg[seg.cluster == c]
    clusters.append(dict(name=names[c], segments=len(s), spend=round(s.spend.sum()), ctr=round(prof.loc[c, "ctr"], 2),
        cvr=round(prof.loc[c, "cvr"], 2), roas=round(prof.loc[c, "roas"], 2), cpc=round(prof.loc[c, "cpc"], 1),
        top=[f"{r.campaign} · {r.city} · {r.age}" for r in s.sort_values("spend", ascending=False).head(3).itertuples()]))
clusters.sort(key=lambda d: -d["roas"])

# Unusual days: each campaign's daily ROAS/CTR/CPC vs its own normal
day = df.groupby(["date", "campaign"]).apply(kpis, include_groups=False).reset_index()
Z = day.groupby("campaign")[["ctr", "cpc", "cvr", "roas"]].transform(lambda s: (s - s.mean()) / (s.std() + 1e-9))
iso = IsolationForest(contamination=0.03, random_state=7).fit(Z)
day["score"] = -iso.score_samples(Z); day["flag"] = iso.predict(Z) == -1
med = day.groupby("campaign")[["ctr", "cpc", "roas"]].transform("median")
def why(i, r):
    m = med.loc[i]
    if r.roas > 2 * m.roas: return "ROAS far above normal"
    if r.roas < 0.4 * m.roas: return "ROAS collapsed"
    if r.cpc > 1.6 * m.cpc: return "Cost per click spiked"
    if r.ctr < 0.6 * m.ctr: return "CTR dropped"
    return "Mixed pattern vs its norm"
unusual = [dict(date=str(r.date.date()), campaign=r.campaign, spend=round(r.spend), ctr=round(r.ctr, 2),
    cpc=round(r.cpc, 1), roas=round(r.roas, 2), reason=why(i, r)) for i, r in day[day.flag].sort_values("score", ascending=False).head(12).iterrows()]

camp = pd.DataFrame(by("campaign")).sort_values("roas", ascending=False)
city = pd.DataFrame(by("city")).sort_values("roas", ascending=False)
recs = [f"Shift budget toward {camp.iloc[0].campaign} (ROAS {camp.iloc[0].roas}) and review {camp.iloc[-1].campaign} (ROAS {camp.iloc[-1].roas}).",
        f"Best city on return: {city.iloc[0].city} (ROAS {city.iloc[0].roas}); weakest: {city.iloc[-1].city} ({city.iloc[-1].roas}).",
        f"Revisit the '{clusters[-1]['name']}' segments, which hold {clusters[-1]['spend']:,} of spend at ROAS {clusters[-1]['roas']}."]
json.dump(dict(overall=overall, campaign=camp.to_dict("records"), city=city.to_dict("records"), device=by("device"),
    age=by("age"), gender=by("gender"), clusters=clusters, unusual=unusual, n_unusual=int(day.flag.sum()), recs=recs,
    span=[str(df.date.min().date()), str(df.date.max().date())]), open("ads_results.json", "w"), default=float, indent=1)
print(overall); print(camp[["campaign", "ctr", "cvr", "roas"]].to_string()); print(city[["city", "roas"]].to_string())
for c in clusters: print(c)
print(unusual[:3])
