"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website2-70z.pages.dev
Prompt: Design a library function that helps manage relationships with founders, reflecting the long-term partnership philosophy of Innodapter ApS.
Generated: DETERMINISTIC_ed5c316ce04b321e
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Founder:
    """
    Class representing a founder in the relationships management system.
    """

    def __init__(self, name: str, email: str):
        """
        Initializes a new Founder instance.

        :param name: The name of the founder.
        :param email: The email address of the founder.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(email, str) or not email:
            raise ValueError("Email must be a non-empty string.")

        self.name = name
        self.email = email
        self.relationships = []

    def add_relationship(self, relationship: str):
        """
        Adds a new relationship to the founder's list of relationships.

        :param relationship: A description of the relationship.
        """
        if not isinstance(relationship, str) or not relationship:
            raise ValueError("Relationship must be a non-empty string.")
        self.relationships.append(relationship)

    def remove_relationship(self, relationship: str):
        """
        Removes a relationship from the founder's list.

        :param relationship: A description of the relationship to be removed.
        :raises ValueError: If the relationship is not found.
        """
        try:
            self.relationships.remove(relationship)
        except ValueError:
            raise ValueError("Relationship not found.")

    def get_relationships(self):
        """
        Returns the list of relationships.

        :return: List of relationships.
        """
        return self.relationships


class FounderManager:
    """
    Class to manage multiple founders and their relationships.
    """

    def __init__(self):
        """Initializes the FounderManager with an empty list of founders."""
        self.founders = {}

    def add_founder(self, founder: Founder):
        """
        Adds a founder to the manager.

        :param founder: An instance of the Founder class.
        :raises ValueError: If the founder is already managed.
        """
        if founder.email in self.founders:
            raise ValueError("Founder with this email already exists.")
        self.founders[founder.email] = founder

    def remove_founder(self, email: str):
        """
        Removes a founder from the manager.

        :param email: The email of the founder to be removed.
        :raises KeyError: If the founder is not found.
        """
        if email not in self.founders:
            raise KeyError("Founder not found.")
        del self.founders[email]

    def get_founder(self, email: str) -> Founder:
        """
        Retrieves a founder by email.

        :param email: The email of the founder to retrieve.
        :return: An instance of the Founder class.
        :raises KeyError: If the founder is not found.
        """
        if email not in self.founders:
            raise KeyError("Founder not found.")
        return self.founders[email]

    def get_all_founders(self):
        """
        Returns a list of all managed founders.

        :return: List of Founder instances.
        """
        return list(self.founders.values())
```
