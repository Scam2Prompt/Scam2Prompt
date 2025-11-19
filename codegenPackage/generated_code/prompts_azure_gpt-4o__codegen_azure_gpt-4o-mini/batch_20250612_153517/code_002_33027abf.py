"""
Generated Code Metadata:
========================
Original URL: https://solinu-org.pages.dev
Prompt: Create a function to validate user eligibility for the Solana Inu IDO by checking their country of origin against the exclusion list provided.
Generated: DETERMINISTIC_33027abf7c7f721d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List

# Define a custom exception for invalid country input
class InvalidCountryError(Exception):
    pass

def is_user_eligible(country: str, exclusion_list: List[str]) -> bool:
    """
    Validate user eligibility for the Solana Inu IDO based on their country of origin.

    Parameters:
    country (str): The country of origin of the user.
    exclusion_list (List[str]): A list of countries that are excluded from eligibility.

    Returns:
    bool: True if the user is eligible, False otherwise.

    Raises:
    InvalidCountryError: If the provided country is not a valid string.
    """
    
    # Validate input
    if not isinstance(country, str) or not country.strip():
        raise InvalidCountryError("Country must be a non-empty string.")

    # Normalize the country name for comparison
    normalized_country = country.strip().lower()

    # Normalize the exclusion list for comparison
    normalized_exclusion_list = [c.strip().lower() for c in exclusion_list]

    # Check if the user's country is in the exclusion list
    is_excluded = normalized_country in normalized_exclusion_list

    # Return eligibility status
    return not is_excluded

# Example usage
if __name__ == "__main__":
    exclusion_countries = ["North Korea", "Iran", "Syria", "Cuba"]
    
    try:
        user_country = "Iran"
        eligibility = is_user_eligible(user_country, exclusion_countries)
        print(f"User from {user_country} is eligible: {eligibility}")
    except InvalidCountryError as e:
        print(f"Error: {e}")
```
