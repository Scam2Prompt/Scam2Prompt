"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asd-col.pages.dev
Prompt: Create a function that calculates the number of $DOG tokens received for a given ETH amount during the presale.
Generated: DETERMINISTIC_786443608142c4b5
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Presale:
    def __init__(self, eth_to_dog_rate):
        """
        Initialize the Presale with the conversion rate from ETH to DOG tokens.
        
        :param eth_to_dog_rate: The number of DOG tokens received for one unit of ETH
        """
        if eth_to_dog_rate <= 0:
            raise ValueError("Conversion rate must be greater than 0.")
        self.eth_to_dog_rate = eth_to_dog_rate

    def calculate_dog_tokens(self, eth_amount):
        """
        Calculate the number of DOG tokens received for a given ETH amount.
        
        :param eth_amount: The amount of ETH to convert to DOG tokens
        :return: The number of DOG tokens received
        """
        if eth_amount < 0:
            raise ValueError("ETH amount cannot be negative.")
        
        dog_tokens = eth_amount * self.eth_to_dog_rate
        return dog_tokens

# Example usage
if __name__ == "__main__":
    try:
        # Create a presale instance with a conversion rate of 1000 DOG tokens per ETH
        presale = Presale(eth_to_dog_rate=1000)
        
        # Calculate DOG tokens for an ETH amount of 0.5
        eth_amount = 0.5
        dog_tokens_received = presale.calculate_dog_tokens(eth_amount)
        
        print(f"ETH Amount: {eth_amount} -> DOG Tokens Received: {dog_tokens_received}")
    
    except ValueError as e:
        print(f"Error: {e}")
```
