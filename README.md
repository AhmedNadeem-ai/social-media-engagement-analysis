# Social Media Engagement & Sentiment Analysis

Exploratory analysis of 2,260 social media posts (13 columns) in pandas, run in Google Colab.

## Data source
mrudukp/social-media-sentiment-analysis on GitHub (https://github.com/mrudukp/social-media-sentiment-analysis).
License: not stated. Collection method: not stated; possibly synthetic. Findings describe this dataset only,
not any real brand or country.

## Contents
- `project1_social_media_analysis.ipynb`: full analysis (cleaning, statistics, charts, scaling test, ML preview)
- `report.pdf`: findings, recommendation, limitation
- `tables/`: data dictionary, cleaning log, summary and scaling results
- `charts/`: figures used in the report

## Key results
1. TikTok and Instagram posts get more likes than LinkedIn and Facebook posts (median likes: TikTok 44, Instagram 37, Facebook 26, LinkedIn 20).
2. The ranking holds per follower: median engagement per follower is TikTok 0.0346 vs LinkedIn 0.0124.


## Project Structure

```text
social-media-engagement-analysis/
├── README.md
├── project1_social_media_analysis.ipynb
├── report.pdf
├── charts/
│   ├── chart1_sentiment_counts.png
│   ├── chart2_median_likes_by_platform.png
│   ├── chart3_likes_vs_comments.png
│   ├── chart4_likes_distribution.png
│   └── chart5_posts_per_month.png
└── tables/
    ├── data_dictionary.csv
    ├── cleaning_log.csv
    ├── dataset_summary.csv
    ├── stats_by_platform.csv
    └── scaling_results.csv
```

## How to run
Open the notebook in Google Colab, run all cells, and upload the CSV when asked.
