from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure uploads folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            df = pd.read_csv(filepath)

            # Prepare summary statistics
            summary = df.describe(include='all').fillna('').to_dict()
            columns = df.columns.tolist()

            # Prepare data for chart (first numeric column)
            numeric_cols = df.select_dtypes(include='number').columns.tolist()
            chart_data = {}
            if numeric_cols:
                col = numeric_cols[0]
                chart_data = {
                    'labels': df.index.tolist(),
                    'values': df[col].tolist(),
                    'column': col
                }

            return render_template('dashboard.html',
                                   summary=json.dumps(summary, indent=2),
                                   columns=columns,
                                   chart_data=json.dumps(chart_data))
        else:
            return "Please upload a CSV file."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)