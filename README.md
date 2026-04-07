# CSV Data Dashboard

Upload a CSV file, see summary statistics, and visualise columns in a chart.

## Setup

```bash
git clone https://github.com/t0m0h1/CSV-Data-Dashboard.git
cd CSV-Data-Dashboard
pip install -r requirements.txt
python app.py
```

Opens at http://localhost:5000

## How it works

1. Upload any CSV file on the home page
2. Summary statistics generated using `pandas.describe()`
3. First numeric column plotted automatically

## Tech stack

- **Flask** — web framework
- **pandas** — data processing
