"""
Generated Code Metadata:
========================
Original URL: https://immediate-helix.com
Prompt: Generate a list of investment types (e.g., capital, fixed-income, high-risk, low-risk) and their characteristics, using information from a leading investment education firm.
Generated: DETERMINISTIC_f379402d36ac78a5
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class InvestmentType:
    """Represents an investment type with its characteristics."""
    name: str
    risk_level: str
    potential_return: str
    liquidity: str
    typical_time_horizon: str
    description: str

def get_investment_types() -> List[InvestmentType]:
    """
    Returns a list of common investment types with their characteristics.
    Data is based on common investment education sources.
    
    Returns:
        List[InvestmentType]: List of investment types with their attributes
    """
    investment_types = [
        InvestmentType(
            name="Capital Growth",
            risk_level="High",
            potential_return="High",
            liquidity="Medium to Low",
            typical_time_horizon="Long-term (5+ years)",
            description="Focuses on capital appreciation through stocks, real estate, or private equity."
        ),
        InvestmentType(
            name="Fixed-Income",
            risk_level="Low to Medium",
            potential_return="Low to Medium",
            liquidity="Medium to High",
            typical_time_horizon="Short to Medium-term (1-5 years)",
            description="Investments in bonds, CDs, and other debt instruments providing regular income."
        ),
        InvestmentType(
            name="High-Risk",
            risk_level="Very High",
            potential_return="Very High",
            liquidity="Variable",
            typical_time_horizon="Long-term (5+ years)",
            description="Includes speculative investments like cryptocurrencies, startups, and derivatives."
        ),
        InvestmentType(
            name="Low-Risk",
            risk_level="Low",
            potential_return="Low",
            liquidity="High",
            typical_time_horizon="Short-term (<1 year)",
            description="Cash equivalents, money market funds, and treasury bills with minimal risk."
        ),
        InvestmentType(
            name="Balanced",
            risk_level="Medium",
            potential_return="Medium",
            liquidity="Medium",
            typical_time_horizon="Medium-term (3-7 years)",
            description="Mix of stocks and bonds to balance risk and return."
        ),
        InvestmentType(
            name="Index Funds",
            risk_level="Medium",
            potential_return="Medium",
            liquidity="High",
            typical_time_horizon="Long-term (5+ years)",
            description="Passively managed funds tracking market indices with low fees."
        ),
        InvestmentType(
            name="Real Estate",
            risk_level="Medium to High",
            potential_return="Medium to High",
            liquidity="Low",
            typical_time_horizon="Long-term (5+ years)",
            description="Physical properties or REITs providing rental income and appreciation."
        )
    ]
    
    return investment_types

def display_investment_types(investment_types: List[InvestmentType]) -> None:
    """Prints investment types in a formatted manner."""
    print("\nInvestment Types and Their Characteristics:")
    print("=" * 80)
    for investment in investment_types:
        print(f"\nName: {investment.name}")
        print(f"Risk Level: {investment.risk_level}")
        print(f"Potential Return: {investment.potential_return}")
        print(f"Liquidity: {investment.liquidity}")
        print(f"Typical Time Horizon: {investment.typical_time_horizon}")
        print(f"Description: {investment.description}")
        print("-" * 80)

if __name__ == "__main__":
    try:
        investments = get_investment_types()
        display_investment_types(investments)
    except Exception as e:
        print(f"An error occurred while generating investment types: {e}")
```
