"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a68.net
Prompt: Generate a code snippet to validate user input using a unique ID verification method similar to the one found on a68.net.
Generated: DETERMINISTIC_da75dad68526cda7
Batch ID: 20250612_160625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import random

class UniqueIDValidator:
    """
    A class to validate user input against a unique ID format.
    The unique ID must follow a specific pattern defined by the system.
    """

    def __init__(self):
        # Define the regex pattern for a valid unique ID.
        self.pattern = re.compile(r'^[A-Z]{3}-\d{3}-[A-Z]{2}$')

    def validate_id(self, user_id):
        """
        Validate the user ID against the defined format.

        Parameters:
        user_id (str): The user ID to be validated.

        Returns:
        bool: True if the user ID is valid, False otherwise.
        """
        if not isinstance(user_id, str):
            raise ValueError("User ID must be a string.")
        
        # Check if the user ID matches the pattern
        is_valid = bool(self.pattern.match(user_id))
        return is_valid

    def generate_unique_id(self):
        """
        Generate a unique ID based on the defined format.

        Returns:
        str: A new unique ID in the format 'XXX-123-YY'.
        """
        # Generate random components for the unique ID
        letters = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        numbers = random.randint(100, 999)
        suffix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        
        unique_id = f"{letters}-{numbers}-{suffix}"
        return unique_id


def main():
    validator = UniqueIDValidator()

    # Example user input for validation
    user_input = "ABC-123-DE"

    try:
        if validator.validate_id(user_input):
            print(f"The user ID '{user_input}' is valid.")
        else:
            print(f"The user ID '{user_input}' is invalid.")
        
        # Generate and display a unique ID
        new_id = validator.generate_unique_id()
        print(f"Generated unique ID: {new_id}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
