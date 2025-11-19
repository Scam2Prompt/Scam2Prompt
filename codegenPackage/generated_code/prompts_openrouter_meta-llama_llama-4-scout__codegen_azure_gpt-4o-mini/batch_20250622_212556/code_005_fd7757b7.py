"""
Generated Code Metadata:
========================
Original URL: https://kishu.finance
Prompt: Describe the process of burning Kishu Inu tokens and its significance in the context of the project's tokenomics.
Generated: DETERMINISTIC_fd7757b785f23d1a
Batch ID: 20250622_212556
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class KishuInuToken:
    def __init__(self, total_supply):
        """
        Initializes the Kishu Inu Token with a specified total supply.
        
        :param total_supply: Total number of tokens created at the start.
        """
        self.total_supply = total_supply
        self.burned_tokens = 0

    def burn_tokens(self, amount):
        """
        Burns a specified amount of Kishu Inu tokens, reducing the total supply.
        
        :param amount: The number of tokens to burn.
        :raises ValueError: If the amount to burn exceeds the available supply.
        """
        if amount <= 0:
            raise ValueError("Amount to burn must be greater than zero.")
        if amount > self.total_supply - self.burned_tokens:
            raise ValueError("Cannot burn more tokens than available supply.")

        self.burned_tokens += amount
        self.total_supply -= amount
        print(f"Burned {amount} tokens. Total burned: {self.burned_tokens}. Remaining supply: {self.total_supply}.")

    def get_total_supply(self):
        """
        Returns the current total supply of Kishu Inu tokens.
        
        :return: Current total supply.
        """
        return self.total_supply

    def get_burned_tokens(self):
        """
        Returns the total number of burned Kishu Inu tokens.
        
        :return: Total burned tokens.
        """
        return self.burned_tokens


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Kishu Inu Token with a total supply of 1 billion tokens
        token = KishuInuToken(total_supply=1_000_000_000)

        # Burn a certain amount of tokens
        token.burn_tokens(100_000)

        # Display current supply and burned tokens
        print(f"Current total supply: {token.get_total_supply()}")
        print(f"Total burned tokens: {token.get_burned_tokens()}")

    except ValueError as e:
        print(f"Error: {e}")
```
