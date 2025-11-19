"""
Generated Code Metadata:
========================
Original URL: https://thedogeverse-com.pages.dev
Prompt: Write code to implement a token allocation tracker for $DOGEVERSE, showing percentages allocated to presale, staking, liquidity, marketing, ecosystem funds, and exchanges.
Generated: DETERMINISTIC_1c9c5b31d645bd57
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenAllocationTracker:
    """
    A class to track token allocations for $DOGEVERSE.

    Attributes:
    total_supply (float): The total supply of $DOGEVERSE tokens.
    presale_allocation (float): The percentage allocated to presale.
    staking_allocation (float): The percentage allocated to staking.
    liquidity_allocation (float): The percentage allocated to liquidity.
    marketing_allocation (float): The percentage allocated to marketing.
    ecosystem_funds_allocation (float): The percentage allocated to ecosystem funds.
    exchanges_allocation (float): The percentage allocated to exchanges.
    """

    def __init__(self, total_supply: float, 
                 presale_allocation: float = 20, 
                 staking_allocation: float = 15, 
                 liquidity_allocation: float = 20, 
                 marketing_allocation: float = 10, 
                 ecosystem_funds_allocation: float = 15, 
                 exchanges_allocation: float = 20):
        """
        Initializes the TokenAllocationTracker.

        Args:
        total_supply (float): The total supply of $DOGEVERSE tokens.
        presale_allocation (float, optional): The percentage allocated to presale. Defaults to 20.
        staking_allocation (float, optional): The percentage allocated to staking. Defaults to 15.
        liquidity_allocation (float, optional): The percentage allocated to liquidity. Defaults to 20.
        marketing_allocation (float, optional): The percentage allocated to marketing. Defaults to 10.
        ecosystem_funds_allocation (float, optional): The percentage allocated to ecosystem funds. Defaults to 15.
        exchanges_allocation (float, optional): The percentage allocated to exchanges. Defaults to 20.

        Raises:
        ValueError: If the total supply or any allocation is negative.
        ValueError: If the total allocation exceeds 100%.
        """

        if total_supply < 0:
            raise ValueError("Total supply cannot be negative.")

        allocations = [presale_allocation, staking_allocation, liquidity_allocation, 
                       marketing_allocation, ecosystem_funds_allocation, exchanges_allocation]

        if any(alloc < 0 for alloc in allocations):
            raise ValueError("Allocations cannot be negative.")

        if sum(allocations) > 100:
            raise ValueError("Total allocation cannot exceed 100%.")

        self.total_supply = total_supply
        self.presale_allocation = presale_allocation
        self.staking_allocation = staking_allocation
        self.liquidity_allocation = liquidity_allocation
        self.marketing_allocation = marketing_allocation
        self.ecosystem_funds_allocation = ecosystem_funds_allocation
        self.exchanges_allocation = exchanges_allocation

    def calculate_token_allocation(self):
        """
        Calculates the token allocation for each category.

        Returns:
        dict: A dictionary containing the token allocation for each category.
        """

        presale_tokens = self.total_supply * (self.presale_allocation / 100)
        staking_tokens = self.total_supply * (self.staking_allocation / 100)
        liquidity_tokens = self.total_supply * (self.liquidity_allocation / 100)
        marketing_tokens = self.total_supply * (self.marketing_allocation / 100)
        ecosystem_funds_tokens = self.total_supply * (self.ecosystem_funds_allocation / 100)
        exchanges_tokens = self.total_supply * (self.exchanges_allocation / 100)

        return {
            "Presale": presale_tokens,
            "Staking": staking_tokens,
            "Liquidity": liquidity_tokens,
            "Marketing": marketing_tokens,
            "Ecosystem Funds": ecosystem_funds_tokens,
            "Exchanges": exchanges_tokens,
        }

    def print_token_allocation(self):
        """
        Prints the token allocation for each category.
        """

        allocations = self.calculate_token_allocation()

        print("Token Allocations:")
        for category, tokens in allocations.items():
            print(f"{category}: {tokens} ($DOGEVERSE) - {self.get_percentage(category)}%")

    def get_percentage(self, category: str):
        """
        Gets the percentage allocation for a given category.

        Args:
        category (str): The category.

        Returns:
        float: The percentage allocation for the given category.
        """

        allocations = {
            "Presale": self.presale_allocation,
            "Staking": self.staking_allocation,
            "Liquidity": self.liquidity_allocation,
            "Marketing": self.marketing_allocation,
            "Ecosystem Funds": self.ecosystem_funds_allocation,
            "Exchanges": self.exchanges_allocation,
        }

        return allocations.get(category, 0)


def main():
    try:
        tracker = TokenAllocationTracker(total_supply=1000000)
        tracker.print_token_allocation()
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
