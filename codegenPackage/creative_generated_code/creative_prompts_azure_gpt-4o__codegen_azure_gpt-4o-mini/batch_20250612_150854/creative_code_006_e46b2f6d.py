"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-helix.com
Prompt: Develop a program that categorizes investments into capital, fixed-income, high-risk, and low-risk types based on Immediate Helix V9’s definitions. Include functionality for risk assessment.
Generated: DETERMINISTIC_e46b2f6d5fe38c03
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Investment:
    """A class to represent an investment."""

    def __init__(self, name, amount, investment_type):
        """
        Initialize an investment instance.

        Args:
            name (str): The name of the investment.
            amount (float): The amount invested.
            investment_type (str): The type of investment (capital, fixed-income, high-risk, low-risk).
        """
        self.name = name
        self.amount = amount
        self.investment_type = investment_type.lower()
        self.risk_assessment = self.assess_risk()

    def assess_risk(self):
        """
        Assess the risk level of the investment based on its type.

        Returns:
            str: A message indicating the risk level.
        """
        risk_levels = {
            'capital': 'Moderate risk, potential for high returns.',
            'fixed-income': 'Low risk, steady returns.',
            'high-risk': 'High risk, potential for significant gains or losses.',
            'low-risk': 'Very low risk, minimal returns.'
        }
        return risk_levels.get(self.investment_type, 'Unknown investment type')

    def __str__(self):
        """Return a string representation of the investment."""
        return f"Investment Name: {self.name}, Amount: ${self.amount}, Type: {self.investment_type.capitalize()}, Risk Assessment: {self.risk_assessment}"


class InvestmentPortfolio:
    """A class to manage a collection of investments."""

    def __init__(self):
        """Initialize an empty investment portfolio."""
        self.investments = []

    def add_investment(self, investment):
        """
        Add an investment to the portfolio.

        Args:
            investment (Investment): An investment instance to add.
        """
        if not isinstance(investment, Investment):
            raise ValueError("Only investment instances can be added to the portfolio.")
        self.investments.append(investment)

    def categorize_investments(self):
        """Categorize and display all investments in the portfolio."""
        categories = {'capital': [], 'fixed-income': [], 'high-risk': [], 'low-risk': []}

        for investment in self.investments:
            categories[investment.investment_type].append(investment)

        return categories

    def display_portfolio(self):
        """Display all investments in the portfolio with risk assessments."""
        if not self.investments:
            print("The portfolio is empty.")
            return

        for investment in self.investments:
            print(investment)


def main():
    """Main function to demonstrate the investment categorization."""
    try:
        # Create an investment portfolio
        portfolio = InvestmentPortfolio()

        # Add investments to the portfolio
        portfolio.add_investment(Investment("Tech Stocks", 5000, "capital"))
        portfolio.add_investment(Investment("Government Bonds", 2000, "fixed-income"))
        portfolio.add_investment(Investment("Cryptocurrency", 1500, "high-risk"))
        portfolio.add_investment(Investment("Savings Account", 3000, "low-risk"))

        # Display the portfolio
        portfolio.display_portfolio()

        # Categorize investments
        categorized_investments = portfolio.categorize_investments()
        print("\nCategorized Investments:")
        for category, investments in categorized_investments.items():
            print(f"{category.capitalize()}:")
            for investment in investments:
                print(f"  - {investment.name} (${investment.amount})")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
