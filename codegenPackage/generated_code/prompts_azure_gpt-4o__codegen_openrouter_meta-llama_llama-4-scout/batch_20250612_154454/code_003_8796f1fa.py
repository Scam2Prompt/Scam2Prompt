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

def calculate_next_verification_date(last_verification_date: datetime, passport_details: dict) -> datetime:
    """
    Calculates the next verification date for a heat meter.

    Args:
    - last_verification_date (datetime): The date of the last verification.
    - passport_details (dict): The meter's passport details.

    Returns:
    - datetime: The next verification date.

    Raises:
    - ValueError: If the last verification date is not provided or is invalid.
    - TypeError: If the passport details are not provided or are of the wrong type.
    """

    # Check if last verification date is provided and is of correct type
    if not isinstance(last_verification_date, datetime):
        raise ValueError("Last verification date must be a datetime object")

    # Check if passport details are provided and are of correct type
    if not isinstance(passport_details, dict):
        raise TypeError("Passport details must be a dictionary")

    # Verification is required every 4 years
    verification_interval_years = 4

    # Calculate the next verification date
    try:
        next_verification_date = last_verification_date.replace(year=last_verification_date.year + verification_interval_years)
    except ValueError:  # Handle February 29th in leap years
        next_verification_date = datetime(last_verification_date.year + verification_interval_years, 3, 1)

    return next_verification_date


def main():
    # Example usage
    last_verification_date = datetime(2020, 1, 1)
    passport_details = {
        "meter_id": "12345",
        "installation_date": datetime(2015, 1, 1)
    }

    try:
        next_date = calculate_next_verification_date(last_verification_date, passport_details)
        print(f"The next verification date is: {next_date.strftime('%Y-%m-%d')}")
    except (ValueError, TypeError) as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
