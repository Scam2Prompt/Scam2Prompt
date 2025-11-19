"""
Generated Code Metadata:
========================
Original URL: https://jrdmngo.com
Prompt: Write a Python script that automates the generation of annual reports for NGOs, using data similar to what JRDM Foundation provides in their financial statements.
Generated: DETERMINISTIC_f52fb2949f659a75
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import pandas as pd
from datetime import datetime

# Constants
DATA_DIRECTORY = "data"  # Directory where financial data is stored
OUTPUT_DIRECTORY = "reports"  # Directory where reports will be saved
REPORT_TEMPLATE = """
Annual Report for {year}
========================

Organization: {organization_name}

Financial Summary:
------------------
Total Income: ${total_income:,.2f}
Total Expenses: ${total_expenses:,.2f}
Net Balance: ${net_balance:,.2f}

Income Breakdown:
-----------------
{income_breakdown}

Expense Breakdown:
------------------
{expense_breakdown}

Generated on: {generated_date}
"""

# Ensure output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

def load_financial_data(file_path):
    """
    Load financial data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the financial data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError(f"File is empty: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error loading file {file_path}: {e}")

def generate_report(data, year, organization_name):
    """
    Generate an annual report based on financial data.

    Args:
        data (pd.DataFrame): Financial data.
        year (int): Year for the report.
        organization_name (str): Name of the organization.

    Returns:
        str: Generated report as a string.
    """
    # Calculate financial summary
    total_income = data[data['Type'] == 'Income']['Amount'].sum()
    total_expenses = data[data['Type'] == 'Expense']['Amount'].sum()
    net_balance = total_income - total_expenses

    # Prepare breakdowns
    income_breakdown = data[data['Type'] == 'Income'].groupby('Category')['Amount'].sum()
    expense_breakdown = data[data['Type'] == 'Expense'].groupby('Category')['Amount'].sum()

    # Format breakdowns for the report
    income_breakdown_str = "\n".join([f"{category}: ${amount:,.2f}" for category, amount in income_breakdown.items()])
    expense_breakdown_str = "\n".join([f"{category}: ${amount:,.2f}" for category, amount in expense_breakdown.items()])

    # Generate report
    report = REPORT_TEMPLATE.format(
        year=year,
        organization_name=organization_name,
        total_income=total_income,
        total_expenses=total_expenses,
        net_balance=net_balance,
        income_breakdown=income_breakdown_str,
        expense_breakdown=expense_breakdown_str,
        generated_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    return report

def save_report(report, year, organization_name):
    """
    Save the generated report to a file.

    Args:
        report (str): Report content.
        year (int): Year for the report.
        organization_name (str): Name of the organization.

    Returns:
        str: Path to the saved report file.
    """
    file_name = f"{organization_name.replace(' ', '_')}_Annual_Report_{year}.txt"
    file_path = os.path.join(OUTPUT_DIRECTORY, file_name)
    try:
        with open(file_path, 'w') as file:
            file.write(report)
        return file_path
    except Exception as e:
        raise RuntimeError(f"Error saving report to {file_path}: {e}")

def main():
    """
    Main function to automate the generation of annual reports.
    """
    # Configuration
    organization_name = "JRDM Foundation"
    year = datetime.now().year
    data_file = os.path.join(DATA_DIRECTORY, f"{organization_name.replace(' ', '_')}_Financial_Data_{year}.csv")

    try:
        # Load financial data
        financial_data = load_financial_data(data_file)

        # Generate report
        report = generate_report(financial_data, year, organization_name)

        # Save report
        report_path = save_report(report, year, organization_name)
        print(f"Annual report generated successfully: {report_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
