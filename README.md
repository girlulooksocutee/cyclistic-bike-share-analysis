# cyclistic-bike-share-analysis
Cyclistic bike-share analysis using Python and pandas to compare casual riders and annual members.

# Cyclistic Bike-Share Analysis

## Project Overview

This project analyzes Cyclistic bike-share trip data to understand how casual riders and annual members use the service differently.

Cyclistic is a fictional bike-share company used in the Google Data Analytics Capstone case study. The analysis uses public Divvy bike-share data from **Q1 2019** and **Q1 2020**.

The goal of the project is to identify meaningful riding patterns that could help support marketing strategies aimed at converting casual riders into annual members.

---

## Business Question

**How do annual members and casual riders use Cyclistic bikes differently?**

The analysis focuses on differences in:

- Ride duration
- Day-of-week behavior
- Number of rides
- Overall riding patterns

---

## Tools Used

- Python
- pandas
- VS Code
- CSV
- GitHub

---

## Data Preparation

The 2019 and 2020 datasets used different column names and formats, so the data was cleaned and standardized before analysis.

The main preparation steps included:

- Renaming 2019 columns to match the 2020 dataset
- Converting `ride_id` and `rideable_type` to consistent data types
- Combining both datasets into one DataFrame
- Removing columns that were not consistently available in both datasets
- Standardizing rider categories:
  - `Subscriber` → `member`
  - `Customer` → `casual`
- Converting ride start and end times to datetime format
- Creating new columns for:
  - Date
  - Month
  - Day
  - Year
  - Day of week
- Calculating ride duration using a new `ride_length` variable
- Removing invalid records such as negative ride durations and quality-control rides

---

## Analysis

The cleaned dataset was used to compare the behavior of casual riders and annual members.

The analysis included:

- Descriptive statistics for ride duration
- Mean, median, minimum, and maximum ride duration by rider type
- Average ride duration by rider type and day of week
- Number of rides by rider type and weekday
- Creation of summary data for further analysis and visualization

---

## Key Findings

The analysis revealed several differences between casual riders and annual members:

- **Casual riders generally took longer rides than annual members.**
- Differences in ride duration remained visible across multiple days of the week.
- Member and casual riding behavior varied by weekday.
- The patterns suggest that casual riders and members may use bike-share services for different purposes.

These differences could help Cyclistic better understand when and how to target casual riders with membership-focused marketing.

---

## Recommendations

Based on the analysis, Cyclistic could:

1. **Target casual riders during periods of high casual usage** with annual membership promotions.
2. **Highlight the financial and convenience benefits of membership** to riders who use Cyclistic frequently or take longer rides.
3. **Use day-of-week riding patterns to create more focused digital marketing campaigns** for casual riders.

---

## Data Limitations

This analysis uses only **Q1 2019 and Q1 2020** data rather than a complete year of trips.

Because of this, the findings should not be treated as representative of full-year seasonal behavior. A future analysis using twelve consecutive months of data could provide a more complete view of Cyclistic rider patterns.

---

## Data Source

This project uses public Divvy bike-share trip data:
- Divvy Trips 2019 Q1
- Divvy Trips 2020 Q1

The original raw datasets are not included in this repository due to file size.

## Repository Structure

```text
cyclistic-bike-share-analysis/
│
├── README.md
├── cyclistic_analysis.py
│
├── data/
│   └── avg_ride_length.csv
│
└── charts/
    └── visualizations
