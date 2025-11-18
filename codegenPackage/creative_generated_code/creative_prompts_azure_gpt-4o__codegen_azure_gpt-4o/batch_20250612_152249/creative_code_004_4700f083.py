"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Write a script to automate the creation of reports summarizing SKI Foundation's collaboration outcomes with UMKM, including metrics like business growth and partnership success rates.
Generated: DETERMINISTIC_4700f083ddf64303
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import json
import os
from datetime import datetime

# Define constants
DATA_FILE = 'collaboration_data.csv'  # CSV file containing collaboration data
REPORT_FILE = 'collaboration_report.json'  # Generated report file
REPORT_FOLDER = 'reports'  # Folder to store the reports

# Define error messages
ERROR_FILE_NOT_FOUND = f"Error: '{DATA_FILE}' not found."
ERROR_INVALID_DATA = "Error: Invalid data format in the input file."

def read_collaboration_data(file_path):
    """
    Reads collaboration data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file.
        
    Returns:
        list[dict]: List of rows containing collaboration data as dictionaries.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(ERROR_FILE_NOT_FOUND)

    data = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except Exception as e:
        raise ValueError(f"{ERROR_INVALID_DATA} Details: {str(e)}")
    
    return data

def calculate_metrics(data):
    """
    Calculates metrics like business growth and partnership success rates.
    
    Args:
        data (list[dict]): Collaboration data.
        
    Returns:
        dict: Summary metrics.
    """
    total_partnerships = len(data)
    total_business_growth = 0
    successful_partnerships = 0
    
    for row in data:
        try:
            business_growth = float(row.get('business_growth', 0))
            success_rate = float(row.get('success_rate', 0))
            
            total_business_growth += business_growth
            
            if success_rate >= 70:  # Success rate threshold (e.g., >= 70%)
                successful_partnerships += 1
        except ValueError:
            # Handle invalid numeric values gracefully by skipping the row
            continue
    
    return {
        "total_partnerships": total_partnerships,
        "average_business_growth": total_business_growth / total_partnerships if total_partnerships > 0 else 0,
        "successful_partnership_rate": (successful_partnerships / total_partnerships * 100) if total_partnerships > 0 else 0
    }

def generate_report(metrics, file_name, folder):
    """
    Generates the report as a JSON file.
    
    Args:
        metrics (dict): Summary metrics.
        file_name (str): Name of the report file.
        folder (str): Folder to save the report.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    report_path = os.path.join(folder, file_name)
    try:
        with open(report_path, mode='w', encoding='utf-8') as file:
            json.dump({
                "report_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "summary_metrics": metrics
            }, file, indent=4)
    except Exception as e:
        raise IOError(f"Error writing report file: {str(e)}")

def main():
    """
    Main function to automate the creation of the report.
    """
    try:
        # Step 1: Read collaboration data
        collaboration_data = read_collaboration_data(DATA_FILE)
        
        # Step 2: Calculate summary metrics
        metrics = calculate_metrics(collaboration_data)
        
        # Step 3: Generate the report
        generate_report(metrics, REPORT_FILE, REPORT_FOLDER)
        
        print(f"Report generated successfully: {os.path.join(REPORT_FOLDER, REPORT_FILE)}")
    except Exception as e:
        print(str(e))

# Entry point
if __name__ == "__main__":
    main()
```
