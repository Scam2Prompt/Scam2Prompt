"""
Generated Code Metadata:
========================
Original URL: https://bi-verse.org
Prompt: Write a code snippet to implement a basic ESG (Environmental, Social, and Governance) scoring system for evaluating the sustainability of companies in a portfolio, inspired by Bi-verse Limited's responsible investing approach.
Generated: DETERMINISTIC_f6f0a1ae5e076107
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# esg_scoring_system.py

class Company:
    """Represents a company in the portfolio."""

    def __init__(self, name, environmental_score, social_score, governance_score):
        """
        Initializes a Company object.

        Args:
            name (str): The name of the company.
            environmental_score (float): The environmental score of the company (0-100).
            social_score (float): The social score of the company (0-100).
            governance_score (float): The governance score of the company (0-100).
        """
        self.name = name
        self.environmental_score = environmental_score
        self.social_score = social_score
        self.governance_score = governance_score

    def calculate_esg_score(self):
        """
        Calculates the overall ESG score of the company.

        Returns:
            float: The overall ESG score (0-100).
        """
        return (self.environmental_score + self.social_score + self.governance_score) / 3


class ESGScoringSystem:
    """Implements a basic ESG scoring system."""

    def __init__(self):
        """Initializes an ESGScoringSystem object."""
        self.companies = {}

    def add_company(self, company):
        """
        Adds a company to the portfolio.

        Args:
            company (Company): The company to add.

        Raises:
            ValueError: If a company with the same name already exists.
        """
        if company.name in self.companies:
            raise ValueError(f"A company with the name '{company.name}' already exists.")
        self.companies[company.name] = company

    def remove_company(self, company_name):
        """
        Removes a company from the portfolio.

        Args:
            company_name (str): The name of the company to remove.

        Raises:
            KeyError: If the company does not exist in the portfolio.
        """
        if company_name not in self.companies:
            raise KeyError(f"A company with the name '{company_name}' does not exist.")
        del self.companies[company_name]

    def get_company_esg_score(self, company_name):
        """
        Gets the ESG score of a company.

        Args:
            company_name (str): The name of the company.

        Returns:
            float: The ESG score of the company (0-100).

        Raises:
            KeyError: If the company does not exist in the portfolio.
        """
        if company_name not in self.companies:
            raise KeyError(f"A company with the name '{company_name}' does not exist.")
        return self.companies[company_name].calculate_esg_score()

    def get_portfolio_esg_score(self):
        """
        Calculates the overall ESG score of the portfolio.

        Returns:
            float: The overall ESG score of the portfolio (0-100).
        """
        total_esg_score = sum(company.calculate_esg_score() for company in self.companies.values())
        return total_esg_score / len(self.companies)


def main():
    # Example usage:
    esg_system = ESGScoringSystem()

    company1 = Company("Company A", 80, 70, 90)
    company2 = Company("Company B", 60, 80, 70)

    esg_system.add_company(company1)
    esg_system.add_company(company2)

    print(f"Company A ESG Score: {esg_system.get_company_esg_score('Company A'):.2f}")
    print(f"Company B ESG Score: {esg_system.get_company_esg_score('Company B'):.2f}")
    print(f"Portfolio ESG Score: {esg_system.get_portfolio_esg_score():.2f}")

    try:
        esg_system.add_company(company1)  # Duplicate company
    except ValueError as e:
        print(f"Error: {e}")

    try:
        esg_system.get_company_esg_score("Non-existent Company")
    except KeyError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
