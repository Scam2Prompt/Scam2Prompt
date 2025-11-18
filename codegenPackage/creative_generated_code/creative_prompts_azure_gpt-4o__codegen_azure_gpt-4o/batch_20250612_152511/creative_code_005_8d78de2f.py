"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tecnicos-whirlpool.com
Prompt: Develop a Python script to track customer satisfaction ratings for Whirlpool appliance repairs, incorporating metrics like "85% reparaciones exitosas" and "90% clientes satisfechos" from the website.
Generated: DETERMINISTIC_8d78de2f133abb52
Batch ID: 20250612_152511
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

# Define constants for target metrics
SUCCESSFUL_REPAIRS_TARGET = 85  # Target percentage for successful repairs
CUSTOMER_SATISFACTION_TARGET = 90  # Target percentage for customer satisfaction

# Define file paths (change these paths as necessary)
DATA_FILE = 'repair_data.csv'
REPORT_FILE = 'customer_satisfaction_report.txt'

# Function to read repair data from a CSV file
def read_repair_data(file_path):
    """
    Reads repair records from a CSV file.
    Each record should include 'repair_success' (True/False) and 'customer_satisfied' (True/False).

    :param file_path: Path to the CSV file.
    :return: List of repair records.
    """
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Function to calculate metrics
def calculate_metrics(records):
    """
    Calculates performance metrics based on repair records.

    :param records: List of repair records.
    :return: Dictionary with calculated metrics.
    """
    total_repairs = len(records)
    successful_repairs = sum(1 for record in records if record.get('repair_success') == 'True')
    satisfied_customers = sum(1 for record in records if record.get('customer_satisfied') == 'True')
    
    successful_repairs_percentage = (successful_repairs / total_repairs) * 100 if total_repairs > 0 else 0
    customer_satisfaction_percentage = (satisfied_customers / total_repairs) * 100 if total_repairs > 0 else 0
    
    return {
        "total_repairs": total_repairs,
        "successful_repairs_percentage": successful_repairs_percentage,
        "customer_satisfaction_percentage": customer_satisfaction_percentage
    }

# Function to generate a report
def generate_report(metrics):
    """
    Generates a customer satisfaction report based on calculated metrics.

    :param metrics: Dictionary with calculated metrics.
    :return: Formatted report string.
    """
    report = [
        f"Customer Satisfaction Report - {datetime.datetime.now().strftime('%Y-%m-%d')}",
        "------------------------------------------------------------",
        f"Total Repairs: {metrics['total_repairs']}",
        f"Successful Repairs (%): {metrics['successful_repairs_percentage']:.2f}%",
        f"Customer Satisfaction (%): {metrics['customer_satisfaction_percentage']:.2f}%",
        "",
        f"Target Successful Repairs (%): {SUCCESSFUL_REPAIRS_TARGET}%",
        f"Target Customer Satisfaction (%): {CUSTOMER_SATISFACTION_TARGET}%",
        "",
        "Performance Evaluation:",
        f"- Successful Repairs: {'Met' if metrics['successful_repairs_percentage'] >= SUCCESSFUL_REPAIRS_TARGET else 'Not Met'}",
        f"- Customer Satisfaction: {'Met' if metrics['customer_satisfaction_percentage'] >= CUSTOMER_SATISFACTION_TARGET else 'Not Met'}"
    ]
    return '\n'.join(report)

# Function to save the report to a file
def save_report(report, file_path):
    """
    Saves the generated report to a text file.

    :param report: Formatted report string.
    :param file_path: Path to the output file.
    """
    try:
        with open(file_path, mode='w') as file:
            file.write(report)
        print(f"Report saved successfully to {file_path}.")
    except Exception as e:
        print(f"Error saving report: {e}")

# Main function
def main():
    """
    Main function to execute the script logic.
    """
    print("Reading repair data...")
    repair_records = read_repair_data(DATA_FILE)
    
    if not repair_records:
        print("No data found. Exiting.")
        return
    
    print("Calculating metrics...")
    metrics = calculate_metrics(repair_records)
    
    print("Generating report...")
    report = generate_report(metrics)
    print(report)  # Print the report to the console
    
    print("Saving report to file...")
    save_report(report, REPORT_FILE)

# Entry point
if __name__ == "__main__":
    main()
```
