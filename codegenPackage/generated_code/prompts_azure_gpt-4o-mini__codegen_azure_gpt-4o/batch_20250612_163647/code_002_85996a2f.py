"""
Generated Code Metadata:
========================
Original URL: https://vimsa.com.br
Prompt: What are the steps to register and recharge a Vimsa card, and how can I implement this process programmatically?
Generated: DETERMINISTIC_85996a2fec821c2f
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import datetime

# Define a class for the Vimsa card system
class VimsaCardSystem:
    def __init__(self):
        # Initialize a dictionary to store card information
        self.cards = {}

    def register_card(self, card_id, owner_name):
        """
        Registers a new Vimsa card.
        
        Args:
            card_id (str): Unique identifier for the card.
            owner_name (str): Name of the card owner.
        
        Returns:
            str: Success message or error message.
        """
        if card_id in self.cards:
            return f"Error: Card ID '{card_id}' is already registered."
        
        # Register the card with initial balance of 0
        self.cards[card_id] = {
            "owner_name": owner_name,
            "balance": 0.0,
            "registration_date": datetime.datetime.now()
        }
        return f"Card '{card_id}' successfully registered for {owner_name}."

    def recharge_card(self, card_id, amount):
        """
        Recharges a Vimsa card with a specified amount.
        
        Args:
            card_id (str): Unique identifier for the card.
            amount (float): Amount to recharge.
        
        Returns:
            str: Success message or error message.
        """
        if card_id not in self.cards:
            return f"Error: Card ID '{card_id}' is not registered."
        
        if amount <= 0:
            return "Error: Recharge amount must be greater than zero."
        
        # Update the card balance
        self.cards[card_id]["balance"] += amount
        return f"Card '{card_id}' successfully recharged with ${amount:.2f}. Current balance: ${self.cards[card_id]['balance']:.2f}."

    def get_card_info(self, card_id):
        """
        Retrieves information about a Vimsa card.
        
        Args:
            card_id (str): Unique identifier for the card.
        
        Returns:
            dict: Card information or error message.
        """
        if card_id not in self.cards:
            return {"error": f"Card ID '{card_id}' is not registered."}
        
        return self.cards[card_id]


# Example usage
if __name__ == "__main__":
    # Create an instance of the VimsaCardSystem
    vimsa_system = VimsaCardSystem()

    # Register a new card
    print(vimsa_system.register_card("12345", "Alice"))

    # Attempt to register the same card again
    print(vimsa_system.register_card("12345", "Alice"))

    # Recharge the card
    print(vimsa_system.recharge_card("12345", 50.0))

    # Attempt to recharge a non-existent card
    print(vimsa_system.recharge_card("67890", 20.0))

    # Attempt to recharge with an invalid amount
    print(vimsa_system.recharge_card("12345", -10.0))

    # Retrieve card information
    print(vimsa_system.get_card_info("12345"))

    # Attempt to retrieve information for a non-existent card
    print(vimsa_system.get_card_info("67890"))
```

This code implements a simple Vimsa card registration and recharge system, adhering to the requirements for clean, efficient, and well-documented code.
