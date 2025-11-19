"""
Generated Code Metadata:
========================
Original URL: https://stakingstory.org
Prompt: Compare the features of the Story Staking protocol with other DeFi staking platforms, focusing on security, rewards, and multi-chain compatibility.
Generated: DETERMINISTIC_2c34eb75555b95e8
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional

class DeFiStakingComparison:
    """
    Compare DeFi staking platforms based on security, rewards, and multi-chain compatibility.
    """
    
    def __init__(self):
        self.platforms = {
            "Story Staking": {
                "security": "High (Audited smart contracts, multi-sig wallets)",
                "rewards": "Dynamic APY based on protocol performance",
                "multi_chain": "Ethereum, Polygon, Binance Smart Chain"
            },
            "Aave": {
                "security": "High (Formal verification, bug bounty program)",
                "rewards": "Variable APY based on market conditions",
                "multi_chain": "Ethereum, Polygon, Avalanche"
            },
            "Compound": {
                "security": "High (Audited, decentralized governance)",
                "rewards": "Fixed APY with COMP token incentives",
                "multi_chain": "Ethereum"
            },
            "PancakeSwap": {
                "security": "Medium (Audited but centralized aspects)",
                "rewards": "High APY with CAKE token rewards",
                "multi_chain": "Binance Smart Chain"
            }
        }
    
    def compare_features(self, platform1: str, platform2: str) -> Optional[Dict]:
        """
        Compare two staking platforms across key features.
        
        Args:
            platform1: First platform name
            platform2: Second platform name
            
        Returns:
            Dictionary with comparison or None if platforms not found
        """
        if platform1 not in self.platforms or platform2 not in self.platforms:
            return None
            
        return {
            platform1: self.platforms[platform1],
            platform2: self.platforms[platform2]
        }
    
    def get_all_platforms(self) -> List[Dict]:
        """
        Get all platform data for comparison.
        
        Returns:
            List of dictionaries containing platform data
        """
        return [
            {"name": name, **data} 
            for name, data in self.platforms.items()
        ]
    
    def get_feature_matrix(self) -> Dict:
        """
        Generate a feature comparison matrix across all platforms.
        
        Returns:
            Dictionary with feature comparison matrix
        """
        features = ["security", "rewards", "multi_chain"]
        matrix = {
            "platforms": list(self.platforms.keys()),
            "features": {feature: [] for feature in features}
        }
        
        for platform in self.platforms:
            for feature in features:
                matrix["features"][feature].append(self.platforms[platform][feature])
                
        return matrix
    
    def export_comparison(self, filename: str = "staking_comparison.json") -> bool:
        """
        Export platform comparison data to JSON file.
        
        Args:
            filename: Output filename
            
        Returns:
            True if successful, False otherwise
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.get_feature_matrix(), f, indent=4)
            return True
        except Exception as e:
            print(f"Error exporting comparison: {e}")
            return False

# Example usage
if __name__ == "__main__":
    comparator = DeFiStakingComparison()
    
    # Compare two platforms
    comparison = comparator.compare_features("Story Staking", "Aave")
    print("Comparison between Story Staking and Aave:")
    print(json.dumps(comparison, indent=4))
    
    # Get all platform data
    print("\nAll platforms:")
    print(json.dumps(comparator.get_all_platforms(), indent=4))
    
    # Export feature matrix
    if comparator.export_comparison():
        print("\nFeature matrix exported successfully")
```
