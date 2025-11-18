"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Develop a Python program that outputs a summary of the portfolio allocation for each quarter based on the SUI Strategies investment plan, and formats the data into a CSV file.
Generated: DETERMINISTIC_adf08d01e2bf6250
Batch ID: 20250612_145516
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
from collections import defaultdict

def generate_portfolio_summary(plan, start_date, end_date, output_file):
    """
    Generates a portfolio summary based on the investment plan and saves it to a CSV file.

    :param plan: Dictionary containing the investment plan. Keys are asset classes, values are percentages (0-100).
    :param start_date: Start date for the portfolio summary (YYYY-MM-DD format).
    :param end_date: End date for the portfolio summary (YYYY-MM-DD format).
    :param output_file: Filepath for the output CSV file.
    """
    try:
        # Ensure that the plan's percentages sum to 100
        if not (0 <= sum(plan.values()) <= 100):
            raise ValueError("The total allocation in the investment plan must sum to 100.")

        # Parse start and end dates
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')

        if start_date > end_date:
            raise ValueError("Start date must be before or equal to the end date.")

        # Generate quarterly summaries
        portfolio_summary = []
        current_date = start_date

        while current_date <= end_date:
            quarter_end_month = ((current_date.month - 1) // 3 + 1) * 3
            quarter_end_date = datetime.datetime(current_date.year, quarter_end_month, 1)
            quarter_end_date += datetime.timedelta(days=-1)
            
            # Adjust quarter end date if it exceeds the end_date
            if quarter_end_date > end_date:
                quarter_end_date = end_date

            portfolio_summary.append({
                "Quarter Start": current_date.strftime('%Y-%m-%d'),
                "Quarter End": quarter_end_date.strftime('%Y-%m-%d'),
                **plan
            })
            
            # Move to the next quarter
            next_quarter_start = quarter_end_date + datetime.timedelta(days=1)
            current_date = next_quarter_start

        # Write portfolio summary to a CSV file
        with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ["Quarter Start", "Quarter End"] + list(plan.keys())
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # Write header
            writer.writeheader()

            # Write each row of the portfolio summary
            for row in portfolio_summary:
                writer.writerow(row)

        print(f"Portfolio summary successfully written to {output_file}.")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Define the SUI Strategies investment plan
    sui_investment_plan = {
        "Equities": 50,    # 50% allocation to Equities
        "Bonds": 30,       # 30% allocation to Bonds
        "Real Estate": 15, # 15% allocation to Real Estate
        "Cash": 5          # 5% allocation to Cash
    }

    # Define start and end dates for the portfolio summary
    portfolio_start_date = "2023-01-01"
    portfolio_end_date = "2023-12-31"

    # Define the output CSV file
    output_csv_file = "portfolio_summary.csv"

    # Generate the portfolio summary and save it to the CSV file
    generate_portfolio_summary(sui_investment_plan, portfolio_start_date, portfolio_end_date, output_csv_file)
```
