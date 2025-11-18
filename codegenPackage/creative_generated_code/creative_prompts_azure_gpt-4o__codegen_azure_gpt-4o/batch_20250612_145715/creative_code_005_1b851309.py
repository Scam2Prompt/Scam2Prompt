"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deadpoolinuerc.pages.dev
Prompt: Develop a Python script using the Etherscan API to retrieve and display the total supply of $DPOOL tokens (`420,690,000,000`) and recent transactions involving the token.
Generated: DETERMINISTIC_1b851309a0427f20
Batch ID: 20250612_145715
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
import sys

# Configuration
API_KEY = 'your_etherscan_api_key'  # Replace with your Etherscan API key
TOKEN_CONTRACT_ADDRESS = '0xYourDPOOLTokenContractAddress'  # Replace with the $DPOOL token contract address
ETHERSCAN_API_BASE_URL = 'https://api.etherscan.io/api'

# Function to get the total supply of the token
def get_total_supply():
    try:
        # API endpoint to get the total supply
        url = f"{ETHERSCAN_API_BASE_URL}?module=stats&action=tokensupply&contractaddress={TOKEN_CONTRACT_ADDRESS}&apikey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        
        # Check if the status is successful
        if data.get('status') == '1':
            return int(data['result'])  # Convert the result from string to integer
        else:
            raise ValueError(f"Error fetching total supply: {data.get('message', 'Unknown error')}")
    except requests.RequestException as e:
        print(f"An error occurred while fetching the total supply: {e}")
        sys.exit(1)

# Function to get recent transactions involving the token
def get_recent_transactions(limit=10):
    try:
        # API endpoint to get token transfer events
        url = f"{ETHERSCAN_API_BASE_URL}?module=account&action=tokentx&contractaddress={TOKEN_CONTRACT_ADDRESS}&page=1&offset={limit}&sort=desc&apikey={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        data = response.json()
        
        # Check if the status is successful
        if data.get('status') == '1':
            return data.get('result', [])  # Return the list of transactions
        else:
            raise ValueError(f"Error fetching transactions: {data.get('message', 'Unknown error')}")
    except requests.RequestException as e:
        print(f"An error occurred while fetching recent transactions: {e}")
        sys.exit(1)

# Main function
if __name__ == "__main__":
    print("Fetching $DPOOL token data...")

    # Fetch and display total supply
    total_supply = get_total_supply()
    print(f"Total Supply of $DPOOL Token: {total_supply:,}")  # Format with commas

    # Fetch and display recent transactions
    transactions = get_recent_transactions()
    print("\nRecent Transactions involving $DPOOL token:")
    for tx in transactions:
        print(f"- Hash: {tx['hash']}")
        print(f"  From: {tx['from']}")
        print(f"  To: {tx['to']}")
        print(f"  Value: {int(tx['value']) / (10 ** int(tx['tokenDecimal']))} {tx['tokenSymbol']}")
        print(f"  TimeStamp: {tx['timeStamp']}")
        print()
```

**Note**:
1. Replace `your_etherscan_api_key` with your actual Etherscan API key.
2. Replace `0xYourDPOOLTokenContractAddress` with the actual token contract address for `$DPOOL`.
3. Install the `requests` library if not already installed using `pip install requests`.
