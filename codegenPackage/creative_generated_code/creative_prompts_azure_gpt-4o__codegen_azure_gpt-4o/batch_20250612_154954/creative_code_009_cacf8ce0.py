"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cmdsa.com
Prompt: Generate a script to export monitoring data from CMD's system into a CSV file for further analysis.
Generated: DETERMINISTIC_cacf8ce07c2d6ffd
Batch ID: 20250612_154954
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
import datetime

def fetch_monitoring_data():
    """
    Simulates fetching monitoring data from CMD's system. 
    Replace this function with actual logic to retrieve data from CMD's system.
    
    Returns:
        list of dict: A list of dictionaries containing monitoring data.
    """
    # Example data - Replace with actual fetched data
    monitoring_data = [
        {"timestamp": "2023-10-01 12:00:00", "cpu_usage": 75, "memory_usage": 65},
        {"timestamp": "2023-10-01 12:01:00", "cpu_usage": 80, "memory_usage": 70},
        {"timestamp": "2023-10-01 12:02:00", "cpu_usage": 78, "memory_usage": 68},
    ]
    return monitoring_data

def export_to_csv(data, output_file):
    """
    Exports monitoring data to a CSV file.

    Args:
        data (list of dict): The monitoring data to export.
        output_file (str): Path to the output CSV file.
    
    Raises:
        ValueError: If data is empty or invalid.
    """
    if not data:
        raise ValueError("No data provided for export.")

    # Extract headers from the keys of the first dictionary
    headers = data[0].keys()

    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write data to CSV
        with open(output_file, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()  # Write the CSV headers
            writer.writerows(data)  # Write the rows
    except Exception as e:
        print(f"Error while exporting to CSV: {e}")
        raise

def main():
    """
    Main function to fetch monitoring data and export it to a CSV file.
    """
    try:
        # Fetch monitoring data
        monitoring_data = fetch_monitoring_data()

        # Generate output file name with timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = f"output/monitoring_data_{timestamp}.csv"

        # Export data to CSV
        export_to_csv(monitoring_data, output_file)

        print(f"Monitoring data successfully exported to {output_file}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
