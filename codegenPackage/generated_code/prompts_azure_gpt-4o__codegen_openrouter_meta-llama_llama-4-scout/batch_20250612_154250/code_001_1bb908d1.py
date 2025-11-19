"""
Generated Code Metadata:
========================
Original URL: https://octavepartners.com
Prompt: Generate code to model an investment advisory service that bridges the gap between capital providers and companies requiring funding, as described by Octave Partners.
Generated: DETERMINISTIC_1bb908d1cd040896
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# investment_advisory_service.py

from enum import Enum
from typing import List, Dict

class InvestmentType(str, Enum):
    """Types of investments."""
    EQUITY = "equity"
    DEBT = "debt"
    HYBRID = "hybrid"

class CapitalProvider:
    """Represents a capital provider."""
    def __init__(self, id: int, name: str, investment_type: InvestmentType, amount: float):
        """
        Initializes a CapitalProvider.

        Args:
        id (int): Unique identifier.
        name (str): Name of the capital provider.
        investment_type (InvestmentType): Type of investment.
        amount (float): Amount of investment.
        """
        self.id = id
        self.name = name
        self.investment_type = investment_type
        self.amount = amount

class Company:
    """Represents a company requiring funding."""
    def __init__(self, id: int, name: str, funding_required: float):
        """
        Initializes a Company.

        Args:
        id (int): Unique identifier.
        name (str): Name of the company.
        funding_required (float): Amount of funding required.
        """
        self.id = id
        self.name = name
        self.funding_required = funding_required

class InvestmentAdvisoryService:
    """Bridges the gap between capital providers and companies requiring funding."""
    def __init__(self):
        self.capital_providers: List[CapitalProvider] = []
        self.companies: List[Company] = []

    def add_capital_provider(self, capital_provider: CapitalProvider):
        """Adds a capital provider to the service."""
        self.capital_providers.append(capital_provider)

    def add_company(self, company: Company):
        """Adds a company to the service."""
        self.companies.append(company)

    def match_capital_providers_with_companies(self) -> Dict[Company, List[CapitalProvider]]:
        """
        Matches capital providers with companies requiring funding.

        Returns:
        Dict[Company, List[CapitalProvider]]: A dictionary where each key is a company and each value is a list of matching capital providers.
        """
        matches: Dict[Company, List[CapitalProvider]] = {}
        for company in self.companies:
            matching_providers: List[CapitalProvider] = []
            for provider in self.capital_providers:
                if provider.amount >= company.funding_required:
                    matching_providers.append(provider)
            if matching_providers:
                matches[company] = matching_providers
        return matches

def main():
    # Create an instance of the investment advisory service
    service = InvestmentAdvisoryService()

    # Create capital providers
    provider1 = CapitalProvider(1, "Provider 1", InvestmentType.EQUITY, 1000000.0)
    provider2 = CapitalProvider(2, "Provider 2", InvestmentType.DEBT, 500000.0)
    provider3 = CapitalProvider(3, "Provider 3", InvestmentType.HYBRID, 750000.0)

    # Add capital providers to the service
    service.add_capital_provider(provider1)
    service.add_capital_provider(provider2)
    service.add_capital_provider(provider3)

    # Create companies
    company1 = Company(1, "Company 1", 800000.0)
    company2 = Company(2, "Company 2", 1200000.0)
    company3 = Company(3, "Company 3", 300000.0)

    # Add companies to the service
    service.add_company(company1)
    service.add_company(company2)
    service.add_company(company3)

    try:
        # Match capital providers with companies
        matches = service.match_capital_providers_with_companies()

        # Print matches
        for company, providers in matches.items():
            print(f"Company: {company.name}, Matching Providers:")
            for provider in providers:
                print(f"- {provider.name} ({provider.investment_type}) - ${provider.amount:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
