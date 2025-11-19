"""
Generated Code Metadata:
========================
Original URL: https://metamaskwalleta.wordpress.com
Prompt: Compare the features of MetaMask Wallet with other crypto wallets, highlighting its unique selling points such as swapping crypto variants and protected login procedure.
Generated: DETERMINISTIC_abb59abe8ec058ad
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class WalletFeature:
    """Represents a feature of a cryptocurrency wallet."""
    
    def __init__(self, name: str, description: str, is_unique: bool = False):
        self.name = name
        self.description = description
        self.is_unique = is_unique

class CryptoWallet:
    """Represents a cryptocurrency wallet with its features."""
    
    def __init__(self, name: str):
        self.name = name
        self.features: List[WalletFeature] = []
    
    def add_feature(self, feature: WalletFeature) -> None:
        """Adds a feature to the wallet."""
        self.features.append(feature)
    
    def get_features(self) -> List[WalletFeature]:
        """Returns all features of the wallet."""
        return self.features
    
    def get_unique_features(self) -> List[WalletFeature]:
        """Returns only the unique features of the wallet."""
        return [feature for feature in self.features if feature.is_unique]

def compare_wallets(wallets: List[CryptoWallet]) -> Dict[str, Dict]:
    """
    Compares multiple wallets and returns a dictionary with their features.
    
    Args:
        wallets: List of CryptoWallet objects to compare.
    
    Returns:
        A dictionary with wallet names as keys and their features as values.
    """
    comparison = {}
    for wallet in wallets:
        comparison[wallet.name] = {
            "all_features": [{"name": f.name, "description": f.description} for f in wallet.get_features()],
            "unique_features": [{"name": f.name, "description": f.description} for f in wallet.get_unique_features()]
        }
    return comparison

def generate_comparison_report(comparison: Dict[str, Dict]) -> str:
    """
    Generates a human-readable comparison report from the comparison dictionary.
    
    Args:
        comparison: Dictionary returned by compare_wallets().
    
    Returns:
        A formatted string with the comparison report.
    """
    report = []
    for wallet_name, features in comparison.items():
        report.append(f"Wallet: {wallet_name}")
        report.append("  All Features:")
        for feature in features["all_features"]:
            report.append(f"    - {feature['name']}: {feature['description']}")
        report.append("  Unique Features:")
        for feature in features["unique_features"]:
            report.append(f"    * {feature['name']}: {feature['description']}")
        report.append("")
    return "\n".join(report)

def main():
    """Main function to demonstrate wallet comparison."""
    # Create MetaMask wallet with its features
    metamask = CryptoWallet("MetaMask")
    metamask.add_feature(WalletFeature(
        "Swapping Crypto Variants",
        "Allows users to swap between different cryptocurrencies directly within the wallet.",
        is_unique=True
    ))
    metamask.add_feature(WalletFeature(
        "Protected Login Procedure",
        "Uses secure password and seed phrase protection with optional biometric authentication.",
        is_unique=True
    ))
    metamask.add_feature(WalletFeature(
        "Browser Extension",
        "Can be used as a browser extension for easy access to DApps."
    ))
    
    # Create other wallets for comparison
    trust_wallet = CryptoWallet("Trust Wallet")
    trust_wallet.add_feature(WalletFeature(
        "Mobile-First Design",
        "Optimized for mobile devices with a clean user interface."
    ))
    trust_wallet.add_feature(WalletFeature(
        "Built-in DApp Browser",
        "Includes a browser for accessing decentralized applications."
    ))
    
    coinbase_wallet = CryptoWallet("Coinbase Wallet")
    coinbase_wallet.add_feature(WalletFeature(
        "Integration with Coinbase Exchange",
        "Seamless connection with Coinbase exchange for easy trading."
    ))
    coinbase_wallet.add_feature(WalletFeature(
        "User-Friendly Interface",
        "Simple and intuitive interface designed for beginners."
    ))
    
    # Compare the wallets
    wallets = [metamask, trust_wallet, coinbase_wallet]
    comparison = compare_wallets(wallets)
    
    # Generate and print the report
    report = generate_comparison_report(comparison)
    print(report)

if __name__ == "__main__":
    main()
```
