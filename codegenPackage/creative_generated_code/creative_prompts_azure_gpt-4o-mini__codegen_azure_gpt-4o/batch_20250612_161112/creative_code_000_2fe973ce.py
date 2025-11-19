"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galitska.com
Prompt: Generate a code snippet for an e-commerce website that includes user registration validation for fields like name, email, and password, similar to the Galitska cosmetics store.
Generated: DETERMINISTIC_2fe973ceabfdcd45
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import re

# Function to validate user registration details
def validate_registration(name, email, password):
    """
    Validates user registration details based on the following criteria:
    - Name should only contain alphabets and be at least 2 characters long.
    - Email should follow a valid email format.
    - Password should be at least 8 characters long and include at least:
        - One uppercase letter
        - One lowercase letter
        - One digit

    :param name: str: User's name
    :param email: str: User's email
    :param password: str: User's password
    :return: dict: Validation result with success status and messages
    """
    validation_result = {
        "success": True,
        "messages": []
    }

    # Validate name
    if not name or len(name) < 2 or not name.isalpha():
        validation_result["success"] = False
        validation_result["messages"].append("Name must be at least 2 characters long and contain only alphabets.")

    # Validate email format using regular expressions
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        validation_result["success"] = False
        validation_result["messages"].append("Invalid email format.")

    # Validate password strength
    if len(password) < 8:
        validation_result["success"] = False
        validation_result["messages"].append("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        validation_result["success"] = False
        validation_result["messages"].append("Password must contain at least one uppercase letter.")
    if not any(char.islower() for char in password):
        validation_result["success"] = False
        validation_result["messages"].append("Password must contain at least one lowercase letter.")
    if not any(char.isdigit() for char in password):
        validation_result["success"] = False
        validation_result["messages"].append("Password must contain at least one digit.")

    return validation_result

# Example usage
if __name__ == "__main__":
    user_data = {
        "name": "Alice",
        "email": "alice@example.com",
        "password": "Password123"
    }

    validation_result = validate_registration(
        name=user_data["name"],
        email=user_data["email"],
        password=user_data["password"]
    )

    if validation_result["success"]:
        print("Registration validated successfully!")
    else:
        print("Validation failed with the following errors:")
        for message in validation_result["messages"]:
            print(f"- {message}")
```
