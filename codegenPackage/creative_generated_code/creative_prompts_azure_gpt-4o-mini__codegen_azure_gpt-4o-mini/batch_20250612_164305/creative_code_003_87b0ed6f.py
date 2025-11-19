"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiaoni35loah6mxudvrxltj6qkb5afmoqjqbg2spapid2kltvnqvby.ipfs.dweb.link
Prompt: Create a function that calculates the potential bonus interest shares for liquidity providers on the NAVI Protocol, considering the maximum rate of 23%.
Generated: DETERMINISTIC_87b0ed6fd598ae4b
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NAVIBonusCalculator:
    """
    A class to calculate potential bonus interest shares for liquidity providers on the NAVI Protocol.
    """

    MAX_RATE = 0.23  # Maximum bonus interest rate of 23%

    def __init__(self, total_shares, liquidity_contributed):
        """
        Initializes the NAVIBonusCalculator with required parameters.

        Parameters:
        total_shares (float): The total shares in the liquidity pool.
        liquidity_contributed (float): The amount of liquidity contributed by the provider.
        """
        self.total_shares = total_shares
        self.liquidity_contributed = liquidity_contributed

    def calculate_bonus_interest(self):
        """
        Calculates the potential bonus interest shares based on contributions.

        Returns:
        float: The potential bonus interest shares for the liquidity provider.

        Raises:
        ValueError: If total_shares or liquidity_contributed are non-positive.
        """
        if self.total_shares <= 0:
            raise ValueError("Total shares must be greater than zero.")
        if self.liquidity_contributed < 0:
            raise ValueError("Liquidity contributed cannot be negative.")

        # Calculate the share of liquidity provider in the total shares
        share_of_provider = self.liquidity_contributed / self.total_shares
        
        # Calculate the potential bonus interest shares
        bonus_interest = share_of_provider * self.MAX_RATE
        
        return bonus_interest

# Example usage
if __name__ == "__main__":
    try:
        total_shares = 1000000.0  # Example total shares in the pool
        liquidity_contributed = 5000.0  # Example liquidity contributed by the provider

        calculator = NAVIBonusCalculator(total_shares, liquidity_contributed)
        bonus = calculator.calculate_bonus_interest()
        
        print(f"Potential Bonus Interest Shares: {bonus:.4f}")
    except ValueError as e:
        print(f"Error: {e}")
```
