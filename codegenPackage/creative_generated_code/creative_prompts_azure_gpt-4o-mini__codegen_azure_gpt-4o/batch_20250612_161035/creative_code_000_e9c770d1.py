"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifqsy4i2xejq5goxyzbuufogxpqgugbowdte35bpuvzrccwy5cnr4.ipfs.dweb.link
Prompt: Generate a code snippet to check eligibility for participating in the Gyroscope Community based on the information provided on the website.
Generated: DETERMINISTIC_e9c770d12139b192
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python code to check eligibility for participating in the Gyroscope Community

def check_eligibility(age, country, has_account):
    """
    Function to check eligibility for participating in the Gyroscope Community.

    Parameters:
    age (int): Age of the participant.
    country (str): Country of residence.
    has_account (bool): Whether the participant has a Gyroscope account.

    Returns:
    str: Eligibility status message.
    """
    try:
        # Validate input types
        if not isinstance(age, int):
            raise ValueError("Age must be an integer.")
        if not isinstance(country, str):
            raise ValueError("Country must be a string.")
        if not isinstance(has_account, bool):
            raise ValueError("Account status must be a boolean.")

        # Eligibility criteria
        MIN_AGE = 18
        ALLOWED_COUNTRIES = {"USA", "Canada", "UK", "Australia"}

        # Check age eligibility
        if age < MIN_AGE:
            return "Ineligible: Must be at least 18 years old."

        # Check country eligibility
        if country not in ALLOWED_COUNTRIES:
            return "Ineligible: Country not supported for participation."

        # Check account status eligibility
        if not has_account:
            return "Ineligible: Must have a Gyroscope account."

        # If all criteria are met
        return "Eligible: You can participate in the Gyroscope Community."
    
    except Exception as e:
        # Handle unexpected errors
        return f"Error: {str(e)}"

# Example Usage:
if __name__ == "__main__":
    # Test the function with some inputs
    age = 25
    country = "USA"
    has_account = True
    
    # Print eligibility status
    print(check_eligibility(age, country, has_account))
```
