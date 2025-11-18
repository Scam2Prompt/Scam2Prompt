"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://afranaden.org
Prompt: Write a script to automate reporting on medical operations performed in a hospital, such as the complex arterial clot removal procedures described on the Gulf and Aden Development and Humanitarian Services Authority's site.
Generated: DETERMINISTIC_67e5ecdd20519343
Batch ID: 20250612_153224
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
import json
import os

# Constants for input and output file paths
INPUT_FILE = "medical_operations.csv"  # Path to the input file containing operation data
REPORT_FILE = "operation_report.json"  # Path to the generated report file

def read_operations(file_path):
    """
    Reads operations data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of dictionaries representing each operation record.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Input file '{file_path}' does not exist.")
    
    operations = []
    try:
        with open(file_path, mode='r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert fields to appropriate data types
                row['Date'] = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
                row['Duration'] = int(row['Duration'])  # Duration in minutes
                row['Success'] = row['Success'].lower() == 'true'
                operations.append(row)
    except Exception as e:
        raise ValueError(f"Error reading the CSV file: {e}")

    return operations

def generate_report(operations):
    """
    Generates a summary report based on the operations data.

    Args:
        operations (list): List of operation records.

    Returns:
        dict: Report containing summarized metrics.
    """
    report = {
        "total_operations": len(operations),
        "successful_operations": sum(op['Success'] for op in operations),
        "failed_operations": sum(not op['Success'] for op in operations),
        "average_duration": round(sum(op['Duration'] for op in operations) / len(operations), 2),
        "operations_by_type": {},
    }

    for op in operations:
        op_type = op['Operation Type']
        if op_type not in report["operations_by_type"]:
            report["operations_by_type"][op_type] = 0
        report["operations_by_type"][op_type] += 1

    return report

def write_report(report, file_path):
    """
    Writes the report to a JSON file.

    Args:
        report (dict): Report data to write.
        file_path (str): Path to the output file.
    """
    try:
        with open(file_path, mode='w') as f:
            json.dump(report, f, indent=4, default=str)  # Using default=str to handle datetime serialization
    except Exception as e:
        raise ValueError(f"Error writing the report file: {e}")

def main():
    """
    Main function to automate reporting on medical operations.
    """
    try:
        # Step 1: Read operations data
        operations = read_operations(INPUT_FILE)

        # Step 2: Generate the report
        report = generate_report(operations)

        # Step 3: Write the report to a file
        write_report(report, REPORT_FILE)

        print(f"Report generated successfully and saved to '{REPORT_FILE}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
