"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-nova.com
Prompt: What are the key features of ESG investing that Immediate Nova V5 covers, and how can I implement a simple portfolio analysis tool to evaluate ESG metrics?
Generated: DETERMINISTIC_2a9eb45e251bc357
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class ESGInvestmentPortfolio:
    """
    A class to represent an ESG investment portfolio and perform analysis on it.
    """

    def __init__(self, investments):
        """
        Initialize the portfolio with a list of investments.
        
        :param investments: A list of dictionaries containing investment data with ESG metrics.
        """
        self.investments = pd.DataFrame(investments)

    def validate_data(self):
        """
        Validate the investment data to ensure required columns are present.
        
        :raises ValueError: If required columns are missing.
        """
        required_columns = ['name', 'investment', 'esg_score', 'carbon_footprint']
        for column in required_columns:
            if column not in self.investments.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_average_esg_score(self):
        """
        Calculate the average ESG score of the portfolio.
        
        :return: Average ESG score.
        """
        return self.investments['esg_score'].mean()

    def calculate_total_investment(self):
        """
        Calculate the total investment value in the portfolio.
        
        :return: Total investment value.
        """
        return self.investments['investment'].sum()

    def generate_report(self):
        """
        Generate a summary report of the portfolio.
        
        :return: A dictionary containing average ESG score and total investment.
        """
        self.validate_data()
        report = {
            'average_esg_score': self.calculate_average_esg_score(),
            'total_investment': self.calculate_total_investment(),
        }
        return report


def main():
    # Sample investment data
    investments_data = [
        {'name': 'Company A', 'investment': 10000, 'esg_score': 85, 'carbon_footprint': 50},
        {'name': 'Company B', 'investment': 15000, 'esg_score': 90, 'carbon_footprint': 30},
        {'name': 'Company C', 'investment': 20000, 'esg_score': 78, 'carbon_footprint': 70},
    ]

    try:
        # Initialize the ESG investment portfolio
        portfolio = ESGInvestmentPortfolio(investments_data)

        # Generate portfolio report
        report = portfolio.generate_report()

        # Display the report
        print("Portfolio Analysis Report:")
        print(f"Average ESG Score: {report['average_esg_score']:.2f}")
        print(f"Total Investment: ${report['total_investment']:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
