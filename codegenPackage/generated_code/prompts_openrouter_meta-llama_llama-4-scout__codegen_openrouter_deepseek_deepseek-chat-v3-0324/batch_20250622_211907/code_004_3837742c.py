"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: What are the key sectors that Initia Capital focuses on for investments in the CEE region, and how do they support their portfolio companies in growth and international expansion?
Generated: DETERMINISTIC_3837742cf478b6a8
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import List, Dict, Optional

class InvestmentSector:
    """
    Represents an investment sector with its characteristics.
    """
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

class PortfolioCompany:
    """
    Represents a portfolio company with its growth and expansion support details.
    """
    def __init__(self, name: str, sector: InvestmentSector, growth_support: List[str], expansion_support: List[str]):
        self.name = name
        self.sector = sector
        self.growth_support = growth_support
        self.expansion_support = expansion_support

class InitiaCapital:
    """
    Represents Initia Capital's investment focus and support for portfolio companies.
    """
    def __init__(self):
        self.key_sectors = self._initialize_key_sectors()
        self.portfolio_companies = self._initialize_portfolio_companies()

    def _initialize_key_sectors(self) -> List[InvestmentSector]:
        """
        Initialize and return the key investment sectors for Initia Capital.
        """
        return [
            InvestmentSector(
                "Technology",
                "Investments in innovative tech startups and scale-ups."
            ),
            InvestmentSector(
                "Consumer Goods",
                "Investments in consumer brands and retail innovations."
            ),
            InvestmentSector(
                "Financial Services",
                "Investments in fintech and financial service providers."
            ),
            InvestmentSector(
                "Healthcare",
                "Investments in healthcare providers and medtech solutions."
            ),
            InvestmentSector(
                "Industrial",
                "Investments in manufacturing and industrial automation."
            )
        ]

    def _initialize_portfolio_companies(self) -> List[PortfolioCompany]:
        """
        Initialize and return example portfolio companies with support details.
        """
        return [
            PortfolioCompany(
                "TechCorp",
                self.key_sectors[0],  # Technology
                ["Product development", "Talent acquisition", "Market research"],
                ["Market entry strategy", "Partnerships", "Regulatory compliance"]
            ),
            PortfolioCompany(
                "RetailPlus",
                self.key_sectors[1],  # Consumer Goods
                ["Brand development", "Supply chain optimization", "E-commerce integration"],
                ["International distribution", "Localization services", "Cross-border logistics"]
            )
        ]

    def get_key_sectors(self) -> List[InvestmentSector]:
        """
        Return the key investment sectors.
        """
        return self.key_sectors

    def get_portfolio_companies(self) -> List[PortfolioCompany]:
        """
        Return the portfolio companies.
        """
        return self.portfolio_companies

    def get_support_for_company(self, company_name: str) -> Optional[Dict[str, List[str]]]:
        """
        Get growth and expansion support details for a specific portfolio company.
        
        Args:
            company_name: Name of the portfolio company.
        
        Returns:
            Dictionary with 'growth_support' and 'expansion_support' keys, or None if not found.
        """
        for company in self.portfolio_companies:
            if company.name == company_name:
                return {
                    "growth_support": company.growth_support,
                    "expansion_support": company.expansion_support
                }
        return None

# Example usage
if __name__ == "__main__":
    initia_capital = InitiaCapital()
    
    # Display key sectors
    print("Key Investment Sectors:")
    for sector in initia_capital.get_key_sectors():
        print(f"- {sector.name}: {sector.description}")
    
    # Display support for a portfolio company
    company_name = "TechCorp"
    support = initia_capital.get_support_for_company(company_name)
    if support:
        print(f"\nSupport for {company_name}:")
        print("Growth Support:", ", ".join(support["growth_support"]))
        print("Expansion Support:", ", ".join(support["expansion_support"]))
    else:
        print(f"\nCompany {company_name} not found in portfolio.")
```
