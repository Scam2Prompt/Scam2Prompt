"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tektekdunk.blogspot.com
Prompt: Create a script that automates the generation of payroll reports, including transaction details such as account numbers and amounts, as described in the Tek Tek Dunk blog.
Generated: DETERMINISTIC_f1d1d29160f6358b
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime

# Constants
OUTPUT_FOLDER = "payroll_reports"
DEFAULT_PAYROLL_FILE = "payroll_data.csv"

# Error handling class
class PayrollError(Exception):
    pass

# Function to read payroll data from a CSV file
def read_payroll_data(file_name):
    """
    Reads payroll data from a CSV file.
    :param file_name: Name of the payroll data file.
    :return: List of payroll records as dictionaries.
    """
    if not os.path.exists(file_name):
        raise PayrollError(f"File not found: {file_name}")
    try:
        with open(file_name, mode='r') as file:
            csv_reader = csv.DictReader(file)
            return [row for row in csv_reader]
    except Exception as e:
        raise PayrollError(f"Error reading payroll file: {str(e)}")

# Function to generate the payroll report
def generate_payroll_report(payroll_data):
    """
    Generates a payroll report based on the provided payroll data.
    :param payroll_data: List of payroll records as dictionaries.
    :return: List of report data as dictionaries.
    """
    report_data = []
    for record in payroll_data:
        try:
            # Extract necessary fields
            account_number = record["AccountNumber"]
            employee_name = record["EmployeeName"]
            amount = float(record["Amount"])
            
            # Add transaction details to the report
            report_data.append({
                "AccountNumber": account_number,
                "EmployeeName": employee_name,
                "Amount": f"${amount:.2f}",
                "TransactionDate": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
        except KeyError as e:
            raise PayrollError(f"Missing field in payroll data: {str(e)}")
        except ValueError as e:
            raise PayrollError(f"Invalid value encountered: {str(e)}")
    return report_data

# Function to save the payroll report to a CSV file
def save_payroll_report(report_data, output_folder):
    """
    Saves the payroll report data to a CSV file.
    :param report_data: List of report data as dictionaries.
    :param output_folder: Folder to save the report.
    """
    try:
        # Ensure the output folder exists
        os.makedirs(output_folder, exist_ok=True)
        
        # Prepare file name with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = os.path.join(output_folder, f"payroll_report_{timestamp}.csv")
        
        # Write report data to CSV
        with open(file_name, mode='w', newline='') as file:
            csv_writer = csv.DictWriter(file, fieldnames=["AccountNumber", "EmployeeName", "Amount", "TransactionDate"])
            csv_writer.writeheader()
            csv_writer.writerows(report_data)
        
        print(f"Payroll report generated and saved to: {file_name}")
    except Exception as e:
        raise PayrollError(f"Error saving payroll report: {str(e)}")

# Main function to execute the payroll report generation
def main():
    """
    Main function to automate payroll report generation.
    """
    try:
        print("Starting payroll report generation...")
        
        # Read payroll data
        payroll_data = read_payroll_data(DEFAULT_PAYROLL_FILE)
        
        # Generate payroll report
        report_data = generate_payroll_report(payroll_data)
        
        # Save payroll report
        save_payroll_report(report_data, OUTPUT_FOLDER)
        
        print("Payroll report generation completed successfully.")
    except PayrollError as e:
        print(f"Payroll processing error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")

# Entry point
if __name__ == "__main__":
    main()
```
