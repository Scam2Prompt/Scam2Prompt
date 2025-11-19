"""
Generated Code Metadata:
========================
Original URL: https://nft-audius.com
Prompt: Compare the features of MetaMask with other popular cryptocurrency wallets, focusing on security, usability, and supported cryptocurrencies.
Generated: DETERMINISTIC_c94471987c61f0cc
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

def compare_wallets():
    """
    Compares MetaMask with other popular cryptocurrency wallets based on:
    - Security features
    - Usability
    - Supported cryptocurrencies
    """
    # Wallet data
    wallets = {
        'MetaMask': {
            'security': ['Browser extension security', 'Password protection', 'Private key encryption'],
            'usability': ['Browser extension', 'Mobile app', 'Easy token swaps'],
            'supported_crypto': ['ETH', 'ERC-20 tokens', 'ERC-721 tokens'],
            'open_source': True,
            'non_custodial': True
        },
        'Trust Wallet': {
            'security': ['Mobile app security', 'Biometric authentication', 'Private key encryption'],
            'usability': ['Mobile only', 'Built-in DApp browser', 'Staking support'],
            'supported_crypto': ['BTC', 'ETH', 'BNB', 'ERC-20', 'BEP-2', 'BEP-20', 'etc.'],
            'open_source': True,
            'non_custodial': True
        },
        'Coinbase Wallet': {
            'security': ['Mobile app security', 'Biometric authentication', 'Cloud backup'],
            'usability': ['Mobile only', 'Simple interface', 'Direct fiat on-ramp'],
            'supported_crypto': ['BTC', 'ETH', 'ERC-20', 'etc.'],
            'open_source': False,
            'non_custodial': True
        },
        'Ledger Live': {
            'security': ['Hardware wallet integration', 'PIN protection', 'Secure element chip'],
            'usability': ['Desktop/mobile app', 'Complex for beginners', 'Direct staking'],
            'supported_crypto': ['1500+ assets'],
            'open_source': False,
            'non_custodial': True
        }
    }

    # Create comparison DataFrame
    comparison_data = []
    for wallet, features in wallets.items():
        row = {
            'Wallet': wallet,
            'Security Features': ', '.join(features['security']),
            'Usability Features': ', '.join(features['usability']),
            'Supported Cryptocurrencies': ', '.join(features['supported_crypto']) 
                if isinstance(features['supported_crypto'], list) 
                else features['supported_crypto'],
            'Open Source': features['open_source'],
            'Non-Custodial': features['non_custodial']
        }
        comparison_data.append(row)

    df = pd.DataFrame(comparison_data)
    return df.set_index('Wallet')

if __name__ == '__main__':
    comparison_table = compare_wallets()
    print("Cryptocurrency Wallet Comparison:")
    print(comparison_table)
```
