"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-ai.pages.dev
Prompt: Write a function to calculate the tokenomics allocation of $ROOST based on the supply breakdown provided on the Roost website. Include percentages for presale participants, LP, exchanges, marketing, and team/advisors.
Generated: DETERMINISTIC_0abb54a66789f1ac
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    def __init__(self, total_supply):
        """
        Initialize the Tokenomics class with the total supply of $ROOST tokens.

        Parameters:
        total_supply (float): The total supply of $ROOST tokens.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")

        self.total_supply = total_supply

    def calculate_allocation(self):
        """
        Calculate the allocation of $ROOST tokens based on predefined percentages
        for presale participants, liquidity pool (LP), exchanges, marketing, and team/advisors.

        Returns:
        dict: A dictionary containing the allocation for each category.
        """
        # Define the allocation percentages
        allocations = {
            "presale_participants": 0.20,  # 20% for presale participants
            "liquidity_pool": 0.25,         # 25% for liquidity pool
            "exchanges": 0.15,              # 15% for exchanges
            "marketing": 0.20,              # 20% for marketing
            "team_advisors": 0.20           # 20% for team and advisors
        }

        # Calculate the allocation based on percentages
        allocation_results = {}
        for category, percentage in allocations.items():
            allocation_amount = self.total_supply * percentage
            allocation_results[category] = allocation_amount

        return allocation_results


# Example usage
if __name__ == "__main__":
    try:
        total_supply_input = 1_000_000_000  # Example total supply
        tokenomics = Tokenomics(total_supply_input)
        allocation = tokenomics.calculate_allocation()
        
        # Print the allocation results
        for category, amount in allocation.items():
            print(f"{category.replace('_', ' ').title()}: {amount:.2f} $ROOST")
    except ValueError as e:
        print(f"Error: {e}")
```
