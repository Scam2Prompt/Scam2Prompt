"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Create a Python script to simulate the deflationary burn process of $GFOX tokens, reducing the circulating supply after each transaction.
Generated: DETERMINISTIC_28992b0b1de2cc81
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GFOXToken:
    """Class to represent the GFOX token and manage its deflationary burn process."""
    
    def __init__(self, total_supply: float):
        """Initialize the GFOX token with a total supply.
        
        Args:
            total_supply (float): The total supply of GFOX tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        
        self.total_supply = total_supply  # Total supply of GFOX tokens
        self.circulating_supply = total_supply  # Circulating supply of GFOX tokens

    def burn_tokens(self, amount: float) -> None:
        """Burn a specified amount of GFOX tokens from the circulating supply.
        
        Args:
            amount (float): The amount of tokens to burn.
        
        Raises:
            ValueError: If the amount to burn is negative or exceeds the circulating supply.
        """
        if amount < 0:
            raise ValueError("Burn amount must be non-negative.")
        if amount > self.circulating_supply:
            raise ValueError("Burn amount exceeds circulating supply.")
        
        self.circulating_supply -= amount  # Reduce circulating supply
        print(f"Burned {amount} GFOX tokens. New circulating supply: {self.circulating_supply:.2f} GFOX")

    def simulate_transaction(self, transaction_amount: float, burn_percentage: float) -> None:
        """Simulate a transaction and burn a specified percentage of the transaction amount.
        
        Args:
            transaction_amount (float): The amount of GFOX tokens involved in the transaction.
            burn_percentage (float): The percentage of the transaction amount to burn.
        
        Raises:
            ValueError: If the transaction amount is negative or burn percentage is out of bounds.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        if not (0 <= burn_percentage <= 100):
            raise ValueError("Burn percentage must be between 0 and 100.")
        
        # Calculate the burn amount based on the transaction amount and burn percentage
        burn_amount = transaction_amount * (burn_percentage / 100)
        print(f"Transaction amount: {transaction_amount:.2f} GFOX, Burn percentage: {burn_percentage}%, Amount to burn: {burn_amount:.2f} GFOX")
        
        # Burn the calculated amount of tokens
        self.burn_tokens(burn_amount)

    def get_supply_info(self) -> None:
        """Print the current supply information of the GFOX token."""
        print(f"Total Supply: {self.total_supply:.2f} GFOX")
        print(f"Circulating Supply: {self.circulating_supply:.2f} GFOX")


# Example usage
if __name__ == "__main__":
    try:
        # Create a GFOX token with a total supply of 1,000,000 tokens
        gfox = GFOXToken(total_supply=1_000_000)

        # Display initial supply information
        gfox.get_supply_info()

        # Simulate transactions with different burn percentages
        gfox.simulate_transaction(transaction_amount=1000, burn_percentage=2)
        gfox.simulate_transaction(transaction_amount=2000, burn_percentage=5)
        
        # Display final supply information
        gfox.get_supply_info()
    except Exception as e:
        print(f"An error occurred: {e}")
```
