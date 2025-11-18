"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poverka-gazvoda.ru
Prompt: Write a Python function that calculates the next verification date for a heat meter, assuming the verification is required every four years. Include input parameters for the last verification date and the meter's passport details.
Generated: DETERMINISTIC_8796f1fa5f536ee5
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta

def calculate_next_verification_date(last_verification_date: str, meter_passport_details: dict) -> str:
    """
    Calculates the next verification date for a heat meter.

    Args:
        last_verification_date (str): The last verification date in the format 'YYYY-MM-DD'.
        meter_passport_details (dict): Dictionary containing meter passport details (e.g., serial number, model, etc.).

    Returns:
        str: The next verification date in the format 'YYYY-MM-DD'.

    Raises:
        ValueError: If the last_verification_date is not in the correct format.
    """
    try:
        # Parse the last verification date from the input string
        last_verification_date_obj = datetime.strptime(last_verification_date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")

    # Calculate the next verification date (4 years later)
    next_verification_date_obj = last_verification_date_obj + timedelta(days=4 * 365)  # Approximation for 4 years

    # Format the next verification date as a string
    next_verification_date = next_verification_date_obj.strftime('%Y-%m-%d')

    # Log the operation (could be replaced with actual logging in production)
    print(f"Heat meter verification calculation performed.")
    print(f"Meter Passport Details: {meter_passport_details}")
    print(f"Last Verification Date: {last_verification_date}")
    print(f"Next Verification Date: {next_verification_date}")

    return next_verification_date

# Example usage:
# last_verification_date = "2023-10-15"
# meter_passport = {"serial_number": "12345ABC", "model": "HeatMeterX"}
# print(calculate_next_verification_date(last_verification_date, meter_passport))
```
