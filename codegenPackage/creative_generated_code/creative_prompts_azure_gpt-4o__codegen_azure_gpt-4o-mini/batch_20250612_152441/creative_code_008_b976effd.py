"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.whitecattoken.com
Prompt: Write code to simulate the process of token distribution during an ICO phase, adhering to the allocation percentages provided in the Crypto N' Kafe FAQ.
Generated: DETERMINISTIC_b976effd0fd4b6c5
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenDistribution:
    def __init__(self, total_tokens):
        """
        Initialize the TokenDistribution with a total number of tokens.
        
        :param total_tokens: Total number of tokens to be distributed.
        """
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive integer.")
        self.total_tokens = total_tokens
        self.allocations = {
            "team": 0.20,       # 20% for team
            "advisors": 0.10,   # 10% for advisors
            "development": 0.25, # 25% for development
            "marketing": 0.15,  # 15% for marketing
            "investors": 0.30    # 30% for investors
        }
        self.distributed_tokens = {}

    def distribute_tokens(self):
        """
        Distribute tokens according to the defined allocations.
        
        :return: A dictionary with the number of tokens distributed to each category.
        """
        for category, percentage in self.allocations.items():
            # Calculate the number of tokens for each category
            tokens_for_category = self.total_tokens * percentage
            self.distributed_tokens[category] = tokens_for_category

        return self.distributed_tokens

    def display_distribution(self):
        """
        Print the distribution of tokens in a user-friendly format.
        """
        distribution = self.distribute_tokens()
        print("Token Distribution:")
        for category, amount in distribution.items():
            print(f"{category.capitalize()}: {amount} tokens")

if __name__ == "__main__":
    try:
        # Example: Initialize with 1,000,000 total tokens
        total_tokens = 1000000
        token_distribution = TokenDistribution(total_tokens)
        token_distribution.display_distribution()
    except ValueError as e:
        print(f"Error: {e}")
```
