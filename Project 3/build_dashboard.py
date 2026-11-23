import json
d = json.load(open("results.json"))
import os
if os.path.exists("ads_results.json"): d["ads"] = json.load(open("ads_results.json"))
html = r'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Audience & Campaign Intelligence Engine</title>
<style>
:root{box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);--bg:#faf8f5;--card:#fff;--tx:#1f2328;--mu:#6b7280;--ac:#0f766e;--bd:#e5e1da;--wa:#b45309}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#15181b;--card:#1e2327;--tx:#e8eaed;--mu:#9aa3ad;--ac:#2dd4bf;--bd:#2f363c;--wa:#fbbf24}}
:root[data-theme="dark"]{--bg:#15181b;--card:#1e2327;--tx:#e8eaed;--mu:#9aa3ad;--ac:#2dd4bf;--bd:#2f363c;--wa:#fbbf24}
html{scroll-padding-top:env(safe-area-inset-top,0px)}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.5 system-ui,-apple-system,Segoe UI,sans-serif}
main{max-width:980px;margin:0 auto;padding:20px 16px 48px}
h1{font-size:22px;margin:0 0 4px}.sub{color:var(--mu);margin:0 0 14px}
.note{background:var(--card);border:1px solid var(--wa);color:var(--wa);border-radius:8px;padding:8px 12px;font-size:13px;margin-bottom:14px}
.kpis{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:14px}
.kpi,.card{background:var(--card);border:1px solid var(--bd);border-radius:10px;padding:12px 14px}
.kpi b{display:block;font-size:22px}.kpi span{color:var(--mu);font-size:12px}
nav{display:flex;gap:6px;overflow-x:auto;margin-bottom:12px;padding-bottom:4px}
nav button{white-space:nowrap;border:1px solid var(--bd);background:var(--card);color:var(--tx);padding:7px 12px;border-radius:20px;font:inherit;cursor:pointer}
nav button.on{background:var(--ac);color:#fff;border-color:var(--ac)}
section{display:none}section.on{display:block}
.row{display:grid;grid-template-columns:150px 1fr 90px;gap:10px;align-items:center;margin:6px 0;font-size:13px}
.bar{height:14px;background:var(--bd);border-radius:7px;overflow:hidden}.bar i{display:block;height:100%;background:var(--ac)}
.row em{font-style:normal;color:var(--mu);text-align:right}
.wrap{overflow-x:auto}table{border-collapse:collapse;width:100%;font-size:13px}
th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--bd);white-space:nowrap}th{color:var(--mu);font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}
.tag{display:inline-block;background:var(--bd);border-radius:4px;padding:1px 6px;font-size:12px;margin:2px 3px 0 0}
.ex{color:var(--mu);font-size:13px;margin:2px 0}h3{margin:0 0 6px;font-size:16px}h2{font-size:17px;margin:0 0 8px}
select{font:inherit;padding:5px;background:var(--card);color:var(--tx);border:1px solid var(--bd);border-radius:6px}
.rec{border-left:3px solid var(--ac);padding:4px 0 4px 12px;margin:10px 0}.rec small{color:var(--mu);display:block}
</style></head><body><main>
<h1>Audience &amp; Campaign Intelligence Engine</h1>
<p class="sub">Women's lawn suits · Instagram, TikTok, Facebook · clustering-based audience segments</p>
<div class="note">Demonstration data: all posts and comments are simulated (is_simulated = true). Replace with permitted real data to get real findings.</div>
<div class="kpis" id="kpis"></div>
<nav id="nav"></nav><div id="views"></div>
<script>
const D=__DATA__;
const fmt=n=>Math.round(n).toLocaleString();
const bars=(rows,max,f)=>rows.map(r=>`<div class="row"><span>${r[0]}</span><div class="bar"><i style="width:${r[1]/max*100}%"></i></div><em>${f(r[1])}</em></div>`).join('');
const K=[[fmt(D.n_posts),'posts'],[fmt(D.n_comments),'comments'],[D.clusters.length,'audience clusters'],[D.purity+'%','cluster purity vs labels'],[D.n_unusual,'unusual posts']];
kpis.innerHTML=K.map(k=>`<div class="kpi"><b>${k[0]}</b><span>${k[1]}</span></div>`).join('');
const perf=[...D.perf];
const tabs={
'1 · Content':()=>{const m=Math.max(...perf.map(p=>p.avg_views));
 return `<div class="card"><h2>Which content attracts attention?</h2>${bars(perf.map(p=>[p.content_type,p.avg_views]),m,fmt)}<p class="sub">Average views per post</p>
 <div class="wrap"><table><tr><th>Content type</th><th>Posts</th><th>Likes</th><th>Comments</th><th>Shares</th><th>Eng. rate</th></tr>${perf.map(p=>`<tr><td>${p.content_type}</td><td>${p.posts}</td><td>${fmt(p.avg_likes)}</td><td>${p.avg_comments.toFixed(1)}</td><td>${fmt(p.avg_shares)}</td><td>${(p.eng_rate*100).toFixed(1)}%</td></tr>`).join('')}</table></div>
 <h2 style="margin-top:14px">By platform</h2>${bars(D.plat.map(p=>[p.platform,p.avg_views]),Math.max(...D.plat.map(p=>p.avg_views)),fmt)}</div>`},
'2 · Wants':()=>{const t=Object.entries(D.topics).sort((a,b)=>b[1]-a[1]);
 return `<div class="card"><h2>What does the audience want?</h2>${bars(t,t[0][1],v=>v+'%')}<p class="sub">Share of comments by topic</p>
 <h2>Language mix</h2>${bars(Object.entries(D.langs),60,v=>v+'%')}</div>`},
'3 · Unusual':()=>`<div class="card"><h2>Which marketing patterns are unusual?</h2><p class="sub">Isolation Forest on engagement features, standardised within content type and platform, so each post is compared to comparable posts. Treat as leads to investigate.</p>
 <div>${Object.entries(D.reasons).map(r=>`<span class="tag">${r[0]}: ${r[1]}</span>`).join('')}</div>
 <div class="wrap"><table><tr><th>Post</th><th>Platform</th><th>Type</th><th>Views</th><th>Likes</th><th>Comments</th><th>Shares</th><th>Why flagged</th></tr>${D.unusual.map(u=>`<tr><td>${u.post_id}</td><td>${u.platform}</td><td>${u.content_type}</td><td>${fmt(u.views)}</td><td>${fmt(u.likes)}</td><td>${u.comments}</td><td>${u.shares}</td><td>${u.reason}</td></tr>`).join('')}</table></div><p class="sub">Top 15 of ${D.n_unusual} shown.</p></div>`,
'4 · Segments':()=>`<div class="card"><h2>Which audience needs should the brand address?</h2><p class="sub">TF-IDF (word + character n-grams) → KMeans, k=${D.clusters.length}. Purity = how much of each cluster matches the manual topic label.</p></div><div class="grid" style="margin-top:12px">${D.clusters.map(c=>`<div class="card"><h3>${c.label}</h3><div class="sub">${fmt(c.size)} comments · ${c.share}% · purity ${c.purity}%</div>${c.keywords.map(k=>`<span class="tag">${k}</span>`).join('')}<div style="margin-top:6px">${c.examples.slice(0,4).map(e=>`<p class="ex">“${e}”</p>`).join('')}</div></div>`).join('')}</div>`,
'5 · Actions':()=>`<div class="card"><h2>What should the marketing team do next?</h2>${D.recs.map(r=>`<div class="rec"><b>${r.area}:</b> ${r.action}<small>Evidence: ${r.evidence}</small></div>`).join('')}</div>`,
'6 · Ad performance':()=>{const A=D.ads;if(!A)return '<div class="card">No ad data loaded.</div>';const o=A.overall;
 const tbl=(rows,key)=>`<div class="wrap"><table><tr><th>${key}</th><th>Spend</th><th>CTR %</th><th>CPC</th><th>CVR %</th><th>ROAS</th></tr>${rows.map(r=>`<tr><td>${r[key]}</td><td>${fmt(r.spend)}</td><td>${r.ctr}</td><td>${r.cpc}</td><td>${r.cvr}</td><td><b>${r.roas}</b></td></tr>`).join('')}</table></div>`;
 return `<div class="card"><h2>Campaign performance (Project 2 data)</h2><p class="sub">${fmt(o.rows)} ad rows, ${A.span[0]} to ${A.span[1]} · overall CTR ${o.ctr}% · CVR ${o.cvr}% · ROAS ${o.roas}</p>${bars(A.campaign.map(c=>[c.campaign,c.roas]),Math.max(...A.campaign.map(c=>c.roas)),v=>v+'x')}<p class="sub">ROAS by campaign</p>${tbl(A.campaign,'campaign')}</div>
 <div class="card" style="margin-top:12px"><h2>By city</h2>${tbl(A.city,'city')}<h2 style="margin-top:14px">By device</h2>${tbl(A.device,'device')}<h2 style="margin-top:14px">By age</h2>${tbl(A.age,'age')}</div>
 <div class="card" style="margin-top:12px"><h2>Audience segment clusters</h2><p class="sub">Campaign × city × age segments grouped by KMeans on CTR, CVR, ROAS and CPC.</p><div class="grid">${A.clusters.map(c=>`<div class="card"><h3>${c.name}</h3><div class="sub">${c.segments} segments · spend ${fmt(c.spend)}</div><span class="tag">ROAS ${c.roas}</span><span class="tag">CTR ${c.ctr}%</span><span class="tag">CVR ${c.cvr}%</span><span class="tag">CPC ${c.cpc}</span>${c.top.map(t=>`<p class="ex">${t}</p>`).join('')}</div>`).join('')}</div></div>
 <div class="card" style="margin-top:12px"><h2>Unusual days (${A.n_unusual} flagged)</h2><div class="wrap"><table><tr><th>Date</th><th>Campaign</th><th>Spend</th><th>CTR %</th><th>CPC</th><th>ROAS</th><th>Why</th></tr>${A.unusual.map(u=>`<tr><td>${u.date}</td><td>${u.campaign}</td><td>${fmt(u.spend)}</td><td>${u.ctr}</td><td>${u.cpc}</td><td>${u.roas}</td><td>${u.reason}</td></tr>`).join('')}</table></div></div>
 <div class="card" style="margin-top:12px"><h2>Budget actions</h2>${A.recs.map(r=>`<div class="rec">${r}</div>`).join('')}</div>`}
};
const names=Object.keys(tabs);
nav.innerHTML=names.map((n,i)=>`<button data-i="${i}">${n}</button>`).join('');
views.innerHTML=names.map((n,i)=>`<section id="s${i}">${tabs[n]()}</section>`).join('');
function show(i){document.querySelectorAll('section').forEach((s,j)=>s.classList.toggle('on',i===j));document.querySelectorAll('nav button').forEach((b,j)=>b.classList.toggle('on',i===j));try{history.replaceState(null,'','#t'+i)}catch(e){}}
nav.onclick=e=>{if(e.target.dataset.i!==undefined)show(+e.target.dataset.i)};
show(Math.min(names.length-1,Math.max(0,parseInt((location.hash||'#t0').slice(2))||0)));
</script></main></body></html>'''
open("dashboard.html","w",encoding="utf-8").write(html.replace("__DATA__",json.dumps(d,ensure_ascii=False)))
