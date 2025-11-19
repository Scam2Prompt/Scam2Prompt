"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-io.pages.dev
Prompt: Describe the tokenomics of $FROP and provide a code snippet that demonstrates how to allocate the total supply across different segments.
Generated: DETERMINISTIC_c89aaa32950029b8
Batch ID: 20250612_163854
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
    A class to represent the tokenomics of a cryptocurrency, specifically for the $FROP token.
    """

    def __init__(self, total_supply):
        """
        Initializes the Tokenomics instance with a total supply.

        Args:
            total_supply (float): The total supply of the $FROP token.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        self.total_supply = total_supply
        self.allocation = {
            "team": 0,
            "development": 0,
            "marketing": 0,
            "liquidity": 0,
            "community": 0,
            "reserve": 0,
        }

    def allocate(self, team_percentage, development_percentage, marketing_percentage,
                 liquidity_percentage, community_percentage, reserve_percentage):
        """
        Allocates the total supply of $FROP based on provided percentages.

        Args:
            team_percentage (float): Percentage for team allocation.
            development_percentage (float): Percentage for development allocation.
            marketing_percentage (float): Percentage for marketing allocation.
            liquidity_percentage (float): Percentage for liquidity allocation.
            community_percentage (float): Percentage for community allocation.
            reserve_percentage (float): Percentage for reserve allocation.

        Raises:
            ValueError: If total percentage does not equal 100 or if any percentage is negative.
        """
        total_percentage = (
            team_percentage + development_percentage + marketing_percentage +
            liquidity_percentage + community_percentage + reserve_percentage
        )

        if total_percentage != 100:
            raise ValueError("Total allocation percentages must equal 100.")
        
        if any(p < 0 for p in [
            team_percentage, development_percentage, marketing_percentage,
            liquidity_percentage, community_percentage, reserve_percentage
        ]):
            raise ValueError("Allocation percentages must be non-negative.")

        # Calculate the allocation based on the percentages
        self.allocation["team"] = (team_percentage / 100) * self.total_supply
        self.allocation["development"] = (development_percentage / 100) * self.total_supply
        self.allocation["marketing"] = (marketing_percentage / 100) * self.total_supply
        self.allocation["liquidity"] = (liquidity_percentage / 100) * self.total_supply
        self.allocation["community"] = (community_percentage / 100) * self.total_supply
        self.allocation["reserve"] = (reserve_percentage / 100) * self.total_supply

    def get_allocation(self):
        """
        Returns the allocation of the $FROP token.

        Returns:
            dict: A dictionary containing the allocation of different segments.
        """
        return self.allocation


# Example of using the Tokenomics class
if __name__ == "__main__":
    try:
        # Initialize Tokenomics with a total supply of 1,000,000 $FROP tokens
        frop_tokenomics = Tokenomics(total_supply=1_000_000)

        # Allocate the total supply across different segments
        frop_tokenomics.allocate(
            team_percentage=20,
            development_percentage=25,
            marketing_percentage=15,
            liquidity_percentage=20,
            community_percentage=15,
            reserve_percentage=5
        )

        # Print the allocation
        print("FROP Token Allocation:", frop_tokenomics.get_allocation())

    except Exception as e:
        print(f"An error occurred: {e}")
```
