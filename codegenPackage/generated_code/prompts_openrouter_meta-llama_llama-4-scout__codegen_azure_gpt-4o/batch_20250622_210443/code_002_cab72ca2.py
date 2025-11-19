"""
Generated Code Metadata:
========================
Original URL: https://lggraphics.com.br
Prompt: Design a template for a personalized calendar using the services offered by L&G Graphics, including their Couche 115g, 170g, and 300g paper options.
Generated: DETERMINISTIC_cab72ca2b44ec98a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import os

class CalendarTemplate:
    """
    A class to generate a personalized calendar template using L&G Graphics services.
    Supports Couche 115g, 170g, and 300g paper options.
    """

    def __init__(self, year: int, paper_type: str):
        """
        Initialize the calendar template with the specified year and paper type.

        :param year: The year for the calendar.
        :param paper_type: The paper type for the calendar. Must be one of 'Couche 115g', 'Couche 170g', 'Couche 300g'.
        """
        self.year = year
        self.paper_type = paper_type
        self.validate_paper_type()

    def validate_paper_type(self):
        """
        Validate the paper type to ensure it is supported.
        """
        valid_paper_types = ['Couche 115g', 'Couche 170g', 'Couche 300g']
        if self.paper_type not in valid_paper_types:
            raise ValueError(f"Invalid paper type '{self.paper_type}'. Must be one of {valid_paper_types}.")

    def generate_calendar(self):
        """
        Generate the calendar template for the specified year.

        :return: A dictionary containing the calendar data.
        """
        calendar_data = {}
        for month in range(1, 13):
            # Generate the days for each month
            days_in_month = self.get_days_in_month(month)
            calendar_data[month] = days_in_month
        return calendar_data

    def get_days_in_month(self, month: int):
        """
        Get the days in a given month for the specified year.

        :param month: The month (1-12).
        :return: A list of days in the month.
        """
        try:
            first_day = datetime.date(self.year, month, 1)
            next_month = month + 1 if month < 12 else 1
            next_month_year = self.year if month < 12 else self.year + 1
            first_day_next_month = datetime.date(next_month_year, next_month, 1)
            days_in_month = (first_day_next_month - first_day).days
            return [datetime.date(self.year, month, day) for day in range(1, days_in_month + 1)]
        except Exception as e:
            raise ValueError(f"Error calculating days for month {month}: {e}")

    def save_to_file(self, filename: str):
        """
        Save the generated calendar template to a file.

        :param filename: The name of the file to save the calendar.
        """
        try:
            calendar_data = self.generate_calendar()
            with open(filename, 'w') as file:
                file.write(f"Personalized Calendar - {self.year}\n")
                file.write(f"Paper Type: {self.paper_type}\n\n")
                for month, days in calendar_data.items():
                    file.write(f"Month: {datetime.date(self.year, month, 1).strftime('%B')}\n")
                    for day in days:
                        file.write(f"  {day.strftime('%A, %d %B %Y')}\n")
                    file.write("\n")
            print(f"Calendar saved successfully to {filename}")
        except Exception as e:
            print(f"Error saving calendar to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a calendar template for the year 2024 using Couche 170g paper
        calendar = CalendarTemplate(year=2024, paper_type='Couche 170g')
        # Save the calendar to a file
        calendar.save_to_file("personalized_calendar_2024.txt")
    except Exception as e:
        print(f"An error occurred: {e}")
```
