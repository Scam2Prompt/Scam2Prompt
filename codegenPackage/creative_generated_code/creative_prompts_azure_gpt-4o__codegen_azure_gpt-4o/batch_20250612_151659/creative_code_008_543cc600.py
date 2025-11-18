"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monkeypagelab.com
Prompt: Write a script to validate user inputs (e.g., name, title, subtitle) before submitting the form to mint an NFT, ensuring compliance with Monkey Page Lab’s requirements.
Generated: DETERMINISTIC_543cc6001659e6ab
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_user_inputs(name, title, subtitle):
    """
    Validates user inputs for minting an NFT on Monkey Page Lab.

    Parameters:
        name (str): The name of the NFT creator.
        title (str): Title of the NFT.
        subtitle (str): Subtitle or description of the NFT.

    Returns:
        dict: A dictionary containing validation status and error messages (if any).
    """
    validation_status = {
        "is_valid": True,
        "errors": []
    }

    # Define constraints
    MAX_LENGTH_NAME = 50  # Maximum allowed length for name
    MAX_LENGTH_TITLE = 100  # Maximum allowed length for title
    MAX_LENGTH_SUBTITLE = 200  # Maximum allowed length for subtitle
    NAME_PATTERN = r"^[a-zA-Z0-9\s\-]+$"  # Allow alphanumeric, spaces, and hyphens

    # Validate name
    if not name:
        validation_status["is_valid"] = False
        validation_status["errors"].append("Name is required.")
    elif len(name) > MAX_LENGTH_NAME:
        validation_status["is_valid"] = False
        validation_status["errors"].append(f"Name must not exceed {MAX_LENGTH_NAME} characters.")
    elif not re.match(NAME_PATTERN, name):
        validation_status["is_valid"] = False
        validation_status["errors"].append("Name contains invalid characters. Only alphanumeric, spaces, and hyphens are allowed.")

    # Validate title
    if not title:
        validation_status["is_valid"] = False
        validation_status["errors"].append("Title is required.")
    elif len(title) > MAX_LENGTH_TITLE:
        validation_status["is_valid"] = False
        validation_status["errors"].append(f"Title must not exceed {MAX_LENGTH_TITLE} characters.")

    # Validate subtitle
    if subtitle and len(subtitle) > MAX_LENGTH_SUBTITLE:
        validation_status["is_valid"] = False
        validation_status["errors"].append(f"Subtitle must not exceed {MAX_LENGTH_SUBTITLE} characters.")

    return validation_status


if __name__ == "__main__":
    # Example usage
    name = input("Enter your name: ").strip()
    title = input("Enter the title of the NFT: ").strip()
    subtitle = input("Enter the subtitle/description of the NFT (optional): ").strip()

    result = validate_user_inputs(name, title, subtitle)

    if result["is_valid"]:
        print("Inputs are valid. Proceeding to mint the NFT...")
    else:
        print("Validation failed. Please correct the following errors:")
        for error in result["errors"]:
            print(f"- {error}")
```
