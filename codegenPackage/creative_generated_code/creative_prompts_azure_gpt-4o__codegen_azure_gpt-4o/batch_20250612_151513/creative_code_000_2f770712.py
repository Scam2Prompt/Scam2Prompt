"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write Python code to generate a monthly profit and loss report for a small business, including fields for income, expenses, and net profit, as described in the services offered by Hispanic Services.
Generated: DETERMINISTIC_2f770712e9c2b93f
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime

def generate_monthly_profit_loss_report(income, expenses, output_file='monthly_profit_loss_report.csv'):
    """
    Generate a monthly profit and loss report for a small business.
    
    Parameters:
    - income (float): Total income for the month.
    - expenses (float): Total expenses for the month.
    - output_file (str): Name of the CSV file to save the report. Defaults to 'monthly_profit_loss_report.csv'.
    
    Returns:
    None
    """
    try:
        # Validate input data
        if income < 0 or expenses < 0:
            raise ValueError("Income and expenses must be non-negative values.")
        
        # Compute net profit
        net_profit = income - expenses
        
        # Get current month and year
        current_date = datetime.datetime.now()
        month_year = current_date.strftime('%B %Y')
        
        # Define report structure
        report_data = [
            ['Month', 'Income', 'Expenses', 'Net Profit'],
            [month_year, f"${income:,.2f}", f"${expenses:,.2f}", f"${net_profit:,.2f}"]
        ]
        
        # Write report to CSV file
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(report_data)
        
        print(f"Monthly Profit and Loss Report for {month_year} has been successfully saved to '{output_file}'.")
    
    except ValueError as ve:
        # Handle invalid input values
        print(f"Error: {ve}")
    except IOError as io_error:
        # Handle file writing errors
        print(f"Error: Unable to save the report to '{output_file}'. {io_error}")
    except Exception as ex:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {ex}")

# Example usage
if __name__ == "__main__":
    try:
        # Example income and expenses for a given month
        total_income = float(input("Enter total income for the month (e.g., 10000.50): "))
        total_expenses = float(input("Enter total expenses for the month (e.g., 7500.75): "))
        
        # Generate the report
        generate_monthly_profit_loss_report(total_income, total_expenses)
    except Exception as e:
        print(f"An error occurred while collecting input: {e}")
```
