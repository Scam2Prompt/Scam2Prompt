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
from datetime import datetime, timedelta

class NepaliDateConverter:
    """
    A class used to convert English dates to Nepali dates.

    Attributes:
    ----------
    english_date : str
        The English date to be converted in 'YYYY-MM-DD' format.

    Methods:
    -------
    convert_to_nepali_date()
        Converts the English date to Nepali date.
    """

    def __init__(self, english_date):
        """
        Initializes the NepaliDateConverter object.

        Parameters:
        ----------
        english_date : str
            The English date to be converted in 'YYYY-MM-DD' format.
        """
        self.english_date = english_date

    def convert_to_nepali_date(self):
        """
        Converts the English date to Nepali date.

        Returns:
        -------
        str
            The Nepali date in 'YYYY-MM-DD' format.

        Raises:
        ------
        ValueError
            If the English date is not in 'YYYY-MM-DD' format.
        """
        try:
            # Parse the English date
            english_date_obj = datetime.strptime(self.english_date, '%Y-%m-%d')

            # Define the Nepali calendar's epoch (Bikram Sambat)
            nepali_epoch = datetime(2016, 9, 16)  # BS 2073-06-01

            # Calculate the difference between the English date and the epoch
            delta = english_date_obj - nepali_epoch

            # Calculate the Nepali date
            nepali_year = 2073 + delta.days // 365
            remaining_days = delta.days % 365

            # Define the months and their days in the Nepali calendar
            nepali_months = [30, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30, 31]

            # Calculate the Nepali month and day
            nepali_month = 0
            nepali_day = 0
            for i, days in enumerate(nepali_months):
                if remaining_days < days:
                    nepali_month = i + 1
                    nepali_day = remaining_days + 1
                    break
                else:
                    remaining_days -= days

            # Adjust for the Nepali New Year
            if nepali_month > 6:
                nepali_year += 1
                nepali_month -= 6
            else:
                nepali_month += 6

            # Format the Nepali date
            nepali_date = f'{nepali_year:04}-{nepali_month:02}-{nepali_day:02}'

            return nepali_date

        except ValueError as e:
            print(f"Invalid date format: {e}")
            return None


def main():
    english_date = input("Enter the English date (YYYY-MM-DD): ")
    converter = NepaliDateConverter(english_date)
    nepali_date = converter.convert_to_nepali_date()

    if nepali_date:
        print(f"The Nepali date is: {nepali_date}")


if __name__ == "__main__":
    main()
```
