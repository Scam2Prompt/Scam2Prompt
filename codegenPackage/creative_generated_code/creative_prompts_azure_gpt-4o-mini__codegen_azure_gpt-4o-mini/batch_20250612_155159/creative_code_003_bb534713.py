"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade-verified.com
Prompt: Generate a code snippet that integrates supplier assessment data into a dashboard for real-time monitoring of supply chain risks.
Generated: DETERMINISTIC_bb5347134911435c
Batch ID: 20250612_155159
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, jsonify
import sqlite3

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE = 'supplier_assessment.db'

def get_db_connection():
    """Establish a connection to the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def fetch_supplier_data():
    """Fetch supplier assessment data from the database."""
    try:
        conn = get_db_connection()
        query = "SELECT supplier_name, risk_score, assessment_date FROM supplier_assessments;"
        data = conn.execute(query).fetchall()
        conn.close()
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []

@app.route('/')
def index():
    """Render the main dashboard page."""
    return render_template('dashboard.html')

@app.route('/api/suppliers')
def suppliers():
    """API endpoint to retrieve supplier data for the dashboard."""
    data = fetch_supplier_data()
    return jsonify([dict(row) for row in data])

def plot_risk_distribution(data):
    """Plot the distribution of risk scores."""
    if not data:
        print("No data available to plot.")
        return

    risk_scores = [row['risk_score'] for row in data]
    
    plt.figure(figsize=(10, 6))
    plt.hist(risk_scores, bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Supplier Risk Scores')
    plt.xlabel('Risk Score')
    plt.ylabel('Number of Suppliers')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('static/risk_distribution.png')
    plt.close()

if __name__ == '__main__':
    # Fetch data and generate initial plots on startup
    supplier_data = fetch_supplier_data()
    plot_risk_distribution(supplier_data)

    # Run the Flask application
    app.run(debug=True)
```

**HTML Template (templates/dashboard.html):**
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Supplier Assessment Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="mt-5">Supplier Assessment Dashboard</h1>
        <div id="chart" class="mt-4">
            <h2>Risk Distribution</h2>
            <img src="{{ url_for('static', filename='risk_distribution.png') }}" alt="Risk Distribution">
        </div>
        <h2 class="mt-5">Supplier Data</h2>
        <table class="table">
            <thead>
                <tr>
                    <th>Supplier Name</th>
                    <th>Risk Score</th>
                    <th>Assessment Date</th>
                </tr>
            </thead>
            <tbody id="supplier-data">
                <!-- Supplier data will be populated here -->
            </tbody>
        </table>
    </div>
    <script>
        fetch('/api/suppliers')
            .then(response => response.json())
            .then(data => {
                const tableBody = document.getElementById('supplier-data');
                data.forEach(supplier => {
                    const row = `<tr>
                                    <td>${supplier.supplier_name}</td>
                                    <td>${supplier.risk_score}</td>
                                    <td>${supplier.assessment_date}</td>
                                 </tr>`;
                    tableBody.innerHTML += row;
                });
            })
            .catch(error => console.error('Error fetching supplier data:', error));
    </script>
</body>
</html>
```

**Note:** Ensure to create the SQLite database `supplier_assessment.db` and the table `supplier_assessments` with appropriate columns for this code to work.
