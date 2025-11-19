"""
Generated Code Metadata:
========================
Original URL: https://everyworld-app.pages.dev
Prompt: Write a function to validate user eligibility for Everyworld participation based on country restrictions and age requirements, as outlined in the platform's terms of use.
Generated: DETERMINISTIC_3f6d87a4a6185491
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class EligibilityError(Exception):
    """Custom exception for eligibility validation errors."""
    pass

def is_eligible_for_everyworld(birthdate: str, country: str) -> bool:
    """
    Validate user eligibility for Everyworld participation based on country restrictions and age requirements.

    Args:
        birthdate (str): User's birthdate in 'YYYY-MM-DD' format.
        country (str): User's country of residence.

    Returns:
        bool: True if the user is eligible, False otherwise.

    Raises:
        ValueError: If the birthdate is not in the correct format.
        EligibilityError: If the user is from a restricted country or does not meet age requirements.
    """
    
    # Define the minimum age for participation
    MINIMUM_AGE = 18
    
    # Define restricted countries
    RESTRICTED_COUNTRIES = {'CountryA', 'CountryB', 'CountryC'}

    # Check if the country is restricted
    if country in RESTRICTED_COUNTRIES:
        raise EligibilityError(f"Participation is not allowed from {country}.")

    # Parse the birthdate and calculate age
    try:
        birthdate_obj = datetime.strptime(birthdate, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Birthdate must be in 'YYYY-MM-DD' format.")

    # Calculate the user's age
    today = datetime.today()
    age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))

    # Check if the user meets the minimum age requirement
    if age < MINIMUM_AGE:
        raise EligibilityError("User must be at least 18 years old to participate.")

    return True

# Example usage:
if __name__ == "__main__":
    try:
        eligible = is_eligible_for_everyworld("2005-05-15", "CountryX")
        print("User is eligible for Everyworld participation." if eligible else "User is not eligible.")
    except (ValueError, EligibilityError) as e:
        print(f"Eligibility check failed: {e}")
```
