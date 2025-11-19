"""
Generated Code Metadata:
========================
Original URL: https://curly-sun-6227.on.fleek.co
Prompt: Compare the features of PinkSale with other token sale platforms and highlight the unique features of PinkSale.
Generated: DETERMINISTIC_a0cd50686c320d2e
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict

class TokenSalePlatformComparator:
    """
    A class to compare features of PinkSale with other token sale platforms.
    """
    
    def __init__(self):
        self.platforms_data = {
            "PinkSale": {
                "features": [
                    "Multi-chain support",
                    "Fair launches",
                    "Anti-bot measures",
                    "Locking liquidity",
                    "KYC options",
                    "Whitelisting",
                    "Vesting schedules",
                    "Customizable UI",
                    "No coding required",
                    "Gas fee optimization",
                    "Multi-sig wallets",
                    "Token minting"
                ],
                "unique_features": [
                    "Gas fee optimization",
                    "Anti-bot measures",
                    "Customizable UI without coding",
                    "Integrated multi-sig wallets"
                ]
            },
            "Uniswap": {
                "features": [
                    "Decentralized exchange",
                    "Automated market maker",
                    "Liquidity pools",
                    "ERC-20 support",
                    "Permissionless listing"
                ],
                "unique_features": [
                    "Permissionless listing",
                    "Automated market maker"
                ]
            },
            "DAO Maker": {
                "features": [
                    "DAO infrastructure",
                    "Venture bonds",
                    "KYC/AML",
                    "Whitelisting",
                    "Vesting",
                    "Multi-chain support"
                ],
                "unique_features": [
                    "Venture bonds",
                    "DAO infrastructure"
                ]
            },
            "Polkastarter": {
                "features": [
                    "Cross-chain token pools",
                    "KYC projects",
                    "Whitelisting",
                    "Fixed swap sales",
                    "Interoperability"
                ],
                "unique_features": [
                    "Cross-chain token pools",
                    "Fixed swap sales"
                ]
            }
        }
    
    def get_all_features_comparison(self) -> pd.DataFrame:
        """
        Returns a DataFrame comparing features across all platforms.
        """
        all_features = set()
        for platform in self.platforms_data.values():
            all_features.update(platform["features"])
        
        comparison_data = []
        for platform_name, data in self.platforms_data.items():
            row = {"Platform": platform_name}
            for feature in all_features:
                row[feature] = feature in data["features"]
            comparison_data.append(row)
        
        return pd.DataFrame(comparison_data).set_index("Platform")
    
    def get_unique_features(self, platform_name: str) -> List[str]:
        """
        Returns the unique features of a specified platform.
        
        Args:
            platform_name: Name of the platform to check
            
        Returns:
            List of unique features
            
        Raises:
            ValueError: If platform name is not found
        """
        if platform_name not in self.platforms_data:
            raise ValueError(f"Platform {platform_name} not found in data")
        return self.platforms_data[platform_name]["unique_features"]
    
    def compare_with_pinksale(self, other_platform: str) -> Dict:
        """
        Compares PinkSale with another specified platform.
        
        Args:
            other_platform: Name of the platform to compare with PinkSale
            
        Returns:
            Dictionary with comparison results
            
        Raises:
            ValueError: If platform name is not found
        """
        if other_platform not in self.platforms_data:
            raise ValueError(f"Platform {other_platform} not found in data")
            
        pinksale_features = set(self.platforms_data["PinkSale"]["features"])
        other_features = set(self.platforms_data[other_platform]["features"])
        
        return {
            "common_features": list(pinksale_features & other_features),
            "pinksale_only": list(pinksale_features - other_features),
            "other_only": list(other_features - pinksale_features),
            "pinksale_unique": self.platforms_data["PinkSale"]["unique_features"]
        }

# Example usage
if __name__ == "__main__":
    comparator = TokenSalePlatformComparator()
    
    # Get full feature comparison
    print("Feature Comparison:")
    print(comparator.get_all_features_comparison())
    
    # Get PinkSale's unique features
    print("\nPinkSale Unique Features:")
    print(comparator.get_unique_features("PinkSale"))
    
    # Compare PinkSale with another platform
    print("\nComparison with Uniswap:")
    print(comparator.compare_with_pinksale("Uniswap"))
```
