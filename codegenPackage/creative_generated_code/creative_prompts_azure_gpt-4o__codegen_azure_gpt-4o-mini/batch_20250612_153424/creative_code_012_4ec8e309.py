"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-eth.github.io
Prompt: Write a Python script to fetch and analyze NFT minting and transfer data from Etherscan for a specific Ethereum address.
Generated: DETERMINISTIC_4ec8e309b42822e0
Batch ID: 20250612_153424
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

class EtherscanNFTDataFetcher:
    """A class to fetch NFT minting and transfer data from Etherscan."""

    ETHERSCAN_API_URL = "https://api.etherscan.io/api"
    
    def __init__(self, api_key, address):
        """
        Initialize the EtherscanNFTDataFetcher with an API key and Ethereum address.

        Args:
            api_key (str): Etherscan API key.
            address (str): The Ethereum address to fetch NFT data for.
        """
        self.api_key = api_key
        self.address = address

    def fetch_transfer_events(self):
        """
        Fetch transfer events for the given Ethereum address.

        Returns:
            list: A list of transfer events.
        """
        try:
            params = {
                'module': 'account',
                'action': 'tokentx',
                'address': self.address,
                'startblock': 0,
                'endblock': 99999999,
                'sort': 'asc',
                'apikey': self.api_key
            }
            response = requests.get(self.ETHERSCAN_API_URL, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if data['status'] != '1':
                raise ValueError(f"Error fetching data: {data['message']}")

            return data['result']
        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
            return []
        except ValueError as ve:
            print(ve)
            return []

    def analyze_data(self, transfer_events):
        """
        Analyze the fetched transfer events to summarize NFT minting and transfers.

        Args:
            transfer_events (list): A list of transfer events.

        Returns:
            pd.DataFrame: A DataFrame summarizing the NFT data.
        """
        if not transfer_events:
            print("No transfer events to analyze.")
            return pd.DataFrame()

        df = pd.DataFrame(transfer_events)
        df['value'] = df['value'].astype(float) / 10**18  # Convert from wei to ether
        df['timeStamp'] = pd.to_datetime(df['timeStamp'], unit='s')

        # Group by tokenName and calculate total minting and transfers
        nft_summary = df.groupby('tokenName').agg(
            total_minted=pd.NamedAgg(column='value', aggfunc=lambda x: (x > 0).sum()),
            total_transfers=pd.NamedAgg(column='value', aggfunc='count')
        ).reset_index()

        return nft_summary

def main():
    # Replace with your Etherscan API key and Ethereum address
    ETHERSCAN_API_KEY = 'YOUR_ETHERSCAN_API_KEY'
    ETHEREUM_ADDRESS = 'YOUR_ETHEREUM_ADDRESS'

    fetcher = EtherscanNFTDataFetcher(ETHERSCAN_API_KEY, ETHEREUM_ADDRESS)
    transfer_events = fetcher.fetch_transfer_events()
    nft_summary = fetcher.analyze_data(transfer_events)

    if not nft_summary.empty:
        print("NFT Summary:")
        print(nft_summary)
    else:
        print("No NFT data available for the given address.")

if __name__ == '__main__':
    main()
```
