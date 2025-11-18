"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Write code to design and export a calendar layout suitable for offset printing, incorporating features similar to Ram Digi's calendar printing services.
Generated: DETERMINISTIC_d43bfb561c11e0a9
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import calendar
from fpdf import FPDF
import datetime
import os

class CalendarPDF(FPDF):
    """
    A class to create a calendar PDF layout for offset printing.
    """

    def __init__(self, year, month):
        super().__init__()
        self.year = year
        self.month = month
        self.output_file = f'calendar_{self.year}_{self.month}.pdf'

    def header(self):
        """Add a header with the month and year."""
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f'{calendar.month_name[self.month]} {self.year}', 0, 1, 'C')

    def footer(self):
        """Add a footer with page number."""
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def add_month(self):
        """Generate the calendar for the given month."""
        self.add_page()
        self.set_font('Arial', '', 12)

        # Days of the week
        days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
        for day in days:
            self.cell(28, 10, day, 1, 0, 'C')
        self.ln()

        # Create a month calendar
        month_calendar = calendar.monthcalendar(self.year, self.month)

        for week in month_calendar:
            for day in week:
                if day == 0:
                    self.cell(28, 10, '', 1, 0, 'C')  # Empty cell for days not in the month
                else:
                    self.cell(28, 10, str(day), 1, 0, 'C')
            self.ln()

    def save_pdf(self):
        """Save the PDF to a file."""
        try:
            self.output(self.output_file)
            print(f'Successfully saved calendar to {self.output_file}')
        except Exception as e:
            print(f'Error saving PDF: {e}')

def create_calendar(year: int, month: int):
    """
    Create a calendar PDF for a specific year and month.

    :param year: The year of the calendar.
    :param month: The month of the calendar.
    """
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    
    if year < 1:
        raise ValueError("Year must be a positive integer.")

    # Create a calendar PDF object
    calendar_pdf = CalendarPDF(year, month)
    calendar_pdf.add_month()
    calendar_pdf.save_pdf()

if __name__ == "__main__":
    # Example usage
    try:
        # Example: Create calendar for January 2024
        create_calendar(2024, 1)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

### Requirements:
- Install the `fpdf` package if you haven't already by running `pip install fpdf`.
- The code generates a PDF file for the specified month and year, formatted for offset printing. Adjust the PDF layout as needed for your specific design preferences.
