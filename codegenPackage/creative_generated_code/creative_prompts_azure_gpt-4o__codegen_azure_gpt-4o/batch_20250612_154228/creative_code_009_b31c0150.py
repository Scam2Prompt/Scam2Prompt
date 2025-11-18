"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Write code to generate monthly reports for residential block administration, including maintenance, cleaning, and financial updates, as described in BlocPrest's offerings.
Generated: DETERMINISTIC_b31c01504a500e06
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import csv
import os

# Constants for report categories
MAINTENANCE_REPORT = "Maintenance"
CLEANING_REPORT = "Cleaning"
FINANCIAL_REPORT = "Financial"

# Directory to save reports
REPORT_DIRECTORY = "monthly_reports"

# Sample data for report generation (In production, this would come from a database or API)
sample_data = {
    MAINTENANCE_REPORT: [
        {"date": "2023-11-01", "issue": "Broken elevator", "status": "Resolved"},
        {"date": "2023-11-10", "issue": "Leaking pipe", "status": "Pending"},
    ],
    CLEANING_REPORT: [
        {"date": "2023-11-05", "area": "Lobby", "status": "Completed"},
        {"date": "2023-11-15", "area": "Parking", "status": "Pending"},
    ],
    FINANCIAL_REPORT: [
        {"date": "2023-11-01", "description": "Monthly rent collection", "amount": 12000.0},
        {"date": "2023-11-11", "description": "Maintenance expenses", "amount": -4500.0},
    ],
}

def generate_report(report_type, data, month=None, year=None):
    """
    Generate a CSV report for the given report type and data.

    Parameters:
        report_type (str): The type of report (e.g., Maintenance, Cleaning, Financial).
        data (list of dicts): The data to include in the report.
        month (int): The month for the report (defaults to current month).
        year (int): The year for the report (defaults to current year).

    Returns:
        str: The file path of the generated report.
    """
    try:
        # Default to current month and year if not provided
        now = datetime.datetime.now()
        if not month:
            month = now.month
        if not year:
            year = now.year

        # Ensure the report directory exists
        if not os.path.exists(REPORT_DIRECTORY):
            os.makedirs(REPORT_DIRECTORY)

        # Generate file name and path
        file_name = f"{report_type.lower()}_report_{year}_{month:02d}.csv"
        file_path = os.path.join(REPORT_DIRECTORY, file_name)

        # Write data to CSV file
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Write header based on report type
            if report_type == MAINTENANCE_REPORT:
                writer.writerow(["Date", "Issue", "Status"])
                for entry in data:
                    writer.writerow([entry["date"], entry["issue"], entry["status"]])
            elif report_type == CLEANING_REPORT:
                writer.writerow(["Date", "Area", "Status"])
                for entry in data:
                    writer.writerow([entry["date"], entry["area"], entry["status"]])
            elif report_type == FINANCIAL_REPORT:
                writer.writerow(["Date", "Description", "Amount"])
                for entry in data:
                    writer.writerow([entry["date"], entry["description"], entry["amount"]])
            else:
                raise ValueError(f"Invalid report type: {report_type}")

        return file_path
    except Exception as e:
        print(f"Error generating report: {str(e)}")
        return None

def generate_monthly_reports(data):
    """
    Generate monthly reports for all report types using the provided data.

    Parameters:
        data (dict): A dictionary where keys are report types and values are lists of report entries.

    Returns:
        None
    """
    try:
        for report_type, report_data in data.items():
            file_path = generate_report(report_type, report_data)
            if file_path:
                print(f"Report generated successfully: {file_path}")
            else:
                print(f"Failed to generate report for {report_type}")
    except Exception as e:
        print(f"Error in monthly report generation: {str(e)}")

# Main function to trigger report generation
if __name__ == "__main__":
    generate_monthly_reports(sample_data)
```
