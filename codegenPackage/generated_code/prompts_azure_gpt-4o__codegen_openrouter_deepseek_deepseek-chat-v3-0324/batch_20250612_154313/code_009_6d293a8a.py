"""
Generated Code Metadata:
========================
Original URL: https://amexgiftcardbalance.net
Prompt: Write a tutorial for implementing a "no hidden fees" prepaid card system similar to the Amex Gift Card, based on the benefits highlighted on AmexGiftCard.com.
Generated: DETERMINISTIC_6d293a8a627dc787
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Prepaid Card System Implementation
Inspired by Amex Gift Card features:
- No hidden fees
- Easy online balance check
- Secure transactions
- Wide acceptance
"""

import uuid
import datetime
from decimal import Decimal
from typing import Optional, List, Dict

class PrepaidCard:
    """
    Represents a prepaid card with no hidden fees.
    """
    
    def __init__(self, initial_balance: Decimal, card_number: Optional[str] = None):
        """
        Initialize a new prepaid card.
        
        Args:
            initial_balance: Initial amount loaded onto the card
            card_number: Optional card number (will generate if None)
        """
        if initial_balance <= Decimal('0'):
            raise ValueError("Initial balance must be positive")
            
        self.card_number = card_number or str(uuid.uuid4()).replace('-', '')[:16]
        self.balance = initial_balance
        self.activation_date = datetime.datetime.now()
        self.expiration_date = self.activation_date + datetime.timedelta(days=365*5)  # 5 years
        self.transaction_history: List[Dict] = []
        self.is_active = True
        
    def make_purchase(self, amount: Decimal, merchant: str) -> bool:
        """
        Process a purchase transaction.
        
        Args:
            amount: Transaction amount
            merchant: Merchant name
            
        Returns:
            bool: True if transaction succeeded, False otherwise
        """
        if not self.is_active:
            raise ValueError("Card is not active")
            
        if amount <= Decimal('0'):
            raise ValueError("Amount must be positive")
            
        if datetime.datetime.now() > self.expiration_date:
            raise ValueError("Card has expired")
            
        if amount > self.balance:
            return False
            
        self.balance -= amount
        self._record_transaction(
            amount=amount,
            merchant=merchant,
            transaction_type="PURCHASE"
        )
        return True
        
    def check_balance(self) -> Decimal:
        """
        Check the current card balance.
        
        Returns:
            Decimal: Current balance
        """
        return self.balance
        
    def get_transaction_history(self) -> List[Dict]:
        """
        Get full transaction history.
        
        Returns:
            List[Dict]: List of transaction records
        """
        return self.transaction_history.copy()
        
    def deactivate(self) -> None:
        """
        Deactivate the card.
        """
        self.is_active = False
        
    def _record_transaction(self, amount: Decimal, merchant: str, transaction_type: str) -> None:
        """
        Record a transaction in history.
        
        Args:
            amount: Transaction amount
            merchant: Merchant name
            transaction_type: Type of transaction
        """
        self.transaction_history.append({
            'timestamp': datetime.datetime.now(),
            'amount': amount,
            'merchant': merchant,
            'type': transaction_type,
            'remaining_balance': self.balance
        })

class PrepaidCardSystem:
    """
    Manages multiple prepaid cards in a system.
    """
    
    def __init__(self):
        self.cards: Dict[str, PrepaidCard] = {}
        
    def issue_card(self, initial_balance: Decimal) -> PrepaidCard:
        """
        Issue a new prepaid card.
        
        Args:
            initial_balance: Initial amount to load
            
        Returns:
            PrepaidCard: The newly created card
        """
        card = PrepaidCard(initial_balance)
        self.cards[card.card_number] = card
        return card
        
    def get_card(self, card_number: str) -> Optional[PrepaidCard]:
        """
        Retrieve a card by number.
        
        Args:
            card_number: Card identifier
            
        Returns:
            Optional[PrepaidCard]: Card if found, None otherwise
        """
        return self.cards.get(card_number)
        
    def check_balance(self, card_number: str) -> Optional[Decimal]:
        """
        Check balance of a card.
        
        Args:
            card_number: Card identifier
            
        Returns:
            Optional[Decimal]: Balance if card found, None otherwise
        """
        card = self.get_card(card_number)
        return card.check_balance() if card else None
        
    def make_purchase(self, card_number: str, amount: Decimal, merchant: str) -> bool:
        """
        Process a purchase with a card.
        
        Args:
            card_number: Card identifier
            amount: Transaction amount
            merchant: Merchant name
            
        Returns:
            bool: True if transaction succeeded, False otherwise
        """
        card = self.get_card(card_number)
        if not card:
            return False
        return card.make_purchase(amount, merchant)

# Example usage
if __name__ == "__main__":
    # Initialize the card system
    system = PrepaidCardSystem()
    
    # Issue a new card with $100 balance
    card = system.issue_card(Decimal('100.00'))
    print(f"Card issued: {card.card_number}")
    
    # Check balance
    balance = system.check_balance(card.card_number)
    print(f"Initial balance: ${balance}")
    
    # Make a purchase
    success = system.make_purchase(card.card_number, Decimal('25.50'), "Amazon")
    print(f"Purchase {'succeeded' if success else 'failed'}")
    
    # Check new balance
    balance = system.check_balance(card.card_number)
    print(f"New balance: ${balance}")
    
    # Get transaction history
    history = card.get_transaction_history()
    print(f"Transaction history: {history}")
```
