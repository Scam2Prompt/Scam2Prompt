"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geosatelites.com
Prompt: Write a script in Python to automate calibration data processing for equipment like total stations and electronic theodolites, as offered by Geosatelites.
Generated: DETERMINISTIC_a055d2bd3c20792c
Batch ID: 20250612_145136
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="calibration_processing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data(file_path):
    """
    Load calibration data from a given file (CSV or JSON).
    Args:
        file_path (str): Path to the calibration data file.
    Returns:
        list[dict]: List of calibration records.
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file format is unsupported.
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")

    file_extension = os.path.splitext(file_path)[1].lower()
    try:
        if file_extension == ".csv":
            logging.info(f"Loading CSV file: {file_path}")
            with open(file_path, mode="r", encoding="utf-8") as csv_file:
                reader = csv.DictReader(csv_file)
                return [row for row in reader]
        elif file_extension == ".json":
            logging.info(f"Loading JSON file: {file_path}")
            with open(file_path, mode="r", encoding="utf-8") as json_file:
                return json.load(json_file)
        else:
            logging.error(f"Unsupported file format: {file_extension}")
            raise ValueError("Unsupported file format. Only CSV and JSON are supported.")
    except Exception as e:
        logging.error(f"Error loading file: {e}")
        raise

def process_calibration_data(calibration_data):
    """
    Process calibration data (e.g., validating and calculating necessary metrics).
    Args:
        calibration_data (list[dict]): List of calibration records.
    Returns:
        list[dict]: List of processed calibration records.
    """
    processed_data = []
    for record in calibration_data:
        try:
            # Example validation: Check if necessary fields exist
            required_fields = ["equipment_id", "calibration_date", "measurement_1", "measurement_2"]
            for field in required_fields:
                if field not in record or not record[field]:
                    raise ValueError(f"Missing or invalid field: {field} in record {record}")

            # Parse calibration date
            calibration_date = datetime.strptime(record["calibration_date"], "%Y-%m-%d")
            record["calibration_date"] = calibration_date.strftime("%Y-%m-%d")

            # Example calculation: Average of two measurements
            measurement_1 = float(record["measurement_1"])
            measurement_2 = float(record["measurement_2"])
            record["average_measurement"] = round((measurement_1 + measurement_2) / 2, 2)

            processed_data.append(record)
        except Exception as e:
            logging.warning(f"Error processing record {record}: {e}")
            continue  # Skip invalid records
    return processed_data

def save_processed_data(processed_data, output_file):
    """
    Save processed calibration data to a file (CSV).
    Args:
        processed_data (list[dict]): List of processed calibration records.
        output_file (str): Path to the output file.
    """
    try:
        logging.info(f"Saving processed data to {output_file}")
        with open(output_file, mode="w", encoding="utf-8", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=processed_data[0].keys())
            writer.writeheader()
            writer.writerows(processed_data)
        logging.info("Data saved successfully.")
    except Exception as e:
        logging.error(f"Error saving processed data: {e}")
        raise

def main():
    """
    Main function to automate calibration data processing.
    """
    input_file = "calibration_data.csv"  # Replace with your input file path
    output_file = "processed_calibration_data.csv"  # Replace with your output file path

    try:
        # Step 1: Load data
        calibration_data = load_data(input_file)

        # Step 2: Process data
        processed_data = process_calibration_data(calibration_data)

        # Step 3: Save processed data
        save_processed_data(processed_data, output_file)

        logging.info("Calibration data processing completed successfully.")
    except Exception as e:
        logging.error(f"Failed to process calibration data: {e}")

if __name__ == "__main__":
    main()
```
