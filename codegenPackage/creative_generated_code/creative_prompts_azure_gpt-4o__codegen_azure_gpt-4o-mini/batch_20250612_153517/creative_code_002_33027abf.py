"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solinu-org.pages.dev
Prompt: Create a function to validate user eligibility for the Solana Inu IDO by checking their country of origin against the exclusion list provided.
Generated: DETERMINISTIC_33027abf7c7f721d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List

class EligibilityError(Exception):
    """Custom exception for eligibility validation errors."""
    pass

def is_user_eligible(country: str, exclusion_list: List[str]) -> bool:
    """
    Validate if a user is eligible for the Solana Inu IDO based on their country of origin.

    Args:
        country (str): The country of origin of the user.
        exclusion_list (List[str]): A list of countries that are excluded from participating.

    Returns:
        bool: True if the user is eligible, False otherwise.

    Raises:
        ValueError: If the country or exclusion_list is not valid.
    """
    # Check for valid input
    if not isinstance(country, str) or not country.strip():
        raise ValueError("Country must be a non-empty string.")
    
    if not isinstance(exclusion_list, list) or not all(isinstance(item, str) for item in exclusion_list):
        raise ValueError("Exclusion list must be a list of strings.")

    # Normalize the country string for comparison
    normalized_country = country.strip().lower()

    # Check if the country is in the exclusion list
    if normalized_country in (item.strip().lower() for item in exclusion_list):
        return False  # User is not eligible

    return True  # User is eligible

# Example usage
if __name__ == "__main__":
    exclusion_countries = ["United States", "China", "North Korea"]
    user_country = "Canada"

    try:
        eligibility = is_user_eligible(user_country, exclusion_countries)
        print(f"User from {user_country} is {'eligible' if eligibility else 'not eligible'} for the IDO.")
    except ValueError as e:
        print(f"Error validating eligibility: {e}")
```
