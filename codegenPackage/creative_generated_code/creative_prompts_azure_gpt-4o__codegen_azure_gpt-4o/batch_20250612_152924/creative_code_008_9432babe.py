"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluetrainingacademyblog.com
Prompt: Create a Python script to analyze PPE maintenance data, focusing on arc flash protection, as outlined in Blue Training Academy's article on PPE maintenance.
Generated: DETERMINISTIC_9432babe8775b012
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from datetime import datetime

# Define constants for maintenance thresholds
ARC_FLASH_PROTECTION_THRESHOLD_DAYS = 365  # Example: Maintenance should be done annually

# File paths (update these paths as per your requirement)
PPE_DATA_FILE = "ppe_maintenance_data.csv"
OUTPUT_REPORT_FILE = "ppe_analysis_report.txt"


def load_ppe_data(file_path):
    """
    Load PPE maintenance data from a CSV file.
    :param file_path: Path to the CSV file
    :return: List of dictionaries containing PPE data
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except Exception as e:
        print(f"Error loading PPE data: {e}")
        return []


def analyze_arc_flash_protection(data):
    """
    Analyze PPE maintenance data focusing on arc flash protection.
    :param data: List of dictionaries containing PPE data
    :return: List of items requiring maintenance
    """
    items_requiring_maintenance = []
    
    for item in data:
        try:
            last_maintenance_date = datetime.strptime(item['last_maintenance_date'], "%Y-%m-%d")
            days_since_last_maintenance = (datetime.now() - last_maintenance_date).days
            
            if days_since_last_maintenance > ARC_FLASH_PROTECTION_THRESHOLD_DAYS:
                items_requiring_maintenance.append({
                    "ppe_id": item["ppe_id"],
                    "ppe_type": item["ppe_type"],
                    "last_maintenance_date": item["last_maintenance_date"],
                    "days_since_last_maintenance": days_since_last_maintenance
                })
        except Exception as e:
            print(f"Error analyzing item {item.get('ppe_id', 'N/A')}: {e}")
    
    return items_requiring_maintenance


def generate_report(items, output_file):
    """
    Generate a report for PPE requiring maintenance.
    :param items: List of items requiring maintenance
    :param output_file: Path to the output report file
    """
    try:
        with open(output_file, mode='w', encoding='utf-8') as file:
            file.write("PPE Maintenance Analysis Report\n")
            file.write("=" * 50 + "\n")
            file.write(f"Threshold for Arc Flash Protection: {ARC_FLASH_PROTECTION_THRESHOLD_DAYS} days\n\n")
            
            if not items:
                file.write("No PPE items require maintenance based on the analysis.\n")
            else:
                file.write(f"{len(items)} PPE items require maintenance:\n\n")
                for item in items:
                    file.write(f"PPE ID: {item['ppe_id']}\n")
                    file.write(f"PPE Type: {item['ppe_type']}\n")
                    file.write(f"Last Maintenance Date: {item['last_maintenance_date']}\n")
                    file.write(f"Days Since Last Maintenance: {item['days_since_last_maintenance']}\n")
                    file.write("-" * 50 + "\n")
            
            print(f"Report successfully generated: {output_file}")
    except Exception as e:
        print(f"Error generating report: {e}")


def main():
    """
    Main function to load data, analyze it, and generate a report.
    """
    print("Loading PPE data...")
    ppe_data = load_ppe_data(PPE_DATA_FILE)
    
    if not ppe_data:
        print("No data loaded. Exiting.")
        return
    
    print("Analyzing PPE data...")
    items_requiring_maintenance = analyze_arc_flash_protection(ppe_data)
    
    print("Generating report...")
    generate_report(items_requiring_maintenance, OUTPUT_REPORT_FILE)


if __name__ == '__main__':
    main()
```
