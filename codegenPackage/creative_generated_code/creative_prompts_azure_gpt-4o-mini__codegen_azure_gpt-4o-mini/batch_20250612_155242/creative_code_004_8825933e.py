"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimehere.pages.dev
Prompt: Explain how to use the Verse Burn Engine to reduce the total supply of VERSE tokens, including any relevant code examples.
Generated: DETERMINISTIC_8825933e1b8c6d7f
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Verse Burn Engine - Token Reduction using VERSE Tokens

This script demonstrates how to use the Verse Burn Engine to reduce the total supply of VERSE tokens.
It includes a simple class structure and methods for burning tokens while ensuring proper error handling.
"""

class VerseToken:
    def __init__(self, total_supply: int):
        """
        Initializes the VerseToken class with a total supply of tokens.
        
        Parameters:
            total_supply (int): The initial total supply of VERSE tokens.
        """
        self.total_supply = total_supply

    def burn_tokens(self, amount: int) -> None:
        """
        Burns a specified amount of VERSE tokens, reducing the total supply.
        
        Parameters:
            amount (int): The number of tokens to burn.
        
        Raises:
            ValueError: If the amount is greater than the current total supply
                         or if the amount is not positive.
        """
        # Validate the amount to burn
        if amount <= 0:
            raise ValueError("Amount to burn must be positive and greater than zero.")
        if amount > self.total_supply:
            raise ValueError("Cannot burn more tokens than the current total supply.")

        # Reduce the total supply
        self.total_supply -= amount
        print(f"Burned {amount} VERSE tokens. New total supply: {self.total_supply}")

def main():
    """
    Main function to execute the token burning process.
    """
    # Initialize with a total supply of 1,000,000 VERSE tokens
    verse_token = VerseToken(total_supply=1_000_000)

    try:
        # Example: Burn 10,000 VERSE tokens
        verse_token.burn_tokens(10_000)

        # Attempt to burn an invalid amount
        verse_token.burn_tokens(1_200_000)  # This will raise an error

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
