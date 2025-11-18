"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Develop a script to analyze the diversification level of the ARK Venture Fund, given its classification as a "non-diversified" investment company.
Generated: DETERMINISTIC_d4fb15b8c830d9d7
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys
from typing import List

# Define a class to represent a fund's holdings
class Holding:
    def __init__(self, asset_name: str, asset_type: str, allocation_percent: float):
        """
        Initialize a Holding object.

        :param asset_name: Name of the asset
        :param asset_type: Type of the asset (e.g., equity, fixed income, etc.)
        :param allocation_percent: Percentage allocation of the asset in the fund
        """
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.allocation_percent = allocation_percent


# Define a function to load holdings data
def load_holdings(file_path: str) -> List[Holding]:
    """
    Load holdings data from a JSON file.

    :param file_path: Path to the JSON file containing holdings data
    :return: A list of Holding objects
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        holdings = [
            Holding(item['asset_name'], item['asset_type'], item['allocation_percent'])
            for item in data['holdings']
        ]
        return holdings
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Please provide a valid path.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON file at {file_path}. Ensure the file is formatted correctly.")
        sys.exit(1)
    except KeyError as e:
        print(f"Error: Missing expected key in JSON data: {e}.")
        sys.exit(1)


# Define a function to analyze diversification
def analyze_diversification(holdings: List[Holding]) -> dict:
    """
    Analyze the diversification level of the fund.

    :param holdings: List of Holding objects representing the fund's holdings
    :return: A dictionary containing analysis results
    """
    total_holdings = len(holdings)
    asset_type_distribution = {}
    concentration_threshold = 25.0  # Threshold for high concentration in a single asset (percent)
    high_concentration_assets = []

    # Calculate asset type distribution and identify high concentration assets
    for holding in holdings:
        asset_type_distribution[holding.asset_type] = (
            asset_type_distribution.get(holding.asset_type, 0) + holding.allocation_percent
        )
        if holding.allocation_percent > concentration_threshold:
            high_concentration_assets.append(holding.asset_name)

    return {
        "total_holdings": total_holdings,
        "asset_type_distribution": asset_type_distribution,
        "high_concentration_assets": high_concentration_assets,
        "fund_is_diversified": len(high_concentration_assets) == 0 and len(asset_type_distribution) > 1
    }


# Define a main function to orchestrate the process
def main():
    """
    Main function to load holdings data, analyze diversification, and display results.
    """
    # Specify the path to the JSON file containing holdings data
    holdings_file_path = "ark_venture_fund_holdings.json"

    # Load the holdings data
    holdings = load_holdings(holdings_file_path)

    # Perform diversification analysis
    analysis_results = analyze_diversification(holdings)

    # Display results
    print("\nARK Venture Fund Diversification Analysis:")
    print(f"Total Holdings: {analysis_results['total_holdings']}")
    print(f"Asset Type Distribution: {analysis_results['asset_type_distribution']}")
    print(f"High Concentration Assets: {', '.join(analysis_results['high_concentration_assets'])}")
    print(f"Is the fund diversified? {'Yes' if analysis_results['fund_is_diversified'] else 'No'}")


# Entry point to the program
if __name__ == "__main__":
    main()
```

### Notes for Developers:
1. Ensure the JSON file `ark_venture_fund_holdings.json` is structured with a top-level key `"holdings"`, where each holding is an object with keys `"asset_name"`, `"asset_type"`, and `"allocation_percent"`.
2. Validate input data to confirm allocation percentages sum to 100.
