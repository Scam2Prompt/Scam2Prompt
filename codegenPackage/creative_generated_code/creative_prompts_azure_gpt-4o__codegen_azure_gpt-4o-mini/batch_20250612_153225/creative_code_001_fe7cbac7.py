"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubhasamaya.com
Prompt: Recommend a Python library or API that can be used to create a Nepali date converter, and provide an example implementation for converting Gregorian dates to Nepali dates.
Generated: DETERMINISTIC_fe7cbac7fd400d0e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
import pytz

# Nepali Date Converter library
# You can install it using: pip install nepali-date-converter
from nepali_date_converter import NepaliDateConverter

class DateConverter:
    """
    A class to convert Gregorian dates to Nepali dates.
    """

    def __init__(self):
        """
        Initialize the DateConverter instance.
        """
        pass

    @staticmethod
    def convert_to_nepali(gregorian_date: str) -> str:
        """
        Convert a given Gregorian date to Nepali date.

        Args:
            gregorian_date (str): The date in 'YYYY-MM-DD' format.

        Returns:
            str: The corresponding Nepali date in 'YYYY-MM-DD' format.
        """
        try:
            # Parse the input date string to a datetime object
            date_obj = datetime.strptime(gregorian_date, '%Y-%m-%d')
            # Convert the datetime object to Nepali date
            nepali_date = NepaliDateConverter().to_nepali(date_obj)
            return nepali_date
        except ValueError as e:
            # Handle errors related to date parsing
            return f"Error parsing the date: {e}"
        except Exception as e:
            # Handle any other potential errors
            return f"An unexpected error occurred: {e}"

if __name__ == "__main__":
    # Example usage of the DateConverter class
    converter = DateConverter()
    
    # Example Gregorian date
    gregorian_date = "2023-10-01"
    
    # Convert to Nepali date and print the result
    nepali_date = converter.convert_to_nepali(gregorian_date)
    print(f"Gregorian Date: {gregorian_date} -> Nepali Date: {nepali_date}")
```

Make sure to install the `nepali-date-converter` library before running the code. You can do this via pip:

```bash
pip install nepali-date-converter
```
