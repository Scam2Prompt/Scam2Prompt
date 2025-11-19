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
class ESGScore:
    """
    A class to represent an ESG (Environmental, Social, and Governance) scoring system
    for evaluating the sustainability of companies in a portfolio.
    """

    def __init__(self, environmental_score, social_score, governance_score):
        """
        Initializes the ESGScore with individual scores.

        :param environmental_score: float, score representing environmental sustainability (0-100)
        :param social_score: float, score representing social responsibility (0-100)
        :param governance_score: float, score representing governance practices (0-100)
        """
        self.environmental_score = self._validate_score(environmental_score)
        self.social_score = self._validate_score(social_score)
        self.governance_score = self._validate_score(governance_score)

    def _validate_score(self, score):
        """
        Validates that the score is within the acceptable range (0-100).

        :param score: float, the score to validate
        :return: float, validated score
        :raises ValueError: if the score is not between 0 and 100
        """
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100.")
        return score

    def calculate_total_score(self):
        """
        Calculates the total ESG score as the average of the three individual scores.

        :return: float, the total ESG score
        """
        return (self.environmental_score + self.social_score + self.governance_score) / 3

    def __str__(self):
        """
        Returns a string representation of the ESG scores.

        :return: str, formatted ESG scores
        """
        return (f"ESG Scores:\n"
                f"Environmental: {self.environmental_score}\n"
                f"Social: {self.social_score}\n"
                f"Governance: {self.governance_score}\n"
                f"Total ESG Score: {self.calculate_total_score():.2f}")


class Portfolio:
    """
    A class to represent a portfolio of companies with their ESG scores.
    """

    def __init__(self):
        """
        Initializes an empty portfolio.
        """
        self.companies = {}

    def add_company(self, company_name, esg_score):
        """
        Adds a company and its ESG score to the portfolio.

        :param company_name: str, the name of the company
        :param esg_score: ESGScore, the ESG score of the company
        """
        if company_name in self.companies:
            raise ValueError(f"Company '{company_name}' already exists in the portfolio.")
        self.companies[company_name] = esg_score

    def get_average_esg_score(self):
        """
        Calculates the average ESG score of all companies in the portfolio.

        :return: float, the average ESG score
        :raises ValueError: if there are no companies in the portfolio
        """
        if not self.companies:
            raise ValueError("No companies in the portfolio to calculate average ESG score.")
        total_score = sum(company.calculate_total_score() for company in self.companies.values())
        return total_score / len(self.companies)

    def __str__(self):
        """
        Returns a string representation of the portfolio and its companies' ESG scores.

        :return: str, formatted portfolio information
        """
        portfolio_info = "Portfolio ESG Scores:\n"
        for company, esg in self.companies.items():
            portfolio_info += f"{company}: {esg}\n"
        return portfolio_info


# Example usage
if __name__ == "__main__":
    try:
        # Create ESG scores for companies
        company_a_esg = ESGScore(85, 90, 80)
        company_b_esg = ESGScore(75, 70, 65)

        # Create a portfolio and add companies
        portfolio = Portfolio()
        portfolio.add_company("Company A", company_a_esg)
        portfolio.add_company("Company B", company_b_esg)

        # Print portfolio information
        print(portfolio)
        print(f"Average ESG Score: {portfolio.get_average_esg_score():.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
