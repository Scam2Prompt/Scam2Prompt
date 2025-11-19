"""
Generated Code Metadata:
========================
Original URL: https://tos.hyperliquidfndn.org
Prompt: Write a Python function that checks if a user has agreed to the terms of service and privacy policy before allowing participation in an event, based on the structure seen in the Hyper Foundation's terms.
Generated: DETERMINISTIC_f5338b96d70ae76e
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UserAgreementError(Exception):
    """Custom exception for user agreement validation."""
    pass

def check_user_agreement(user_agreed: bool, terms_version: str, user_terms_version: str) -> bool:
    """
    Check if the user has agreed to the terms of service and privacy policy.

    Parameters:
    user_agreed (bool): Indicates if the user has agreed to the terms.
    terms_version (str): The current version of the terms of service and privacy policy.
    user_terms_version (str): The version of the terms the user agreed to.

    Returns:
    bool: True if the user can participate, False otherwise.

    Raises:
    UserAgreementError: If the user has not agreed to the terms or if the versions do not match.
    """
    # Check if the user has agreed to the terms
    if not user_agreed:
        raise UserAgreementError("User has not agreed to the terms of service and privacy policy.")

    # Check if the user's agreed version matches the current version
    if user_terms_version != terms_version:
        raise UserAgreementError("User's agreed terms version does not match the current version.")

    # If both checks pass, the user can participate
    return True

# Example usage
if __name__ == "__main__":
    try:
        # Current version of the terms
        current_terms_version = "1.0.0"
        
        # User's agreement status and version
        user_agreed = True
        user_agreed_version = "1.0.0"

        # Check if the user can participate
        can_participate = check_user_agreement(user_agreed, current_terms_version, user_agreed_version)
        print("User can participate:", can_participate)

    except UserAgreementError as e:
        print("Error:", e)
```
