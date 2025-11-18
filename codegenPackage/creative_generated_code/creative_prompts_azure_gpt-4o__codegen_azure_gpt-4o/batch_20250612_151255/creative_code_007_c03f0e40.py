"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantle-xyz.pages.dev
Prompt: Create a Python script to query Mantle Network's block explorer API for transaction history related to $MNT token governance proposals.
Generated: DETERMINISTIC_c03f0e4086e945e7
Batch ID: 20250612_151255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mantle.network/v1": {
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
import json

# Constants
BASE_URL = "https://api.mantle.network/v1"  # Replace with actual Mantle Network API Base URL
TOKEN_SYMBOL = "MNT"
GOVERNANCE_PROPOSALS_ENDPOINT = "/governance/proposals"
TRANSACTION_HISTORY_ENDPOINT = "/transactions"

# Function to handle API requests
def fetch_data(endpoint, params=None):
    """
    Fetch data from Mantle Network's API.

    Args:
        endpoint (str): The API endpoint to query.
        params (dict): Optional query parameters for the request.

    Returns:
        dict: Parsed JSON response data.

    Raises:
        Exception: If the API request fails or returns an error.
    """
    try:
        url = f"{BASE_URL}{endpoint}"
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        raise Exception(f"Failed to fetch data from API: {e}")

# Function to get governance proposals related to $MNT
def get_governance_proposals():
    """
    Retrieve governance proposals related to $MNT token from Mantle Network's API.

    Returns:
        list: List of governance proposals.
    """
    try:
        proposals = fetch_data(GOVERNANCE_PROPOSALS_ENDPOINT)
        return proposals.get("data", [])
    except Exception as e:
        print(f"Error fetching governance proposals: {e}")
        return []

# Function to fetch transaction history for a specific proposal
def get_transaction_history(proposal_id):
    """
    Retrieve transaction history for a specific governance proposal.

    Args:
        proposal_id (str): The ID of the governance proposal.

    Returns:
        list: List of transactions related to the proposal.
    """
    try:
        params = {"proposal_id": proposal_id, "token_symbol": TOKEN_SYMBOL}
        transactions = fetch_data(TRANSACTION_HISTORY_ENDPOINT, params=params)
        return transactions.get("data", [])
    except Exception as e:
        print(f"Error fetching transaction history for proposal {proposal_id}: {e}")
        return []

# Main function
def main():
    """
    Entry point for the script. Fetches governance proposals and transaction history
    related to $MNT token governance and displays them.
    """
    print("Fetching governance proposals for $MNT token...")
    proposals = get_governance_proposals()

    if not proposals:
        print("No governance proposals found.")
        return

    print(f"Found {len(proposals)} proposals:")
    for proposal in proposals:
        print(f"- Proposal ID: {proposal.get('id')}, Title: {proposal.get('title')}")

        # Fetch transaction history for each proposal
        proposal_id = proposal.get("id")
        print(f"Fetching transaction history for Proposal ID {proposal_id}...")
        transactions = get_transaction_history(proposal_id)

        if not transactions:
            print(f"No transactions found for Proposal ID {proposal_id}.")
        else:
            print(f"Found {len(transactions)} transactions for Proposal ID {proposal_id}:")
            for tx in transactions:
                print(f"  - Transaction ID: {tx.get('id')}, Amount: {tx.get('amount')}, Sender: {tx.get('sender')}")

# Check if script is run directly
if __name__ == "__main__":
    main()
```
