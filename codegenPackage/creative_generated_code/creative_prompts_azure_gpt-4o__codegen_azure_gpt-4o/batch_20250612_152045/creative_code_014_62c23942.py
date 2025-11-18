"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mdatechsys.com
Prompt: Create a Python script for generating ROI reports, based on the ROI software solutions mentioned by MDA Tech Sys.
Generated: DETERMINISTIC_62c2394271f743a2
Batch ID: 20250612_152045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ROI Report Generator Script
This script generates ROI (Return on Investment) reports based on input data
from MDA Tech Sys ROI software solutions. It processes the data, calculates ROI metrics, 
and outputs the results in a structured format.
"""

import csv
import os
from datetime import datetime
from typing import List, Dict

# Define constants for the report
DEFAULT_INPUT_FILE = "roi_data.csv"
DEFAULT_OUTPUT_FILE = "roi_report.csv"
DATE_FORMAT = "%Y-%m-%d"


def load_data(file_path: str) -> List[Dict[str, str]]:
    """
    Load ROI data from a CSV file.
    :param file_path: Path to the input CSV file
    :return: List of data rows as dictionaries
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file '{file_path}' not found.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while loading data: {str(e)}")


def calculate_roi(data: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Calculate ROI metrics for each record in the data.
    :param data: List of dictionaries containing input data
    :return: List of dictionaries containing input data and calculated ROI metrics
    """
    results = []
    for row in data:
        try:
            # Extract required fields
            investment = float(row.get("Investment", "0.0"))
            revenue = float(row.get("Revenue", "0.0"))

            # Calculate ROI (Return on Investment formula: ROI = (Revenue - Investment) / Investment * 100)
            if investment > 0:
                roi = ((revenue - investment) / investment) * 100
            else:
                roi = 0.0

            # Append calculated ROI to the row data
            row["ROI (%)"] = round(roi, 2)
            results.append(row)
        except ValueError:
            raise ValueError(f"Invalid numeric values in row: {row}")
    return results


def save_report(data: List[Dict[str, str]], file_path: str) -> None:
    """
    Save the ROI report to a CSV file.
    :param data: List of dictionaries containing ROI report data
    :param file_path: Path to the output CSV file
    """
    try:
        with open(file_path, mode='w', encoding='utf-8', newline='') as file:
            # Get headers from data keys
            headers = data[0].keys() if data else []
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
    except Exception as e:
        raise RuntimeError(f"An error occurred while saving the report: {str(e)}")


def generate_roi_report(input_file: str = DEFAULT_INPUT_FILE, output_file: str = DEFAULT_OUTPUT_FILE) -> None:
    """
    Main function to generate the ROI report.
    :param input_file: Path to the input CSV file
    :param output_file: Path to the output CSV file
    """
    try:
        print(f"Loading data from '{input_file}'...")
        data = load_data(input_file)

        print("Calculating ROI metrics...")
        report_data = calculate_roi(data)

        print(f"Saving report to '{output_file}'...")
        save_report(report_data, output_file)

        print("ROI report generated successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    # Run the ROI report generator
    input_file_path = input("Enter input file path (default: roi_data.csv): ").strip() or DEFAULT_INPUT_FILE
    output_file_path = input("Enter output file path (default: roi_report.csv): ").strip() or DEFAULT_OUTPUT_FILE
    
    generate_roi_report(input_file_path, output_file_path)
```
