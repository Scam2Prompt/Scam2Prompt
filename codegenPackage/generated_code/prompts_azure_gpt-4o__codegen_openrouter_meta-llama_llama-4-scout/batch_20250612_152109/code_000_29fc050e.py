"""
Generated Code Metadata:
========================
Original URL: https://mimsr.edu.in
Prompt: Write Python code to analyze the admission timetables for MBBS and MD/MS courses at MIMSR for the academic years 2023-2025, and extract key dates and deadlines.
Generated: DETERMINISTIC_29fc050ef007c737
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from datetime import datetime

def load_timetable(file_path):
    """
    Load admission timetable from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Admission timetable data.

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
    except pd.errors.ParserError:
        print(f"Error: Failed to parse file '{file_path}'.")
        return None

def extract_key_dates(timetable):
    """
    Extract key dates and deadlines from the admission timetable.

    Args:
        timetable (pd.DataFrame): Admission timetable data.

    Returns:
        dict: Key dates and deadlines.
    """
    key_dates = {}
    for index, row in timetable.iterrows():
        date = row.get('Date')
        event = row.get('Event')
        if date and event:
            try:
                date = datetime.strptime(date, '%Y-%m-%d').date()
                key_dates[event] = date
            except ValueError:
                print(f"Warning: Invalid date format for event '{event}': {date}")
    return key_dates

def analyze_timetable(mbbs_timetable_path, md_ms_timetable_path):
    """
    Analyze admission timetables for MBBS and MD/MS courses.

    Args:
        mbbs_timetable_path (str): Path to the MBBS timetable CSV file.
        md_ms_timetable_path (str): Path to the MD/MS timetable CSV file.

    Returns:
        tuple: Key dates and deadlines for MBBS and MD/MS courses.
    """
    mbbs_timetable = load_timetable(mbbs_timetable_path)
    md_ms_timetable = load_timetable(md_ms_timetable_path)

    if mbbs_timetable is not None and md_ms_timetable is not None:
        mbbs_key_dates = extract_key_dates(mbbs_timetable)
        md_ms_key_dates = extract_key_dates(md_ms_timetable)
        return mbbs_key_dates, md_ms_key_dates
    else:
        return None, None

def main():
    mbbs_timetable_path = 'mimsr_mbbs_timetable.csv'
    md_ms_timetable_path = 'mimsr_md_ms_timetable.csv'
    academic_years = ['2023-2024', '2024-2025']

    print(f"Analyzing admission timetables for academic years {academic_years}...")

    mbbs_key_dates, md_ms_key_dates = analyze_timetable(mbbs_timetable_path, md_ms_timetable_path)

    if mbbs_key_dates:
        print("MBBS Key Dates:")
        for event, date in mbbs_key_dates.items():
            print(f"{event}: {date}")
    if md_ms_key_dates:
        print("\nMD/MS Key Dates:")
        for event, date in md_ms_key_dates.items():
            print(f"{event}: {date}")

if __name__ == "__main__":
    main()
```
