"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buylibracoins.com
Prompt: Write a script to calculate bonus credits dynamically for slot games based on wallet transactions, ensuring compatibility with systems like "สล็อตวอเลทแตกง่าย."
Generated: DETERMINISTIC_ffe7ebda2d326065
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture debug information
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class WalletTransaction:
    """A class to represent a wallet transaction."""
    def __init__(self, transaction_id: str, user_id: str, amount: float):
        self.transaction_id = transaction_id
        self.user_id = user_id
        self.amount = amount

class BonusCalculator:
    """A class to calculate bonus credits based on wallet transactions."""
    
    def __init__(self, bonus_percentage: float):
        if not (0 <= bonus_percentage <= 100):
            raise ValueError("Bonus percentage must be between 0 and 100.")
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self, transaction: WalletTransaction) -> float:
        """
        Calculate the bonus credits for a given transaction.
        
        Args:
            transaction (WalletTransaction): The wallet transaction to calculate the bonus for.
        
        Returns:
            float: The calculated bonus.
        """
        if transaction.amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        
        bonus = transaction.amount * (self.bonus_percentage / 100)
        logging.debug(f"Calculated bonus for transaction {transaction.transaction_id}: {bonus}")
        return bonus

def process_transactions(transactions: list, bonus_calculator: BonusCalculator):
    """
    Process a list of wallet transactions and calculate bonuses.
    
    Args:
        transactions (list): List of WalletTransaction objects.
        bonus_calculator (BonusCalculator): The BonusCalculator instance.
    
    Returns:
        dict: A dictionary with user IDs as keys and their total bonuses as values.
    """
    user_bonuses = {}
    
    for transaction in transactions:
        try:
            bonus = bonus_calculator.calculate_bonus(transaction)
            if transaction.user_id in user_bonuses:
                user_bonuses[transaction.user_id] += bonus
            else:
                user_bonuses[transaction.user_id] = bonus
        except ValueError as e:
            logging.error(f"Error processing transaction {transaction.transaction_id}: {e}")
    
    return user_bonuses

def main():
    """Main function to execute the bonus calculation."""
    # Example transactions (mock data)
    transactions = [
        WalletTransaction(transaction_id="TX001", user_id="user1", amount=100),
        WalletTransaction(transaction_id="TX002", user_id="user2", amount=200),
        WalletTransaction(transaction_id="TX003", user_id="user1", amount=50),
    ]
    
    # Create a BonusCalculator with a 10% bonus rate
    bonus_calculator = BonusCalculator(bonus_percentage=10)
    
    # Process the transactions and calculate bonuses
    user_bonuses = process_transactions(transactions, bonus_calculator)

    # Output the calculated bonuses
    for user_id, bonus in user_bonuses.items():
        print(f"User ID: {user_id}, Total Bonus: {bonus:.2f}")

if __name__ == "__main__":
    main()
```
