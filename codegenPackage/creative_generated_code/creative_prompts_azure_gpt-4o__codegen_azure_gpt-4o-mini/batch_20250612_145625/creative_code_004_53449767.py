"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enacoin-newbridge.com
Prompt: Create a function to validate invite codes for early access to Ethena's platform and display the corresponding user data.
Generated: DETERMINISTIC_5344976753804494
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class InviteCodeValidator:
    def __init__(self, invite_codes_file):
        """
        Initialize the InviteCodeValidator with a JSON file containing valid invite codes and user data.
        
        :param invite_codes_file: Path to the JSON file containing invite codes and user information.
        """
        self.invite_codes_file = invite_codes_file
        self.invite_codes_data = self.load_invite_codes()

    def load_invite_codes(self):
        """
        Load the invite codes data from a JSON file.

        :return: A dictionary containing invite codes and corresponding user data.
        :raises FileNotFoundError: If the invite codes file does not exist.
        :raises json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(self.invite_codes_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Error: The file {self.invite_codes_file} was not found.") from e
        except json.JSONDecodeError as e:
            raise ValueError("Error: The invite codes file contains invalid JSON.") from e

    def validate_invite_code(self, code):
        """
        Validate the invite code and return the corresponding user data if valid.

        :param code: The invite code to validate.
        :return: User data associated with the valid invite code.
        :raises ValueError: If the invite code is invalid.
        """
        if code in self.invite_codes_data:
            return self.invite_codes_data[code]
        else:
            raise ValueError("Invalid invite code. Please check the code and try again.")

def main():
    """
    Main function to demonstrate the invite code validation process.
    """
    # Path to the JSON file containing invite codes and user data
    invite_codes_file = 'invite_codes.json'

    # Create an instance of InviteCodeValidator
    validator = InviteCodeValidator(invite_codes_file)

    # Example invite code to validate
    invite_code_to_validate = input("Please enter your invite code: ")

    try:
        # Validate the invite code and retrieve user data
        user_data = validator.validate_invite_code(invite_code_to_validate)
        print("Welcome! Here is your user data:", user_data)
    except (ValueError, FileNotFoundError) as e:
        print(e)

if __name__ == "__main__":
    main()
```

**Example content of `invite_codes.json`:**
```json
{
    "CODE123": {"name": "Alice", "email": "alice@example.com"},
    "CODE456": {"name": "Bob", "email": "bob@example.com"}
}
```
