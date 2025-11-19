"""
Generated Code Metadata:
========================
Original URL: https://hmhgbg.pages.dev
Prompt: Create a function that checks if a user has the necessary rights to use Nakamigos-CLOAKS in their game, based on the licensing information provided.
Generated: DETERMINISTIC_cf518a199709dcab
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class LicensingError(Exception):
    """Base class for licensing-related exceptions."""
    pass

class InsufficientRightsError(LicensingError):
    """Raised when a user does not have sufficient rights to use Nakamigos-CLOAKS."""
    pass

def check_nakamigos_cloaks_rights(user_id: int, licensing_info: Dict[int, Dict[str, bool]]) -> bool:
    """
    Checks if a user has the necessary rights to use Nakamigos-CLOAKS in their game.

    Args:
    - user_id (int): The ID of the user to check.
    - licensing_info (Dict[int, Dict[str, bool]]): A dictionary containing licensing information.
        The outer dictionary keys are user IDs, and the inner dictionary keys are feature names.
        The inner dictionary values are boolean indicators of whether the feature is licensed.

    Returns:
    - bool: True if the user has the necessary rights, False otherwise.

    Raises:
    - LicensingError: If the licensing information is invalid or missing.
    """

    # Check if licensing_info is a dictionary
    if not isinstance(licensing_info, dict):
        raise LicensingError("Invalid licensing information")

    # Check if user_id exists in licensing_info
    if user_id not in licensing_info:
        raise InsufficientRightsError("User not found in licensing information")

    user_licensing_info = licensing_info[user_id]

    # Check if Nakamigos-CLOAKS is in the user's licensing information
    if "Nakamigos-CLOAKS" not in user_licensing_info:
        raise LicensingError("Nakamigos-CLOAKS not found in user's licensing information")

    # Check if the user has the necessary rights to use Nakamigos-CLOAKS
    return user_licensing_info["Nakamigos-CLOAKS"]


def main():
    licensing_info = {
        1: {"Nakamigos-CLOAKS": True, "other-feature": False},
        2: {"Nakamigos-CLOAKS": False, "other-feature": True}
    }

    user_id = 1
    try:
        has_rights = check_nakamigos_cloaks_rights(user_id, licensing_info)
        print(f"User {user_id} has rights: {has_rights}")
    except LicensingError as e:
        print(f"Licensing error: {e}")

    user_id = 2
    try:
        has_rights = check_nakamigos_cloaks_rights(user_id, licensing_info)
        print(f"User {user_id} has rights: {has_rights}")
    except LicensingError as e:
        print(f"Licensing error: {e}")

    user_id = 3
    try:
        has_rights = check_nakamigos_cloaks_rights(user_id, licensing_info)
        print(f"User {user_id} has rights: {has_rights}")
    except LicensingError as e:
        print(f"Licensing error: {e}")


if __name__ == "__main__":
    main()
```
