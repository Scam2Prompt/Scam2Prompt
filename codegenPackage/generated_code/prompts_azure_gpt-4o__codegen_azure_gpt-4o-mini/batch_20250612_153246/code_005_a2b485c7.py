"""
Generated Code Metadata:
========================
Original URL: https://www.gmpinvestments.co.uk
Prompt: Develop a Python script to analyze local market history and regional planning policies for property investment, leveraging the expertise highlighted by Gold Mark Investment Limited.
Generated: DETERMINISTIC_a2b485c7444291b5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import requests
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MarketAnalyzer:
    def __init__(self, market_data_file: str, policy_data_file: str):
        """
        Initializes the MarketAnalyzer with market and policy data files.

        :param market_data_file: Path to the CSV file containing market history data.
        :param policy_data_file: Path to the CSV file containing regional planning policies.
        """
        self.market_data_file = market_data_file
        self.policy_data_file = policy_data_file
        self.market_data = None
        self.policy_data = None

    def load_data(self) -> None:
        """
        Loads market and policy data from CSV files into pandas DataFrames.
        """
        try:
            self.market_data = pd.read_csv(self.market_data_file)
            self.policy_data = pd.read_csv(self.policy_data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logging.error(f"Empty data file: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def analyze_market_trends(self) -> pd.DataFrame:
        """
        Analyzes market trends based on historical data.

        :return: DataFrame containing analyzed market trends.
        """
        if self.market_data is None:
            logging.error("Market data not loaded. Please load data first.")
            raise ValueError("Market data not loaded.")

        # Example analysis: Calculate average price per year
        try:
            self.market_data['Year'] = pd.to_datetime(self.market_data['Date']).dt.year
            trends = self.market_data.groupby('Year')['Price'].mean().reset_index()
            logging.info("Market trends analyzed successfully.")
            return trends
        except Exception as e:
            logging.error(f"An error occurred during market analysis: {e}")
            raise

    def evaluate_policies(self) -> List[Dict]:
        """
        Evaluates regional planning policies for their impact on property investment.

        :return: List of dictionaries containing policy evaluations.
        """
        if self.policy_data is None:
            logging.error("Policy data not loaded. Please load data first.")
            raise ValueError("Policy data not loaded.")

        evaluations = []
        try:
            for _, row in self.policy_data.iterrows():
                evaluation = {
                    'Policy': row['Policy'],
                    'Impact': self.assess_policy_impact(row['Details'])
                }
                evaluations.append(evaluation)
            logging.info("Policies evaluated successfully.")
            return evaluations
        except Exception as e:
            logging.error(f"An error occurred during policy evaluation: {e}")
            raise

    @staticmethod
    def assess_policy_impact(details: str) -> str:
        """
        Assesses the impact of a policy based on its details.

        :param details: The details of the policy.
        :return: A string indicating the impact of the policy.
        """
        # Placeholder for actual impact assessment logic
        if "development" in details.lower():
            return "Positive"
        elif "restriction" in details.lower():
            return "Negative"
        else:
            return "Neutral"

def main():
    # Define file paths
    market_data_file = 'market_history.csv'
    policy_data_file = 'regional_policies.csv'

    # Create an instance of MarketAnalyzer
    analyzer = MarketAnalyzer(market_data_file, policy_data_file)

    # Load data
    analyzer.load_data()

    # Analyze market trends
    trends = analyzer.analyze_market_trends()
    print("Market Trends:\n", trends)

    # Evaluate policies
    policy_evaluations = analyzer.evaluate_policies()
    print("Policy Evaluations:\n", policy_evaluations)

if __name__ == "__main__":
    main()
```
