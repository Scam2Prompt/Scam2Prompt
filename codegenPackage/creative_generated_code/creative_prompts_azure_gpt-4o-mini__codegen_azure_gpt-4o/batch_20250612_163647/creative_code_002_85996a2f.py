"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vimsa.com.br
Prompt: What are the steps to register and recharge a Vimsa card, and how can I implement this process programmatically?
Generated: DETERMINISTIC_85996a2fec821c2f
Batch ID: 20250612_163647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is Python code implementing the requested functionality to register and recharge a Vimsa card programmatically. The code adheres to the requirements and follows best practices.

```python
import uuid

# Define a dictionary to hold registered cards
registered_cards = {}

class Card:
    """Class representing a Vimsa card"""
    
    def __init__(self, card_id, owner_name, balance=0):
        """
        Initialize the Vimsa card with a unique ID, owner's name, and initial balance.
        
        Args:
            card_id (str): Unique identifier for the card.
            owner_name (str): Name of the card owner.
            balance (float): Initial balance on the card. Default is 0.
        """
        self.card_id = card_id
        self.owner_name = owner_name
        self.balance = balance

    def recharge(self, amount):
        """
        Recharge the card with a specified amount.
        
        Args:
            amount (float): The amount to add to the card's balance.
            
        Raises:
            ValueError: If the recharge amount is not positive.
        """
        if amount <= 0:
            raise ValueError("Recharge amount must be greater than zero.")
        self.balance += amount
        return self.balance

def register_card(owner_name):
    """
    Register a new Vimsa card for the given owner name.
    
    Args:
        owner_name (str): Name of the card owner.
        
    Returns:
        Card: The newly registered Vimsa card object.
        
    Raises:
        ValueError: If the owner name is not provided or is empty.
    """
    if not owner_name or not isinstance(owner_name, str):
        raise ValueError("Owner name must be a non-empty string.")
    
    card_id = str(uuid.uuid4())  # Generate a unique card ID
    new_card = Card(card_id=card_id, owner_name=owner_name)
    registered_cards[card_id] = new_card
    return new_card

def recharge_card(card_id, amount):
    """
    Recharge an existing Vimsa card by its card ID.
    
    Args:
        card_id (str): The unique identifier of the card to recharge.
        amount (float): The amount to add to the card's balance.
        
    Returns:
        float: The updated balance of the card.
        
    Raises:
        ValueError: If the card ID is invalid or the amount is not positive.
        KeyError: If the card ID does not exist in the system.
    """
    if card_id not in registered_cards:
        raise KeyError("Card ID not found.")
    
    card = registered_cards[card_id]
    return card.recharge(amount)

# Example Usage
if __name__ == "__main__":
    try:
        # Register a new card
        owner_name = "John Doe"
        new_card = register_card(owner_name)
        print(f"Card registered successfully: ID = {new_card.card_id}, Owner = {new_card.owner_name}, Balance = {new_card.balance}")

        # Recharge the card
        recharge_amount = 100
        updated_balance = recharge_card(new_card.card_id, recharge_amount)
        print(f"Card recharged successfully: New Balance = {updated_balance}")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

This code defines the necessary steps for registering and recharging a Vimsa card programmatically, including error handling and adherence to production-quality standards.
