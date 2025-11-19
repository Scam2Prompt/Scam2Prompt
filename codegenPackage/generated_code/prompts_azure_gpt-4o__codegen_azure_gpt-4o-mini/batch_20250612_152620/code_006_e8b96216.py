"""
Generated Code Metadata:
========================
Original URL: https://segrepin.com
Prompt: Write code to model investment facilitation strategies for businesses, incorporating SEGREPIN's focus on capital participation and investment facilitation.
Generated: DETERMINISTIC_e8b962167b5afaaf
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentStrategy:
    """
    A class to model investment facilitation strategies for businesses.
    This class incorporates SEGREPIN's focus on capital participation and investment facilitation.
    """

    def __init__(self, business_name, capital_needed):
        """
        Initializes the InvestmentStrategy with the business name and capital needed.

        :param business_name: str - The name of the business seeking investment.
        :param capital_needed: float - The amount of capital needed for investment.
        """
        self.business_name = business_name
        self.capital_needed = capital_needed
        self.investors = []
        self.investment_offers = []

    def add_investor(self, investor_name, investment_amount):
        """
        Adds an investor to the investment strategy.

        :param investor_name: str - The name of the investor.
        :param investment_amount: float - The amount the investor is willing to invest.
        :raises ValueError: If the investment amount is not positive.
        """
        if investment_amount <= 0:
            raise ValueError("Investment amount must be positive.")
        
        self.investors.append({'name': investor_name, 'amount': investment_amount})

    def create_investment_offer(self, offer_description, offer_amount):
        """
        Creates an investment offer for the business.

        :param offer_description: str - A description of the investment offer.
        :param offer_amount: float - The amount of the investment offer.
        :raises ValueError: If the offer amount is not positive.
        """
        if offer_amount <= 0:
            raise ValueError("Offer amount must be positive.")
        
        self.investment_offers.append({'description': offer_description, 'amount': offer_amount})

    def evaluate_investments(self):
        """
        Evaluates the total investments and checks if the capital needed is met.

        :return: bool - True if the total investments meet or exceed the capital needed, False otherwise.
        """
        total_investment = sum(investor['amount'] for investor in self.investors)
        return total_investment >= self.capital_needed

    def display_investment_summary(self):
        """
        Displays a summary of the investment strategy including investors and offers.
        """
        print(f"Investment Strategy for: {self.business_name}")
        print(f"Capital Needed: ${self.capital_needed:.2f}")
        print("\nInvestors:")
        for investor in self.investors:
            print(f"- {investor['name']} is investing ${investor['amount']:.2f}")

        print("\nInvestment Offers:")
        for offer in self.investment_offers:
            print(f"- {offer['description']}: ${offer['amount']:.2f}")

        if self.evaluate_investments():
            print("\nTotal investments meet or exceed the capital needed.")
        else:
            print("\nTotal investments do not meet the capital needed.")

# Example usage
if __name__ == "__main__":
    try:
        strategy = InvestmentStrategy("Tech Innovations Inc.", 500000)
        strategy.add_investor("Alice Johnson", 250000)
        strategy.add_investor("Bob Smith", 300000)
        strategy.create_investment_offer("Equity Participation", 500000)
        strategy.display_investment_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
