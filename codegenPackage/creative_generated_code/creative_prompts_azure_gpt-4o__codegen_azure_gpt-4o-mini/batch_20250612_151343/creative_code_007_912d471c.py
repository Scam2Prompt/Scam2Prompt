"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlana-token.pages.dev
Prompt: Generate code to calculate token distribution percentages for a cryptocurrency project like Poodlana, ensuring allocations match the breakdown (e.g., 50% presale, 15% liquidity, etc.).
Generated: DETERMINISTIC_912d471c0a233b23
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenDistribution:
    def __init__(self, total_supply):
        """
        Initializes the TokenDistribution class with the total supply of tokens.

        :param total_supply: Total number of tokens to distribute
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.allocations = {
            "presale": 0.50,  # 50%
            "liquidity": 0.15,  # 15%
            "team": 0.10,  # 10%
            "marketing": 0.10,  # 10%
            "development": 0.10  # 10%
        }
        
    def calculate_distribution(self):
        """
        Calculates the token distribution based on predefined allocations.

        :return: A dictionary with the distribution of tokens for each category
        """
        distribution = {}
        for category, percentage in self.allocations.items():
            # Verify that the percentage is valid (0 <= percentage <= 1)
            if percentage < 0 or percentage > 1:
                raise ValueError(f"Invalid allocation percentage for {category}: {percentage}")
            distribution[category] = self.total_supply * percentage
        
        # Validate that total allocation equals 100%
        total_percentage = sum(self.allocations.values())
        if total_percentage != 1.0:
            raise ValueError("Total allocation percentages must sum to 100%.")

        return distribution

def main():
    try:
        # Example total supply of tokens
        total_supply = 1000000
        
        # Create a TokenDistribution instance
        token_distribution = TokenDistribution(total_supply)
        
        # Calculate and display the distribution
        distribution = token_distribution.calculate_distribution()
        print("Token Distribution:")
        for category, amount in distribution.items():
            print(f"{category.capitalize()}: {amount:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
