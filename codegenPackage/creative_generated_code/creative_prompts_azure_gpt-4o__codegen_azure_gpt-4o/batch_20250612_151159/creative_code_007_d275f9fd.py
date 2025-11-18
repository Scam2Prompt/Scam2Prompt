"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgeqom.pages.dev
Prompt: Write code to mint and manage QOM.One Cards on the QOM blockchain, ensuring compliance with community-driven project guidelines.
Generated: DETERMINISTIC_d275f9fdd7de48be
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import hashlib
import json
from datetime import datetime
from uuid import uuid4

class QOMCard:
    """
    Class representing a QOM.One Card.
    """

    def __init__(self, name, description, owner_address):
        """
        Initialize a QOMCard instance.

        :param name: Name of the card
        :param description: Description of the card
        :param owner_address: Blockchain address of the card owner
        """
        self.card_id = self._generate_card_id()
        self.name = name
        self.description = description
        self.owner_address = owner_address
        self.minted_at = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    def _generate_card_id(self):
        """
        Generate a unique card ID using UUID and hashing.

        :return: A unique card ID string
        """
        unique_data = str(uuid4())
        return hashlib.sha256(unique_data.encode()).hexdigest()

    def to_dict(self):
        """
        Convert the QOMCard instance to a dictionary for serialization.

        :return: Dictionary representation of the QOMCard
        """
        return {
            'card_id': self.card_id,
            'name': self.name,
            'description': self.description,
            'owner_address': self.owner_address,
            'minted_at': self.minted_at
        }


class QOMBlockchain:
    """
    Simplified representation of a QOM blockchain for managing cards.
    """

    def __init__(self):
        """
        Initialize the QOMBlockchain instance.
        """
        self.cards = []
        self.card_index = {}

    def mint_card(self, name, description, owner_address):
        """
        Mint a new QOM.One card and add it to the blockchain.

        :param name: Name of the card
        :param description: Description of the card
        :param owner_address: Blockchain address of the card owner
        :return: The minted card details
        """
        if not name or not owner_address:
            raise ValueError("Card name and owner address are required.")
        
        new_card = QOMCard(name, description, owner_address)

        # Add the card to the blockchain
        self.cards.append(new_card)
        self.card_index[new_card.card_id] = new_card

        return new_card.to_dict()

    def transfer_card(self, card_id, new_owner_address):
        """
        Transfer ownership of a QOM.One card to a new owner.

        :param card_id: ID of the card to transfer
        :param new_owner_address: Blockchain address of the new owner
        :return: Updated card details
        """
        if card_id not in self.card_index:
            raise ValueError("Card not found.")

        if not new_owner_address:
            raise ValueError("New owner address is required.")

        # Update card ownership
        card = self.card_index[card_id]
        card.owner_address = new_owner_address

        return card.to_dict()

    def get_card(self, card_id):
        """
        Retrieve details of a specific QOM.One card.

        :param card_id: ID of the card to retrieve
        :return: Card details
        """
        if card_id not in self.card_index:
            raise ValueError("Card not found.")

        return self.card_index[card_id].to_dict()

    def list_cards(self):
        """
        List all QOM.One cards on the blockchain.

        :return: List of all card details
        """
        return [card.to_dict() for card in self.cards]


# Example usage (Uncomment to test the code)
# blockchain = QOMBlockchain()
# minted_card = blockchain.mint_card("QOMCard #1", "First card in the series", "0x1234abcd")
# print("Minted Card:", minted_card)
# updated_card = blockchain.transfer_card(minted_card['card_id'], "0x5678efgh")
# print("Updated Card:", updated_card)
# print("All Cards:", blockchain.list_cards())
```
