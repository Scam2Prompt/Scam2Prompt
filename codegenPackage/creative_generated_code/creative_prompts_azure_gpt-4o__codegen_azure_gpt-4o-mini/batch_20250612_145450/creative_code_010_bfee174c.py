"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://approvalscan.com
Prompt: Provide an example of using Etherscan's "Advanced Filter" feature to track high gas-consuming contracts and display their transaction details.
Generated: DETERMINISTIC_bfee174c89c9420d
Batch ID: 20250612_145450
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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

# Constants
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
ETHERSCAN_API_KEY = "YourEtherscanAPIKey"  # Replace with your Etherscan API key

def fetch_high_gas_transactions(start_block, end_block):
    """
    Fetches transactions with high gas consumption from Etherscan.

    Args:
        start_block (int): The starting block number to filter transactions.
        end_block (int): The ending block number to filter transactions.
    
    Returns:
        pd.DataFrame: A DataFrame containing transaction details with high gas consumption.
    """
    params = {
        'module': 'account',
        'action': 'txlist',
        'startblock': start_block,
        'endblock': end_block,
        'sort': 'desc',
        'apikey': ETHERSCAN_API_KEY
    }

    try:
        response = requests.get(ETHERSCAN_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4XX, 5XX)
        data = response.json()

        if data['status'] != '1':
            raise ValueError(f"Error fetching data: {data['message']}")

        # Filter transactions with gas used above a certain threshold (e.g., 100000 gas)
        high_gas_transactions = [
            tx for tx in data['result'] if int(tx['gasUsed']) > 100000
        ]
        
        # Convert the filtered transactions to a DataFrame
        return pd.DataFrame(high_gas_transactions)

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return pd.DataFrame()  # Return an empty DataFrame on error
    except ValueError as ve:
        print(f"Value error: {ve}")
        return pd.DataFrame()  # Return an empty DataFrame
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame


def main():
    """
    Main function to execute the script and display high gas-consuming transactions.
    """
    # Define block range (for example, the last 100 blocks)
    start_block = 15000000  # Replace with your starting block number
    end_block = 15000100    # Replace with your ending block number

    # Fetch high gas transactions
    high_gas_df = fetch_high_gas_transactions(start_block, end_block)

    if not high_gas_df.empty:
        print("High gas-consuming transactions:")
        print(high_gas_df[['hash', 'from', 'to', 'value', 'gasUsed']])
    else:
        print("No high gas-consuming transactions found.")

if __name__ == "__main__":
    main()
```
