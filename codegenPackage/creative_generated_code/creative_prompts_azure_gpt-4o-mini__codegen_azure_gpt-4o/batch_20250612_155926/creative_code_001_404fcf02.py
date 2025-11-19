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
import datetime
from typing import List, Dict

# Define constants
DELIVERIES_FILE = "vehicle_deliveries.csv"  # Input CSV file containing delivery data
REPORT_FILE = "delivery_report.json"       # Output JSON file for the report

def read_deliveries(file_path: str) -> List[Dict[str, str]]:
    """
    Reads the delivery data from the specified CSV file and returns it as a list of dictionaries.
    
    :param file_path: Path to the CSV file containing delivery data.
    :return: List of dictionaries, each representing a row of delivery data.
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: Failed to read the file '{file_path}'. Details: {e}")
        return []

def generate_report(deliveries: List[Dict[str, str]]) -> Dict:
    """
    Generates a summary report based on the delivery data.
    
    :param deliveries: List of dictionaries containing delivery data.
    :return: Dictionary containing the aggregated report information.
    """
    report = {
        "total_deliveries": len(deliveries),
        "vehicles_by_type": {},  # Count vehicles by type
        "latest_delivery_date": None  # Latest delivery date
    }

    latest_date = None

    for delivery in deliveries:
        vehicle_type = delivery.get("Vehicle Type", "Unknown")
        delivery_date = delivery.get("Delivery Date", None)

        # Update vehicle type counts
        if vehicle_type in report["vehicles_by_type"]:
            report["vehicles_by_type"][vehicle_type] += 1
        else:
            report["vehicles_by_type"][vehicle_type] = 1

        # Update the latest delivery date
        if delivery_date:
            try:
                delivery_date_obj = datetime.datetime.strptime(delivery_date, "%Y-%m-%d")
                if latest_date is None or delivery_date_obj > latest_date:
                    latest_date = delivery_date_obj
            except ValueError:
                print(f"Warning: Incorrect date format in delivery data: {delivery_date}")

    report["latest_delivery_date"] = latest_date.strftime("%Y-%m-%d") if latest_date else None
    return report

def save_report(report: Dict, file_path: str) -> None:
    """
    Saves the report data as a JSON file.
    
    :param report: Dictionary containing the report data.
    :param file_path: Path to the output JSON file.
    """
    try:
        with open(file_path, mode='w', encoding='utf-8') as file:
            json.dump(report, file, indent=4)
        print(f"Report successfully saved to '{file_path}'.")
    except Exception as e:
        print(f"Error: Failed to save the report to '{file_path}'. Details: {e}")

def main():
    """
    Main function to automate the reporting of vehicle deliveries.
    """
    print("Reading vehicle deliveries data...")
    deliveries = read_deliveries(DELIVERIES_FILE)
    
    if not deliveries:
        print("No deliveries data found. Exiting.")
        return
    
    print("Generating report...")
    report = generate_report(deliveries)
    
    print("Saving report...")
    save_report(report, REPORT_FILE)

if __name__ == "__main__":
    main()
```
