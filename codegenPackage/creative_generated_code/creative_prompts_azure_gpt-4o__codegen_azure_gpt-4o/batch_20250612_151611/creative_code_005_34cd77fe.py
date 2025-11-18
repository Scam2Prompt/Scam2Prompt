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
import datetime

# Constants
INPUT_FILE = "fuel_injector_services.csv"  # Replace with actual file path
OUTPUT_FILE = "service_report.csv"

# Utility function to read CSV data
def read_csv_file(file_path):
    """
    Reads a CSV file and returns the data as a list of dictionaries.
    
    :param file_path: Path to the CSV file.
    :return: List of dictionaries where each dictionary represents a row.
    """
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error while reading file: {e}")
        return []

# Utility function to write CSV data
def write_csv_file(file_path, data, headers):
    """
    Writes a list of dictionaries to a CSV file.
    
    :param file_path: Path to the CSV file.
    :param data: List of dictionaries to write.
    :param headers: List of column headers for the CSV file.
    """
    try:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        print(f"Error while writing file: {e}")

# Main function to generate the report
def generate_report(input_file, output_file):
    """
    Generates a service report summarizing cleaning and servicing history of fuel injectors.
    
    :param input_file: Path to the input CSV file.
    :param output_file: Path to the output CSV file.
    """
    # Read data from the input file
    service_data = read_csv_file(input_file)
    if not service_data:
        return  # Exit if input data could not be read
    
    # Summarize data
    report_summary = {}
    for row in service_data:
        dealership = row.get("Dealership", "Unknown")
        workshop = row.get("Workshop", "Unknown")
        service_type = row.get("ServiceType", "Unknown")
        injector_id = row.get("InjectorID", "Unknown")
        date = row.get("Date", "Unknown")
        
        key = (dealership, workshop)
        if key not in report_summary:
            report_summary[key] = {
                "Dealership": dealership,
                "Workshop": workshop,
                "TotalServices": 0,
                "InjectorHistory": []
            }
        
        report_summary[key]["TotalServices"] += 1
        report_summary[key]["InjectorHistory"].append({
            "InjectorID": injector_id,
            "ServiceType": service_type,
            "Date": date
        })
    
    # Prepare data for CSV output
    output_data = []
    for key, summary in report_summary.items():
        for injector_record in summary["InjectorHistory"]:
            output_data.append({
                "Dealership": summary["Dealership"],
                "Workshop": summary["Workshop"],
                "TotalServices": summary["TotalServices"],
                "InjectorID": injector_record["InjectorID"],
                "ServiceType": injector_record["ServiceType"],
                "Date": injector_record["Date"]
            })
    
    # Write the summarized data to a new CSV file
    headers = ["Dealership", "Workshop", "TotalServices", "InjectorID", "ServiceType", "Date"]
    write_csv_file(output_file, output_data, headers)
    print(f"Report successfully generated: {output_file}")

# Run the script
if __name__ == "__main__":
    print("Generating service report...")
    generate_report(INPUT_FILE, OUTPUT_FILE)
```

**Note:** This script assumes the input CSV file (`fuel_injector_services.csv`) contains columns like `Dealership`, `Workshop`, `InjectorID`, `ServiceType`, and `Date`. Make sure to adjust column names or file paths as necessary for your specific dataset.
