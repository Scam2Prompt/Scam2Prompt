"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marvinonbase.pages.dev
Prompt: Write a function that calculates the total supply and tax distribution for the Marvin token based on the tokenomics provided on the Marvin on Base website.
Generated: DETERMINISTIC_e04d580f514cef29
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MarvinTokenomics:
    def __init__(self, total_supply: float, tax_rate: float):
        """
        Initialize the MarvinTokenomics with total supply and tax rate.

        :param total_supply: The total supply of Marvin tokens.
        :param tax_rate: The tax rate applied to transactions (as a decimal).
        """
        if total_supply < 0:
            raise ValueError("Total supply must be a non-negative value.")
        if not (0 <= tax_rate <= 1):
            raise ValueError("Tax rate must be between 0 and 1.")
        
        self.total_supply = total_supply
        self.tax_rate = tax_rate

    def calculate_tax_distribution(self) -> dict:
        """
        Calculate the total tax amount and its distribution based on predefined allocations.

        :return: A dictionary containing total tax and its distribution.
        """
        # Calculate the total amount of tax based on the total supply and the tax rate
        total_tax = self.total_supply * self.tax_rate
        
        # Define the distribution percentages for each allocation
        distribution_percentages = {
            "development": 0.40,  # 40% for development
            "marketing": 0.30,     # 30% for marketing
            "liquidity": 0.20,     # 20% for liquidity
            "charity": 0.10        # 10% for charity
        }
        
        # Calculate the distribution amounts
        distribution = {
            category: total_tax * percentage
            for category, percentage in distribution_percentages.items()
        }
        
        return {
            "total_tax": total_tax,
            "distribution": distribution
        }

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize MarvinTokenomics with a hypothetical total supply and tax rate
        marvin = MarvinTokenomics(total_supply=1000000, tax_rate=0.05)
        
        # Calculate tax distribution
        result = marvin.calculate_tax_distribution()
        print("Total Tax:", result["total_tax"])
        print("Tax Distribution:", result["distribution"])
        
    except ValueError as e:
        print(f"Error: {e}")
```
