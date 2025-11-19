"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbalance.com
Prompt: What are the steps to access USDT on different blockchains like Ethereum and Solana for a developer project?
Generated: DETERMINISTIC_afde078be501d50a
Batch ID: 20250612_163601
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.solscan.io/token": {
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

class USDTAccess:
    """
    A class to handle access to USDT on different blockchains such as Ethereum and Solana.
    """

    def __init__(self):
        self.blockchain_apis = {
            'ethereum': 'https://api.etherscan.io/api',
            'solana': 'https://api.solscan.io/token'
        }
        self.api_keys = {
            'ethereum': 'YOUR_ETHERSCAN_API_KEY',
            'solana': None  # Solana does not require an API key for public endpoints
        }

    def get_usdt_balance(self, blockchain: str, wallet_address: str) -> float:
        """
        Fetches the USDT balance of a given wallet address for the specified blockchain.

        Parameters:
            blockchain (str): The blockchain to query (e.g., 'ethereum', 'solana').
            wallet_address (str): The wallet address to query.

        Returns:
            float: The USDT balance if successful, otherwise raises an Exception.

        Raises:
            ValueError: If an unsupported blockchain is specified.
            Exception: If the API request fails or returns an error.
        """
        if blockchain not in self.blockchain_apis:
            raise ValueError(f"Unsupported blockchain: {blockchain}")

        if blockchain == 'ethereum':
            return self._get_eth_usdt_balance(wallet_address)
        elif blockchain == 'solana':
            return self._get_solana_usdt_balance(wallet_address)

    def _get_eth_usdt_balance(self, wallet_address: str) -> float:
        """
        Fetches USDT balance from Ethereum blockchain using Etherscan API.

        Parameters:
            wallet_address (str): The Ethereum wallet address.

        Returns:
            float: The USDT balance for the given wallet address.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        params = {
            'module': 'account',
            'action': 'tokenbalance',
            'contractaddress': '0xdac17f958d2ee523a2206206994597c13d831ec7',  # USDT contract address
            'address': wallet_address,
            'tag': 'latest',
            'apikey': self.api_keys['ethereum']
        }

        response = requests.get(self.blockchain_apis['ethereum'], params=params)

        if response.status_code != 200:
            raise Exception(f"Error fetching data from Etherscan: {response.text}")

        data = response.json()

        if data['status'] != '1':
            raise Exception(f"Error from Etherscan API: {data['message']}")

        balance = int(data['result']) / 1e6  # USDT has 6 decimals
        return balance

    def _get_solana_usdt_balance(self, wallet_address: str) -> float:
        """
        Fetches USDT balance from Solana blockchain using Solscan API.

        Parameters:
            wallet_address (str): The Solana wallet address.

        Returns:
            float: The USDT balance for the given wallet address.

        Raises:
            Exception: If the API request fails or returns an error.
        """
        url = f"{self.blockchain_apis['solana']}/{wallet_address}/tokens"
        response = requests.get(url)

        if response.status_code != 200:
            raise Exception(f"Error fetching data from Solscan: {response.text}")

        data = response.json()

        if 'data' not in data:
            raise Exception("No data found for the given wallet address.")

        usdt_balance = 0.0
        # Iterate through the tokens to find USDT
        for token in data['data']:
            if token['tokenSymbol'] == 'USDT':
                usdt_balance = float(token['tokenAmount']) / 1e6  # USDT has 6 decimals
                break

        return usdt_balance

# Example usage:
if __name__ == "__main__":
    usdt_access = USDTAccess()
    try:
        eth_balance = usdt_access.get_usdt_balance('ethereum', 'YOUR_ETHEREUM_WALLET_ADDRESS')
        print(f"Ethereum USDT Balance: {eth_balance}")
        
        sol_balance = usdt_access.get_usdt_balance('solana', 'YOUR_SOLANA_WALLET_ADDRESS')
        print(f"Solana USDT Balance: {sol_balance}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

Make sure to replace `YOUR_ETHERSCAN_API_KEY`, `YOUR_ETHEREUM_WALLET_ADDRESS`, and `YOUR_SOLANA_WALLET_ADDRESS` with actual values before running the code.
