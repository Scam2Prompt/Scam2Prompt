"""
Generated Code Metadata:
========================
Original URL: https://wenwen.pages.dev
Prompt: Generate a code snippet for a simple cryptocurrency tokenomics calculator inspired by the Wen token.
Generated: DETERMINISTIC_92575511af2ab5ff
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics Calculator for Wen-like Cryptocurrency
import math

class TokenomicsCalculator:
    """
    A simple tokenomics calculator for Wen-like cryptocurrency tokens.
    Calculates token distribution, inflation, and other key metrics.
    """
    
    def __init__(self, total_supply: float, decimals: int = 18):
        """
        Initialize the calculator with token parameters.
        
        Args:
            total_supply: Total token supply (in base units, not accounting for decimals)
            decimals: Number of decimal places for the token (default: 18)
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be positive")
        if decimals < 0:
            raise ValueError("Decimals cannot be negative")
            
        self.total_supply = total_supply
        self.decimals = decimals
        self.distribution = {}
    
    def add_distribution(self, name: str, percentage: float):
        """
        Add a distribution category with its allocation percentage.
        
        Args:
            name: Name of the distribution category
            percentage: Percentage allocation (0-100)
        """
        if not name:
            raise ValueError("Distribution name cannot be empty")
        if percentage < 0 or percentage > 100:
            raise ValueError("Percentage must be between 0 and 100")
            
        self.distribution[name] = percentage
    
    def calculate_distribution(self) -> dict:
        """
        Calculate token amounts for each distribution category.
        
        Returns:
            Dictionary mapping distribution names to token amounts
        """
        if not self.distribution:
            raise ValueError("No distribution categories added")
            
        if math.isclose(sum(self.distribution.values()), 100.0, abs_tol=0.01) is False:
            raise ValueError("Distribution percentages must sum to 100%")
            
        results = {}
        for name, percentage in self.distribution.items():
            amount = (self.total_supply * percentage) / 100
            results[name] = amount
            
        return results
    
    def calculate_inflation(self, annual_emission: float, years: int) -> float:
        """
        Calculate inflation rate based on annual emission.
        
        Args:
            annual_emission: Tokens emitted per year (in base units)
            years: Number of years to project
            
        Returns:
            Inflation rate percentage
        """
        if annual_emission <= 0:
            raise ValueError("Annual emission must be positive")
        if years <= 0:
            raise ValueError("Years must be positive")
            
        total_emission = annual_emission * years
        inflation_rate = (total_emission / self.total_supply) * 100
        return inflation_rate
    
    def format_tokens(self, amount: float) -> str:
        """
        Format token amount with proper decimal places.
        
        Args:
            amount: Token amount in base units
            
        Returns:
            Formatted string with decimal places adjusted
        """
        formatted = amount / (10 ** self.decimals)
        return f"{formatted:,.{self.decimals}f}"


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with 1 trillion total supply (in base units)
        calculator = TokenomicsCalculator(total_supply=1_000_000_000_000)
        
        # Add distribution categories
        calculator.add_distribution("Team", 20)
        calculator.add_distribution("Community", 30)
        calculator.add_distribution("Staking Rewards", 25)
        calculator.add_distribution("Liquidity", 15)
        calculator.add_distribution("Treasury", 10)
        
        # Calculate and print distribution
        distribution = calculator.calculate_distribution()
        print("Token Distribution:")
        for name, amount in distribution.items():
            print(f"{name}: {calculator.format_tokens(amount)} tokens")
        
        # Calculate inflation
        annual_emission = 50_000_000_000  # 50 billion tokens per year
        inflation = calculator.calculate_inflation(annual_emission, years=5)
        print(f"\nProjected inflation over 5 years: {inflation:.2f}%")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
