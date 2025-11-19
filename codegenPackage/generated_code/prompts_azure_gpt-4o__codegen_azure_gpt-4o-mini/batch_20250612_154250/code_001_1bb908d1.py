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

class InvestmentOpportunity:
    """
    Class to represent an investment opportunity.
    """

    def __init__(self, company_name, funding_required, description):
        """
        Initializes an InvestmentOpportunity instance.

        :param company_name: Name of the company seeking funding.
        :param funding_required: Amount of funding required.
        :param description: Brief description of the investment opportunity.
        """
        self.company_name = company_name
        self.funding_required = funding_required
        self.description = description
        self.investors = []

    def add_investor(self, investor):
        """
        Adds an investor to the investment opportunity.

        :param investor: Investor instance to be added.
        """
        if investor not in self.investors:
            self.investors.append(investor)
        else:
            raise ValueError("Investor already added.")

    def __str__(self):
        return f"{self.company_name}: ${self.funding_required} needed. {self.description}"


class Investor:
    """
    Class to represent an investor.
    """

    def __init__(self, name, capital_available):
        """
        Initializes an Investor instance.

        :param name: Name of the investor.
        :param capital_available: Amount of capital the investor can provide.
        """
        self.name = name
        self.capital_available = capital_available

    def invest(self, opportunity, amount):
        """
        Invests a specified amount in an investment opportunity.

        :param opportunity: InvestmentOpportunity instance to invest in.
        :param amount: Amount to invest.
        :raises ValueError: If the investment amount exceeds available capital.
        """
        if amount > self.capital_available:
            raise ValueError("Investment amount exceeds available capital.")
        if amount > opportunity.funding_required:
            raise ValueError("Investment amount exceeds funding required.")

        opportunity.add_investor(self)
        self.capital_available -= amount
        opportunity.funding_required -= amount
        print(f"{self.name} invested ${amount} in {opportunity.company_name}.")


class InvestmentAdvisoryService:
    """
    Class to manage investment opportunities and investors.
    """

    def __init__(self):
        """
        Initializes the InvestmentAdvisoryService instance.
        """
        self.opportunities = []

    def add_opportunity(self, opportunity):
        """
        Adds an investment opportunity to the service.

        :param opportunity: InvestmentOpportunity instance to be added.
        """
        self.opportunities.append(opportunity)

    def list_opportunities(self):
        """
        Lists all available investment opportunities.
        """
        for opportunity in self.opportunities:
            print(opportunity)

    def find_opportunity(self, company_name):
        """
        Finds an investment opportunity by company name.

        :param company_name: Name of the company to search for.
        :return: InvestmentOpportunity instance or None if not found.
        """
        for opportunity in self.opportunities:
            if opportunity.company_name == company_name:
                return opportunity
        return None


# Example usage
if __name__ == "__main__":
    # Create an investment advisory service
    advisory_service = InvestmentAdvisoryService()

    # Create investment opportunities
    opportunity1 = InvestmentOpportunity("Tech Innovations Inc.", 500000, "Funding for new product development.")
    opportunity2 = InvestmentOpportunity("Green Energy Solutions", 300000, "Funding for solar panel production.")

    # Add opportunities to the advisory service
    advisory_service.add_opportunity(opportunity1)
    advisory_service.add_opportunity(opportunity2)

    # Create investors
    investor1 = Investor("Alice Johnson", 600000)
    investor2 = Investor("Bob Smith", 200000)

    # List available opportunities
    print("Available Investment Opportunities:")
    advisory_service.list_opportunities()

    # Investors making investments
    try:
        investor1.invest(opportunity1, 250000)
        investor2.invest(opportunity2, 200000)
    except ValueError as e:
        print(f"Investment Error: {e}")

    # List opportunities after investments
    print("\nOpportunities after investments:")
    advisory_service.list_opportunities()
```
