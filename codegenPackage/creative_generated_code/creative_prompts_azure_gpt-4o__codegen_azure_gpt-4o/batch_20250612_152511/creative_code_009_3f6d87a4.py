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
import datetime

def validate_user_eligibility(user_country, user_birth_date):
    """
    Validates user eligibility for Everyworld participation based on country restrictions and age requirements.

    Args:
        user_country (str): The country of the user (e.g., 'USA', 'Canada').
        user_birth_date (str): The user's date of birth in the format 'YYYY-MM-DD'.

    Returns:
        dict: A dictionary containing eligibility status and reason/message:
              {'eligible': True/False, 'message': 'Reason for ineligibility or success'}
    """
    # List of restricted countries where participation is not allowed
    restricted_countries = [
        'North Korea', 'Iran', 'Syria', 'Cuba', 'Sudan'
    ]
    
    # Minimum age requirement for participation
    MINIMUM_AGE = 18

    # Check for country restriction
    if user_country in restricted_countries:
        return {
            'eligible': False,
            'message': f"Users from {user_country} are not eligible to participate due to country restrictions."
        }

    # Validate and parse the user's birth date
    try:
        birth_date = datetime.datetime.strptime(user_birth_date, '%Y-%m-%d').date()
    except ValueError:
        return {
            'eligible': False,
            'message': "Invalid birth date format. Please use 'YYYY-MM-DD'."
        }

    # Calculate the user's age
    today = datetime.date.today()
    age = today.year - birth_date.year - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )

    # Check age eligibility
    if age < MINIMUM_AGE:
        return {
            'eligible': False,
            'message': f"Users must be at least {MINIMUM_AGE} years old to participate. You are {age} years old."
        }

    # If all checks pass, the user is eligible
    return {
        'eligible': True,
        'message': "You are eligible to participate in Everyworld."
    }

# Example usage:
# user_eligibility = validate_user_eligibility('USA', '2005-05-20')
# print(user_eligibility)
```
