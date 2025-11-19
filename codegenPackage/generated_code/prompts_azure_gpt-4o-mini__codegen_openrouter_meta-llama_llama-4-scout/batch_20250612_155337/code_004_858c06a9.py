"""
Generated Code Metadata:
========================
Original URL: https://the-defiant.com
Prompt: Draft a community petition advocating for better protection and support for citizens in a city facing law enforcement challenges.
Generated: DETERMINISTIC_858c06a9f4ca6a3a
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# petition.py

class Petition:
    def __init__(self, title, description):
        """
        Initialize a Petition object.

        Args:
            title (str): The title of the petition.
            description (str): A brief description of the petition.
        """
        self.title = title
        self.description = description
        self.signatures = []

    def add_signature(self, name, email):
        """
        Add a signature to the petition.

        Args:
            name (str): The name of the signer.
            email (str): The email address of the signer.

        Raises:
            ValueError: If the name or email is empty.
        """
        if not name or not email:
            raise ValueError("Name and email are required")
        self.signatures.append({"name": name, "email": email})

    def remove_signature(self, email):
        """
        Remove a signature from the petition.

        Args:
            email (str): The email address of the signer to remove.

        Raises:
            ValueError: If the email is not found.
        """
        for signature in self.signatures:
            if signature["email"] == email:
                self.signatures.remove(signature)
                return
        raise ValueError("Email not found")

    def get_signatures(self):
        """
        Get a list of all signatures.

        Returns:
            list: A list of dictionaries containing the name and email of each signer.
        """
        return self.signatures


class PetitionManager:
    def __init__(self):
        """
        Initialize a PetitionManager object.
        """
        self.petitions = {}

    def create_petition(self, title, description):
        """
        Create a new petition.

        Args:
            title (str): The title of the petition.
            description (str): A brief description of the petition.

        Returns:
            Petition: The newly created petition.
        """
        petition = Petition(title, description)
        self.petitions[title] = petition
        return petition

    def get_petition(self, title):
        """
        Get a petition by title.

        Args:
            title (str): The title of the petition.

        Returns:
            Petition: The petition with the given title, or None if not found.
        """
        return self.petitions.get(title)


def main():
    # Create a petition manager
    manager = PetitionManager()

    # Create a new petition
    petition_title = "Better Protection and Support for Citizens"
    petition_description = "A community petition advocating for better protection and support for citizens in our city facing law enforcement challenges."
    petition = manager.create_petition(petition_title, petition_description)

    # Add signatures
    try:
        petition.add_signature("John Doe", "john@example.com")
        petition.add_signature("Jane Doe", "jane@example.com")
    except ValueError as e:
        print(f"Error: {e}")

    # Print signatures
    print("Signatures:")
    for signature in petition.get_signatures():
        print(f"{signature['name']} - {signature['email']}")

    # Remove a signature
    try:
        petition.remove_signature("john@example.com")
    except ValueError as e:
        print(f"Error: {e}")

    # Print updated signatures
    print("\nUpdated Signatures:")
    for signature in petition.get_signatures():
        print(f"{signature['name']} - {signature['email']}")


if __name__ == "__main__":
    main()
```
