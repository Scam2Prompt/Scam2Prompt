"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudminingglobal.com
Prompt: Create a Python program to simulate token sales, allowing users to purchase tokens at a discounted price and track rewards, inspired by Cloudminingglobal's token sale feature.
Generated: DETERMINISTIC_77572dc7c12e60f8
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class TokenSale:
    """
    A class to simulate token sales with discounts and rewards tracking.
    """

    def __init__(self, token_price, discount_rate, reward_rate):
        """
        Initialize the TokenSale class.

        Args:
            token_price (float): Base price of one token.
            discount_rate (float): Discount rate applied to purchases (0-1).
            reward_rate (float): Reward rate for tokens purchased (0-1).
        """
        self.token_price = token_price
        self.discount_rate = discount_rate
        self.reward_rate = reward_rate
        self.sales = []  # List to track all token sales transactions

    def calculate_discounted_price(self, quantity):
        """
        Calculate the discounted price for purchasing tokens.

        Args:
            quantity (int): Number of tokens being purchased.

        Returns:
            float: Total cost after applying discount.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        return quantity * self.token_price * (1 - self.discount_rate)

    def calculate_rewards(self, quantity):
        """
        Calculate reward tokens based on the quantity purchased.

        Args:
            quantity (int): Number of tokens being purchased.

        Returns:
            float: Number of reward tokens earned.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        return quantity * self.reward_rate

    def purchase_tokens(self, buyer_name, quantity):
        """
        Process the token purchase transaction and record it.

        Args:
            buyer_name (str): Name of the buyer.
            quantity (int): Number of tokens being purchased.

        Returns:
            dict: Details of the completed transaction.
        """
        if not buyer_name:
            raise ValueError("Buyer name cannot be empty.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

        try:
            discounted_price = self.calculate_discounted_price(quantity)
            rewards = self.calculate_rewards(quantity)

            # Generate a unique transaction ID
            transaction_id = uuid.uuid4()

            # Create transaction record
            transaction = {
                "transaction_id": str(transaction_id),
                "buyer_name": buyer_name,
                "quantity_purchased": quantity,
                "discounted_price": discounted_price,
                "reward_tokens": rewards,
                "timestamp": datetime.now().isoformat()
            }

            # Save the transaction
            self.sales.append(transaction)

            return transaction

        except Exception as e:
            raise RuntimeError(f"Error processing token purchase: {str(e)}") from e

    def list_sales(self):
        """
        List all token sales transactions.

        Returns:
            list: List of all sales records.
        """
        return self.sales


# Example usage:
if __name__ == "__main__":
    # Set up the token sale instance
    token_sale = TokenSale(token_price=10.0, discount_rate=0.2, reward_rate=0.05)

    try:
        # Simulate a token purchase
        transaction = token_sale.purchase_tokens(buyer_name="Alice", quantity=100)
        print("Transaction successful!")
        print(transaction)

        # List all sales records
        print("\nAll Sales Records:")
        for sale in token_sale.list_sales():
            print(sale)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
