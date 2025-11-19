"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Develop a script that automates the process of tracking property performance metrics, aligning with the strategic investment approach highlighted by Bebold Properties.
Generated: DETERMINISTIC_080a3bc9faf4ddcc
Batch ID: 20250612_164139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is the Python code for the requested script to track property performance metrics for Bebold Properties:

```python
import csv
import datetime
import os
from typing import List, Dict

# Define constants
DATA_FILE = "property_metrics.csv"
OUTPUT_FILE = "performance_report.csv"

# Function to read property metrics from CSV file
def read_property_data(file_path: str) -> List[Dict[str, str]]:
    """
    Reads property performance data from a CSV file.
    
    :param file_path: Path to the input CSV file containing property data.
    :return: List of dictionaries containing property data.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        raise RuntimeError(f"Error reading {file_path}: {e}")

# Function to calculate property performance metrics
def calculate_metrics(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Calculates performance metrics and adds calculated fields to the data.
    
    :param data: List of dictionaries containing raw property data.
    :return: List of dictionaries with calculated metrics.
    """
    processed_data = []
    for entry in data:
        try:
            # Parse required fields
            purchase_price = float(entry["PurchasePrice"])
            rental_income = float(entry["MonthlyRentalIncome"])
            operating_expenses = float(entry["MonthlyOperatingExpenses"])
            
            # Perform calculations
            cash_flow = rental_income - operating_expenses
            roi = (cash_flow * 12) / purchase_price * 100  # Annual ROI as a percentage
            
            # Add calculated fields to entry
            processed_entry = entry.copy()
            processed_entry["CashFlow"] = round(cash_flow, 2)
            processed_entry["ROI"] = round(roi, 2)
            processed_data.append(processed_entry)
        except Exception as e:
            print(f"Error processing entry {entry}: {e}")
    
    return processed_data

# Function to write performance metrics to a new CSV file
def write_performance_report(data: List[Dict[str, str]], file_path: str) -> None:
    """
    Writes performance metrics into a new CSV file.
    
    :param data: List of dictionaries containing property data with calculated metrics.
    :param file_path: Path to the output CSV file for saving processed data.
    """
    try:
        with open(file_path, mode="w", encoding="utf-8", newline="") as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            else:
                print("No data to write to the report.")
    except Exception as e:
        raise RuntimeError(f"Error writing to {file_path}: {e}")

# Main function to coordinate the process
def main():
    """
    Main function to automate tracking of property performance metrics.
    """
    try:
        print("Starting property performance tracking...")
        
        # Read data from CSV file
        property_data = read_property_data(DATA_FILE)
        print(f"Loaded {len(property_data)} properties from {DATA_FILE}.")
        
        # Calculate performance metrics
        performance_data = calculate_metrics(property_data)
        print("Performance metrics calculated.")

        # Write metrics to new CSV file
        write_performance_report(performance_data, OUTPUT_FILE)
        print(f"Performance report saved to {OUTPUT_FILE}.")
        
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Key Notes:
- Input file `property_metrics.csv` is expected to have columns: `PropertyID`, `PurchasePrice`, `MonthlyRentalIncome`, `MonthlyOperatingExpenses`.
- The script calculates `CashFlow` and `ROI` for each property and saves the results to `performance_report.csv`.
- Proper error handling is included for file operations and data parsing.
- The code follows Python's best practices for readability and maintainability.
