"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buy-dogepreneur.pages.dev
Prompt: Explain how DogePreneur token holders can earn passive income through real estate rental profits and provide an example of the tokenomics involved.
Generated: DETERMINISTIC_8eae1935fad32ed3
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DogePreneur:
    """
    A class to represent the DogePreneur token and its functionality for passive income 
    generation through real estate rental profits.
    """

    def __init__(self, total_supply: float):
        """
        Initialize the DogePreneur token with a total supply.
        
        :param total_supply: Total supply of DogePreneur tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.token_holders = {}  # Dictionary to hold token holders and their balances
        self.rental_income = 0.0  # Total rental income from real estate properties

    def add_token_holder(self, holder_address: str, amount: float):
        """
        Add a token holder and their balance to the system.
        
        :param holder_address: The address of the token holder.
        :param amount: The amount of tokens held by the holder.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        self.token_holders[holder_address] = self.token_holders.get(holder_address, 0) + amount

    def distribute_rental_income(self, income: float):
        """
        Distribute rental income to token holders based on their holdings.
        
        :param income: The total rental income to be distributed.
        """
        if income < 0:
            raise ValueError("Income must be a non-negative number.")
        
        self.rental_income += income  # Accumulate rental income
        
        # Calculate income per token
        income_per_token = self.rental_income / self.total_supply
        
        # Distribute income to each holder
        for holder, amount in self.token_holders.items():
            earnings = income_per_token * amount
            print(f"Distributing ${earnings:.2f} to {holder} for {amount} tokens held.")

    def get_holder_balance(self, holder_address: str) -> float:
        """
        Retrieve the balance of a token holder.
        
        :param holder_address: The address of the token holder.
        :return: The amount of tokens held by the holder.
        """
        return self.token_holders.get(holder_address, 0.0)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the DogePreneur token with a total supply of 1,000,000 tokens
        doge_token = DogePreneur(total_supply=1_000_000)

        # Add token holders
        doge_token.add_token_holder("address_1", 100_000)
        doge_token.add_token_holder("address_2", 200_000)
        
        # Simulate rental income generation
        doge_token.distribute_rental_income(income=10_000)  # Distributing $10,000 rental income
        
    except ValueError as e:
        print(f"Error: {e}")
```
