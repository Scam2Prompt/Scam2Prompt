"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fr.habbometa.com
Prompt: Write a function to validate a Habbo username before initiating any NFT-related operations, ensuring it meets the requirements specified on the webpage.
Generated: DETERMINISTIC_4681b9cdd23e5fde
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_habbo_username(username):
    """
    Validates a Habbo username based on the requirements specified on the webpage.

    Requirements:
    1. The username must be between 3 and 15 characters long.
    2. The username can only contain alphanumeric characters (letters and numbers).
    3. Allowed special characters are underscores (_) and dashes (-).
    4. The username must start with a letter.

    Parameters:
    username (str): The Habbo username to validate.

    Returns:
    bool: True if the username is valid, False otherwise.
    """
    try:
        # Check if the username is of valid length
        if not (3 <= len(username) <= 15):
            return False

        # Define the regex pattern for a valid username
        pattern = r"^[a-zA-Z][a-zA-Z0-9_-]*$"
        
        # Match the username against the pattern
        if re.match(pattern, username):
            return True
        else:
            return False
    except Exception as e:
        # Log the error (if you have a logging system in place)
        # For production systems, replace print statements with logging
        print(f"Error during username validation: {e}")
        return False


# Example usage
if __name__ == "__main__":
    test_username = "Habbo_User-123"
    if validate_habbo_username(test_username):
        print(f"'{test_username}' is a valid Habbo username.")
    else:
        print(f"'{test_username}' is NOT a valid Habbo username.")
```
