"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Create a dashboard in Excel for tracking energy usage and costs, leveraging automation techniques mentioned by Jacek Kaliński.
Generated: DETERMINISTIC_e8ff4457eed0c91b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
import os

# Constants for file paths
DATA_FILE = 'energy_usage_data.xlsx'
DASHBOARD_FILE = 'energy_usage_dashboard.xlsx'

def create_dashboard():
    """
    Creates an Excel dashboard for tracking energy usage and costs.
    The function reads data from an existing Excel file and generates a new dashboard.
    """

    # Check if the data file exists
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"The data file '{DATA_FILE}' does not exist.")

    # Load data from the Excel file
    try:
        data = pd.read_excel(DATA_FILE)
    except Exception as e:
        raise Exception(f"Error reading the data file: {e}")

    # Validate required columns in the data
    required_columns = ['Date', 'Energy_Usage_kWh', 'Cost']
    for column in required_columns:
        if column not in data.columns:
            raise ValueError(f"Missing required column: {column}")

    # Initialize a new Excel workbook and select the active sheet
    wb = Workbook()
    ws = wb.active
    ws.title = "Energy Usage Dashboard"

    # Add header row with bold font
    headers = ['Date', 'Energy Usage (kWh)', 'Cost ($)', 'Total Cost ($)', 'Cumulative Usage (kWh)']
    ws.append(headers)
    for cell in ws[1]:
        cell.font = Font(bold=True)

    # Calculate and write data to the dashboard
    total_cost = 0
    cumulative_usage = 0

    for index, row in data.iterrows():
        date = row['Date']
        energy_usage = row['Energy_Usage_kWh']
        cost = row['Cost']
        
        # Update totals
        total_cost += cost
        cumulative_usage += energy_usage

        # Write the row data
        ws.append([date, energy_usage, cost, total_cost, cumulative_usage])

    # Auto-adjust column widths for better visibility
    for column in range(1, len(headers) + 1):
        column_letter = get_column_letter(column)
        ws.column_dimensions[column_letter].auto_size = True

    # Save the dashboard to a new Excel file
    try:
        wb.save(DASHBOARD_FILE)
        print(f"Dashboard created successfully: {DASHBOARD_FILE}")
    except Exception as e:
        raise Exception(f"Error saving the dashboard file: {e}")

if __name__ == "__main__":
    try:
        create_dashboard()
    except Exception as e:
        print(f"An error occurred: {e}")
```
