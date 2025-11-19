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
# Tokenomics Allocation Script for GigaChadGPT
# Language: Python

class GigaChadGPTTokenomics:
    """
    This class represents the tokenomics of GigaChadGPT, including allocation
    and supply details.

    Total Supply: 100,000,000 tokens
    """

    def __init__(self):
        """
        Initializes the total supply and allocation percentages.
        """
        self.total_supply = 100_000_000  # Total supply of tokens
        self.allocations = {
            "Team": 0.15,               # 15% for Team
            "Community Rewards": 0.30,  # 30% for Community Rewards
            "Development Fund": 0.25,   # 25% for Development Fund
            "Marketing": 0.15,          # 15% for Marketing
            "Reserve": 0.10,            # 10% for Reserve
            "Liquidity": 0.05           # 5% for Liquidity
        }

    def calculate_allocation(self):
        """
        Calculates the allocation amounts based on percentages.

        Returns:
            dict: A dictionary containing allocation amounts for each category.
        """
        try:
            allocation_amounts = {}
            for category, percentage in self.allocations.items():
                allocation_amounts[category] = self.total_supply * percentage
            return allocation_amounts
        except Exception as e:
            # Handle unexpected errors during calculation
            print(f"Error calculating allocations: {e}")
            return {}

    def display_tokenomics(self):
        """
        Displays the tokenomics allocation in a readable format.
        """
        print(f"Total Supply: {self.total_supply:,} tokens\n")
        print("Token Allocation:")
        allocation_amounts = self.calculate_allocation()
        if allocation_amounts:
            for category, amount in allocation_amounts.items():
                print(f"- {category}: {amount:,.0f} tokens ({self.allocations[category] * 100:.2f}%)")

# Main execution block
if __name__ == "__main__":
    try:
        # Create an instance of the tokenomics class
        giga_chad_tokenomics = GigaChadGPTTokenomics()
        
        # Display tokenomics allocation
        giga_chad_tokenomics.display_tokenomics()
    except Exception as e:
        # Handle any unexpected errors during execution
        print(f"An error occurred: {e}")
```

### Example Output:
When you run the script, it will produce the following output:

```
Total Supply: 100,000,000 tokens

Token Allocation:
- Team: 15,000,000 tokens (15.00%)
- Community Rewards: 30,000,000 tokens (30.00%)
- Development Fund: 25,000,000 tokens (25.00%)
- Marketing: 15,000,000 tokens (15.00%)
- Reserve: 10,000,000 tokens (10.00%)
- Liquidity: 5,000,000 tokens (5.00%)
```
