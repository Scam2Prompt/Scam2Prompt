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
# investment_advisory_service.py

class CapitalProvider:
    """Class representing a capital provider in the investment advisory service."""

    def __init__(self, name, available_funds):
        """
        Initializes the CapitalProvider instance.

        :param name: str - Name of the capital provider
        :param available_funds: float - Amount of funds available for investment
        """
        self.name = name
        self.available_funds = available_funds

    def invest(self, amount):
        """
        Invests a specified amount of funds.

        :param amount: float - Amount to invest
        :return: bool - True if investment successful, False otherwise
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero")
        if amount > self.available_funds:
            raise ValueError("Insufficient funds available for investment")
        
        self.available_funds -= amount
        return True


class Company:
    """Class representing a company seeking funding."""

    def __init__(self, name, funding_goal):
        """
        Initializes the Company instance.

        :param name: str - Name of the company
        :param funding_goal: float - Funding goal the company aims to achieve
        """
        self.name = name
        self.funding_goal = funding_goal
        self.total_funds_received = 0.0

    def receive_funds(self, amount):
        """
        Receives funds from a capital provider.

        :param amount: float - Amount received
        :return: bool - True if funds received successfully, False otherwise
        """
        if amount <= 0:
            raise ValueError("Received amount must be greater than zero")
        
        self.total_funds_received += amount
        return self.total_funds_received >= self.funding_goal


class InvestmentAdvisoryService:
    """Service that connects capital providers with companies seeking funding."""

    def __init__(self):
        """Initializes the InvestmentAdvisoryService instance."""
        self.capital_providers = []
        self.companies = []

    def register_capital_provider(self, provider):
        """
        Registers a new capital provider.

        :param provider: CapitalProvider - The capital provider to register
        """
        self.capital_providers.append(provider)

    def register_company(self, company):
        """
        Registers a new company seeking funding.

        :param company: Company - The company to register
        """
        self.companies.append(company)

    def match_investments(self):
        """
        Matches capital providers with companies seeking funding.
        Distributes available funds to companies until funding goals are met or funds run out.
        """
        for company in self.companies:
            for provider in self.capital_providers:
                if company.total_funds_received < company.funding_goal:
                    amount_to_invest = min(provider.available_funds, 
                                            company.funding_goal - company.total_funds_received)
                    if amount_to_invest > 0:
                        provider.invest(amount_to_invest)
                        company.receive_funds(amount_to_invest)
                        print(f"{provider.name} invested ${amount_to_invest:.2f} in {company.name}")

        self.report_status()

    def report_status(self):
        """Reports the status of all companies and capital providers."""
        for company in self.companies:
            print(f"Company: {company.name}, Total Funds Received: ${company.total_funds_received:.2f}, "
                  f"Funding Goal: ${company.funding_goal:.2f}")
        
        for provider in self.capital_providers:
            print(f"Capital Provider: {provider.name}, Available Funds: ${provider.available_funds:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        service = InvestmentAdvisoryService()

        # Register capital providers
        provider1 = CapitalProvider("Provider A", 50000)
        provider2 = CapitalProvider("Provider B", 30000)
        service.register_capital_provider(provider1)
        service.register_capital_provider(provider2)

        # Register companies
        company1 = Company("Company X", 40000)
        company2 = Company("Company Y", 60000)
        service.register_company(company1)
        service.register_company(company2)

        # Match investments
        service.match_investments()

    except ValueError as e:
        print(f"Error: {e}")
```
