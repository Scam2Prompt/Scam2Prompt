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

class VerificationDateError(Exception):
    """Custom exception for verification date errors."""
    pass

def calculate_next_verification_date(last_verification_date: str, passport_details: str) -> str:
    """
    Calculate the next verification date for a heat meter.
    
    Parameters:
    last_verification_date (str): The last verification date in 'YYYY-MM-DD' format.
    passport_details (str): The passport details of the heat meter (for documentation purposes).
    
    Returns:
    str: The next verification date in 'YYYY-MM-DD' format.
    
    Raises:
    VerificationDateError: If the last verification date is invalid or in the future.
    """
    
    # Define the verification period in years
    verification_period_years = 4
    
    # Attempt to parse the last verification date
    try:
        last_date = datetime.strptime(last_verification_date, '%Y-%m-%d')
    except ValueError as e:
        raise VerificationDateError("Invalid date format for last verification date. Please use 'YYYY-MM-DD'.") from e
    
    # Check if the last verification date is in the future
    if last_date > datetime.now():
        raise VerificationDateError("Last verification date cannot be in the future.")
    
    # Calculate the next verification date by adding the verification period
    next_verification_date = last_date.replace(year=last_date.year + verification_period_years)
    
    return next_verification_date.strftime('%Y-%m-%d')

# Example usage:
if __name__ == "__main__":
    try:
        last_verification = "2019-05-15"
        passport = "Heat Meter Passport #123456"
        next_date = calculate_next_verification_date(last_verification, passport)
        print(f"The next verification date for the heat meter is: {next_date}")
    except VerificationDateError as e:
        print(f"Error: {e}")
```
