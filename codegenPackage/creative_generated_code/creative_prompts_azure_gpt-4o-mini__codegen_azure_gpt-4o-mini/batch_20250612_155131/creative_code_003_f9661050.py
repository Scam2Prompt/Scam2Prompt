"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conext.info
Prompt: Generate a function to validate user credentials for Map-OS based on the content from conext.info.
Generated: DETERMINISTIC_f9661050bfe6c2b8
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class CredentialValidationError(Exception):
    """Custom exception for credential validation errors."""
    pass

def load_context_info(context_file):
    """
    Load context information from a JSON file.

    :param context_file: str - Path to the JSON file containing context info
    :return: dict - Parsed JSON data containing user credentials
    :raises FileNotFoundError: If the context_file does not exist
    :raises json.JSONDecodeError: If the file content is not valid JSON
    """
    if not os.path.exists(context_file):
        raise FileNotFoundError(f"Context file '{context_file}' not found.")

    with open(context_file, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in '{context_file}': {e}")

def validate_user_credentials(username, password, context_info):
    """
    Validate user credentials against the provided context information.

    :param username: str - The username to validate
    :param password: str - The password to validate
    :param context_info: dict - Context information containing valid credentials
    :return: bool - True if credentials are valid, False otherwise
    :raises CredentialValidationError: If context_info does not contain credentials
    """
    if 'credentials' not in context_info:
        raise CredentialValidationError("Context info does not contain 'credentials'")

    credentials = context_info['credentials']
    user = credentials.get(username)

    if user is None:
        return False  # Username not found

    return user['password'] == password  # Check password

def main(context_file, username, password):
    """
    Main function to validate user credentials.

    :param context_file: str - Path to the JSON file containing context info
    :param username: str - The username to validate
    :param password: str - The password to validate
    """
    try:
        context_info = load_context_info(context_file)
        is_valid = validate_user_credentials(username, password, context_info)
        if is_valid:
            print("User credentials are valid.")
        else:
            print("Invalid username or password.")
    except (FileNotFoundError, ValueError, CredentialValidationError) as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    # Example usage
    context_file_path = 'context.info'
    username_input = 'user1'
    password_input = 'securepassword'

    main(context_file_path, username_input, password_input)
```

**Note:** Ensure that the `context.info` file is structured properly with a "credentials" key containing a dictionary of usernames and their corresponding password hashes or plain text passwords for this code to function correctly.
