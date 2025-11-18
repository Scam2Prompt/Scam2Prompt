"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Write a Python script to generate a report summarizing enrollment statistics for ISIV's programs, grouped by categories like "Carreras de Nivel Superior" and "Programas Ejecutivos."
Generated: DETERMINISTIC_aba5c99cfc165089
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Loads enrollment data from a CSV file.

    :param file_path: str - Path to the CSV file containing enrollment data
    :return: DataFrame - Loaded data as a pandas DataFrame
    """
    try:
        data = pd.read_csv(file_path)
        logging.info("Data loaded successfully from %s", file_path)
        return data
    except FileNotFoundError as e:
        logging.error("File not found: %s", e)
        raise
    except pd.errors.EmptyDataError as e:
        logging.error("No data found: %s", e)
        raise
    except Exception as e:
        logging.error("An error occurred while loading data: %s", e)
        raise

def generate_report(data):
    """
    Generates a report summarizing enrollment statistics.

    :param data: DataFrame - Data containing enrollment information
    :return: DataFrame - Summary report of enrollment statistics
    """
    try:
        # Group the data by program category and count enrollments
        report = data.groupby('Category')['Enrollments'].sum().reset_index()
        logging.info("Report generated successfully")
        return report
    except KeyError as e:
        logging.error("Missing expected column in data: %s", e)
        raise
    except Exception as e:
        logging.error("An error occurred while generating the report: %s", e)
        raise

def save_report(report, output_path):
    """
    Saves the summary report to a CSV file.

    :param report: DataFrame - Summary report of enrollment statistics
    :param output_path: str - Path to save the report CSV file
    """
    try:
        report.to_csv(output_path, index=False)
        logging.info("Report saved successfully to %s", output_path)
    except Exception as e:
        logging.error("An error occurred while saving the report: %s", e)
        raise

def main(input_file, output_file):
    """
    Main function to load data, generate the report, and save it.

    :param input_file: str - Path to the input CSV file containing enrollment data
    :param output_file: str - Path to the output CSV file for the summary report
    """
    data = load_data(input_file)
    report = generate_report(data)
    save_report(report, output_file)

if __name__ == "__main__":
    # Define input and output file paths
    input_file_path = 'enrollment_data.csv'  # Change as necessary
    output_file_path = 'enrollment_report.csv'  # Change as necessary

    # Run the main process
    main(input_file_path, output_file_path)
```
