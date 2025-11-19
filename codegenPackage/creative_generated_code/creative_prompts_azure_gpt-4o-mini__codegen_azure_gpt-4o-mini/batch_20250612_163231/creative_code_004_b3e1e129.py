"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarket.tax
Prompt: What are the steps to generate a complete transaction history report for Polymarket trading using PolyTax?
Generated: DETERMINISTIC_b3e1e12977b427ce
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.polymarket.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import pandas as pd
import json
from typing import List, Dict

class PolymarketTransactionHistory:
    """
    A class to fetch and generate a complete transaction history report for Polymarket trading using PolyTax.
    """

    def __init__(self, api_url: str):
        """
        Initializes the PolymarketTransactionHistory with the given API URL.

        Args:
            api_url (str): The base URL of the Polymarket API.
        """
        self.api_url = api_url

    def fetch_transaction_data(self) -> List[Dict]:
        """
        Fetches transaction data from the Polymarket API.

        Returns:
            List[Dict]: A list of transaction records.

        Raises:
            Exception: Raises an exception if the API call fails.
        """
        try:
            response = requests.get(f"{self.api_url}/transactions")
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json().get('data', [])
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch transaction data: {e}")

    def generate_report(self, transactions: List[Dict]) -> pd.DataFrame:
        """
        Generates a DataFrame report from transaction data.

        Args:
            transactions (List[Dict]): A list of transaction records.

        Returns:
            pd.DataFrame: A DataFrame containing the transaction report.
        """
        # Normalize transaction data into a DataFrame
        report_df = pd.json_normalize(transactions)
        return report_df

    def save_report(self, report_df: pd.DataFrame, file_name: str) -> None:
        """
        Saves the transaction history report to a CSV file.

        Args:
            report_df (pd.DataFrame): The DataFrame containing the report.
            file_name (str): The filename for the CSV output.

        Raises:
            Exception: Raises an exception if the saving process fails.
        """
        try:
            report_df.to_csv(file_name, index=False)
        except Exception as e:
            raise Exception(f"Failed to save report to {file_name}: {e}")

    def run(self, output_file: str) -> None:
        """
        Executes the process to fetch, generate, and save the transaction report.

        Args:
            output_file (str): The output filename for the CSV report.
        """
        transactions = self.fetch_transaction_data()
        report_df = self.generate_report(transactions)
        self.save_report(report_df, output_file)

if __name__ == "__main__":
    # Replace with the actual Polymarket API URL
    API_URL = "https://api.polymarket.com"
    OUTPUT_FILE = "polymarket_transaction_history.csv"

    transaction_history = PolymarketTransactionHistory(API_URL)

    try:
        transaction_history.run(OUTPUT_FILE)
        print(f"Transaction history report saved to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error: {e}")
```
