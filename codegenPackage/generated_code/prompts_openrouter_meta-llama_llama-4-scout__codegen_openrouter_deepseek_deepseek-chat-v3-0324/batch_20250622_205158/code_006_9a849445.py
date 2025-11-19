"""
Generated Code Metadata:
========================
Original URL: https://allocation-blast.io
Prompt: Compare the features and security measures of MetaMask with other popular crypto wallet platforms, and recommend the best option for a specific use case.
Generated: DETERMINISTIC_9a849445bbf217e7
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class WalletFeature(Enum):
    """Enum representing different wallet features."""
    MULTI_CHAIN = "Multi-chain support"
    DEFI_INTEGRATION = "DeFi integration"
    NFT_SUPPORT = "NFT support"
    HARDWARE_WALLET = "Hardware wallet support"
    MOBILE_APP = "Mobile app"
    BROWSER_EXTENSION = "Browser extension"
    SWAP_FEATURE = "Built-in swap feature"
    STAKING = "Staking support"
    CROSS_PLATFORM = "Cross-platform sync"

class SecurityMeasure(Enum):
    """Enum representing different security measures."""
    SEED_PHRASE = "Seed phrase backup"
    BIOMETRICS = "Biometric authentication"
    TWO_FACTOR = "Two-factor authentication"
    MULTISIG = "Multi-signature support"
    OPEN_SOURCE = "Open-source code"
    NON_CUSTODIAL = "Non-custodial"
    TRANSACTION_SIMULATION = "Transaction simulation"
    PHISHING_DETECTION = "Phishing detection"
    PRIVATE_KEY_LOCAL = "Private keys stored locally"

class WalletPlatform:
    """Class representing a wallet platform with its features and security measures."""
    
    def __init__(self, name: str):
        self.name = name
        self.features: List[WalletFeature] = []
        self.security_measures: List[SecurityMeasure] = []
    
    def add_feature(self, feature: WalletFeature) -> None:
        """Add a feature to the wallet platform."""
        if feature not in self.features:
            self.features.append(feature)
    
    def add_security_measure(self, measure: SecurityMeasure) -> None:
        """Add a security measure to the wallet platform."""
        if measure not in self.security_measures:
            self.security_measures.append(measure)
    
    def to_dict(self) -> Dict:
        """Convert the wallet platform to a dictionary."""
        return {
            "name": self.name,
            "features": [feature.value for feature in self.features],
            "security_measures": [measure.value for measure in self.security_measures]
        }

class WalletComparator:
    """Class to compare different wallet platforms."""
    
    def __init__(self):
        self.wallets: Dict[str, WalletPlatform] = {}
    
    def add_wallet(self, wallet: WalletPlatform) -> None:
        """Add a wallet platform to the comparator."""
        self.wallets[wallet.name] = wallet
    
    def compare_features(self) -> Dict:
        """Compare features across all wallets."""
        comparison = {}
        for wallet_name, wallet in self.wallets.items():
            comparison[wallet_name] = {
                "features": [feature.value for feature in wallet.features]
            }
        return comparison
    
    def compare_security(self) -> Dict:
        """Compare security measures across all wallets."""
        comparison = {}
        for wallet_name, wallet in self.wallets.items():
            comparison[wallet_name] = {
                "security_measures": [measure.value for measure in wallet.security_measures]
            }
        return comparison
    
    def recommend_wallet(self, required_features: List[WalletFeature], 
                        required_security: List[SecurityMeasure]) -> Optional[str]:
        """
        Recommend the best wallet based on required features and security measures.
        Returns the name of the recommended wallet or None if no match found.
        """
        best_match = None
        best_score = 0
        
        for wallet_name, wallet in self.wallets.items():
            feature_score = sum(1 for feature in required_features if feature in wallet.features)
            security_score = sum(1 for measure in required_security if measure in wallet.security_measures)
            total_score = feature_score + security_score
            
            if total_score > best_score:
                best_score = total_score
                best_match = wallet_name
        
        return best_match if best_score > 0 else None

def initialize_wallets() -> WalletComparator:
    """Initialize wallet platforms with their features and security measures."""
    comparator = WalletComparator()
    
    # MetaMask
    metamask = WalletPlatform("MetaMask")
    metamask.add_feature(WalletFeature.BROWSER_EXTENSION)
    metamask.add_feature(WalletFeature.MOBILE_APP)
    metamask.add_feature(WalletFeature.MULTI_CHAIN)
    metamask.add_feature(WalletFeature.DEFI_INTEGRATION)
    metamask.add_feature(WalletFeature.NFT_SUPPORT)
    metamask.add_feature(WalletFeature.SWAP_FEATURE)
    metamask.add_security_measure(SecurityMeasure.SEED_PHRASE)
    metamask.add_security_measure(SecurityMeasure.NON_CUSTODIAL)
    metamask.add_security_measure(SecurityMeasure.PRIVATE_KEY_LOCAL)
    comparator.add_wallet(metamask)
    
    # Trust Wallet
    trust = WalletPlatform("Trust Wallet")
    trust.add_feature(WalletFeature.MOBILE_APP)
    trust.add_feature(WalletFeature.MULTI_CHAIN)
    trust.add_feature(WalletFeature.DEFI_INTEGRATION)
    trust.add_feature(WalletFeature.NFT_SUPPORT)
    trust.add_feature(WalletFeature.STAKING)
    trust.add_feature(WalletFeature.SWAP_FEATURE)
    trust.add_security_measure(SecurityMeasure.SEED_PHRASE)
    trust.add_security_measure(SecurityMeasure.BIOMETRICS)
    trust.add_security_measure(SecurityMeasure.NON_CUSTODIAL)
    trust.add_security_measure(SecurityMeasure.PRIVATE_KEY_LOCAL)
    comparator.add_wallet(trust)
    
    # Ledger Live
    ledger = WalletPlatform("Ledger Live")
    ledger.add_feature(WalletFeature.MOBILE_APP)
    ledger.add_feature(WalletFeature.MULTI_CHAIN)
    ledger.add_feature(WalletFeature.DEFI_INTEGRATION)
    ledger.add_feature(WalletFeature.NFT_SUPPORT)
    ledger.add_feature(WalletFeature.STAKING)
    ledger.add_feature(WalletFeature.SWAP_FEATURE)
    ledger.add_feature(WalletFeature.HARDWARE_WALLET)
    ledger.add_security_measure(SecurityMeasure.SEED_PHRASE)
    ledger.add_security_measure(SecurityMeasure.BIOMETRICS)
    ledger.add_security_measure(SecurityMeasure.HARDWARE_WALLET)
    ledger.add_security_measure(SecurityMeasure.NON_CUSTODIAL)
    comparator.add_wallet(ledger)
    
    # Coinbase Wallet
    coinbase = WalletPlatform("Coinbase Wallet")
    coinbase.add_feature(WalletFeature.MOBILE_APP)
    coinbase.add_feature(WalletFeature.BROWSER_EXTENSION)
    coinbase.add_feature(WalletFeature.MULTI_CHAIN)
    coinbase.add_feature(WalletFeature.DEFI_INTEGRATION)
    coinbase.add_feature(WalletFeature.NFT_SUPPORT)
    coinbase.add_feature(WalletFeature.SWAP_FEATURE)
    coinbase.add_security_measure(SecurityMeasure.SEED_PHRASE)
    coinbase.add_security_measure(SecurityMeasure.BIOMETRICS)
    coinbase.add_security_measure(SecurityMeasure.NON_CUSTODIAL)
    coinbase.add_security_measure(SecurityMeasure.PRIVATE_KEY_LOCAL)
    comparator.add_wallet(coinbase)
    
    return comparator

def main():
    """Main function to demonstrate wallet comparison."""
    comparator = initialize_wallets()
    
    # Example: Compare all wallets
    print("Feature Comparison:")
    print(json.dumps(comparator.compare_features(), indent=2))
    
    print("\nSecurity Comparison:")
    print(json.dumps(comparator.compare_security(), indent=2))
    
    # Example: Recommend wallet for DeFi users who prioritize security
    required_features = [
        WalletFeature.DEFI_INTEGRATION,
        WalletFeature.MULTI_CHAIN,
        WalletFeature.SWAP_FEATURE
    ]
    required_security = [
        SecurityMeasure.NON_CUSTODIAL,
        SecurityMeasure.PRIVATE_KEY_LOCAL,
        SecurityMeasure.SEED_PHRASE
    ]
    
    recommended = comparator.recommend_wallet(required_features, required_security)
    print(f"\nRecommended wallet for DeFi users: {recommended}")

if __name__ == "__main__":
    main()
```
