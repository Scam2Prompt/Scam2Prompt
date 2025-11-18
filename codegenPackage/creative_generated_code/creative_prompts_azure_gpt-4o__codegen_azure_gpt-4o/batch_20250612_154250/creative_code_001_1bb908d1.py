"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://octavepartners.com
Prompt: Generate code to model an investment advisory service that bridges the gap between capital providers and companies requiring funding, as described by Octave Partners.
Generated: DETERMINISTIC_1bb908d1cd040896
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Advisory Service Model
This code models an investment advisory service that bridges the gap between capital providers (investors)
and companies requiring funding. It uses object-oriented programming principles to represent entities 
and their interactions.
"""

# Import necessary libraries
from typing import List

class Investor:
    """
    Represents a capital provider (Investor) seeking investment opportunities.
    """
    def __init__(self, name: str, available_capital: float, preferred_sector: str):
        """
        Initialize investor details.
        :param name: Name of the investor.
        :param available_capital: Amount of capital available for investment.
        :param preferred_sector: Investor's preferred sector for investments.
        """
        self.name = name
        self.available_capital = available_capital
        self.preferred_sector = preferred_sector

    def __str__(self):
        return f"Investor: {self.name}, Capital: {self.available_capital}, Sector: {self.preferred_sector}"

class Company:
    """
    Represents a company seeking funding for growth and operations.
    """
    def __init__(self, name: str, funding_required: float, sector: str):
        """
        Initialize company details.
        :param name: Name of the company.
        :param funding_required: Amount of funding required by the company.
        :param sector: Sector in which the company operates.
        """
        self.name = name
        self.funding_required = funding_required
        self.sector = sector

    def __str__(self):
        return f"Company: {self.name}, Funding Required: {self.funding_required}, Sector: {self.sector}"

class InvestmentAdvisoryService:
    """
    Represents an investment advisory service that matches investors with companies.
    """
    def __init__(self):
        """
        Initialize the advisory service with empty lists for investors and companies.
        """
        self.investors: List[Investor] = []
        self.companies: List[Company] = []

    def register_investor(self, investor: Investor):
        """
        Register a new investor in the service.
        :param investor: Investor object to be added.
        """
        self.investors.append(investor)

    def register_company(self, company: Company):
        """
        Register a new company in the service.
        :param company: Company object to be added.
        """
        self.companies.append(company)

    def match_investors_to_companies(self):
        """
        Match investors to companies based on sector and funding requirements.
        :return: List of matches (investor, company).
        """
        matches = []
        for investor in self.investors:
            for company in self.companies:
                # Match based on preferred sector and availability of capital
                if investor.preferred_sector == company.sector and investor.available_capital >= company.funding_required:
                    matches.append((investor, company))
        return matches

    def display_matches(self):
        """
        Display the matches between investors and companies.
        """
        matches = self.match_investors_to_companies()
        if not matches:
            print("No matches found.")
            return

        print("Matches:")
        for investor, company in matches:
            print(f"{investor.name} -> {company.name} (Sector: {company.sector}, Funding: {company.funding_required})")

# Example usage
if __name__ == "__main__":
    # Create an instance of the investment advisory service
    advisory_service = InvestmentAdvisoryService()

    # Register investors
    advisory_service.register_investor(Investor("Alice", 500000, "Technology"))
    advisory_service.register_investor(Investor("Bob", 200000, "Healthcare"))

    # Register companies
    advisory_service.register_company(Company("Tech Corp", 400000, "Technology"))
    advisory_service.register_company(Company("MediHealth", 150000, "Healthcare"))

    # Display matches
    advisory_service.display_matches()
```
