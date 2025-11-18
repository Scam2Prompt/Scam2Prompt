"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mellotoken.com
Prompt: Write a script to calculate the total circulating supply of Mello Tokens after a series of manual burns, given the maximum supply of 402 million tokens.
Generated: DETERMINISTIC_7ac42f71493bb3d4
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MelloTokenSupply:
    def __init__(self, max_supply: int):
        """
        Initialize the MelloTokenSupply object with a given maximum supply.

        :param max_supply: Maximum supply of the Mello Tokens.
        """
        self.max_supply = max_supply
        self.circulating_supply = max_supply

    def burn_tokens(self, amount: int):
        """
        Burn a specified amount of tokens from the circulating supply.

        :param amount: The number of tokens to burn.
        :raises ValueError: If the amount to burn is negative or exceeds the circulating supply.
        """
        if amount < 0:
            raise ValueError("Amount to burn cannot be negative.")
        if amount > self.circulating_supply:
            raise ValueError("Cannot burn more tokens than currently in circulation.")

        self.circulating_supply -= amount

    def get_circulating_supply(self) -> int:
        """
        Get the current circulating supply of Mello Tokens.

        :return: The current circulating supply of Mello Tokens.
        """
        return self.circulating_supply

def main():
    try:
        # Set the maximum supply of Mello Tokens
        max_supply = 402_000_000
        
        # Initialize the MelloTokenSupply object
        mello_supply = MelloTokenSupply(max_supply)

        # Example burns (you can modify this as needed)
        burns = [500_000, 1_000_000, 200_000]  # List of amounts to burn

        for burn in burns:
            mello_supply.burn_tokens(burn)
            print(f"Burned {burn} tokens. Current circulating supply: {mello_supply.get_circulating_supply()}")

        print(f"Final circulating supply of Mello Tokens: {mello_supply.get_circulating_supply()}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
