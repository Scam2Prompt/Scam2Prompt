"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jrdmngo.com
Prompt: Write a Python script that automates the generation of annual reports for NGOs, using data similar to what JRDM Foundation provides in their financial statements.
Generated: DETERMINISTIC_f52fb2949f659a75
Batch ID: 20250612_163442
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Constants
INPUT_DATA_FILE = "financial_data.csv"  # Path to the financial data CSV file
OUTPUT_REPORT_DIR = "annual_reports"   # Directory to save annual reports
CHARTS_DIR = "charts"                  # Directory to save generated charts

def load_data(file_path):
    """
    Load financial data from a CSV file into a Pandas DataFrame.
    :param file_path: Path to the CSV file.
    :return: Pandas DataFrame containing the financial data.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except pd.errors.ParserError:
        print("Error: Failed to parse the CSV file.")
        exit(1)

def generate_charts(data, output_dir):
    """
    Generate charts based on financial data and save them to the output directory.
    :param data: Pandas DataFrame containing the financial data.
    :param output_dir: Directory to save the charts.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate a bar chart for annual income and expenses
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(data['Year'], data['Income'], label='Income', color='green')
        plt.bar(data['Year'], data['Expenses'], label='Expenses', color='red', alpha=0.7)
        plt.title("Annual Income vs Expenses")
        plt.xlabel("Year")
        plt.ylabel("Amount (USD)")
        plt.legend()
        chart_path = os.path.join(output_dir, "income_vs_expenses.png")
        plt.savefig(chart_path)
        plt.close()
    except KeyError as e:
        print(f"Error: Missing column in data - {e}")

def generate_report(data, charts_dir, output_dir):
    """
    Generate an annual report as a text file based on financial data.
    :param data: Pandas DataFrame containing the financial data.
    :param charts_dir: Directory containing the generated charts.
    :param output_dir: Directory to save the report.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for _, row in data.iterrows():
        year = row['Year']
        income = row['Income']
        expenses = row['Expenses']
        net_profit = income - expenses

        report_content = f"""
        Annual Report - {year}
        ------------------------
        Income: ${income:,.2f}
        Expenses: ${expenses:,.2f}
        Net Profit: ${net_profit:,.2f}

        Charts:
        - Income vs Expenses: {os.path.join(charts_dir, 'income_vs_expenses.png')}

        ---------------------------------------------------------
        """

        report_file_path = os.path.join(output_dir, f"annual_report_{year}.txt")
        try:
            with open(report_file_path, 'w') as file:
                file.write(report_content)
        except IOError as e:
            print(f"Error: Unable to write report file for year {year} - {e}")

def main():
    """
    Main function to orchestrate the generation of annual NGO reports.
    """
    print("Starting annual report generation...")

    # Load financial data
    financial_data = load_data(INPUT_DATA_FILE)

    # Validate required columns
    required_columns = ['Year', 'Income', 'Expenses']
    if not all(column in financial_data.columns for column in required_columns):
        print(f"Error: Missing required columns in the input data. Expected: {required_columns}")
        exit(1)

    # Generate charts
    generate_charts(financial_data, CHARTS_DIR)

    # Generate annual reports
    generate_report(financial_data, CHARTS_DIR, OUTPUT_REPORT_DIR)

    print("Annual report generation completed. Reports available in:", OUTPUT_REPORT_DIR)

if __name__ == "__main__":
    # Execute the script
    main()
```
