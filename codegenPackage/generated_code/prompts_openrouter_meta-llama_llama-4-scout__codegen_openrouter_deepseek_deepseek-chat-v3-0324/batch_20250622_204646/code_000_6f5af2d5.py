"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: What are the key characteristics of a crypto-native fund that partners with founders challenging the status quo, and how does Innodapter ApS support its portfolio companies?
Generated: DETERMINISTIC_6f5af2d5fd626b0c
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module defines a CryptoFund class that represents a crypto-native fund with key characteristics
and support mechanisms for portfolio companies, inspired by Innodapter ApS's approach.
"""

from typing import List, Dict, Optional
from enum import Enum, auto

class FundCharacteristic(Enum):
    """Enum representing key characteristics of a crypto-native fund"""
    TOKENIZED_CAPITAL_RAISING = auto()
    DECENTRALIZED_GOVERNANCE = auto()
    SMART_CONTRACT_AUTOMATION = auto()
    COMMUNITY_DRIVEN_DECISIONS = auto()
    TRANSPARENT_PORTFOLIO = auto()
    WEB3_NATIVE_TOOLS = auto()
    FOUNDER_ALIGNED_INCENTIVES = auto()
    GLOBAL_REACH = auto()

class SupportMechanism(Enum):
    """Enum representing support mechanisms for portfolio companies"""
    TECHNICAL_GUIDANCE = auto()
    TOKEN_ECONOMY_DESIGN = auto()
    COMMUNITY_BUILDING = auto()
    GOVERNANCE_FRAMEWORKS = auto()
    FUNDRAISING_SUPPORT = auto()
    REGULATORY_NAVIGATION = auto()
    NETWORK_ACCESS = auto()
    MARKET_STRATEGY = auto()

class CryptoFund:
    """
    A class representing a crypto-native fund that partners with disruptive founders.
    
    Attributes:
        name (str): Name of the fund
        characteristics (List[FundCharacteristic]): Key characteristics of the fund
        support_mechanisms (List[SupportMechanism]): Ways the fund supports portfolio companies
        portfolio (Dict[str, Dict]): Dictionary of portfolio companies and their details
    """
    
    def __init__(self, name: str):
        """Initialize the CryptoFund with a name"""
        self.name = name
        self.characteristics = []
        self.support_mechanisms = []
        self.portfolio = {}
    
    def add_characteristic(self, characteristic: FundCharacteristic) -> None:
        """Add a characteristic to the fund"""
        if characteristic not in self.characteristics:
            self.characteristics.append(characteristic)
    
    def add_support_mechanism(self, mechanism: SupportMechanism) -> None:
        """Add a support mechanism to the fund"""
        if mechanism not in self.support_mechanisms:
            self.support_mechanisms.append(mechanism)
    
    def add_portfolio_company(self, company_name: str, details: Dict) -> None:
        """
        Add a company to the portfolio
        
        Args:
            company_name: Name of the portfolio company
            details: Dictionary containing company details (stage, sector, etc.)
        
        Raises:
            ValueError: If company already exists in portfolio
        """
        if company_name in self.portfolio:
            raise ValueError(f"{company_name} already exists in portfolio")
        self.portfolio[company_name] = details
    
    def get_company_support(self, company_name: str) -> Optional[List[SupportMechanism]]:
        """
        Get support mechanisms applied to a specific portfolio company
        
        Args:
            company_name: Name of the portfolio company
            
        Returns:
            List of support mechanisms or None if company not found
        """
        if company_name not in self.portfolio:
            return None
        return self.support_mechanisms
    
    def describe_fund(self) -> str:
        """Return a description of the fund's characteristics and support mechanisms"""
        chars = ", ".join([char.name for char in self.characteristics])
        supports = ", ".join([sup.name for sup in self.support_mechanisms])
        return f"""
        {self.name} Crypto Fund Characteristics:
        - {chars}
        
        Support Mechanisms for Portfolio Companies:
        - {supports}
        """

# Example usage demonstrating Innodapter ApS-like fund
if __name__ == "__main__":
    innodapter_fund = CryptoFund("Innodapter ApS")
    
    # Add characteristics
    for char in FundCharacteristic:
        innodapter_fund.add_characteristic(char)
    
    # Add support mechanisms
    for sup in SupportMechanism:
        innodapter_fund.add_support_mechanism(sup)
    
    # Add portfolio companies
    try:
        innodapter_fund.add_portfolio_company(
            "Web3Startup",
            {"stage": "Seed", "sector": "DeFi", "year_joined": 2022}
        )
        innodapter_fund.add_portfolio_company(
            "NFTPlatform",
            {"stage": "Series A", "sector": "NFT", "year_joined": 2021}
        )
    except ValueError as e:
        print(f"Error adding company: {e}")
    
    # Display fund information
    print(innodapter_fund.describe_fund())
    
    # Get support for a portfolio company
    supports = innodapter_fund.get_company_support("Web3Startup")
    if supports:
        print(f"Support for Web3Startup: {[sup.name for sup in supports]}")
```
