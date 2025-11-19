"""
Generated Code Metadata:
========================
Original URL: https://karlmonsterblog.wordpress.com
Prompt: Compare the features of Hackerone, Bugcrowd, and Immunefi for bug bounty hunting.
Generated: DETERMINISTIC_c8bac84e8ef9c58e
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from typing import Dict, List, Optional

class BugBountyPlatform:
    """
    A class to represent and compare features of bug bounty platforms.
    """
    
    def __init__(self, name: str, features: Dict[str, bool]):
        """
        Initialize a bug bounty platform with its name and features.
        
        Args:
            name: Name of the platform (e.g., "Hackerone", "Bugcrowd", "Immunefi")
            features: Dictionary of features and their availability (True/False)
        """
        self.name = name
        self.features = features
    
    def get_feature(self, feature_name: str) -> Optional[bool]:
        """
        Check if a specific feature is available on this platform.
        
        Args:
            feature_name: The feature to check
            
        Returns:
            bool: True if available, False if not, None if feature doesn't exist
        """
        return self.features.get(feature_name)
    
    def __str__(self) -> str:
        """String representation of the platform."""
        return f"{self.name}: {self.features}"

def compare_platforms(platforms: List[BugBountyPlatform], feature: str) -> Dict[str, Optional[bool]]:
    """
    Compare a specific feature across multiple bug bounty platforms.
    
    Args:
        platforms: List of BugBountyPlatform objects to compare
        feature: The feature to compare across platforms
        
    Returns:
        Dict: Mapping of platform names to feature availability
    """
    comparison = {}
    for platform in platforms:
        comparison[platform.name] = platform.get_feature(feature)
    return comparison

def get_all_features_comparison(platforms: List[BugBountyPlatform]) -> Dict[str, Dict[str, Optional[bool]]]:
    """
    Compare all features across multiple bug bounty platforms.
    
    Args:
        platforms: List of BugBountyPlatform objects to compare
        
    Returns:
        Dict: Nested dictionary mapping features to platform availability
    """
    if not platforms:
        return {}
    
    # Get all unique features from all platforms
    all_features = set()
    for platform in platforms:
        all_features.update(platform.features.keys())
    
    comparison = {}
    for feature in all_features:
        comparison[feature] = compare_platforms(platforms, feature)
    
    return comparison

def main():
    # Define platform features (example data - should be updated with real data)
    hackerone = BugBountyPlatform("Hackerone", {
        "private_programs": True,
        "public_programs": True,
        "vdp": True,
        "bounty_amounts": True,
        "swag": True,
        "live_hacking_events": True,
        "crypto_projects": False
    })
    
    bugcrowd = BugBountyPlatform("Bugcrowd", {
        "private_programs": True,
        "public_programs": True,
        "vdp": True,
        "bounty_amounts": True,
        "swag": True,
        "live_hacking_events": True,
        "crypto_projects": False
    })
    
    immunefi = BugBountyPlatform("Immunefi", {
        "private_programs": False,
        "public_programs": True,
        "vdp": False,
        "bounty_amounts": True,
        "swag": False,
        "live_hacking_events": False,
        "crypto_projects": True
    })
    
    platforms = [hackerone, bugcrowd, immunefi]
    
    # Example comparison
    print("Comparison of crypto_projects support:")
    print(compare_platforms(platforms, "crypto_projects"))
    
    print("\nFull feature comparison:")
    full_comparison = get_all_features_comparison(platforms)
    for feature, results in full_comparison.items():
        print(f"\n{feature}:")
        for platform, available in results.items():
            print(f"  {platform}: {available}")

if __name__ == "__main__":
    main()
```
