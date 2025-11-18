"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogleonidas.pages.dev
Prompt: Develop a function to display the total supply of $DOG tokens (100,000,000 DOG) and track the remaining tokens available for presale.
Generated: DETERMINISTIC_1e90638bf4ab9c1d
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DogTokenPresale:
    def __init__(self, total_supply: int = 100_000_000):
        """
        Initializes the DogTokenPresale class with the total supply of DOG tokens.

        :param total_supply: The total supply of DOG tokens, default is 100,000,000
        """
        self.total_supply = total_supply
        self.remaining_tokens = total_supply  # Remaining tokens available for presale

    def display_total_supply(self) -> None:
        """
        Displays the total supply of DOG tokens.
        """
        print(f"Total Supply of DOG Tokens: {self.total_supply:,} DOG")
    
    def get_remaining_tokens(self) -> int:
        """
        Returns the number of remaining tokens available for presale.

        :return: Remaining tokens
        """
        return self.remaining_tokens

    def purchase_tokens(self, amount: int) -> str:
        """
        Allows users to purchase DOG tokens from the presale.

        :param amount: The amount of DOG tokens to purchase
        :return: Confirmation message or error message
        """
        if amount <= 0:
            return "Error: Purchase amount must be greater than zero."
        if amount > self.remaining_tokens:
            return "Error: Not enough tokens remaining for the purchase."
        
        self.remaining_tokens -= amount
        return f"Successfully purchased {amount} DOG tokens."

    def display_remaining_tokens(self) -> None:
        """
        Displays the number of remaining DOG tokens available for presale.
        """
        print(f"Remaining DOG Tokens for Presale: {self.remaining_tokens:,} DOG")


# Example usage
if __name__ == "__main__":
    presale = DogTokenPresale()
    presale.display_total_supply()
    presale.display_remaining_tokens()
    
    # Example of purchasing tokens
    result = presale.purchase_tokens(10_000)
    print(result)
    
    presale.display_remaining_tokens()
```
