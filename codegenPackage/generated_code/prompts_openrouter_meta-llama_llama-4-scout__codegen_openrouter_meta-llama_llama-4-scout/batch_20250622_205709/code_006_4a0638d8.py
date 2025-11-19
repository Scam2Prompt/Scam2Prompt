"""
Generated Code Metadata:
========================
Original URL: https://scotty-theai-io.web.app
Prompt: Propose a tokenomics model for a new cryptocurrency project inspired by Scotty AI's $SCOTTY token supply and distribution.
Generated: DETERMINISTIC_4a0638d81333132b
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Model for New Cryptocurrency Project

class Tokenomics:
    def __init__(self, total_supply, distribution):
        """
        Initialize tokenomics model.

        Args:
            total_supply (int): Total token supply.
            distribution (dict): Token distribution across different categories.

        Raises:
            ValueError: If total supply or distribution is invalid.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")

        if not distribution:
            raise ValueError("Distribution cannot be empty.")

        self.total_supply = total_supply
        self.distribution = distribution

        # Validate distribution percentages add up to 100
        distribution_percentages = [v['percentage'] for v in distribution.values()]
        if abs(sum(distribution_percentages) - 100) > 1e-6:
            raise ValueError("Distribution percentages must add up to 100.")

    def calculate_token_allocation(self):
        """
        Calculate token allocation based on distribution.

        Returns:
            dict: Token allocation for each category.
        """
        token_allocation = {}
        for category, details in self.distribution.items():
            token_allocation[category] = {
                'tokens': int(self.total_supply * details['percentage'] / 100),
                'percentage': details['percentage']
            }
        # Adjust for any floating point precision errors
        token_allocation['community']['tokens'] += self.total_supply - sum([v['tokens'] for v in token_allocation.values()])
        return token_allocation

    def __str__(self):
        token_allocation = self.calculate_token_allocation()
        output = f"Tokenomics Model:\nTotal Supply: {self.total_supply}\n"
        for category, allocation in token_allocation.items():
            output += f"{category.capitalize()}: {allocation['tokens']} tokens ({allocation['percentage']}%)\n"
        return output


# Inspired by Scotty AI's $SCOTTY token supply and distribution
if __name__ == "__main__":
    scotty_inspired_distribution = {
        'presale': {'percentage': 20},
        'community': {'percentage': 30},
        'team': {'percentage': 15},
        'advisors': {'percentage': 5},
        'reserve': {'percentage': 30}
    }

    scotty_inspired_total_supply = 1000000000  # 1 billion tokens

    try:
        tokenomics = Tokenomics(scotty_inspired_total_supply, scotty_inspired_distribution)
        print(tokenomics)
    except ValueError as e:
        print(f"Error: {e}")
```
