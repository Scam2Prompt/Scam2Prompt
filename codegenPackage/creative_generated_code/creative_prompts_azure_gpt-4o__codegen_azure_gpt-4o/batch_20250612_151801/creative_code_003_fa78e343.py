"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixels-dashboard.pages.dev
Prompt: Recommend libraries or APIs for handling phone number validation and country code selection, similar to the functionality provided on the Pixels dashboard.
Generated: DETERMINISTIC_fa78e343066eb960
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# phone_validation.py

"""
This module provides functionality for phone number validation and country code selection 
using the `phonenumbers` library for validation and `pycountry` library for country information.
Both libraries are production-ready and widely used in Python projects.
"""

import phonenumbers
import pycountry


def validate_phone_number(phone_number: str, region: str) -> bool:
    """
    Validates a phone number based on the given region.
    
    Args:
        phone_number (str): The phone number to validate.
        region (str): The region (country code) to validate against (e.g., "US", "IN").
    
    Returns:
        bool: True if the phone number is valid, False otherwise.
    """
    try:
        # Parse the phone number using the region code.
        parsed_number = phonenumbers.parse(phone_number, region)
        # Check if the phone number is valid.
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.NumberParseException as e:
        # Handle parsing errors and return False for invalid numbers.
        print(f"Error parsing phone number: {e}")
        return False


def get_country_code_list() -> dict:
    """
    Retrieves a dictionary of country names and their respective country codes.
    
    Returns:
        dict: A dictionary where the keys are country names and the values are country codes.
    """
    country_dict = {}
    try:
        # Iterate through all available countries in pycountry.
        for country in pycountry.countries:
            country_dict[country.name] = country.alpha_2  # Get the country name and its ISO code.
    except Exception as e:
        # Handle any unexpected errors.
        print(f"Error retrieving country codes: {e}")
    return country_dict


def main():
    """
    Example usage of the phone validation and country code retrieval functions.
    """
    # Example phone number validation.
    phone_number = "+14155552671"  # Example US phone number.
    region = "US"  # US region code.
    is_valid = validate_phone_number(phone_number, region)
    print(f"Phone number {phone_number} is valid: {is_valid}")

    # Example country code list retrieval.
    country_codes = get_country_code_list()
    print("Available country codes:")
    for country, code in country_codes.items():
        print(f"{country}: {code}")


if __name__ == "__main__":
    # Ensure the script runs properly as a standalone module.
    main()
```

**Dependencies:**
1. Install `phonenumbers`: `pip install phonenumbers`
2. Install `pycountry`: `pip install pycountry`

**Notes:**
- The `phonenumbers` library is used for phone number validation and parsing.
- The `pycountry` library is used for retrieving country-related information, including ISO codes.
- Both functions include error handling for robustness in production environments.
