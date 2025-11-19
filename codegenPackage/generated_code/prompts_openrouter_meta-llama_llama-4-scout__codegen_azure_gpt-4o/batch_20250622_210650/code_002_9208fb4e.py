"""
Generated Code Metadata:
========================
Original URL: https://shubhasamaya.com
Prompt: Generate a date converter code in Python that can convert English dates to Nepali dates, similar to the "Date Converter" tool on Shubhasamaya.com.
Generated: DETERMINISTIC_9208fb4e6ff512aa
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class DateConverter:
    """
    A class to convert English dates (Gregorian calendar) to Nepali dates (Bikram Sambat calendar).
    """

    def __init__(self):
        # Define the mapping for Nepali date conversion
        # This is a simplified example; actual conversion requires detailed mapping
        self.start_date_eng = datetime.date(1944, 1, 1)  # Starting English date
        self.start_date_nep = (2000, 9, 17)  # Corresponding Nepali date (Year, Month, Day)
        self.nepali_month_days = [
            [30, 32, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],  # Year 2000
            [31, 31, 31, 32, 31, 30, 30, 30, 29, 30, 29, 31],  # Year 2001
            # Add more years as needed
        ]

    def convert_to_nepali(self, eng_date):
        """
        Convert an English date to a Nepali date.

        :param eng_date: A datetime.date object representing the English date.
        :return: A tuple (year, month, day) representing the Nepali date.
        """
        try:
            # Calculate the difference in days between the input date and the start date
            delta_days = (eng_date - self.start_date_eng).days

            # Initialize Nepali date variables
            nep_year, nep_month, nep_day = self.start_date_nep
            year_index = 0  # Index for nepali_month_days

            # Iterate through the days to calculate the Nepali date
            while delta_days > 0:
                days_in_month = self.nepali_month_days[year_index][nep_month - 1]
                if delta_days < days_in_month:
                    nep_day += delta_days
                    delta_days = 0
                else:
                    delta_days -= days_in_month
                    nep_day = 1
                    nep_month += 1
                    if nep_month > 12:
                        nep_month = 1
                        nep_year += 1
                        year_index += 1
                        if year_index >= len(self.nepali_month_days):
                            raise ValueError("Date out of range for Nepali calendar mapping.")

            return nep_year, nep_month, nep_day
        except Exception as e:
            raise ValueError(f"Error converting date: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Input English date
        english_date = datetime.date(2023, 10, 5)

        # Create an instance of the DateConverter
        converter = DateConverter()

        # Convert the English date to Nepali date
        nepali_date = converter.convert_to_nepali(english_date)

        # Print the result
        print(f"English Date: {english_date}")
        print(f"Nepali Date: Year {nepali_date[0]}, Month {nepali_date[1]}, Day {nepali_date[2]}")
    except ValueError as ve:
        print(f"Error: {ve}")
```

Note: This code provides a simplified example of converting English dates to Nepali dates. The actual conversion requires a detailed mapping of the Bikram Sambat calendar, which varies year by year. You would need to expand the `nepali_month_days` list with accurate data for all years in the range you want to support.
