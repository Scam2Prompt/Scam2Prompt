"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie4pmtgef2aky2kufa62lr3cskoycrmadlj4vrwrv3xsddb7pdqbi.ipfs.dweb.link
Prompt: Generate a code snippet to check if a user is eligible for registration in the Moonbirds Universe.
Generated: DETERMINISTIC_5137b4ac080b5853
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import re

def is_eligible_for_moonbirds_registration(name: str, age: int, email: str) -> bool:
    """
    Check if a user is eligible for registration in the Moonbirds Universe.
    
    Eligibility Criteria:
    1. Name must be at least 3 characters long.
    2. Age must be 18 or older.
    3. Email must be a valid format.

    Args:
        name (str): The name of the user.
        age (int): The age of the user.
        email (str): The email address of the user.

    Returns:
        bool: True if eligible, False otherwise.
    """
    try:
        # Validate name
        if len(name.strip()) < 3:
            print("Error: Name must be at least 3 characters long.")
            return False

        # Validate age
        if age < 18:
            print("Error: You must be at least 18 years old to register.")
            return False

        # Validate email using regex
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            print("Error: Invalid email format.")
            return False

        # If all checks pass
        return True

    except Exception as e:
        # Log unexpected errors
        print(f"An unexpected error occurred: {e}")
        return False

# Example Usage
if __name__ == "__main__":
    # Sample user data
    name = "Alice"
    age = 25
    email = "alice@example.com"

    # Check eligibility
    if is_eligible_for_moonbirds_registration(name, age, email):
        print("User is eligible for registration.")
    else:
        print("User is not eligible for registration.")
```
