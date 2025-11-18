"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cooperativacooprometa.com
Prompt: Generate a script for exporting financial statements and management reports from a CMS system like Nexelit.
Generated: DETERMINISTIC_9c1724809f8e688f
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
import json
from datetime import datetime

# Define constants for output directories
EXPORT_DIRECTORY = "exports"
FINANCIAL_STATEMENTS_FILE = "financial_statements.csv"
MANAGEMENT_REPORTS_FILE = "management_reports.json"

# Function to fetch financial statements from the CMS
def fetch_financial_statements():
    """
    Simulate fetching financial statements from the CMS.
    Replace this function with actual CMS API calls.
    Returns a list of dictionaries representing financial statement data.
    """
    # Example data - replace with actual API response
    return [
        {"date": "2023-10-01", "revenue": 10000, "expenses": 5000, "profit": 5000},
        {"date": "2023-10-02", "revenue": 12000, "expenses": 6000, "profit": 6000},
    ]

# Function to fetch management reports from the CMS
def fetch_management_reports():
    """
    Simulate fetching management reports from the CMS.
    Replace this function with actual CMS API calls.
    Returns a dictionary representing management report data.
    """
    # Example data - replace with actual API response
    return {
        "report_date": "2023-10-01",
        "summary": "Monthly performance overview",
        "details": {
            "total_revenue": 22000,
            "total_expenses": 11000,
            "net_profit": 11000,
        },
    }

# Function to export financial statements to a CSV file
def export_financial_statements(data):
    """
    Exports financial statement data to a CSV file.
    :param data: List of dictionaries containing financial statement data.
    """
    try:
        # Ensure the export directory exists
        os.makedirs(EXPORT_DIRECTORY, exist_ok=True)
        output_file = os.path.join(EXPORT_DIRECTORY, FINANCIAL_STATEMENTS_FILE)
        
        # Write data to a CSV file
        with open(output_file, mode="w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["date", "revenue", "expenses", "profit"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header row
            writer.writeheader()
            
            # Write data rows
            for row in data:
                writer.writerow(row)
        
        print(f"Financial statements exported successfully to {output_file}")
    except Exception as e:
        print(f"Error exporting financial statements: {e}")

# Function to export management reports to a JSON file
def export_management_reports(data):
    """
    Exports management report data to a JSON file.
    :param data: Dictionary containing management report data.
    """
    try:
        # Ensure the export directory exists
        os.makedirs(EXPORT_DIRECTORY, exist_ok=True)
        output_file = os.path.join(EXPORT_DIRECTORY, MANAGEMENT_REPORTS_FILE)
        
        # Write data to a JSON file
        with open(output_file, mode="w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        
        print(f"Management reports exported successfully to {output_file}")
    except Exception as e:
        print(f"Error exporting management reports: {e}")

# Main function
def main():
    """
    Main function to fetch and export data from the CMS.
    """
    print("Starting export process...")

    # Fetch and export financial statements
    print("Fetching financial statements...")
    financial_statements = fetch_financial_statements()
    export_financial_statements(financial_statements)

    # Fetch and export management reports
    print("Fetching management reports...")
    management_reports = fetch_management_reports()
    export_management_reports(management_reports)

    print("Export process completed.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
