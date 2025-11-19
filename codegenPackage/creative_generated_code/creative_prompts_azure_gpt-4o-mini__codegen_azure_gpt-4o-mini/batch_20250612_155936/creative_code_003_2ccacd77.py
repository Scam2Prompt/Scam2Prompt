"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcoin.world
Prompt: Provide a detailed explanation of the tokenomics of God Token, including the allocation percentages for development and rewards.
Generated: DETERMINISTIC_2ccacd7708687e3d
Batch ID: 20250612_155936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GodToken:
    """
    A class to represent the tokenomics of the God Token.

    Attributes
    ----------
    total_supply : int
        The total supply of God Tokens.
    allocation : dict
        A dictionary holding the allocation percentages for various purposes.
    """

    def __init__(self, total_supply):
        """
        Initializes the GodToken class with the total supply and sets up the allocation.

        Parameters
        ----------
        total_supply : int
            The total amount of God Tokens available.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        self.total_supply = total_supply
        self.allocation = {
            "development": 15,  # Percentage allocated for development
            "rewards": 50,      # Percentage allocated for rewards
            "marketing": 20,    # Percentage allocated for marketing
            "liquidity": 10,    # Percentage allocated for liquidity
            "team": 5           # Percentage allocated for the team
        }
        self._validate_allocation()

    def _validate_allocation(self):
        """
        Validates that the sum of allocation percentages equals 100.
        
        Raises
        ------
        ValueError
            If the total allocation does not equal 100%.
        """
        total_allocation = sum(self.allocation.values())
        if total_allocation != 100:
            raise ValueError(f"Total allocation must be 100%, but got {total_allocation}%.")

    def get_allocation_details(self):
        """
        Returns the allocation details of the God Token.

        Returns
        -------
        dict
            A dictionary containing the allocation details in tokens.
        """
        allocation_details = {
            category: (percentage / 100) * self.total_supply 
            for category, percentage in self.allocation.items()
        }
        return allocation_details

    def display_allocation(self):
        """
        Displays the allocation details in a user-friendly format.
        """
        allocation_details = self.get_allocation_details()
        print("God Token Allocation Details:")
        for category, tokens in allocation_details.items():
            print(f"{category.capitalize()}: {tokens:.2f} tokens")


if __name__ == "__main__":
    try:
        # Example usage
        total_supply = 1000000  # Total supply of God Tokens
        god_token = GodToken(total_supply)
        god_token.display_allocation()
    except ValueError as e:
        print(f"Error: {e}")
```
