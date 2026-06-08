# AI Excel Analyst

A Streamlit-based data profiling and reporting tool that helps users quickly analyze CSV datasets, identify data quality issues, generate insights, and export professional PDF reports.

---

## Overview

AI Excel Analyst is an automated data analysis dashboard built using Python, Streamlit, Pandas, Matplotlib, and ReportLab.

The application enables users to upload CSV files and instantly receive:

* Dataset statistics
* Missing value analysis
* Data quality assessment
* Correlation analysis
* Automated findings
* Actionable recommendations
* Downloadable PDF reports

The goal of the project is to reduce the time required for exploratory data analysis (EDA) and dataset profiling.

---

## Features

### Dataset Preview

* Displays uploaded dataset
* Shows first few records for quick inspection

### Dataset Metrics

* Total rows
* Total columns

### Data Type Detection

* Automatically identifies data types of each column

### Summary Statistics

* Mean
* Median
* Standard deviation
* Minimum and maximum values

### Missing Value Analysis

* Column-wise missing value count
* Missing value visualization using bar charts

### Numeric Column Detection

* Automatically identifies numeric columns for analysis

### Interactive Visualization

* Histogram generation for selected numeric columns
* Distribution analysis

### Automated Insights

* Mean vs median comparison
* Distribution pattern detection
* Skewness identification

### Dataset Health Score

* Calculates overall dataset completeness
* Detects duplicate rows

### Key Findings Generation

* Identifies columns with highest missing values
* Detects duplicate records
* Highlights identifier columns
* Reports distribution characteristics

### Executive Summary

* Automatically generates a concise dataset summary

### Column Type Detection

* Identifier columns
* Numeric columns
* Text/Categorical columns

### Correlation Analysis

* Generates correlation matrix for numerical features

### Recommendations Engine

* Suggests removal of highly incomplete columns
* Highlights potential outlier issues
* Recommends preprocessing steps

### PDF Report Generation

* Exports:

  * Executive Summary
  * Key Findings
  * Recommendations
* Includes report generation timestamp

---

## Technology Stack

| Technology | Purpose                 |
| ---------- | ----------------------- |
| Python     | Core Programming        |
| Streamlit  | Web Application         |
| Pandas     | Data Processing         |
| Matplotlib | Data Visualization      |
| ReportLab  | PDF Report Generation   |
| BytesIO    | In-Memory File Handling |

---

## Project Workflow

```text
Upload CSV
      ↓
Data Profiling
      ↓
Data Quality Analysis
      ↓
Insights Generation
      ↓
Recommendations
      ↓
PDF Report Export
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sureyachandranv/AI-Excel-Analyst.git
cd AI-Excel-Analyst
```

Install dependencies:

```bash
pip install streamlit pandas matplotlib reportlab
```

Run the application:

```bash
streamlit run app.py
```

---

## Sample Use Cases

* Exploratory Data Analysis (EDA)
* Data Quality Assessment
* Student Data Science Projects
* Dataset Validation
* CSV Dataset Inspection
* Preprocessing Preparation for Machine Learning

---

## Future Improvements

* AI-powered natural language insights using LLMs
* Interactive correlation heatmaps
* Outlier detection module
* Multi-file analysis
* Excel (.xlsx) support
* Automated data cleaning suggestions

---

## Key Learning Outcomes

This project demonstrates practical experience with:

* Data Analysis
* Data Visualization
* Data Profiling
* Streamlit Application Development
* PDF Generation
* File Handling
* Data Quality Assessment
* Exploratory Data Analysis (EDA)

---

