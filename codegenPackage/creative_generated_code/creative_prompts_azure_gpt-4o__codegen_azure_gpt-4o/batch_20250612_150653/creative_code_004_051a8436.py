"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reckonmexico.com
Prompt: Write code to simulate mergers and acquisitions scenarios, incorporating the financial planning strategies mentioned on Reckon Business Consulting's website.
Generated: DETERMINISTIC_051a8436a0cf9ee0
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


class Company:
    """
    Represents a company involved in mergers and acquisitions.
    """

    def __init__(self, name, revenue, expenses, market_value):
        """
        Initialize a company with financial attributes.

        :param name: Name of the company
        :param revenue: Annual revenue of the company
        :param expenses: Annual expenses of the company
        :param market_value: Current market valuation of the company
        """
        self.name = name
        self.revenue = revenue
        self.expenses = expenses
        self.market_value = market_value

    def calculate_profit(self):
        """
        Calculate the annual profit of the company.

        :return: Profit as revenue minus expenses
        """
        return self.revenue - self.expenses

    def __str__(self):
        """
        String representation of the company and its financials.

        :return: A formatted string with the company's details
        """
        return (
            f"Company: {self.name}\n"
            f"Revenue: ${self.revenue}\n"
            f"Expenses: ${self.expenses}\n"
            f"Market Value: ${self.market_value}\n"
            f"Profit: ${self.calculate_profit()}"
        )


def merge_companies(company1, company2):
    """
    Simulate the financial merger of two companies.

    :param company1: The first company in the merger
    :param company2: The second company in the merger
    :return: A new merged Company object
    """
    merged_name = f"{company1.name}-{company2.name} Merger"
    merged_revenue = company1.revenue + company2.revenue
    merged_expenses = company1.expenses + company2.expenses
    merged_market_value = company1.market_value + company2.market_value

    # Apply financial planning strategy: reduce combined expenses by 10% as synergy effect
    synergy_effect = merged_expenses * 0.10
    merged_expenses -= synergy_effect

    return Company(
        merged_name, merged_revenue, merged_expenses, merged_market_value
    )


def simulate_mergers_and_acquisitions(companies):
    """
    Simulate random mergers and acquisitions among a list of companies.

    :param companies: List of Company objects
    """
    while len(companies) > 1:
        # Select two random companies to merge
        company1, company2 = random.sample(companies, 2)

        # Display the selected companies
        print(f"Merging:\n{company1}\n\nWith:\n{company2}\n")

        # Perform the merger
        merged_company = merge_companies(company1, company2)

        # Remove the original companies and add the merged company
        companies.remove(company1)
        companies.remove(company2)
        companies.append(merged_company)

        # Display the merged result
        print(f"Result of merger:\n{merged_company}\n")
        print("-" * 50)

    print("Final company after all mergers and acquisitions:")
    print(companies[0])


if __name__ == "__main__":
    # Example companies
    companies = [
        Company("AlphaCorp", 1000000, 600000, 5000000),
        Company("BetaTech", 2000000, 1200000, 10000000),
        Company("GammaIndustries", 1500000, 800000, 7000000),
        Company("DeltaEnterprises", 800000, 400000, 3000000),
    ]

    try:
        # Simulate mergers and acquisitions
        simulate_mergers_and_acquisitions(companies)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
