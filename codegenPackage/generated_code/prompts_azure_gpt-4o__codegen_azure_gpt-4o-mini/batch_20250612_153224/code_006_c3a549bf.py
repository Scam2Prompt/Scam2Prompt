"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Generate code for a financial disclosure system that allows non-profits to publish annual financial reports, inspired by the "التقارير المالية الإفصاح 2023" section of جمعية الدعوة والإرشاد وتوعية الجاليات بمحافظة سميراء.
Generated: DETERMINISTIC_c3a549bfe5ed6e07
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Directory to store financial reports
REPORTS_DIR = 'financial_reports'

# Ensure the reports directory exists
os.makedirs(REPORTS_DIR, exist_ok=True)

class FinancialReport:
    """Class to represent a financial report."""
    
    def __init__(self, organization_name, year, total_income, total_expenses, net_assets):
        self.organization_name = organization_name
        self.year = year
        self.total_income = total_income
        self.total_expenses = total_expenses
        self.net_assets = net_assets
        self.created_at = datetime.now().isoformat()

    def to_dict(self):
        """Convert the report to a dictionary for JSON serialization."""
        return {
            'organization_name': self.organization_name,
            'year': self.year,
            'total_income': self.total_income,
            'total_expenses': self.total_expenses,
            'net_assets': self.net_assets,
            'created_at': self.created_at
        }

def save_report(report):
    """Save the financial report to a JSON file."""
    file_path = os.path.join(REPORTS_DIR, f"{report.organization_name}_{report.year}.json")
    with open(file_path, 'w') as f:
        json.dump(report.to_dict(), f, ensure_ascii=False, indent=4)

@app.route('/reports', methods=['POST'])
def create_report():
    """Endpoint to create a new financial report."""
    data = request.json
    
    # Validate input data
    required_fields = ['organization_name', 'year', 'total_income', 'total_expenses', 'net_assets']
    for field in required_fields:
        if field not in data:
            abort(400, description=f"Missing field: {field}")

    try:
        report = FinancialReport(
            organization_name=data['organization_name'],
            year=data['year'],
            total_income=float(data['total_income']),
            total_expenses=float(data['total_expenses']),
            net_assets=float(data['net_assets'])
        )
        save_report(report)
        return jsonify(report.to_dict()), 201
    except ValueError as e:
        abort(400, description=f"Invalid data: {str(e)}")

@app.route('/reports/<organization_name>/<int:year>', methods=['GET'])
def get_report(organization_name, year):
    """Endpoint to retrieve a financial report by organization name and year."""
    file_path = os.path.join(REPORTS_DIR, f"{organization_name}_{year}.json")
    
    if not os.path.exists(file_path):
        abort(404, description="Report not found.")
    
    with open(file_path, 'r') as f:
        report = json.load(f)
    
    return jsonify(report)

@app.route('/reports', methods=['GET'])
def list_reports():
    """Endpoint to list all financial reports."""
    reports = []
    for filename in os.listdir(REPORTS_DIR):
        if filename.endswith('.json'):
            with open(os.path.join(REPORTS_DIR, filename), 'r') as f:
                reports.append(json.load(f))
    return jsonify(reports)

if __name__ == '__main__':
    app.run(debug=True)
```
