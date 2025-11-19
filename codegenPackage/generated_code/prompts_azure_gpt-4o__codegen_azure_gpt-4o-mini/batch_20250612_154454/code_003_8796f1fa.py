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

class MeterPassport:
    """
    Class to represent the passport details of a heat meter.
    Attributes:
        meter_id (str): Unique identifier for the heat meter.
        manufacturer (str): Manufacturer of the heat meter.
        model (str): Model of the heat meter.
    """
    def __init__(self, meter_id: str, manufacturer: str, model: str):
        self.meter_id = meter_id
        self.manufacturer = manufacturer
        self.model = model

def calculate_next_verification_date(last_verification_date: str, passport: MeterPassport) -> str:
    """
    Calculate the next verification date for a heat meter.

    Parameters:
        last_verification_date (str): The last verification date in 'YYYY-MM-DD' format.
        passport (MeterPassport): The passport details of the heat meter.

    Returns:
        str: The next verification date in 'YYYY-MM-DD' format.

    Raises:
        ValueError: If the last verification date is not in the correct format.
    """
    # Define the verification interval in years
    verification_interval_years = 4

    # Parse the last verification date
    try:
        last_verification = datetime.strptime(last_verification_date, '%Y-%m-%d')
    except ValueError as e:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    # Calculate the next verification date
    next_verification = last_verification.replace(year=last_verification.year + verification_interval_years)

    # Return the next verification date in 'YYYY-MM-DD' format
    return next_verification.strftime('%Y-%m-%d')

# Example usage
if __name__ == "__main__":
    # Create a meter passport instance
    meter_passport = MeterPassport(meter_id="12345", manufacturer="HeatCo", model="X1000")

    # Last verification date
    last_verification_date = "2020-05-15"

    # Calculate the next verification date
    try:
        next_verification_date = calculate_next_verification_date(last_verification_date, meter_passport)
        print(f"Next verification date for meter {meter_passport.meter_id}: {next_verification_date}")
    except ValueError as e:
        print(f"Error: {e}")
```
