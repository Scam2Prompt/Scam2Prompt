"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a script to generate a report for dealerships and mechanical workshops, summarizing the cleaning and servicing history of fuel injectors based on the services offered by Fuel Injector Services.
Generated: DETERMINISTIC_34cd77fe16b122bd
Batch ID: 20250612_151611
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a class to represent a fuel injector service record
class FuelInjectorServiceRecord:
    def __init__(self, dealership_name: str, workshop_name: str, service_date: str, service_type: str):
        self.dealership_name = dealership_name
        self.workshop_name = workshop_name
        self.service_date = datetime.strptime(service_date, '%Y-%m-%d')
        self.service_type = service_type

    def to_dict(self) -> Dict:
        """Convert the service record to a dictionary."""
        return {
            'dealership_name': self.dealership_name,
            'workshop_name': self.workshop_name,
            'service_date': self.service_date.strftime('%Y-%m-%d'),
            'service_type': self.service_type
        }

# Function to load service records from a CSV file
def load_service_records(csv_file_path: str) -> List[FuelInjectorServiceRecord]:
    records = []
    try:
        with open(csv_file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                record = FuelInjectorServiceRecord(
                    dealership_name=row['dealership_name'],
                    workshop_name=row['workshop_name'],
                    service_date=row['service_date'],
                    service_type=row['service_type']
                )
                records.append(record)
    except FileNotFoundError:
        logging.error(f"File not found: {csv_file_path}")
    except Exception as e:
        logging.error(f"An error occurred while reading the CSV file: {e}")
    return records

# Function to generate a report based on the service records
def generate_report(records: List[FuelInjectorServiceRecord]) -> Dict:
    summary = {}
    for record in records:
        key = (record.dealership_name, record.workshop_name)
        if key not in summary:
            summary[key] = []
        summary[key].append(record)

    report = {}
    for (dealership_name, workshop_name), services in summary.items():
        report[dealership_name] = report.get(dealership_name, {})
        report[dealership_name][workshop_name] = [
            service.to_dict() for service in sorted(services, key=lambda x: x.service_date)
        ]
    
    return report

# Function to save the report to a JSON file
def save_report_to_json(report: Dict, json_file_path: str) -> None:
    try:
        with open(json_file_path, 'w') as jsonfile:
            json.dump(report, jsonfile, indent=4)
        logging.info(f"Report saved successfully to {json_file_path}")
    except Exception as e:
        logging.error(f"An error occurred while saving the report: {e}")

# Main function to orchestrate loading, generating, and saving the report
def main(csv_file_path: str, json_file_path: str) -> None:
    logging.info("Starting the report generation process.")
    records = load_service_records(csv_file_path)
    if records:
        report = generate_report(records)
        save_report_to_json(report, json_file_path)
    else:
        logging.warning("No records found to generate a report.")

# Example usage
if __name__ == "__main__":
    main('fuel_injector_services.csv', 'service_report.json')
```
