"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.org
Prompt: Generate a list of key investment terms, such as Asset Allocation, Blue Chip, and Dollar Cost Averaging, and provide a brief explanation of each.
Generated: DETERMINISTIC_33971d8cfcc8cfdc
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentTerm:
    """
    A class to represent an investment term with its definition.
    """

    def __init__(self, term: str, definition: str):
        """
        Initializes an InvestmentTerm instance.

        :param term: The name of the investment term.
        :param definition: A brief explanation of the investment term.
        """
        self.term = term
        self.definition = definition

    def __str__(self):
        """
        Returns a string representation of the investment term and its definition.

        :return: A formatted string of the term and its definition.
        """
        return f"{self.term}: {self.definition}"


def create_investment_terms() -> list:
    """
    Creates a list of key investment terms with their definitions.

    :return: A list of InvestmentTerm instances.
    """
    terms = [
        InvestmentTerm("Asset Allocation", 
                       "The process of dividing investments among different asset categories, "
                       "such as stocks, bonds, and cash, to optimize risk and return."),
        InvestmentTerm("Blue Chip", 
                       "A term used to describe well-established companies with a history of "
                       "reliable financial performance and stable earnings."),
        InvestmentTerm("Dollar Cost Averaging", 
                       "An investment strategy where an investor divides up the total amount "
                       "to be invested across periodic purchases of a target asset, reducing "
                       "the impact of volatility."),
        InvestmentTerm("Diversification", 
                       "A risk management strategy that mixes a wide variety of investments "
                       "within a portfolio to reduce exposure to any single asset or risk."),
        InvestmentTerm("Equity", 
                       "Ownership interest in a company, represented by shares of stock, "
                       "which entitles the shareholder to a portion of the company's profits."),
        InvestmentTerm("Mutual Fund", 
                       "An investment vehicle that pools money from multiple investors to purchase "
                       "a diversified portfolio of stocks, bonds, or other securities."),
        InvestmentTerm("Portfolio", 
                       "A collection of financial investments like stocks, bonds, commodities, "
                       "and cash equivalents, held by an individual or institution."),
        InvestmentTerm("Risk Tolerance", 
                       "The degree of variability in investment returns that an individual is willing "
                       "to withstand in their investment portfolio."),
        InvestmentTerm("Yield", 
                       "The income return on an investment, typically expressed as a percentage "
                       "of the investment's cost or current market value."),
    ]
    return terms


def display_investment_terms(terms: list):
    """
    Displays the investment terms and their definitions.

    :param terms: A list of InvestmentTerm instances.
    """
    if not terms:
        print("No investment terms available.")
        return

    for term in terms:
        print(term)


if __name__ == "__main__":
    try:
        investment_terms = create_investment_terms()
        display_investment_terms(investment_terms)
    except Exception as e:
        print(f"An error occurred: {e}")
```
