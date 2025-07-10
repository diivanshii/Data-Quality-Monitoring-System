# Data Quality Monitoring System

**Simulating L1 DataOps Monitoring for Ingestion & Analytics Pipelines**  
**Tech Stack:** Python, Pandas | Smart CSV Issue Logging | Data Analyst Utility

---

## 🧠 Overview

In fast-paced data environments, even minor inconsistencies — like nulls or schema shifts — can cause cascading failures across dashboards, reports, and ML models.

This project simulates a **Level 1 (L1) alert monitoring tool** built for ingestion and analytics pipelines. It autonomously inspects structured data (CSV) for foundational quality issues and logs them in a clean, operations-ready format.

---

## 🎯 Why This Project Matters

**What I built here isn't just a script — it's a DataOps mindset in action.**

This utility mimics how modern data teams handle Business-As-Usual (BAU) monitoring by automating:

- Schema validation (missing/renamed columns)
- Null count detection across the dataset
- Outlier flagging in numeric columns (above 99th percentile)
- Duplicate row identification

It acts as a first responder to pipeline issues — exactly what you'd expect from a scalable monitoring system integrated with Airflow, DataDog, or alerting dashboards.

---

## 🚀 Getting Started

### 🧩 Prerequisites

- Python 3.7+
- `pandas` installed (`pip install pandas`)
- A CSV dataset (you can use the [Kaggle dataset](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis))

## 🧪 Sample Output (`issues_log.csv`)

```csv
Issue
Nulls in 'Income': 24
Duplicate Rows: 10
Outliers in 'Year_Birth': 5 values above 99th percentile
Missing expected column: Education_Level
---
```
### 📦 Setup Instructions

```bash
# 1. Clone this repo
git clone https://github.com/yourusername/data-quality-monitor.git
cd data-quality-monitor

# 2. Add your dataset
mv your_dataset.csv marketing_campaign.csv

# 3. Run the monitoring script
python monitor.py

# 4. View the generated issue log
cat issues_log.csv
```
## 💻 How It Works

- Loads your dataset from `marketing_campaign.csv`
- Performs the following checks:
  - ✅ Missing values across all columns
  - ✅ Duplicate rows in the dataset
  - ✅ Outliers in numeric columns (above 99th percentile)
  - ✅ Schema drift against an expected column list
- Logs all detected issues into `issues_log.csv` in a clean, readable format

---

## 🛠 Tech Stack

| Tool     | Used For                           |
|----------|------------------------------------|
| Python   | Core scripting and automation      |
| Pandas   | Data validation, profiling, alerts |
| CSV      | Input/output format                |

---

## 🧪 Sample Output (`issues_log.csv`)

```csv
Issue
Nulls in 'Income': 24
Duplicate Rows: 10
Outliers in 'Year_Birth': 5 values above 99th percentile
Missing expected column: Education_Level
```
---

## 🔍 Use Cases

- Simulate L1 DataOps alerting behavior for pipelines  
- Build operational awareness in data validation  
- Showcase DataOps + Analyst workflow in your portfolio  
- Serve as a pre-processing validator before analytics dashboards  

---

## 🌟 Key Highlights

- Built with **reusability** and **clarity** in mind  
- Plug-and-play with **any structured CSV**  
- Easily extendable to **Slack/Email alerts** or **Airflow DAGs**  
- Emulates monitoring logic used in **production ingestion systems**  

---

## 🧠 Lessons Learned

- Designed logging similar to **SLA-compliant support workflows**  
- Thought critically about **what must be flagged early** in a pipeline  
- Prioritized both **developer readability** and **Ops visibility**  

---

## 👩‍💻 Author

**Divanshi Mamodia**  
📫 [LinkedIn](https://www.linkedin.com/in/divanshi-mamodia-8395a2220)  
📂 [GitHub](https://github.com/diivanshii)  

---

## 🙌 Contribute

Found a better way to detect anomalies?  
Want to extend this with email alerts, Grafana visualizations, or Airflow integration?

**Feel free to fork and contribute — PRs are welcome!**

