"""
Generated Code Metadata:
========================
Original URL: https://gen-da6.pages.dev
Prompt: Describe the role of partners in the $ENTS ecosystem and how they contribute to its tokenomics.
Generated: DETERMINISTIC_72f06ced573a96ba
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# partners.py

from typing import List, Dict

class Partner:
    """Represents a partner in the $ENTS ecosystem."""
    
    def __init__(self, name: str, description: str, role: str):
        """
        Initializes a Partner object.

        Args:
        - name (str): The name of the partner.
        - description (str): A brief description of the partner.
        - role (str): The role of the partner in the $ENTS ecosystem.
        """
        self.name = name
        self.description = description
        self.role = role

class Tokenomics:
    """Represents the tokenomics of the $ENTS ecosystem."""
    
    def __init__(self):
        """Initializes a Tokenomics object."""
        self.partners: List[Partner] = []
        self.token_distribution: Dict[str, float] = {}

    def add_partner(self, partner: Partner):
        """
        Adds a partner to the $ENTS ecosystem.

        Args:
        - partner (Partner): The partner to add.
        """
        self.partners.append(partner)

    def update_token_distribution(self, partner_name: str, percentage: float):
        """
        Updates the token distribution for a partner.

        Args:
        - partner_name (str): The name of the partner.
        - percentage (float): The percentage of tokens allocated to the partner.

        Raises:
        - ValueError: If the partner does not exist in the ecosystem.
        """
        partner = next((p for p in self.partners if p.name == partner_name), None)
        if partner is None:
            raise ValueError(f"Partner '{partner_name}' does not exist in the ecosystem.")
        self.token_distribution[partner_name] = percentage

    def get_partner_roles(self) -> Dict[str, str]:
        """
        Retrieves the roles of all partners in the $ENTS ecosystem.

        Returns:
        - Dict[str, str]: A dictionary mapping partner names to their roles.
        """
        return {partner.name: partner.role for partner in self.partners}

    def get_token_distribution(self) -> Dict[str, float]:
        """
        Retrieves the token distribution for all partners in the $ENTS ecosystem.

        Returns:
        - Dict[str, float]: A dictionary mapping partner names to their token percentages.
        """
        return self.token_distribution


def main():
    try:
        # Create partners
        partner1 = Partner("Partner 1", "Description 1", "Development")
        partner2 = Partner("Partner 2", "Description 2", "Marketing")

        # Create tokenomics
        tokenomics = Tokenomics()
        tokenomics.add_partner(partner1)
        tokenomics.add_partner(partner2)

        # Update token distribution
        tokenomics.update_token_distribution("Partner 1", 20.0)
        tokenomics.update_token_distribution("Partner 2", 30.0)

        # Get partner roles
        partner_roles = tokenomics.get_partner_roles()
        print("Partner Roles:")
        for partner, role in partner_roles.items():
            print(f"{partner}: {role}")

        # Get token distribution
        token_distribution = tokenomics.get_token_distribution()
        print("\nToken Distribution:")
        for partner, percentage in token_distribution.items():
            print(f"{partner}: {percentage}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
