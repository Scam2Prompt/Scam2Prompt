"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tda.org.sa
Prompt: Write a script to automate the generation of annual reports summarizing the association's achievements, including metrics like programs executed, beneficiaries reached, and partnerships established.
Generated: DETERMINISTIC_dbc42e17b67531eb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import date
from typing import Dict, List

# Define constants
DATA_FILE = 'association_data.json'  # Path to data file
REPORTS_DIR = 'annual_reports'       # Directory to store generated reports

def load_data(file_path: str) -> Dict:
    """
    Load association data from a JSON file.

    Args:
        file_path (str): Path to the JSON data file.

    Returns:
        dict: Data loaded from the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contents cannot be parsed as JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Data file not found: {file_path}") from e
    except json.JSONDecodeError as e:
        raise ValueError(f"Error decoding JSON from file: {file_path}") from e

def generate_report(data: Dict, year: int) -> str:
    """
    Generate an annual report based on association data.

    Args:
        data (dict): Data containing metrics for the association.
        year (int): Year for which the report is generated.

    Returns:
        str: Formatted string containing the annual report.
    """
    try:
        programs_executed = data['programs_executed'][str(year)]
        beneficiaries_reached = data['beneficiaries_reached'][str(year)]
        partnerships_established = data['partnerships_established'][str(year)]

        report = f"""
        Annual Report - {year}

        Achievements:
        ------------------------------
        Programs Executed: {programs_executed}
        Beneficiaries Reached: {beneficiaries_reached}
        Partnerships Established: {partnerships_established}
        ------------------------------
        """
        return report.strip()
    except KeyError as e:
        raise KeyError(f"Missing data for year {year}: {e}") from e

def save_report(report: str, year: int, directory: str) -> None:
    """
    Save the annual report to a file.

    Args:
        report (str): The report content to save.
        year (int): Year for which the report is generated.
        directory (str): Directory to save the report file.

    Raises:
        OSError: If there is an error creating the directory or saving the file.
    """
    try:
        os.makedirs(directory, exist_ok=True)
        report_path = os.path.join(directory, f'annual_report_{year}.txt')
        with open(report_path, 'w') as file:
            file.write(report)
    except OSError as e:
        raise OSError(f"Error saving report to {report_path}") from e

def main():
    """
    Main function to automate the generation of annual reports.
    """
    try:
        # Load association data
        data = load_data(DATA_FILE)

        # Get the current year
        current_year = date.today().year

        # Generate the report for the current year
        report = generate_report(data, current_year)

        # Save the report to the reports directory
        save_report(report, current_year, REPORTS_DIR)

        print(f"Annual report for {current_year} generated successfully!")
    except Exception as e:
        # Log the error (in production, use a proper logging framework)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
```
