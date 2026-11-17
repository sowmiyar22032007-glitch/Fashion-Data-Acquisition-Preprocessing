# Fashion Data Acquisition and Preprocessing

Week 2 internship project for the Junior Data Science Analyst role.

## Objective
Document a repeatable workflow for acquiring public fashion/retail data and preparing it for analysis.

## Folder structure
- `data/raw/`: original downloaded files (do not modify)
- `data/processed/`: cleaned output
- `src/preprocess.py`: reusable preprocessing example
- `reports/`: report and source notes

## Data sources to explore
- Google Trends: https://trends.google.com/trends/
- Kaggle Datasets: https://www.kaggle.com/datasets
- UCI Online Retail: https://archive.ics.uci.edu/datasets?search=Online+Retail
- Visuelle 2.0: https://humaticslab.github.io/forecasting/visuelle

Check each dataset's licence and terms before downloading or redistributing it. UCI Online Retail is general online retail data and is not specifically a fashion-only dataset.

## Setup
```bash
pip install -r requirements.txt
```

Place a permitted CSV file at `data/raw/retail_transactions.csv`, then run:
```bash
python src/preprocess.py
```

The script is a template. Update column names and business rules to match the selected dataset. Review returns, missing values and unusual prices before excluding any records.
