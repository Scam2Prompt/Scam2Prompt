"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Write a Python function that calculates the next verification date for a heat meter, assuming the verification is required every four years. Include input parameters for the last verification date and the meter's passport details.
Generated: DETERMINISTIC_8796f1fa5f536ee5
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Optional, Dict


def calculate_next_verification_date(
    last_verification_date: str,
    passport_details: Optional[Dict] = None,
    date_format: str = "%Y-%m-%d"
) -> str:
    """
    Calculate the next verification date for a heat meter, which is required every four years.

    Args:
        last_verification_date: The date of the last verification in string format (e.g., "YYYY-MM-DD").
        passport_details: Optional dictionary containing meter's passport details (not used in current logic).
        date_format: Optional string specifying the date format (default is "%Y-%m-%d").

    Returns:
        The next verification date in the same format as the input date.

    Raises:
        ValueError: If the last_verification_date is not a valid date or cannot be parsed.
    """
    try:
        # Parse the last verification date
        last_date = datetime.strptime(last_verification_date, date_format).date()
        
        # Calculate the next verification date (4 years later)
        next_date = last_date + timedelta(days=4 * 365)
        
        # Adjust for leap years (add 1 day for each leap year in the 4-year span)
        leap_years = sum(1 for year in range(last_date.year, last_date.year + 4) 
                         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
        next_date += timedelta(days=leap_years)
        
        return next_date.strftime(date_format)
    except ValueError as e:
        raise ValueError(f"Invalid date format or value: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        last_date = "2020-01-15"
        next_date = calculate_next_verification_date(last_date)
        print(f"Next verification date: {next_date}")
    except ValueError as e:
        print(f"Error: {e}")
```
