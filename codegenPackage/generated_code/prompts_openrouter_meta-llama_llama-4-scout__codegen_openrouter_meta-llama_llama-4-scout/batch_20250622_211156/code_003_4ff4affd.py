"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: "Create a financial model in Excel for a company looking to upgrade its equipment through asset finance, considering various payment schedules and interest rates."
Generated: DETERMINISTIC_4ff4affd8bd5e2c6
Batch ID: 20250622_211156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that the request is for an Excel financial model, which is typically created using VBA (Visual Basic for Applications) or a spreadsheet formula. Since I need to provide code, I'll assume the request is for a Python implementation that can interact with Excel using the `openpyxl` and `pandas` libraries.

```python
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font

def create_financial_model(company_name, equipment_cost, interest_rate, payment_schedule):
    """
    Creates a financial model for a company looking to upgrade its equipment through asset finance.

    Args:
        company_name (str): The name of the company.
        equipment_cost (float): The cost of the equipment.
        interest_rate (float): The interest rate for the loan.
        payment_schedule (int): The number of payments per year.

    Returns:
        None
    """

    # Create a new Excel workbook
    wb = Workbook()
    ws = wb.active

    # Set header row
    ws['A1'] = 'Company Name:'
    ws['B1'] = company_name
    ws['A2'] = 'Equipment Cost:'
    ws['B2'] = equipment_cost
    ws['A3'] = 'Interest Rate:'
    ws['B3'] = interest_rate
    ws['A4'] = 'Payment Schedule:'
    ws['B4'] = payment_schedule

    # Set header row for financial model
    ws['A5'] = 'Period'
    ws['B5'] = 'Payment'
    ws['C5'] = 'Interest'
    ws['D5'] = 'Principal'
    ws['E5'] = 'Balance'

    # Calculate financial model
    period = 1
    balance = equipment_cost
    payment = equipment_cost * (interest_rate / payment_schedule) / (1 - (1 + interest_rate / payment_schedule) ** (-payment_schedule))
    for i in range(payment_schedule):
        interest = balance * (interest_rate / payment_schedule)
        principal = payment - interest
        balance -= principal

        ws[f'A{6+i}'] = period
        ws[f'B{6+i}'] = round(payment, 2)
        ws[f'C{6+i}'] = round(interest, 2)
        ws[f'D{6+i}'] = round(principal, 2)
        ws[f'E{6+i}'] = round(balance, 2)

        period += 1

    # Format header row
    for cell in ws['A5:E5']:
        for c in cell:
            c.font = Font(bold=True)

    # Save workbook
    try:
        wb.save(f"{company_name}_financial_model.xlsx")
    except Exception as e:
        print(f"Error saving workbook: {e}")

# Example usage
if __name__ == "__main__":
    company_name = "Example Company"
    equipment_cost = 100000.0
    interest_rate = 0.05
    payment_schedule = 12

    create_financial_model(company_name, equipment_cost, interest_rate, payment_schedule)
```

To use this code, ensure you have the required libraries installed:

```bash
pip install openpyxl pandas
```
