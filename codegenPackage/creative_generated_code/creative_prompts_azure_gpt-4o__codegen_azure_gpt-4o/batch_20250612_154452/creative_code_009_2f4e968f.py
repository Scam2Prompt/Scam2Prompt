"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omegaenergy.co
Prompt: Generate a script to automate the creation of sustainability reports, integrating data from Omega Energy's ESG practices and ISO compliance.
Generated: DETERMINISTIC_2f4e968fd3254838
Batch ID: 20250612_154452
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
import os
from datetime import datetime

# Constants
OMEGA_DATA_FILE = "omega_esg_data.json"  # Path to Omega Energy ESG data file (JSON format)
ISO_COMPLIANCE_FILE = "iso_compliance.csv"  # Path to ISO compliance data file (CSV format)
REPORT_OUTPUT_FILE = "sustainability_report.txt"  # Path for the generated sustainability report

def load_omega_esg_data(file_path):
    """
    Load Omega Energy's ESG data from a JSON file.

    :param file_path: Path to the JSON file containing ESG data
    :return: A dictionary with ESG data
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"ESG data file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in ESG data file: {file_path}")

def load_iso_compliance_data(file_path):
    """
    Load ISO compliance data from a CSV file.

    :param file_path: Path to the CSV file containing ISO compliance data
    :return: A list of dictionaries, where each dictionary represents a row of data
    """
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"ISO compliance data file not found: {file_path}")
    except csv.Error:
        raise ValueError(f"Invalid CSV format in ISO compliance data file: {file_path}")

def generate_sustainability_report(esg_data, iso_data, output_file):
    """
    Generate a sustainability report based on ESG and ISO data.

    :param esg_data: Dictionary containing ESG data
    :param iso_data: List of dictionaries containing ISO compliance data
    :param output_file: Path to save the generated report
    """
    try:
        with open(output_file, 'w') as file:
            file.write("Sustainability Report\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("=" * 50 + "\n\n")
            
            # Write ESG practices
            file.write("Omega Energy ESG Practices:\n")
            for key, value in esg_data.items():
                file.write(f"  {key}: {value}\n")
            file.write("\n")
            
            # Write ISO compliance data
            file.write("ISO Compliance Data:\n")
            for row in iso_data:
                file.write("  " + ", ".join(f"{key}: {value}" for key, value in row.items()) + "\n")
            file.write("\n")
            
            file.write("=" * 50 + "\n")
            file.write("End of Report\n")
        
        print(f"Sustainability report successfully generated: {output_file}")
    except IOError:
        raise IOError(f"Failed to write the report to file: {output_file}")

def main():
    """
    Main function to orchestrate the report generation process.
    """
    try:
        # Load ESG and ISO data
        esg_data = load_omega_esg_data(OMEGA_DATA_FILE)
        iso_data = load_iso_compliance_data(ISO_COMPLIANCE_FILE)

        # Generate the sustainability report
        generate_sustainability_report(esg_data, iso_data, REPORT_OUTPUT_FILE)

    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
