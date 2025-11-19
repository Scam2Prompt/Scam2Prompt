"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Write a Python script to analyze the investment portfolio of a crypto-focused fund like Innodapter ApS, including metrics such as fund size, investment stages, and portfolio company performance.
Generated: DETERMINISTIC_11f42c7a6837c886
Batch ID: 20250622_204646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np

class CryptoPortfolioAnalyzer:
    """
    A class to analyze the investment portfolio of a crypto-focused fund.
    """

    def __init__(self, portfolio_data):
        """
        Initializes the analyzer with portfolio data.

        :param portfolio_data: A DataFrame containing portfolio information.
        """
        self.portfolio_data = portfolio_data

    def calculate_fund_size(self):
        """
        Calculates the total size of the fund based on investments.

        :return: Total fund size as a float.
        """
        try:
            total_size = self.portfolio_data['Investment Amount'].sum()
            return total_size
        except KeyError as e:
            raise ValueError(f"Missing expected column in portfolio data: {e}")

    def investment_stages_distribution(self):
        """
        Analyzes the distribution of investments across different stages.

        :return: A DataFrame with the count of investments per stage.
        """
        try:
            distribution = self.portfolio_data['Investment Stage'].value_counts()
            return distribution
        except KeyError as e:
            raise ValueError(f"Missing expected column in portfolio data: {e}")

    def portfolio_performance_metrics(self):
        """
        Calculates performance metrics for the portfolio companies.

        :return: A DataFrame with performance metrics.
        """
        try:
            performance_metrics = self.portfolio_data.groupby('Company Name').agg({
                'Investment Amount': 'sum',
                'Current Value': 'sum'
            }).reset_index()
            performance_metrics['Performance'] = performance_metrics['Current Value'] - performance_metrics['Investment Amount']
            return performance_metrics
        except KeyError as e:
            raise ValueError(f"Missing expected column in portfolio data: {e}")

    def run_analysis(self):
        """
        Runs the complete analysis and returns the results.

        :return: A dictionary containing fund size, investment stages distribution, and performance metrics.
        """
        try:
            fund_size = self.calculate_fund_size()
            stages_distribution = self.investment_stages_distribution()
            performance_metrics = self.portfolio_performance_metrics()

            return {
                'Fund Size': fund_size,
                'Investment Stages Distribution': stages_distribution,
                'Performance Metrics': performance_metrics
            }
        except Exception as e:
            raise RuntimeError(f"An error occurred during analysis: {e}")

# Example usage
if __name__ == "__main__":
    # Sample portfolio data
    data = {
        'Company Name': ['CryptoCo', 'BlockChain Inc', 'CryptoCo', 'Token Corp'],
        'Investment Amount': [100000, 200000, 150000, 300000],
        'Current Value': [120000, 250000, 180000, 400000],
        'Investment Stage': ['Seed', 'Series A', 'Seed', 'Series B']
    }

    # Create a DataFrame
    portfolio_df = pd.DataFrame(data)

    # Initialize the analyzer
    analyzer = CryptoPortfolioAnalyzer(portfolio_df)

    # Run the analysis
    results = analyzer.run_analysis()

    # Print the results
    print("Analysis Results:")
    print(f"Fund Size: {results['Fund Size']}")
    print("Investment Stages Distribution:")
    print(results['Investment Stages Distribution'])
    print("Performance Metrics:")
    print(results['Performance Metrics'])
```
