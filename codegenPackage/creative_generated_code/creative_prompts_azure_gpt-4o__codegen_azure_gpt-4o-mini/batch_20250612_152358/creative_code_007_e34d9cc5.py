"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://choccoin-dashboard.pages.dev
Prompt: Write a script to validate a user's eligibility to participate in the $CHOC presale based on their country of residence, excluding restricted regions.
Generated: DETERMINISTIC_e34d9cc58bf70031
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# eligibility_validator.py

# List of restricted countries
RESTRICTED_COUNTRIES = {
    "North Korea",
    "Iran",
    "Syria",
    "Cuba",
    "Sudan",
    "Russia",
    "Ukraine"
}

def is_eligible_for_presale(country: str) -> bool:
    """
    Check whether the user is eligible to participate in the $CHOC presale
    based on their country of residence.
    
    Args:
        country (str): The user's country of residence.

    Returns:
        bool: True if eligible, False otherwise.
    """
    if not isinstance(country, str):
        raise ValueError("Country must be a string.")

    country = country.strip()  # Remove any leading or trailing whitespace

    # Validate country name
    if not country:
        raise ValueError("Country name cannot be empty.")
    
    # Check if the country is in the restricted list
    if country in RESTRICTED_COUNTRIES:
        return False  # Not eligible

    return True  # Eligible

def main():
    """
    Main function to execute the eligibility check.
    """
    user_country = input("Enter your country of residence: ")
    
    try:
        if is_eligible_for_presale(user_country):
            print("You are eligible to participate in the $CHOC presale.")
        else:
            print("You are NOT eligible to participate in the $CHOC presale due to your country of residence.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
