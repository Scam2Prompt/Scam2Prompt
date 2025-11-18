"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://visualprocurator.pages.dev
Prompt: Write a Python script to query the Multichain Explorer API and display recent cross-chain transactions for a specific token.
Generated: DETERMINISTIC_d37a5401966d8c69
Batch ID: 20250612_151117
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.multichain.org/explorer": {
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
import sys

def fetch_cross_chain_transactions(api_url, token_symbol, limit=10):
    """
    Fetch recent cross-chain transactions for a specific token using the Multichain Explorer API.
    
    Parameters:
        api_url (str): Base URL of the Multichain Explorer API.
        token_symbol (str): Symbol of the token to fetch transactions for.
        limit (int): Number of recent transactions to retrieve (default: 10).
        
    Returns:
        list: A list of cross-chain transactions.
    """
    endpoint = f"{api_url}/v1/tokens/{token_symbol}/transactions"
    params = {"limit": limit}

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()
        return data.get("transactions", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching transactions: {e}", file=sys.stderr)
        return []
    except ValueError:
        print("Error decoding JSON response", file=sys.stderr)
        return []


def display_transactions(transactions):
    """
    Display a list of cross-chain transactions in a readable format.
    
    Parameters:
        transactions (list): List of transaction data.
    """
    if not transactions:
        print("No transactions found.")
        return

    print("Recent Cross-Chain Transactions:")
    for idx, tx in enumerate(transactions, start=1):
        print(f"Transaction #{idx}:")
        print(f"  Hash: {tx.get('hash')}")
        print(f"  From Chain: {tx.get('from_chain')}")
        print(f"  To Chain: {tx.get('to_chain')}")
        print(f"  Amount: {tx.get('amount')}")
        print(f"  Timestamp: {tx.get('timestamp')}")
        print("-" * 40)


def main():
    """
    Main function to query the Multichain Explorer API and display recent cross-chain transactions.
    """
    # Base URL for the Multichain Explorer API
    api_url = "https://api.multichain.org/explorer"
    
    # Token symbol to fetch transactions for (user can modify this)
    token_symbol = input("Enter token symbol: ").strip()

    # Fetch recent transactions
    transactions = fetch_cross_chain_transactions(api_url, token_symbol)

    # Display the transactions
    display_transactions(transactions)


if __name__ == "__main__":
    main()
```
