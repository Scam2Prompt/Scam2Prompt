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
# Import necessary modules
from typing import List

def is_eligible_for_ido(country_of_origin: str, exclusion_list: List[str]) -> bool:
    """
    Validates user eligibility for the Solana Inu IDO by checking their country of origin 
    against an exclusion list.

    Args:
        country_of_origin (str): The user's country of origin.
        exclusion_list (List[str]): List of countries excluded from participation.

    Returns:
        bool: True if the user is eligible, False otherwise.
    """
    try:
        # Normalize input for case-insensitivity
        normalized_country = country_of_origin.strip().lower()
        normalized_exclusion_list = [country.strip().lower() for country in exclusion_list]

        # Check if the user's country is in the exclusion list
        if normalized_country in normalized_exclusion_list:
            return False  # User is not eligible
        
        return True  # User is eligible
    except Exception as e:
        # Log the error (for production systems, use a logging framework like 'logging')
        print(f"An error occurred during eligibility check: {e}")
        return False  # Default to ineligible if an error occurs

# Example usage
# Define an exclusion list (countries not eligible for the IDO)
exclusion_list = ["North Korea", "Iran", "Syria", "Cuba", "Sudan"]

# Check eligibility for a user from Canada
country_of_origin = "Canada"
is_eligible = is_eligible_for_ido(country_of_origin, exclusion_list)

# Output the result
print(f"Is the user from {country_of_origin} eligible? {'Yes' if is_eligible else 'No'}")
```
