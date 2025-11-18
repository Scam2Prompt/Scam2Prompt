"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Write a function to validate user eligibility for Everyworld participation based on country restrictions and age requirements, as outlined in the platform's terms of use.
Generated: DETERMINISTIC_3f6d87a4a6185491
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime

class EligibilityError(Exception):
    """Custom exception for eligibility validation errors."""
    pass

def is_user_eligible(date_of_birth, country):
    """
    Validate user eligibility for Everyworld participation.

    Args:
        date_of_birth (str): User's date of birth in 'YYYY-MM-DD' format.
        country (str): User's country of residence.

    Returns:
        bool: True if eligible, otherwise False.

    Raises:
        EligibilityError: If the date_of_birth is invalid or country restrictions apply.
    """
    # Define age requirement
    MIN_AGE = 18

    # Define restricted countries
    RESTRICTED_COUNTRIES = ['CountryA', 'CountryB', 'CountryC']

    # Validate date_of_birth format
    try:
        birth_date = datetime.strptime(date_of_birth, '%Y-%m-%d')
    except ValueError:
        raise EligibilityError(f"Invalid date format: {date_of_birth}. Expected format: YYYY-MM-DD.")

    # Calculate the age of the user
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    # Check age requirement
    if age < MIN_AGE:
        return False

    # Check country restrictions
    if country in RESTRICTED_COUNTRIES:
        return False

    return True

# Example usage
if __name__ == "__main__":
    try:
        print(is_user_eligible("2005-05-15", "CountryX"))  # Should return False for age
        print(is_user_eligible("2000-01-01", "CountryA"))  # Should return False for country
        print(is_user_eligible("2000-01-01", "CountryZ"))  # Should return True for eligibility
    except EligibilityError as e:
        print(f"Eligibility check failed: {e}")
```
