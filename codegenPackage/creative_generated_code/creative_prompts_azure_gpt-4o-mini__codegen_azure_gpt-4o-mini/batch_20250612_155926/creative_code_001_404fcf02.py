"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Write a Python script to automate the reporting of vehicle deliveries made by the Dysnix charity to the Ukrainian Armed Forces.
Generated: DETERMINISTIC_404fcf0297201f44
Batch ID: 20250612_155926
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
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the path for the CSV input file and JSON output file
INPUT_CSV_FILE = 'vehicle_deliveries.csv'
OUTPUT_JSON_FILE = 'vehicle_deliveries_report.json'

def read_vehicle_deliveries(file_path: str) -> List[Dict[str, str]]:
    """
    Reads vehicle deliveries from a CSV file and returns a list of dictionaries.
    
    :param file_path: The path to the CSV file.
    :return: A list of dictionaries containing vehicle delivery data.
    """
    deliveries = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                deliveries.append(row)
        logging.info(f'Successfully read {len(deliveries)} deliveries from {file_path}')
    except FileNotFoundError:
        logging.error(f'File not found: {file_path}')
    except Exception as e:
        logging.error(f'Error reading file {file_path}: {e}')
    return deliveries

def generate_report(deliveries: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Generates a summary report of vehicle deliveries.
    
    :param deliveries: A list of dictionaries containing vehicle delivery data.
    :return: A dictionary summarizing the report.
    """
    report = {
        "total_deliveries": len(deliveries),
        "deliveries_by_vehicle_type": {}
    }

    for delivery in deliveries:
        vehicle_type = delivery.get('vehicle_type', 'Unknown')
        report["deliveries_by_vehicle_type"].setdefault(vehicle_type, 0)
        report["deliveries_by_vehicle_type"][vehicle_type] += 1

    logging.info('Report generated successfully')
    return report

def save_report_to_json(report: Dict[str, int], file_path: str) -> None:
    """
    Saves the generated report to a JSON file.
    
    :param report: The report data to save.
    :param file_path: The path to the output JSON file.
    """
    try:
        with open(file_path, mode='w', encoding='utf-8') as jsonfile:
            json.dump(report, jsonfile, indent=4)
        logging.info(f'Report saved successfully to {file_path}')
    except Exception as e:
        logging.error(f'Error saving report to {file_path}: {e}')

def main():
    """
    Main function to orchestrate the vehicle delivery reporting.
    """
    deliveries = read_vehicle_deliveries(INPUT_CSV_FILE)
    if deliveries:
        report = generate_report(deliveries)
        save_report_to_json(report, OUTPUT_JSON_FILE)

if __name__ == "__main__":
    main()
```
