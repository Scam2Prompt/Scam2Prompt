"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnifi.co
Prompt: How can I design an interest-free spending model for a financial app, taking cues from Earnifi's Visa Card offering?
Generated: DETERMINISTIC_5864cbd37b69b143
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InterestFreeSpendingModel:
    """
    A class to represent an interest-free spending model for a financial application.
    The model tracks spending and provides methods to manage and display the spending
    while ensuring it remains interest-free.
    """

    def __init__(self, user_id: str, spending_limit: float):
        """
        Initializes the InterestFreeSpendingModel with user ID and spending limit.

        :param user_id: Unique identifier for the user
        :param spending_limit: Maximum allowable spending limit for the user
        :raises ValueError: If spending_limit is not positive
        """
        if spending_limit <= 0:
            raise ValueError("Spending limit must be a positive value.")
        
        self.user_id = user_id
        self.spending_limit = spending_limit
        self.current_spent = 0.0
        self.transactions = []

    def add_transaction(self, amount: float, description: str):
        """
        Adds a new transaction to the user's spending.

        :param amount: Amount spent in the transaction
        :param description: Description of the transaction
        :raises ValueError: If the amount is negative or exceeds the spending limit
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        if self.current_spent + amount > self.spending_limit:
            raise ValueError("Transaction exceeds spending limit.")

        self.current_spent += amount
        self.transactions.append({'amount': amount, 'description': description})
    
    def display_transactions(self):
        """
        Displays all transactions made by the user.
        """
        if not self.transactions:
            print("No transactions recorded.")
            return

        print(f"Transactions for User ID: {self.user_id}")
        for transaction in self.transactions:
            print(f"- {transaction['description']}: ${transaction['amount']:.2f}")

    def reset_spending(self):
        """
        Resets the current spending and clears all transactions.
        """
        self.current_spent = 0.0
        self.transactions.clear()
        print("Spending has been reset.")

    def get_current_spending(self) -> float:
        """
        Returns the current spending amount.

        :return: Current amount spent
        """
        return self.current_spent

    def is_within_limit(self) -> bool:
        """
        Checks if the current spending is within the allowed spending limit.

        :return: True if within limit, False otherwise
        """
        return self.current_spent <= self.spending_limit


# Example usage
if __name__ == "__main__":
    try:
        user_spending_model = InterestFreeSpendingModel(user_id="user123", spending_limit=1000.0)
        user_spending_model.add_transaction(amount=250.0, description="Grocery Purchase")
        user_spending_model.add_transaction(amount=300.0, description="Restaurant Bill")
        
        user_spending_model.display_transactions()

        print(f"Current Spending: ${user_spending_model.get_current_spending():.2f}")
        print(f"Is within limit? {user_spending_model.is_within_limit()}")

        user_spending_model.reset_spending()
    except ValueError as e:
        print(f"Error: {e}")
```
