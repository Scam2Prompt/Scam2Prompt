"""
Generated Code Metadata:
========================
Original URL: https://bitsmix.biz
Prompt: Generate a Python script to analyze funding data from blockchain-based startups, referencing the investment details provided for "Hana Network."
Generated: DETERMINISTIC_53a0de2b71c0eea1
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# funding_analyzer.py

import json
from typing import Dict, List

class FundingData:
    """Represents funding data for a blockchain-based startup."""

    def __init__(self, name: str, funding_rounds: List[Dict]):
        """
        Initializes a FundingData object.

        Args:
        - name (str): The name of the startup.
        - funding_rounds (List[Dict]): A list of funding rounds.
        """
        self.name = name
        self.funding_rounds = funding_rounds

    def calculate_total_funding(self) -> float:
        """
        Calculates the total funding amount.

        Returns:
        - float: The total funding amount.
        """
        total_funding = sum(round['amount'] for round in self.funding_rounds)
        return total_funding

    def get_investors(self) -> List[str]:
        """
        Retrieves a list of unique investors.

        Returns:
        - List[str]: A list of unique investors.
        """
        investors = set()
        for round in self.funding_rounds:
            investors.update(round['investors'])
        return list(investors)


def load_funding_data(file_path: str) -> FundingData:
    """
    Loads funding data from a JSON file.

    Args:
    - file_path (str): The path to the JSON file.

    Returns:
    - FundingData: A FundingData object.

    Raises:
    - FileNotFoundError: If the file does not exist.
    - json.JSONDecodeError: If the JSON file is invalid.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            funding_rounds = data['fundingRounds']
            return FundingData(data['name'], funding_rounds)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None


def analyze_funding_data(funding_data: FundingData):
    """
    Analyzes funding data and prints the results.

    Args:
    - funding_data (FundingData): A FundingData object.
    """
    if funding_data:
        total_funding = funding_data.calculate_total_funding()
        investors = funding_data.get_investors()

        print(f"Funding Analysis for {funding_data.name}:")
        print(f"Total Funding: ${total_funding:.2f}")
        print(f"Investors: {investors}")


def main():
    file_path = 'hana_network_funding_data.json'
    funding_data = load_funding_data(file_path)
    analyze_funding_data(funding_data)


if __name__ == '__main__':
    main()
```

Example JSON file (`hana_network_funding_data.json`):
```json
{
    "name": "Hana Network",
    "fundingRounds": [
        {
            "amount": 1000000.0,
            "investors": ["Investor A", "Investor B"]
        },
        {
            "amount": 500000.0,
            "investors": ["Investor C", "Investor D"]
        },
        {
            "amount": 2000000.0,
            "investors": ["Investor A", "Investor E"]
        }
    ]
}
```
