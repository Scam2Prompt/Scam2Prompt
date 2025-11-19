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
import datetime
from calendar import monthrange

class AcademicCalendarGenerator:
    """
    A class to generate academic calendars for pharmacy programs.
    Inspired by the DBCOP academic structure.
    """

    def __init__(self, start_date, end_date):
        """
        Initialize the calendar generator with the academic year start and end dates.

        :param start_date: The beginning of the academic year (YYYY-MM-DD).
        :param end_date: The end of the academic year (YYYY-MM-DD).
        """
        try:
            self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if self.start_date >= self.end_date:
            raise ValueError("Start date must be earlier than end date.")

    def generate_calendar(self):
        """
        Generate the academic calendar based on the specified dates.

        :return: A dictionary containing academic calendar details.
        """
        calendar = {
            "Semester 1": self._generate_semester(self.start_date, self.start_date + datetime.timedelta(days=90)),
            "Semester 2": self._generate_semester(self.start_date + datetime.timedelta(days=91), self.start_date + datetime.timedelta(days=180)),
            "Semester 3": self._generate_semester(self.start_date + datetime.timedelta(days=181), self.end_date),
        }
        return calendar

    def _generate_semester(self, start_date, end_date):
        """
        Generate details for a single semester.

        :param start_date: Start date of the semester.
        :param end_date: End date of the semester.
        :return: A dictionary containing the semester details.
        """
        if end_date > self.end_date:
            end_date = self.end_date
        
        # Calculate number of weeks in the semester
        num_weeks = (end_date - start_date).days // 7

        semester = {
            "Start Date": start_date.strftime('%Y-%m-%d'),
            "End Date": end_date.strftime('%Y-%m-%d'),
            "Number of Weeks": num_weeks,
            "Holidays": self._get_holidays(start_date, end_date)
        }
        return semester

    def _get_holidays(self, start_date, end_date):
        """
        Generate a list of holidays within the semester.

        :param start_date: Start date of the semester.
        :param end_date: End date of the semester.
        :return: A list of holiday dates.
        """
        holidays = []
        current_date = start_date

        # Example: Add weekends as holidays
        while current_date <= end_date:
            if current_date.weekday() in (5, 6):  # Saturday and Sunday
                holidays.append(current_date.strftime('%Y-%m-%d'))
            current_date += datetime.timedelta(days=1)
        
        return holidays

if __name__ == "__main__":
    try:
        start_date = input("Enter academic year start date (YYYY-MM-DD): ")
        end_date = input("Enter academic year end date (YYYY-MM-DD): ")

        generator = AcademicCalendarGenerator(start_date, end_date)
        calendar = generator.generate_calendar()

        print("\nGenerated Academic Calendar:")
        for semester, details in calendar.items():
            print(f"\n{semester}:")
            for key, value in details.items():
                print(f"  {key}: {value}")
    except Exception as e:
        print(f"Error: {e}")
```
