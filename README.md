# YouTube Comments Engagement & Sentiment Analysis

Exploratory analysis of **4,148 YouTube comments (15 columns)** using Python and pandas in Google Colab.

## Data source

The dataset was collected by scraping comments from YouTube videos.

- **Source:** YouTube comments
- **Collection method:** Web scraping
- **Dataset size:** 4,148 comments
- **Coverage:** 29 channels and 49 videos
- **License:** Not specified
- **Unit of analysis:** One YouTube comment

The exact scraping tool, collection criteria, and sampling method are not documented. Findings describe this dataset only and should not be generalized to all YouTube users, channels, or videos.

## Contents

- `project1_youtube_comments_analysis.ipynb`: Full analysis (data cleaning, descriptive statistics, charts, scaling experiment, and machine learning preview)
- `report.pdf`: Main findings, recommendations, and limitations
- `tables/`: Data dictionary, cleaning log, dataset summary, and scaling results
- `charts/`: Figures used in the report

## Key results

1. **Engagement is highly uneven:** Median likes and replies per comment are both 0, although the most-liked comment received 21,108 likes.
2. **Positive sentiment is the most common:** 1,737 comments were classified as positive.
3. **Dataset coverage:** The analysis includes comments from 29 YouTube channels and 49 videos, allowing comparisons across channels and content types.

## Project Structure

```text
social-media-engagement-analysis/
├── README.md
└── Project 1/
    ├── Project 1.ipynb
    ├── report.pdf
    ├── charts/
    │   ├── chart1_sentiment_counts.png
    │   ├── chart2_median_likes_by_channel.png
    │   ├── chart3_likes_vs_comments.png
    │   ├── chart4_likes_distribution.png
    │   └── chart5_comments_per_month.png
    └── tables/
        ├── data_dictionary.csv
        ├── cleaning_log.csv
        ├── dataset_summary.csv
        └── scaling_results.csv
```

## How to run

1. Open the notebook in Google Colab.
2. Run the cells in order.
3. Upload the YouTube comments CSV file when prompted.
4. Run all remaining cells to perform the analysis and generate the outputs.

## Limitations

The dataset does not include video views, impressions, or channel audience sizes, so actual engagement rates cannot be calculated. Sentiment classifications may also contain errors. The results are descriptive and do not establish causal relationships.
