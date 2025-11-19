"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-en.web.app
Prompt: What are the tokenomics of GigaChadGPT, and how is the total supply of 100,000,000 tokens allocated?
Generated: DETERMINISTIC_9bdf160773854b2f
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    """
    A class to represent the tokenomics of GigaChadGPT.
    
    Attributes
    ----------
    total_supply : int
        Total supply of tokens
    allocation : dict
        Allocation of tokens for different purposes
    """

    def __init__(self, total_supply):
        """
        Initializes the Tokenomics with a total supply and its allocation.

        Parameters
        ----------
        total_supply : int
            The total number of tokens available
        """
        self.total_supply = total_supply
        self.allocation = {
            "team": 0.20,       # 20% allocated to the team
            "development": 0.30, # 30% for development and operations
            "marketing": 0.25,   # 25% for marketing
            "community": 0.15,   # 15% for community incentives
            "reserve": 0.10      # 10% reserved for future use
        }
        self.validate_allocation()
    
    def validate_allocation(self):
        """
        Validates the token allocation to ensure it sums up to 100%.
        
        Raises
        ------
        ValueError
            If the total allocation does not add up to 1 (100%)
        """
        total_allocation = sum(self.allocation.values())
        if total_allocation != 1.0:
            raise ValueError(f"Total allocation must equal 1.0, but got {total_allocation}")

    def get_allocation_details(self):
        """
        Returns a detailed breakdown of token allocation.

        Returns
        -------
        dict
            A dictionary with the allocated token amounts for each purpose
        """
        return {key: value * self.total_supply for key, value in self.allocation.items()}

    def display_tokenomics(self):
        """
        Prints the tokenomics details in a readable format.
        """
        print(f"Total Supply: {self.total_supply} tokens")
        print("Token Allocation:")
        for purpose, amount in self.get_allocation_details().items():
            print(f" - {purpose}: {amount} tokens")


# Example usage
if __name__ == "__main__":
    try:
        total_tokens = 100_000_000  # Total supply of tokens
        giga_chad_gpt_tokenomics = Tokenomics(total_tokens)
        giga_chad_gpt_tokenomics.display_tokenomics()
    except ValueError as e:
        print(f"Error: {e}")
```
