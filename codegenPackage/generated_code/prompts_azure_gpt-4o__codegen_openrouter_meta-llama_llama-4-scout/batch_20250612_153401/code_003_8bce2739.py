"""
Generated Code Metadata:
========================
Original URL: https://paperhands-checker.pages.dev
Prompt: Develop a program that uses advanced analytics tools to evaluate NFT trading activity across multiple wallets, inspired by the features on the HALO platform.
Generated: DETERMINISTIC_8bce2739bc5b3aa0
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_analytics.py

import pandas as pd
import numpy as np
from typing import List, Dict

class NFTAnalytics:
    """
    Evaluates NFT trading activity across multiple wallets.
    """

    def __init__(self, wallet_data: List[Dict]):
        """
        Initializes the NFTAnalytics class.

        Args:
        wallet_data (List[Dict]): A list of dictionaries containing wallet data.
            Each dictionary should have the following keys:
                - 'wallet_address' (str): The wallet address.
                - 'nft_transactions' (List[Dict]): A list of NFT transactions.
                    Each transaction dictionary should have the following keys:
                        - 'nft_id' (str): The NFT ID.
                        - 'transaction_date' (str): The transaction date.
                        - 'transaction_type' (str): The transaction type (buy/sell).
                        - 'amount' (float): The transaction amount.
        """
        self.wallet_data = wallet_data

    def calculate_nft_ownership(self) -> Dict:
        """
        Calculates the NFT ownership distribution across wallets.

        Returns:
        Dict: A dictionary with NFT IDs as keys and dictionaries of wallet addresses and their ownership percentages as values.
        """
        nft_ownership = {}
        for wallet in self.wallet_data:
            for transaction in wallet['nft_transactions']:
                nft_id = transaction['nft_id']
                if nft_id not in nft_ownership:
                    nft_ownership[nft_id] = {}
                wallet_address = wallet['wallet_address']
                if wallet_address not in nft_ownership[nft_id]:
                    nft_ownership[nft_id][wallet_address] = 0
                if transaction['transaction_type'] == 'buy':
                    nft_ownership[nft_id][wallet_address] += 1
                elif transaction['transaction_type'] == 'sell':
                    nft_ownership[nft_id][wallet_address] -= 1

        # Calculate ownership percentages
        for nft_id, wallet_ownership in nft_ownership.items():
            total_ownership = sum(abs(ownership) for ownership in wallet_ownership.values())
            for wallet_address, ownership in wallet_ownership.items():
                nft_ownership[nft_id][wallet_address] = (ownership / total_ownership) * 100

        return nft_ownership

    def calculate_wallet_nft_value(self) -> Dict:
        """
        Calculates the total value of NFTs in each wallet.

        Returns:
        Dict: A dictionary with wallet addresses as keys and their total NFT values as values.
        """
        wallet_nft_values = {}
        for wallet in self.wallet_data:
            wallet_address = wallet['wallet_address']
            wallet_nft_values[wallet_address] = 0
            for transaction in wallet['nft_transactions']:
                if transaction['transaction_type'] == 'buy':
                    wallet_nft_values[wallet_address] += transaction['amount']
                elif transaction['transaction_type'] == 'sell':
                    wallet_nft_values[wallet_address] -= transaction['amount']

        return wallet_nft_values

    def calculate_nft_market_trends(self) -> pd.DataFrame:
        """
        Calculates the market trends for each NFT.

        Returns:
        pd.DataFrame: A DataFrame with NFT IDs as indices and columns for average price, total transactions, and price volatility.
        """
        nft_market_trends = {}
        for wallet in self.wallet_data:
            for transaction in wallet['nft_transactions']:
                nft_id = transaction['nft_id']
                if nft_id not in nft_market_trends:
                    nft_market_trends[nft_id] = []
                nft_market_trends[nft_id].append({
                    'transaction_date': transaction['transaction_date'],
                    'amount': transaction['amount']
                })

        # Calculate market trends
        trends_data = []
        for nft_id, transactions in nft_market_trends.items():
            df = pd.DataFrame(transactions)
            avg_price = df['amount'].mean()
            total_transactions = len(df)
            price_volatility = df['amount'].std()
            trends_data.append({
                'nft_id': nft_id,
                'average_price': avg_price,
                'total_transactions': total_transactions,
                'price_volatility': price_volatility
            })

        return pd.DataFrame(trends_data).set_index('nft_id')

def main():
    # Example usage
    wallet_data = [
        {
            'wallet_address': '0x123',
            'nft_transactions': [
                {'nft_id': 'NFT-1', 'transaction_date': '2022-01-01', 'transaction_type': 'buy', 'amount': 100},
                {'nft_id': 'NFT-2', 'transaction_date': '2022-01-15', 'transaction_type': 'buy', 'amount': 200}
            ]
        },
        {
            'wallet_address': '0x456',
            'nft_transactions': [
                {'nft_id': 'NFT-1', 'transaction_date': '2022-02-01', 'transaction_type': 'sell', 'amount': 120},
                {'nft_id': 'NFT-3', 'transaction_date': '2022-03-01', 'transaction_type': 'buy', 'amount': 300}
            ]
        }
    ]

    analytics = NFTAnalytics(wallet_data)
    nft_ownership = analytics.calculate_nft_ownership()
    wallet_nft_values = analytics.calculate_wallet_nft_value()
    nft_market_trends = analytics.calculate_nft_market_trends()

    print("NFT Ownership:")
    print(nft_ownership)
    print("\nWallet NFT Values:")
    print(wallet_nft_values)
    print("\nNFT Market Trends:")
    print(nft_market_trends)

if __name__ == "__main__":
    main()
```
