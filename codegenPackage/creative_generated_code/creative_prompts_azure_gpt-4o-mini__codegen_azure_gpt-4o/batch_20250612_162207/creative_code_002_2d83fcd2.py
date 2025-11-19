"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldd.pages.dev
Prompt: Generate a code snippet to check the eligibility for the $WRLD token distribution based on user location and age.
Generated: DETERMINISTIC_2d83fcd227413d87
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

def check_token_eligibility(user_location, user_dob, eligible_countries, min_age):
    """
    Checks the eligibility for $WRLD token distribution based on user location and age.

    :param user_location: str - The country where the user resides.
    :param user_dob: str - User's date of birth in the format 'YYYY-MM-DD'.
    :param eligible_countries: list - List of countries eligible for token distribution.
    :param min_age: int - Minimum age required to be eligible.
    :return: dict - Result indicating eligibility status and reason if ineligible.
    """
    try:
        # Validate user's date of birth
        user_dob = datetime.datetime.strptime(user_dob, '%Y-%m-%d')
    except ValueError:
        return {
            "eligible": False,
            "reason": "Invalid date format. Use 'YYYY-MM-DD'."
        }

    # Calculate user's age
    today = datetime.date.today()
    user_age = today.year - user_dob.year - ((today.month, today.day) < (user_dob.month, user_dob.day))

    # Check location eligibility
    if user_location not in eligible_countries:
        return {
            "eligible": False,
            "reason": "User's location is not eligible for token distribution."
        }

    # Check age eligibility
    if user_age < min_age:
        return {
            "eligible": False,
            "reason": f"User does not meet the minimum age requirement of {min_age} years."
        }

    # If all checks pass, user is eligible
    return {
        "eligible": True,
        "reason": "User meets all eligibility criteria."
    }

# Example usage
if __name__ == "__main__":
    eligible_countries = ["USA", "Canada", "UK", "Australia"]
    min_age = 18

    # Sample user data
    user_location = "USA"
    user_dob = "2005-05-15"

    result = check_token_eligibility(user_location, user_dob, eligible_countries, min_age)
    print(result)
```
