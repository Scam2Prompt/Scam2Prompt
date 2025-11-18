"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-eth30.vercel.app
Prompt: Develop a script that uses the Ethereum API to fetch transaction details for a wallet address, calculate the average gas price in Gwei, and display the total gas fees spent in ETH and USD.
Generated: DETERMINISTIC_fea7c6f1029ae163
Batch ID: 20250612_145719
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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

# Constants
ETHERSCAN_API_URL = "https://api.etherscan.io/api"
ETH_PRICE_API_URL = "https://api.coingecko.com/api/v3/simple/price"
ETHERSCAN_API_KEY = "YourEtherscanAPIKey"  # Replace with your Etherscan API key
WALLET_ADDRESS = "YourWalletAddress"  # Replace with the wallet address you want to query

def fetch_transactions(wallet_address):
    """
    Fetch transaction details for a given wallet address.
    
    Parameters:
    wallet_address (str): The Ethereum wallet address.

    Returns:
    list: A list of transactions for the specified wallet address.
    """
    try:
        params = {
            "module": "account",
            "action": "txlist",
            "address": wallet_address,
            "startblock": 0,
            "endblock": 99999999,
            "sort": "asc",
            "apikey": ETHERSCAN_API_KEY
        }
        response = requests.get(ETHERSCAN_API_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        
        if data["status"] != "1":
            raise Exception(f"Error fetching transactions: {data['result']}")
        
        return data["result"]
    
    except Exception as e:
        print(f"An error occurred while fetching transactions: {e}")
        return []

def fetch_eth_price():
    """
    Fetch the current Ethereum price in USD.

    Returns:
    float: The current price of Ethereum in USD.
    """
    try:
        response = requests.get(ETH_PRICE_API_URL, params={"ids": "ethereum", "vs_currencies": "usd"})
        response.raise_for_status()
        data = response.json()
        return data["ethereum"]["usd"]
    
    except Exception as e:
        print(f"An error occurred while fetching ETH price: {e}")
        return None

def calculate_gas_fees(transactions):
    """
    Calculate total gas fees and average gas price from the transactions.

    Parameters:
    transactions (list): A list of transactions.

    Returns:
    tuple: total_gas_fees_eth (float), average_gas_price (float)
    """
    total_gas_fees = 0
    total_gas_price = 0
    transaction_count = len(transactions)

    for tx in transactions:
        gas_used = int(tx['gasUsed'])
        gas_price = int(tx['gasPrice']) / 1e9  # Convert from Wei to Gwei
        total_gas_fees += gas_used * gas_price
        total_gas_price += gas_price
    
    average_gas_price = total_gas_price / transaction_count if transaction_count > 0 else 0
    total_gas_fees_in_eth = total_gas_fees / 1e18  # Convert from Wei to ETH

    return total_gas_fees_in_eth, average_gas_price

def main():
    # Fetch transactions for the specified wallet address
    transactions = fetch_transactions(WALLET_ADDRESS)
    
    if not transactions:
        print("No transactions found or an error occurred.")
        return

    # Calculate total gas fees and average gas price
    total_gas_fees_eth, average_gas_price = calculate_gas_fees(transactions)
    
    # Fetch the current ETH price in USD
    eth_price = fetch_eth_price()
    
    if eth_price is None:
        print("Could not fetch ETH price.")
        return

    # Calculate total gas fees in USD
    total_gas_fees_usd = total_gas_fees_eth * eth_price
    
    # Display results
    print(f"Total Gas Fees Spent: {total_gas_fees_eth:.6f} ETH")
    print(f"Total Gas Fees Spent: ${total_gas_fees_usd:.2f} USD")
    print(f"Average Gas Price: {average_gas_price:.2f} Gwei")

if __name__ == "__main__":
    main()
```
