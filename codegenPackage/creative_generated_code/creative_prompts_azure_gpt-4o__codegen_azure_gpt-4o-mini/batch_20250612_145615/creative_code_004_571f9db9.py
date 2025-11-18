"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://light-chain-ai.pages.dev
Prompt: Create a script to calculate token allocation and presale pricing for Lightchain AI, incorporating the current price and next stage price as outlined in the presale details.
Generated: DETERMINISTIC_571f9db9d76def89
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenPresale:
    def __init__(self, current_price: float, next_stage_price: float, total_tokens: int):
        """
        Initialize the TokenPresale class.

        :param current_price: The current price of a token in the presale.
        :param next_stage_price: The price of a token in the next stage of presale.
        :param total_tokens: The total number of tokens available for sale.
        """
        self.current_price = current_price
        self.next_stage_price = next_stage_price
        self.total_tokens = total_tokens

    def calculate_allocation(self, allocation_percentage: float) -> int:
        """
        Calculate the number of tokens allocated based on an allocation percentage.

        :param allocation_percentage: The percentage of total tokens to allocate.
        :return: The number of tokens allocated.
        """
        if not (0 <= allocation_percentage <= 100):
            raise ValueError("Allocation percentage must be between 0 and 100.")
        
        allocation_amount = (allocation_percentage / 100) * self.total_tokens
        return int(allocation_amount)

    def calculate_presale_pricing(self, tokens_requested: int) -> float:
        """
        Calculate the total presale price for a specified number of tokens.

        :param tokens_requested: The number of tokens to purchase.
        :return: The total presale price.
        """
        if tokens_requested < 0:
            raise ValueError("Tokens requested must be a non-negative integer.")
        
        if tokens_requested > self.total_tokens:
            raise ValueError("Requested tokens exceed total available tokens.")
        
        total_price = tokens_requested * self.current_price
        return total_price

    def presale_summary(self, allocation_percentage: float, tokens_requested: int):
        """
        Generate a summary of the presale allocation and pricing.

        :param allocation_percentage: The percentage of total tokens to allocate.
        :param tokens_requested: The number of tokens requested for purchase.
        """
        try:
            allocation = self.calculate_allocation(allocation_percentage)
            total_price = self.calculate_presale_pricing(tokens_requested)

            print(f"Token Allocation based on {allocation_percentage}%: {allocation} tokens")
            print(f"Total price for {tokens_requested} tokens at current price: ${total_price:.2f}")

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Example usage
    presale = TokenPresale(current_price=0.10, next_stage_price=0.15, total_tokens=1000000)
    presale.presale_summary(allocation_percentage=20, tokens_requested=10000)
```
