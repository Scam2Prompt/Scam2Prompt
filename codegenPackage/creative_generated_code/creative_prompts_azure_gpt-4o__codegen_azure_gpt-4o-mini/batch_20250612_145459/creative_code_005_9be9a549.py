"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-kelexo-en.web.app
Prompt: Suggest best practices for implementing Terms & Conditions acceptance during account creation on a blockchain-based platform like Kelexo.
Generated: DETERMINISTIC_9be9a549369b8bfa
Batch ID: 20250612_145459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
import hashlib
import json

class UserAccount:
    """
    A class to represent a user account in a blockchain-based platform.
    """
    
    def __init__(self, username: str, terms_version: str):
        """
        Initializes a new user account.

        :param username: Unique username for the user
        :param terms_version: The version of terms and conditions accepted
        """
        self.username = username
        self.terms_version = terms_version
        self.created_at = datetime.now()
        self.terms_hash = self.generate_terms_hash()

    def generate_terms_hash(self) -> str:
        """
        Generates a hash of the terms and conditions accepted by the user.

        :return: A SHA-256 hash of the terms version string
        """
        return hashlib.sha256(self.terms_version.encode()).hexdigest()

    def to_json(self) -> str:
        """
        Converts the user account information to a JSON string.

        :return: JSON representation of the user account
        """
        return json.dumps({
            "username": self.username,
            "terms_version": self.terms_version,
            "created_at": self.created_at.isoformat(),
            "terms_hash": self.terms_hash
        })


class TermsAndConditions:
    """
    A class to manage the terms and conditions for user acceptance.
    """

    def __init__(self):
        self.terms_versions = {}

    def add_terms_version(self, version: str, content: str):
        """
        Adds a new version of terms and conditions.

        :param version: The version of the terms and conditions
        :param content: The content of the terms and conditions
        """
        self.terms_versions[version] = content

    def get_latest_terms_version(self) -> str:
        """
        Gets the latest version of the terms and conditions.

        :return: The latest terms version
        """
        if not self.terms_versions:
            raise ValueError("No terms versions available.")
        return max(self.terms_versions.keys())

def create_user_account(username: str, terms_and_conditions: TermsAndConditions) -> UserAccount:
    """
    Creates a new user account after confirming terms acceptance.

    :param username: Unique username for the user
    :param terms_and_conditions: Instance of TermsAndConditions to fetch the latest terms
    :return: A UserAccount object if successful
    """
    try:
        # Retrieve the latest version of terms and conditions
        latest_terms_version = terms_and_conditions.get_latest_terms_version()
        
        # Create the user account with the latest terms version
        user_account = UserAccount(username, latest_terms_version)
        return user_account
    
    except ValueError as e:
        print(f"Error creating user account: {e}")
        raise

# Example of usage
if __name__ == "__main__":
    # Create TermsAndConditions instance
    terms_manager = TermsAndConditions()
    
    # Adding terms versions (usually this would come from a database or external source)
    terms_manager.add_terms_version("1.0", "Initial terms and conditions.")
    terms_manager.add_terms_version("2.0", "Updated terms and conditions with privacy policy.")

    # Create a new user account
    try:
        new_user = create_user_account("new_user", terms_manager)
        print("User account created successfully:", new_user.to_json())
    except Exception as e:
        print("Failed to create user account:", e)
```
