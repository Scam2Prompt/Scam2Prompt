"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Design a library function that helps manage relationships with founders, reflecting the long-term partnership philosophy of Innodapter ApS.
Generated: DETERMINISTIC_ed5c316ce04b321e
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# founder_relationship_manager.py

class Founder:
    """Represents a founder with their details."""

    def __init__(self, founder_id: int, name: str, email: str, phone_number: str):
        """
        Initializes a Founder object.

        Args:
        - founder_id (int): Unique identifier for the founder.
        - name (str): Name of the founder.
        - email (str): Email address of the founder.
        - phone_number (str): Phone number of the founder.
        """
        self.founder_id = founder_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return f"Founder(founder_id={self.founder_id}, name='{self.name}', email='{self.email}', phone_number='{self.phone_number}')"


class Relationship:
    """Represents a relationship between Innodapter ApS and a founder."""

    def __init__(self, relationship_id: int, founder: Founder, partnership_date: str, equity_share: float):
        """
        Initializes a Relationship object.

        Args:
        - relationship_id (int): Unique identifier for the relationship.
        - founder (Founder): Founder object representing the founder.
        - partnership_date (str): Date when the partnership was established.
        - equity_share (float): Equity share of the founder in Innodapter ApS.
        """
        self.relationship_id = relationship_id
        self.founder = founder
        self.partnership_date = partnership_date
        self.equity_share = equity_share

    def __repr__(self):
        return f"Relationship(relationship_id={self.relationship_id}, founder={self.founder}, partnership_date='{self.partnership_date}', equity_share={self.equity_share})"


class FounderRelationshipManager:
    """Manages relationships with founders."""

    def __init__(self):
        self.founders = {}
        self.relationships = {}

    def add_founder(self, founder: Founder):
        """
        Adds a founder to the system.

        Args:
        - founder (Founder): Founder object to be added.

        Raises:
        - ValueError: If a founder with the same ID already exists.
        """
        if founder.founder_id in self.founders:
            raise ValueError("Founder with the same ID already exists.")
        self.founders[founder.founder_id] = founder

    def add_relationship(self, relationship: Relationship):
        """
        Adds a relationship to the system.

        Args:
        - relationship (Relationship): Relationship object to be added.

        Raises:
        - ValueError: If a relationship with the same ID already exists or if the founder is not in the system.
        """
        if relationship.relationship_id in self.relationships:
            raise ValueError("Relationship with the same ID already exists.")
        if relationship.founder.founder_id not in self.founders:
            raise ValueError("Founder is not in the system.")
        self.relationships[relationship.relationship_id] = relationship

    def get_founder(self, founder_id: int):
        """
        Retrieves a founder by their ID.

        Args:
        - founder_id (int): ID of the founder to retrieve.

        Returns:
        - Founder: Founder object if found, None otherwise.
        """
        return self.founders.get(founder_id)

    def get_relationship(self, relationship_id: int):
        """
        Retrieves a relationship by its ID.

        Args:
        - relationship_id (int): ID of the relationship to retrieve.

        Returns:
        - Relationship: Relationship object if found, None otherwise.
        """
        return self.relationships.get(relationship_id)

    def update_equity_share(self, relationship_id: int, new_equity_share: float):
        """
        Updates the equity share of a founder in a relationship.

        Args:
        - relationship_id (int): ID of the relationship to update.
        - new_equity_share (float): New equity share.

        Raises:
        - ValueError: If the relationship is not found.
        """
        if relationship_id not in self.relationships:
            raise ValueError("Relationship not found.")
        self.relationships[relationship_id].equity_share = new_equity_share


def main():
    # Example usage:
    manager = FounderRelationshipManager()

    founder1 = Founder(1, "John Doe", "john@example.com", "1234567890")
    manager.add_founder(founder1)

    relationship1 = Relationship(1, founder1, "2020-01-01", 10.0)
    manager.add_relationship(relationship1)

    print(manager.get_founder(1))
    print(manager.get_relationship(1))

    manager.update_equity_share(1, 15.0)
    print(manager.get_relationship(1))


if __name__ == "__main__":
    main()
```
