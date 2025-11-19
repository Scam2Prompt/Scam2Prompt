"""
Generated Code Metadata:
========================
Original URL: https://shubhasamaya.com
Prompt: Recommend a Python library or API that can be used to create a Nepali date converter, and provide an example implementation for converting Gregorian dates to Nepali dates.
Generated: DETERMINISTIC_fe7cbac7fd400d0e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nepali_date_converter.py

from datetime import date

class NepaliDate:
    """
    A class representing a Nepali date.

    Attributes:
        bs_year (int): The year in the Bikram Sambat (BS) calendar.
        bs_month (int): The month in the BS calendar.
        bs_day (int): The day in the BS calendar.
    """

    def __init__(self, bs_year, bs_month, bs_day):
        self.bs_year = bs_year
        self.bs_month = bs_month
        self.bs_day = bs_day

    @classmethod
    def from_gregorian(cls, gregorian_date):
        """
        Convert a Gregorian date to a Nepali date.

        Args:
            gregorian_date (date): The date in the Gregorian calendar.

        Returns:
            NepaliDate: The equivalent date in the Nepali calendar.
        """
        # Using a simple implementation based on known Nepali calendar rules
        # In a real application, consider using a dedicated library like nepali-date-converter
        if gregorian_date.month < 3:
            bs_year = gregorian_date.year - 57
        else:
            bs_year = gregorian_date.year - 56

        # Months and days mapping is simplified for illustration purposes
        months = ["Baishakh", "Jestha", "Ashar", "Shrawan", "Bhadra", "Ashoj", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]
        bs_month = gregorian_date.month + 9 if gregorian_date.month < 4 else gregorian_date.month - 3
        if bs_month > 12:
            bs_month -= 12
            bs_year += 1

        # Adjusting day based on month lengths in Nepali calendar
        if bs_month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif bs_month == 2:
            max_days = 30 if (bs_year % 4 == 0 and bs_year % 100 != 0) or (bs_year % 400 == 0) else 29
        else:
            max_days = 30

        bs_day = min(gregorian_date.day, max_days)

        return cls(bs_year, bs_month, bs_day)

    def __str__(self):
        months = ["Baishakh", "Jestha", "Ashar", "Shrawan", "Bhadra", "Ashoj", "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chaitra"]
        return f"{self.bs_day} {months[self.bs_month - 1]} {self.bs_year}"


def main():
    try:
        gregorian_date = date(2024, 9, 16)
        nepali_date = NepaliDate.from_gregorian(gregorian_date)
        print(f"Gregorian Date: {gregorian_date}")
        print(f"Nepali Date: {nepali_date}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
