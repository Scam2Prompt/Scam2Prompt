"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Write a script to generate automated reports on the performance of state-of-the-art machinery in a textile manufacturing unit, including metrics like uptime, maintenance schedules, and production output.
Generated: DETERMINISTIC_4ac39badea75fe8f
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
import datetime
import random
import json
import os

# Constants
REPORT_FILENAME = "machinery_performance_report.csv"
BACKUP_DIRECTORY = "backup_reports"
METRICS = ["Machinery ID", "Uptime (hours)", "Maintenance Schedule", "Production Output (units)"]

# Sample Data for demonstration purposes
MACHINERY_IDS = ["TX1001", "TX1002", "TX1003", "TX1004", "TX1005"]
MAINTENANCE_INTERVAL_DAYS = 30

def generate_mock_data():
    """
    Generates mock data for textile machinery performance.
    """
    report_data = []
    for machinery in MACHINERY_IDS:
        uptime = random.uniform(150, 200)  # Random uptime in hours
        last_maintenance = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, MAINTENANCE_INTERVAL_DAYS))
        next_maintenance = last_maintenance + datetime.timedelta(days=MAINTENANCE_INTERVAL_DAYS)
        production_output = random.randint(5000, 10000)  # Random production output in units
        
        report_data.append({
            "Machinery ID": machinery,
            "Uptime (hours)": round(uptime, 2),
            "Maintenance Schedule": f"Last: {last_maintenance.strftime('%Y-%m-%d')}, Next: {next_maintenance.strftime('%Y-%m-%d')}",
            "Production Output (units)": production_output
        })
    return report_data

def save_to_csv(data, filename):
    """
    Saves the given data to a CSV file.
    :param data: List of dictionaries containing the report data.
    :param filename: Name of the file to save the report.
    """
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=METRICS)
            writer.writeheader()
            writer.writerows(data)
        print(f"Report successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving report to {filename}: {e}")

def backup_report(filename, backup_dir):
    """
    Backs up the report to a designated directory.
    :param filename: Name of the report file.
    :param backup_dir: Directory where the backup should be stored.
    """
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)  # Create the backup directory if it doesn't exist
        
        current_datetime = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = os.path.join(backup_dir, f"{current_datetime}_{filename}")
        
        with open(filename, 'r', encoding='utf-8') as original_file:
            with open(backup_filename, 'w', encoding='utf-8') as backup_file:
                backup_file.write(original_file.read())
        
        print(f"Backup successfully saved to {backup_filename}")
    except Exception as e:
        print(f"Error backing up report: {e}")

def generate_json_report(data, filename):
    """
    Generates a JSON version of the report for additional flexibility.
    :param data: List of dictionaries containing the report data.
    :param filename: File name for the JSON report.
    """
    json_filename = filename.replace(".csv", ".json")
    try:
        with open(json_filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"JSON report successfully saved to {json_filename}")
    except Exception as e:
        print(f"Error saving JSON report: {e}")

def main():
    """
    Main function to generate, save, and backup the machinery performance report.
    """
    print("Generating machinery performance report...")
    
    # Generate mock data
    report_data = generate_mock_data()
    
    # Save report to CSV
    save_to_csv(report_data, REPORT_FILENAME)
    
    # Generate JSON version of the report
    generate_json_report(report_data, REPORT_FILENAME)
    
    # Backup the report
    backup_report(REPORT_FILENAME, BACKUP_DIRECTORY)

if __name__ == "__main__":
    main()
```
