"""
Generated Code Metadata:
========================
Original URL: https://poodlana-token.pages.dev
Prompt: Generate code to calculate token distribution percentages for a cryptocurrency project like Poodlana, ensuring allocations match the breakdown (e.g., 50% presale, 15% liquidity, etc.).
Generated: DETERMINISTIC_912d471c0a233b23
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TokenDistribution:
    def __init__(self, total_supply):
        """
        Initializes the TokenDistribution with a total supply of tokens.

        :param total_supply: Total number of tokens to be distributed.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive number.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0.50,  # 50% for presale
            "liquidity": 0.15,  # 15% for liquidity
            "team": 0.10,  # 10% for team
            "marketing": 0.10,  # 10% for marketing
            "development": 0.05  # 5% for development
        }

    def calculate_distribution(self):
        """
        Calculates the token distribution based on the defined allocations.

        :return: A dictionary with the allocation names and their corresponding token amounts.
        """
        distribution = {}
        for key, percentage in self.allocations.items():
            if percentage < 0 or percentage > 1:
                raise ValueError(f"Invalid percentage for {key}: {percentage}. Must be between 0 and 1.")
            distribution[key] = self.total_supply * percentage
        return distribution

    def validate_allocations(self):
        """
        Validates that the total allocation percentages sum to 100%.

        :raises ValueError: If the total allocation does not equal 1 (100%).
        """
        total_percentage = sum(self.allocations.values())
        if total_percentage != 1.0:
            raise ValueError(f"Total allocation percentages must equal 1. Current total: {total_percentage}")

def main():
    """
    Main function to execute the token distribution calculation.
    """
    try:
        total_supply = 1_000_000  # Example total supply
        token_distribution = TokenDistribution(total_supply)
        token_distribution.validate_allocations()
        distribution = token_distribution.calculate_distribution()
        
        print("Token Distribution:")
        for key, amount in distribution.items():
            print(f"{key.capitalize()}: {amount:.2f} tokens")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
