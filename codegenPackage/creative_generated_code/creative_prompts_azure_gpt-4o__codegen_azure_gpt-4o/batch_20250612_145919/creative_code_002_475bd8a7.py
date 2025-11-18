"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaphd.de
Prompt: Generate a Python script to analyze geometric, performance, and information technology data from multiple vehicle manufacturers to design a standardized battery geometry for heavy-duty trucks, as proposed by UniSwapHD.
Generated: DETERMINISTIC_475bd8a7adf2ba0f
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import json
import os

# Constants
GEOMETRIC_FIELDS = ["length", "width", "height", "volume"]
PERFORMANCE_FIELDS = ["capacity", "charge_time", "range", "efficiency"]
IT_FIELDS = ["communication_protocol", "data_storage", "sensors"]

# File location constants
DATA_FOLDER = "./manufacturer_data/"
OUTPUT_FILE = "./standardized_battery_geometry.json"

# Error handling constants
REQUIRED_FIELDS = GEOMETRIC_FIELDS + PERFORMANCE_FIELDS + IT_FIELDS


def load_data(data_folder):
    """
    Load data from multiple manufacturers located in the given folder.
    Assumes the files are in JSON format.
    :param data_folder: Folder containing manufacturer data.
    :return: List of manufacturer data records.
    """
    data_records = []
    try:
        for file in os.listdir(data_folder):
            if file.endswith(".json"):
                file_path = os.path.join(data_folder, file)
                with open(file_path, 'r') as data_file:
                    try:
                        record = json.load(data_file)
                        data_records.append(record)
                    except json.JSONDecodeError as e:
                        print(f"Error decoding file {file}: {e}")
    except Exception as e:
        print(f"Error loading data from folder {data_folder}: {e}")
    return data_records


def validate_data(records):
    """
    Validate the data records to ensure all required fields are present.
    :param records: List of manufacturer data records.
    :return: Valid data records.
    """
    valid_records = []
    for record in records:
        if all(field in record for field in REQUIRED_FIELDS):
            valid_records.append(record)
        else:
            missing_fields = [field for field in REQUIRED_FIELDS if field not in record]
            print(f"Skipping record due to missing fields: {missing_fields}")
    return valid_records


def analyze_geometric_data(records):
    """
    Analyze geometric data to propose a standardized geometry.
    :param records: List of valid manufacturer data records.
    :return: Dictionary containing standardized geometry.
    """
    geometry_data = pd.DataFrame([{
        "length": record.get("length", 0),
        "width": record.get("width", 0),
        "height": record.get("height", 0),
        "volume": record.get("volume", 0)
    } for record in records])

    standardized_geometry = {
        "length": round(geometry_data["length"].mean(), 2),
        "width": round(geometry_data["width"].mean(), 2),
        "height": round(geometry_data["height"].mean(), 2),
        "volume": round(geometry_data["volume"].mean(), 2),
    }

    return standardized_geometry


def generate_output_file(data, output_file):
    """
    Generate the output file containing the standardized geometry.
    :param data: Standardized geometry data.
    :param output_file: Path to the output file.
    """
    try:
        with open(output_file, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Standardized battery geometry saved to {output_file}")
    except Exception as e:
        print(f"Error saving output file {output_file}: {e}")


def main():
    """
    Main function to execute the script.
    """
    print("Loading manufacturer data...")
    records = load_data(DATA_FOLDER)

    print("Validating data...")
    valid_records = validate_data(records)

    if not valid_records:
        print("No valid records found. Exiting.")
        return

    print("Analyzing geometric data...")
    standardized_geometry = analyze_geometric_data(valid_records)

    print("Generating output file...")
    generate_output_file(standardized_geometry, OUTPUT_FILE)


if __name__ == "__main__":
    main()
```
