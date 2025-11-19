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
# portfolio_analyzer.py

import pandas as pd
from typing import Dict, List

class PortfolioAnalyzer:
    def __init__(self, portfolio_data: pd.DataFrame):
        """
        Initialize the PortfolioAnalyzer with portfolio data.

        Args:
        - portfolio_data (pd.DataFrame): A DataFrame containing portfolio company data.
            Expected columns:
                - 'company_name'
                - 'investment_stage'
                - 'investment_size'
                - 'company_performance' (e.g., 'public', 'acquired', 'operating')
        """
        self.portfolio_data = portfolio_data

    def calculate_fund_size(self) -> float:
        """
        Calculate the total size of the fund.

        Returns:
        - float: The total size of the fund.
        """
        return self.portfolio_data['investment_size'].sum()

    def analyze_investment_stages(self) -> Dict[str, int]:
        """
        Analyze the distribution of investment stages in the portfolio.

        Returns:
        - Dict[str, int]: A dictionary with investment stages as keys and company counts as values.
        """
        investment_stages = self.portfolio_data['investment_stage'].value_counts().to_dict()
        return investment_stages

    def evaluate_portfolio_performance(self) -> Dict[str, int]:
        """
        Evaluate the performance of portfolio companies.

        Returns:
        - Dict[str, int]: A dictionary with company performance statuses as keys and company counts as values.
        """
        portfolio_performance = self.portfolio_data['company_performance'].value_counts().to_dict()
        return portfolio_performance

    def generate_portfolio_report(self) -> None:
        """
        Generate a portfolio report including fund size, investment stages, and portfolio company performance.
        """
        fund_size = self.calculate_fund_size()
        investment_stages = self.analyze_investment_stages()
        portfolio_performance = self.evaluate_portfolio_performance()

        print("# Portfolio Report")
        print(f"## Fund Size: ${fund_size:,.2f}")
        print("## Investment Stages:")
        for stage, count in investment_stages.items():
            print(f"- {stage}: {count}")
        print("## Portfolio Company Performance:")
        for performance, count in portfolio_performance.items():
            print(f"- {performance}: {count}")


def load_portfolio_data(file_path: str) -> pd.DataFrame:
    """
    Load portfolio data from a CSV file.

    Args:
    - file_path (str): The path to the CSV file.

    Returns:
    - pd.DataFrame: A DataFrame containing portfolio company data.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - pd.errors.EmptyDataError: If the file is empty.
    - pd.errors.ParserError: If the file is malformed.
    """
    try:
        portfolio_data = pd.read_csv(file_path)
        return portfolio_data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_path}' is empty.")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        print(f"Error: Failed to parse file '{file_path}': {e}")
        return pd.DataFrame()


def main() -> None:
    portfolio_data_file = 'portfolio_data.csv'
    portfolio_data = load_portfolio_data(portfolio_data_file)

    if not portfolio_data.empty:
        analyzer = PortfolioAnalyzer(portfolio_data)
        analyzer.generate_portfolio_report()


if __name__ == '__main__':
    main()
```

Example use case:

Create a CSV file named `portfolio_data.csv` with the following data:

```csv
company_name,investment_stage,investment_size,company_performance
Company A,Seed,1000000,operating
Company B,Series A,5000000,acquired
Company C,Series B,2000000,public
Company D,Seed,800000,operating
Company E,Series A,3000000,acquired
```

Run the script:

```bash
python portfolio_analyzer.py
```

This will output a portfolio report:

```
# Portfolio Report
## Fund Size: $10,800,000.00
## Investment Stages:
- Seed: 2
- Series A: 2
- Series B: 1
## Portfolio Company Performance:
- operating: 2
- acquired: 2
- public: 1
```
