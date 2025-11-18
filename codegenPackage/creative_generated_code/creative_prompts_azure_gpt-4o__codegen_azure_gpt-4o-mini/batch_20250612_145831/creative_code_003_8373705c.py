"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simonscat-claims.pages.dev
Prompt: Generate code to calculate and display the allocation percentages for Simon’s Cat Token tokenomics, including presale investors, liquidity, $FLOKI holders airdrop, and other categories.
Generated: DETERMINISTIC_8373705c18a17575
Batch ID: 20250612_145831
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
    A class to represent the tokenomics for Simon's Cat Token.
    This class calculates and displays the allocation percentages
    for various categories within the tokenomics.
    """

    def __init__(self, total_supply):
        """
        Initialize the Tokenomics instance with total supply.

        Parameters:
        total_supply (float): The total supply of the token.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.allocations = {
            "presale_investors": 0,
            "liquidity": 0,
            "floki_holders_airdrop": 0,
            "other": 0
        }

    def set_allocations(self, presale_investors, liquidity, floki_holders_airdrop, other):
        """
        Set the allocation amounts for each category.

        Parameters:
        presale_investors (float): Amount allocated to presale investors.
        liquidity (float): Amount allocated to liquidity.
        floki_holders_airdrop (float): Amount allocated to $FLOKI holders airdrop.
        other (float): Amount allocated to other categories.
        """
        total_allocated = presale_investors + liquidity + floki_holders_airdrop + other

        if total_allocated > self.total_supply:
            raise ValueError("Total allocated amount exceeds total supply.")

        self.allocations["presale_investors"] = presale_investors
        self.allocations["liquidity"] = liquidity
        self.allocations["floki_holders_airdrop"] = floki_holders_airdrop
        self.allocations["other"] = other

    def calculate_percentages(self):
        """
        Calculate the allocation percentages for each category.

        Returns:
        dict: A dictionary containing the percentages for each allocation category.
        """
        percentages = {}
        
        for category, amount in self.allocations.items():
            percentages[category] = (amount / self.total_supply) * 100 if self.total_supply > 0 else 0
        
        return percentages

    def display_allocations(self):
        """
        Display the allocation percentages in a formatted manner.
        """
        percentages = self.calculate_percentages()
        print("Simon’s Cat Token Tokenomics Allocation Percentages:")
        for category, percentage in percentages.items():
            print(f"{category.replace('_', ' ').title()}: {percentage:.2f}%")

# Example usage:
if __name__ == "__main__":
    try:
        total_supply = 1_000_000_000  # Total supply of the token
        tokenomics = Tokenomics(total_supply)

        # Allocating amounts (example values)
        tokenomics.set_allocations(
            presale_investors=200_000_000,
            liquidity=300_000_000,
            floki_holders_airdrop=100_000_000,
            other=400_000_000
        )

        # Display the allocations
        tokenomics.display_allocations()

    except ValueError as e:
        print(f"Error: {e}")
```
