# Hospital Readmission ETL Pipeline (CSV to MySQL)

A beginner-friendly ETL (Extract, Transform, Load) pipeline built in Python. It reads a hospital readmission CSV file (10,000 rows, 15 columns), cleans it with Pandas, and loads it into a MySQL database.

This is the next step after my Flipkart Sales Data Cleaning Pipeline. In that project I saved the cleaned data to a CSV file. In this project I save it into a real database.

## Before vs Now

| | Flipkart Pipeline (Before) | Readmission Pipeline (Now) |
|---|---|---|
| Source | Raw CSV file | Raw CSV file |
| Destination | New CSV file on my PC | MySQL database table |
| Reading data | Whole file at once | In chunks of 10,000 rows |
| Cleaning | Stripped spaces, filled missing Price with 0 | Cleaned column names, removed duplicates, trimmed text, missing values saved as NULL |
| Libraries | Pandas, logging, pathlib | Pandas, SQLAlchemy, PyMySQL, python-dotenv, logging |
| Credentials | None needed | Stored safely in a `.env` file |

## What It Does

Raw CSV -> Extract -> Transform (clean) -> Load -> MySQL table

1. **Extract:** Reads `readmission_dataset.csv` using Pandas.
2. **Transform:** Cleans column names, removes duplicate rows, strips extra spaces from text, and converts missing values (NaN) to NULL.
3. **Load:** Saves the cleaned data into a MySQL table using SQLAlchemy and PyMySQL.

## Dataset

- 10,000 rows and 15 columns
- Target column: `readmitted_within_30days` (1 = readmitted within 30 days, 0 = not readmitted)
- Other columns: age, gender, admission_type, primary_diagnosis_code, num_prior_admissions, time_in_hospital, num_lab_procedures, num_medications, has_comorbidity, discharge_disposition, insurance_type, hospital_id, days_to_readmission

## Tech Used

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pandas | Reading and cleaning data |
| SQLAlchemy + PyMySQL | Connecting Python to MySQL |
| python-dotenv | Keeping the database password safe |
| logging | Tracking pipeline progress and errors |
| MySQL | Storing the final data |

## How to Run

1. Install libraries:
```bash
   pip install pandas sqlalchemy pymysql python-dotenv
```
2. Create a database in MySQL:
```sql
   CREATE DATABASE my_database;
```
3. Create a `.env` file with your MySQL details (user, password, host, port, database name).
4. Run:
```bash
   python pipeline.py
```

If successful, you will see logs like:
```
INFO:root:transforming completed successfully
INFO:root:loading data
INFO:root:pipeline completed successfully
```

## What I Learned

- Connecting Python (Pandas) to a MySQL database using SQLAlchemy
- Loading large data in chunks instead of all at once
- Keeping passwords safe using a `.env` file
- Fixing real errors step by step:
  - `No module named 'pymysql'` (missing library)
  - `Must specify a fill 'value' or 'method'` (wrong use of `fillna`)
  - `missing 1 required positional argument: 'df'` (function argument mistake)
- Checking the data in MySQL after loading (row count and sample rows)

## Note

This is a learning-stage pipeline, not a production tool. Planned next steps:
- Avoid duplicate rows when the pipeline runs again (upsert)
- Add data validation checks
- Run the pipeline automatically on a schedule

## Author
Github=> https://github.com/ravindrachilhate47-create/ravindrachilhate47-create
Linkedin=> https://www.linkedin.com/in/ravindra-chilhate-52084435b/

Built by 
     Ravindra Chilhate as part of my Data Engineering learning journey.
