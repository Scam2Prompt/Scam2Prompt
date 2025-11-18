"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mimsr.edu.in
Prompt: Recommend libraries or APIs to automate the generation of academic calendars for MIMSR, including integration of clinical postings and AETCOM teaching modules.
Generated: DETERMINISTIC_24ee2777d6789240
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pandas as pd
from datetime import datetime, timedelta
import calendar

# Function to generate an academic calendar
def generate_academic_calendar(start_date, end_date, clinical_postings, aetcom_modules):
    """
    Generate an academic calendar with clinical postings and AETCOM teaching modules.

    Parameters:
        start_date (str): Start date of the calendar (format: 'YYYY-MM-DD').
        end_date (str): End date of the calendar (format: 'YYYY-MM-DD').
        clinical_postings (list of dict): List of clinical postings with 'name', 'start_date', and 'end_date'.
        aetcom_modules (list of dict): List of AETCOM modules with 'title', 'date', and 'duration'.

    Returns:
        pd.DataFrame: Academic calendar with clinical postings and AETCOM modules.
    """

    try:
        # Validate and parse dates
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        if start_date > end_date:
            raise ValueError("Start date cannot be after end date.")

        # Generate calendar date range
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        calendar_df = pd.DataFrame(dates, columns=['Date'])
        calendar_df['Day'] = calendar_df['Date'].dt.day_name()

        # Add clinical postings to the calendar
        for posting in clinical_postings:
            posting_start = datetime.strptime(posting['start_date'], "%Y-%m-%d")
            posting_end = datetime.strptime(posting['end_date'], "%Y-%m-%d")
            if posting_start > posting_end:
                raise ValueError(f"Clinical posting '{posting['name']}' has invalid dates.")
            calendar_df.loc[
                (calendar_df['Date'] >= posting_start) & (calendar_df['Date'] <= posting_end),
                'Activity'
            ] = f"Clinical Posting: {posting['name']}"

        # Add AETCOM modules to the calendar
        for module in aetcom_modules:
            module_date = datetime.strptime(module['date'], "%Y-%m-%d")
            if module_date < start_date or module_date > end_date:
                raise ValueError(f"AETCOM module '{module['title']}' has a date outside the calendar range.")
            calendar_df.loc[calendar_df['Date'] == module_date, 'Activity'] = f"AETCOM Module: {module['title']} ({module['duration']} hours)"

        # Fill empty activities with 'Regular Academic Day'
        calendar_df['Activity'].fillna('Regular Academic Day', inplace=True)

        return calendar_df

    except Exception as e:
        print(f"Error while generating academic calendar: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Input data
    start_date = "2024-01-01"
    end_date = "2024-06-30"
    clinical_postings = [
        {"name": "Medicine", "start_date": "2024-01-15", "end_date": "2024-02-15"},
        {"name": "Surgery", "start_date": "2024-03-01", "end_date": "2024-03-31"}
    ]
    aetcom_modules = [
        {"title": "Communication Skills", "date": "2024-02-20", "duration": 3},
        {"title": "Ethics in Medicine", "date": "2024-04-10", "duration": 2}
    ]

    # Generate calendar
    academic_calendar = generate_academic_calendar(start_date, end_date, clinical_postings, aetcom_modules)

    # Save to Excel
    if academic_calendar is not None:
        academic_calendar.to_excel("academic_calendar.xlsx", index=False)
        print("Academic calendar generated and saved to 'academic_calendar.xlsx'.")
```
