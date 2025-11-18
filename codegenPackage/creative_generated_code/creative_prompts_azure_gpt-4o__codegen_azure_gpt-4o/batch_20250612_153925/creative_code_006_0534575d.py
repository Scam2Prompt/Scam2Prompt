"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperblox.vercel.app
Prompt: Create a function to validate user eligibility for the HPB Hunt campaign based on the restrictions outlined for USA, UK, and Canada residents.
Generated: DETERMINISTIC_0534575df109cc14
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def validate_user_eligibility(country: str, age: int, is_registered: bool) -> str:
    """
    Validate user eligibility for the HPB Hunt campaign based on country-specific restrictions.

    Parameters:
    country (str): The country of the user (e.g., 'USA', 'UK', 'Canada').
    age (int): The age of the user.
    is_registered (bool): Whether the user is registered for the campaign.

    Returns:
    str: A message indicating the eligibility status of the user.
    """

    # Define eligibility rules for each country
    eligibility_criteria = {
        "USA": {"min_age": 18, "max_age": 60, "requires_registration": True},
        "UK": {"min_age": 21, "max_age": 65, "requires_registration": True},
        "Canada": {"min_age": 19, "max_age": 60, "requires_registration": False},
    }

    # Check if the country is valid
    if country not in eligibility_criteria:
        return "Error: Invalid country. Campaign is restricted to USA, UK, and Canada residents only."

    # Extract rules for the given country
    rules = eligibility_criteria[country]

    # Validate age
    if age < rules["min_age"] or age > rules["max_age"]:
        return f"Error: Age restriction not met. Eligible age range for {country} is {rules['min_age']} to {rules['max_age']}."

    # Validate registration status, if required
    if rules["requires_registration"] and not is_registered:
        return f"Error: Registration required for users in {country}."

    # If all checks pass, user is eligible
    return "Success: User is eligible for the HPB Hunt campaign."


# Example usage:
if __name__ == "__main__":
    # Test cases
    print(validate_user_eligibility("USA", 25, True))  # Output: Success: User is eligible for the HPB Hunt campaign.
    print(validate_user_eligibility("UK", 20, True))  # Output: Error: Age restriction not met.
    print(validate_user_eligibility("Canada", 30, False))  # Output: Success: User is eligible for the HPB Hunt campaign.
    print(validate_user_eligibility("Canada", 17, True))  # Output: Error: Age restriction not met.
    print(validate_user_eligibility("Australia", 30, True))  # Output: Error: Invalid country.
```
