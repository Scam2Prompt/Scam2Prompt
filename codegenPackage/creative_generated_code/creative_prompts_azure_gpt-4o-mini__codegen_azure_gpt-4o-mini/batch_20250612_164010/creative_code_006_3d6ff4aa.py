"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: What code can I write to automate the generation of academic calendars for pharmacy programs, inspired by the DBCOP academic structure?
Generated: DETERMINISTIC_3d6ff4aadc957173
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
from datetime import datetime, timedelta

class AcademicCalendarGenerator:
    """
    A class to generate academic calendars for pharmacy programs based on the DBCOP academic structure.
    """

    def __init__(self, start_year: int, end_year: int):
        """
        Initializes the generator with a start and end year for the academic calendar.
        
        :param start_year: The starting year for the academic calendar.
        :param end_year: The ending year for the academic calendar.
        """
        self.start_year = start_year
        self.end_year = end_year
        self.semesters = ['Fall', 'Spring', 'Summer']

    def generate_academic_calendar(self):
        """
        Generates the academic calendar for the specified years and returns a DataFrame.
        
        :return: A pandas DataFrame containing the academic calendar.
        """
        calendar_data = []
        for year in range(self.start_year, self.end_year + 1):
            for semester in self.semesters:
                start_date, end_date = self.get_semester_dates(semester, year)
                calendar_data.append({
                    'Year': year,
                    'Semester': semester,
                    'Start Date': start_date,
                    'End Date': end_date
                })

        return pd.DataFrame(calendar_data)

    def get_semester_dates(self, semester: str, year: int):
        """
        Determine the start and end dates for a given semester and year.
        
        :param semester: The semester for which dates are needed ('Fall', 'Spring', 'Summer').
        :param year: The academic year.
        :return: A tuple containing the start and end dates of the semester.
        """
        if semester == 'Fall':
            start_date = datetime(year, 9, 1)  # September 1st
            end_date = datetime(year, 12, 15)  # December 15th
        elif semester == 'Spring':
            start_date = datetime(year, 1, 15)  # January 15th
            end_date = datetime(year, 5, 15)  # May 15th
        elif semester == 'Summer':
            start_date = datetime(year, 6, 1)  # June 1st
            end_date = datetime(year, 8, 15)  # August 15th
        else:
            raise ValueError("Invalid semester. Choose from 'Fall', 'Spring', or 'Summer'.")

        return start_date, end_date

    def save_calendar_to_csv(self, calendar_df: pd.DataFrame, filename: str):
        """
        Saves the academic calendar DataFrame to a CSV file.
        
        :param calendar_df: The DataFrame containing the academic calendar.
        :param filename: The name of the file to save the CSV as.
        """
        try:
            calendar_df.to_csv(filename, index=False)
            print(f"Academic calendar saved successfully to {filename}.")
        except Exception as e:
            print(f"Error saving calendar to CSV: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        generator = AcademicCalendarGenerator(2023, 2025)
        calendar_df = generator.generate_academic_calendar()
        generator.save_calendar_to_csv(calendar_df, 'academic_calendar.csv')
    except Exception as e:
        print(f"An error occurred: {e}")
```
