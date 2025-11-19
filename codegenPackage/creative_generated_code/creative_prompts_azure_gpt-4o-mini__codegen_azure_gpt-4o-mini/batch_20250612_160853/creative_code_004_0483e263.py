"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethermail.pages.dev
Prompt: Provide an example of how to customize an email alias in EtherMail for better user recall and sharing.
Generated: DETERMINISTIC_0483e263eb196c38
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class EmailAlias:
    def __init__(self, user_id: str, domain: str):
        """
        Initializes the EmailAlias object.

        :param user_id: The user's unique identifier or name.
        :param domain: The domain for the email address.
        """
        self.user_id = user_id.lower()  # Normalize the user ID to lowercase
        self.domain = domain.lower()  # Normalize the domain to lowercase

    def create_alias(self, custom_alias: str) -> str:
        """
        Creates a customized email alias.

        :param custom_alias: The desired custom alias string.
        :return: The full email address as a string.
        :raises ValueError: If the custom alias is invalid.
        """
        if not self.is_valid_alias(custom_alias):
            raise ValueError("Invalid custom alias. Must contain only alphanumeric characters and underscores.")

        # Build the full email address
        full_email = f"{custom_alias}@{self.domain}"
        return full_email

    @staticmethod
    def is_valid_alias(alias: str) -> bool:
        """
        Validates the custom alias against defined rules.

        :param alias: The alias to validate.
        :return: True if valid, False otherwise.
        """
        # Allow only alphanumeric characters and underscores
        pattern = r'^[\w]+$'
        return bool(re.match(pattern, alias))

def main():
    """
    Main function to demonstrate the creation of a customized email alias.
    """
    try:
        user_id = "john_doe"  # Example user ID
        domain = "example.com"  # Example domain

        email_alias = EmailAlias(user_id, domain)

        # Example of creating a valid custom alias
        custom_alias = "johnny"
        full_email = email_alias.create_alias(custom_alias)
        print(f"Customized Email Alias: {full_email}")

        # Uncomment the line below to test invalid alias
        # invalid_alias = "johnny@doe"  # This will raise a ValueError
        # email_alias.create_alias(invalid_alias)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
