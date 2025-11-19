"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Write a program to generate summary reports for APBD realization data, similar to the "Info Realisasi APBD" feature described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_9384c01e8db234b8
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# apbd_report_generator.py

import pandas as pd
from datetime import datetime

def load_apbd_data(file_path):
    """
    Load APBD realization data from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded APBD data.

    Raises:
        FileNotFoundError: If the file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
        pd.errors.ParserError: If the file is malformed.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return None
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse file '{file_path}': {e}")
        return None

def generate_summary_report(apbd_data):
    """
    Generate a summary report for APBD realization data.

    Args:
        apbd_data (pd.DataFrame): APBD realization data.

    Returns:
        dict: Summary report.

    Raises:
        ValueError: If the input data is invalid.
    """
    if apbd_data is None or apbd_data.empty:
        raise ValueError("Invalid input data")

    # Calculate total budget and realization
    total_budget = apbd_data['budget'].sum()
    total_realization = apbd_data['realization'].sum()

    # Calculate percentage of realization
    realization_percentage = (total_realization / total_budget) * 100 if total_budget > 0 else 0

    # Create summary report
    report = {
        'total_budget': total_budget,
        'total_realization': total_realization,
        'realization_percentage': realization_percentage
    }

    return report

def save_report_to_file(report, file_path):
    """
    Save the summary report to a file.

    Args:
        report (dict): Summary report.
        file_path (str): Path to the output file.

    Raises:
        IOError: If the file cannot be written.
    """
    try:
        with open(file_path, 'w') as f:
            f.write("Summary Report\n")
            f.write("==============\n")
            f.write(f"Total Budget: {report['total_budget']}\n")
            f.write(f"Total Realization: {report['total_realization']}\n")
            f.write(f"Realization Percentage: {report['realization_percentage']:.2f}%\n")
    except IOError as e:
        print(f"Error: Failed to write to file '{file_path}': {e}")

def main():
    # Load APBD data from CSV file
    apbd_data = load_apbd_data('apbd_data.csv')

    if apbd_data is not None:
        # Generate summary report
        report = generate_summary_report(apbd_data)

        # Save report to file
        save_report_to_file(report, 'apbd_summary_report.txt')

if __name__ == '__main__':
    main()
```

```python
# apbd_data.csv example

budget,realization
1000000,500000
2000000,1000000
3000000,1500000
```

```markdown
# Running the code

## Requirements

* Python 3.8+
* pandas library (`pip install pandas`)

## Usage

1. Save the code in a file named `apbd_report_generator.py`.
2. Create a CSV file named `apbd_data.csv` with the APBD realization data.
3. Run the code using `python apbd_report_generator.py`.
4. The summary report will be saved to a file named `apbd_summary_report.txt`.
```
