"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.xyz
Prompt: Write a Python script using the etherscan API to track transactions involving ETH and USDC between two wallet addresses.
Generated: DETERMINISTIC_5682ca94bbd5ab87
Batch ID: 20250612_150030
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
import time

# Constants
API_KEY = 'your_etherscan_api_key'  # Replace with your Etherscan API key
ETHERSCAN_BASE_URL = 'https://api.etherscan.io/api'
CHECK_INTERVAL = 30  # Time interval (in seconds) to check for new transactions

# Wallet addresses to monitor
WALLET_1 = '0xWalletAddress1'  # Replace with wallet address 1
WALLET_2 = '0xWalletAddress2'  # Replace with wallet address 2

# USDC Token Contract Address (Ethereum Mainnet)
USDC_CONTRACT = '0xA0b86991c6218b36c1d19D4a2e9Eb0CE3606EB48'

# Function to fetch Ethereum transactions for a given wallet address
def fetch_eth_transactions(wallet_address):
    """
    Fetch Ethereum transactions involving the specified wallet.
    :param wallet_address: Wallet address to fetch transactions for.
    :return: List of transactions involving the wallet.
    """
    url = f"{ETHERSCAN_BASE_URL}?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&sort=desc&apikey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['status'] == '1':  # Status '1' indicates success
            return data['result']
        else:
            print(f"Error fetching transactions for {wallet_address}: {data['message']}")
            return []
    except requests.RequestException as e:
        print(f"Network error while fetching ETH transactions: {e}")
        return []

# Function to fetch token transactions for a given wallet address
def fetch_token_transactions(wallet_address, contract_address):
    """
    Fetch token transactions involving the specified wallet and token contract.
    :param wallet_address: Wallet address to fetch transactions for.
    :param contract_address: Token contract address (e.g., USDC).
    :return: List of token transactions involving the wallet.
    """
    url = f"{ETHERSCAN_BASE_URL}?module=account&action=tokentx&contractaddress={contract_address}&address={wallet_address}&startblock=0&endblock=99999999&sort=desc&apikey={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if data['status'] == '1':  # Status '1' indicates success
            return data['result']
        else:
            print(f"Error fetching token transactions for {wallet_address}: {data['message']}")
            return []
    except requests.RequestException as e:
        print(f"Network error while fetching token transactions: {e}")
        return []

# Function to filter transactions between two wallets
def filter_transactions_between_wallets(transactions, wallet_1, wallet_2):
    """
    Filter transactions between two specific wallet addresses.
    :param transactions: List of transactions.
    :param wallet_1: Address of the first wallet.
    :param wallet_2: Address of the second wallet.
    :return: List of filtered transactions between the wallets.
    """
    filtered = []
    for tx in transactions:
        if tx['from'] == wallet_1 and tx['to'] == wallet_2 or tx['from'] == wallet_2 and tx['to'] == wallet_1:
            filtered.append(tx)
    return filtered

# Main function to track transactions
def track_transactions():
    """
    Track both ETH and USDC transactions between WALLET_1 and WALLET_2.
    """
    print("Starting transaction tracker...")

    while True:
        try:
            # Fetch ETH transactions for both wallets
            eth_transactions_wallet_1 = fetch_eth_transactions(WALLET_1)
            eth_transactions_wallet_2 = fetch_eth_transactions(WALLET_2)

            # Fetch USDC transactions for both wallets
            usdc_transactions_wallet_1 = fetch_token_transactions(WALLET_1, USDC_CONTRACT)
            usdc_transactions_wallet_2 = fetch_token_transactions(WALLET_2, USDC_CONTRACT)

            # Filter ETH transactions between the wallets
            eth_between_wallets = filter_transactions_between_wallets(
                eth_transactions_wallet_1 + eth_transactions_wallet_2, WALLET_1, WALLET_2
            )

            # Filter USDC transactions between the wallets
            usdc_between_wallets = filter_transactions_between_wallets(
                usdc_transactions_wallet_1 + usdc_transactions_wallet_2, WALLET_1, WALLET_2
            )

            # Print the filtered transactions
            print("\nETH Transactions between wallets:")
            for tx in eth_between_wallets:
                print(tx)

            print("\nUSDC Transactions between wallets:")
            for tx in usdc_between_wallets:
                print(tx)

            # Wait for the next interval
            time.sleep(CHECK_INTERVAL)

        except KeyboardInterrupt:
            print("\nTransaction tracker stopped.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(CHECK_INTERVAL)

# Entry point of the script
if __name__ == "__main__":
    track_transactions()
```
