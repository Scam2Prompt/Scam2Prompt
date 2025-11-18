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
# Required Library: nepali_datetime
# You can install it using pip: pip install nepali-datetime

from nepali_datetime import date as nepali_date
from datetime import date

def gregorian_to_nepali(gregorian_year, gregorian_month, gregorian_day):
    """
    Convert a Gregorian date to Nepali date.
    
    Args:
        gregorian_year (int): Year in Gregorian calendar.
        gregorian_month (int): Month in Gregorian calendar (1-12).
        gregorian_day (int): Day in Gregorian calendar (1-31).
    
    Returns:
        str: Nepali date in the format YYYY-MM-DD.
    """
    try:
        # Create a Gregorian date object
        gregorian_date = date(gregorian_year, gregorian_month, gregorian_day)
        
        # Convert Gregorian date to Nepali date using nepali_datetime library
        nepali_date_obj = nepali_date.from_datetime_date(gregorian_date)
        
        # Return Nepali date in string format
        return nepali_date_obj.strftime("%Y-%m-%d")
    
    except ValueError as e:
        # Handle invalid date inputs
        return f"Error: Invalid date provided. {str(e)}"
    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {str(e)}"

# Example Usage
if __name__ == "__main__":
    # Input Gregorian date
    gregorian_year = 2022
    gregorian_month = 12
    gregorian_day = 15
    
    # Convert and display Nepali date
    nepali_date = gregorian_to_nepali(gregorian_year, gregorian_month, gregorian_day)
    print(f"Nepali Date: {nepali_date}")
```
