"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muitiathourize-wqme.vercel.app
Prompt: Generate code for presale token management, including token pricing and allocation, as described in the "muitiathourizechain" presale process.
Generated: DETERMINISTIC_611ab4095c836744
Batch ID: 20250612_154016
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# presale_token_management.py

class PresaleTokenManager:
    """
    A class to manage the presale of tokens including pricing and allocation.
    """

    def __init__(self, total_supply: int, token_price: float):
        """
        Initializes the PresaleTokenManager with total supply and token price.
        
        :param total_supply: Total number of tokens available for presale.
        :param token_price: Price of each token in currency units.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if token_price <= 0:
            raise ValueError("Token price must be greater than zero.")
        
        self.total_supply = total_supply
        self.token_price = token_price
        self.tokens_sold = 0
        self.sales_amount = 0.0

    def purchase_tokens(self, amount: float) -> int:
        """
        Lets users purchase tokens and updates the internal state.
        
        :param amount: Amount of currency the user wants to spend.
        :return: Number of tokens purchased.
        """
        if amount <= 0:
            raise ValueError("Purchase amount must be greater than zero.")
        
        tokens_to_purchase = int(amount // self.token_price)
        
        if tokens_to_purchase + self.tokens_sold > self.total_supply:
            raise ValueError(f"Insufficient tokens available. Only {self.total_supply - self.tokens_sold} tokens left.")
        
        self.tokens_sold += tokens_to_purchase
        self.sales_amount += amount
        
        return tokens_to_purchase

    def get_sales_info(self) -> dict:
        """
        Returns a dictionary containing sales information.
        
        :return: A dictionary with total_supply, tokens_sold, and sales_amount.
        """
        return {
            "total_supply": self.total_supply,
            "tokens_sold": self.tokens_sold,
            "sales_amount": self.sales_amount
        }

    def remaining_tokens(self) -> int:
        """
        Returns the number of tokens remaining for sale.
        
        :return: Number of tokens remaining.
        """
        return self.total_supply - self.tokens_sold

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the presale token manager
        presale_manager = PresaleTokenManager(total_supply=10000, token_price=0.5)

        # User purchases tokens
        amount_spent = 100.0
        tokens_purchased = presale_manager.purchase_tokens(amount_spent)
        print(f"Tokens purchased: {tokens_purchased}")

        # Display sales information
        sales_info = presale_manager.get_sales_info()
        print(f"Sales Information: {sales_info}")

        # Display remaining tokens
        remaining = presale_manager.remaining_tokens()
        print(f"Tokens remaining for sale: {remaining}")

    except ValueError as e:
        print(f"Error: {e}")
```
