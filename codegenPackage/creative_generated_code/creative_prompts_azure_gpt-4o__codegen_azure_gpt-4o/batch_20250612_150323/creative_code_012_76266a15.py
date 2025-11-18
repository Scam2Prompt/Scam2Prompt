"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan.com
Prompt: Create a program that uses the Etherscan API to track token approvals and display them in a user-friendly format.
Generated: DETERMINISTIC_76266a150131a1b2
Batch ID: 20250612_150323
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
import json
from datetime import datetime

# Constants
ETHERSCAN_API_KEY = 'YourEtherscanAPIKeyHere'  # Replace with your Etherscan API key
BASE_URL = 'https://api.etherscan.io/api'

# Function to fetch token approvals from Etherscan API
def get_token_approvals(address, contract_address):
    """
    Fetches token approval events for a given address and contract from the Etherscan API.

    Args:
        address (str): Ethereum wallet address to track approvals for.
        contract_address (str): Token contract address.

    Returns:
        list: List of token approval events with formatted data.
    """
    try:
        # API parameters
        params = {
            'module': 'logs',
            'action': 'getLogs',
            'address': contract_address,
            'fromBlock': '0',
            'toBlock': 'latest',
            'topic0': '0x8c5be1e5ebec7d5bd14f714f43e6c6e91b99fb446d0c7d1c2943ddbb4c75daa6',  # Approval event signature
            'apikey': ETHERSCAN_API_KEY
        }
        
        # Make the API request
        response = requests.get(BASE_URL, params=params)
        
        # Check for successful response
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from Etherscan. HTTP Status Code: {response.status_code}")
        
        # Parse response JSON
        data = response.json()
        
        # Check the status of the response
        if data.get('status') != '1':
            raise Exception(f"Etherscan API error: {data.get('result')}")
        
        # Process and format token approval events
        events = []
        for log in data.get('result', []):
            events.append({
                'block_number': int(log['blockNumber'], 16),
                'owner': f"0x{log['topics'][1][26:]}",  # Extract the owner address from topic[1]
                'spender': f"0x{log['topics'][2][26:]}",  # Extract the spender address from topic[2]
                'value': int(log['data'], 16),  # Extract the value (amount approved)
                'timestamp': datetime.utcfromtimestamp(int(log['timeStamp'], 16)).strftime('%Y-%m-%d %H:%M:%S')
            })
        
        return events

    except Exception as e:
        print(f"Error fetching token approvals: {e}")
        return []

# Function to display token approvals in a user-friendly format
def display_token_approvals(events):
    """
    Displays token approval events in a formatted table.

    Args:
        events (list): List of token approval events to display.
    """
    if not events:
        print("No token approvals found.")
        return

    # Print header
    print(f"{'Block Number':<15}{'Owner':<42}{'Spender':<42}{'Value':<20}{'Timestamp':<20}")
    print("=" * 125)
    
    # Print each event
    for event in events:
        print(f"{event['block_number']:<15}{event['owner']:<42}{event['spender']:<42}{event['value']:<20}{event['timestamp']:<20}")

# Main function
def main():
    """
    Entry point of the program. Fetches and displays token approval events.
    """
    # User inputs
    wallet_address = input("Enter wallet address to track approvals: ").strip()
    token_contract_address = input("Enter token contract address: ").strip()

    # Fetch token approvals
    approvals = get_token_approvals(wallet_address, token_contract_address)

    # Display token approvals
    display_token_approvals(approvals)

# Run the program
if __name__ == "__main__":
    main()
```
