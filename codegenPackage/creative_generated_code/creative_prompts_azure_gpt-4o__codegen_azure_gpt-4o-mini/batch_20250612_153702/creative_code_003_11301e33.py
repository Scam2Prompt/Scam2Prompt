"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prize-03.web.app
Prompt: Write a program to calculate the remaining supply of DUST tokens based on the maximum supply of 33,300,000 and the number of tokens already airdropped.
Generated: DETERMINISTIC_11301e3380a1a5a3
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DustTokenSupply:
    MAX_SUPPLY = 33300000  # Maximum supply of DUST tokens

    def __init__(self):
        """Initializes the supply tracker with zero airdropped tokens."""
        self.air_dropped_tokens = 0

    def airdrop_tokens(self, amount: int):
        """
        Airdrop a specific amount of DUST tokens.

        Args:
            amount (int): The number of tokens to airdrop.

        Raises:
            ValueError: If the amount is negative or if it exceeds available supply.
        """
        if amount < 0:
            raise ValueError("Airdrop amount cannot be negative.")
        
        if self.air_dropped_tokens + amount > self.MAX_SUPPLY:
            raise ValueError("Airdrop exceeds maximum supply of DUST tokens.")

        self.air_dropped_tokens += amount

    def remaining_supply(self) -> int:
        """
        Calculate the remaining supply of DUST tokens.

        Returns:
            int: The number of tokens remaining.
        """
        return self.MAX_SUPPLY - self.air_dropped_tokens

    def __str__(self):
        """Provide a string representation of the current supply status."""
        return f"Remaining DUST Supply: {self.remaining_supply()}"

# Example Usage:
if __name__ == "__main__":
    dust_supply = DustTokenSupply()
    
    try:
        dust_supply.airdrop_tokens(500000)  # Airdrop 500,000 tokens
        print(dust_supply)  # Display remaining supply
        
        dust_supply.airdrop_tokens(33300000)  # Attempt to exceed max supply
    except ValueError as e:
        print(f"Error: {e}")
```
