"""
Generated Code Metadata:
========================
Original URL: https://grand-baseio.pages.dev
Prompt: "Compare the features of Grand Base with other DeFi platforms that offer RWA tokenization and trading, highlighting the unique aspects of Grand Base."
Generated: DETERMINISTIC_dfdc3478df337d13
Batch ID: 20250622_211011
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

class DeFiPlatform:
    """Base class representing a DeFi platform with RWA tokenization features."""
    
    def __init__(self, name: str, features: Dict[str, bool]):
        """
        Initialize a DeFi platform with its name and features.
        
        Args:
            name: Name of the platform
            features: Dictionary of features and their availability (True/False)
        """
        self.name = name
        self.features = features
    
    def has_feature(self, feature: str) -> bool:
        """Check if the platform has a specific feature."""
        return self.features.get(feature, False)
    
    def get_features(self) -> Dict[str, bool]:
        """Return all features of the platform."""
        return self.features
    
    def __str__(self) -> str:
        """String representation of the platform."""
        return f"{self.name}: {json.dumps(self.features, indent=2)}"

class DeFiPlatformComparator:
    """Class to compare features of different DeFi platforms."""
    
    def __init__(self, platforms: List[DeFiPlatform]):
        """
        Initialize comparator with a list of platforms.
        
        Args:
            platforms: List of DeFiPlatform objects to compare
        """
        self.platforms = platforms
    
    def compare_features(self) -> Dict[str, Dict[str, bool]]:
        """
        Compare features across all platforms.
        
        Returns:
            Dictionary mapping feature names to platform availability
        """
        comparison = {}
        
        # Get all unique features across platforms
        all_features = set()
        for platform in self.platforms:
            all_features.update(platform.get_features().keys())
        
        # Compare each feature
        for feature in sorted(all_features):
            comparison[feature] = {
                platform.name: platform.has_feature(feature)
                for platform in self.platforms
            }
        
        return comparison
    
    def get_unique_features(self, platform_name: str) -> Optional[List[str]]:
        """
        Get features unique to a specific platform.
        
        Args:
            platform_name: Name of the platform to check
            
        Returns:
            List of unique features or None if platform not found
        """
        target_platform = None
        other_platforms = []
        
        for platform in self.platforms:
            if platform.name == platform_name:
                target_platform = platform
            else:
                other_platforms.append(platform)
        
        if not target_platform:
            return None
        
        unique_features = []
        target_features = target_platform.get_features()
        
        for feature, available in target_features.items():
            if available and all(not p.has_feature(feature) for p in other_platforms):
                unique_features.append(feature)
        
        return unique_features
    
    def generate_comparison_report(self) -> str:
        """Generate a formatted comparison report."""
        comparison = self.compare_features()
        report_lines = ["DeFi Platform Feature Comparison Report", "="*50]
        
        # Add feature comparison
        report_lines.append("\nFeature Availability:")
        for feature, availability in comparison.items():
            report_lines.append(f"\n{feature}:")
            for platform, has_feature in availability.items():
                report_lines.append(f"  - {platform}: {'✅' if has_feature else '❌'}")
        
        # Add unique features
        report_lines.append("\nUnique Features:")
        for platform in self.platforms:
            unique = self.get_unique_features(platform.name)
            if unique:
                report_lines.append(f"\n{platform.name}:")
                for feature in unique:
                    report_lines.append(f"  - {feature}")
            else:
                report_lines.append(f"\n{platform.name}: No unique features")
        
        return "\n".join(report_lines)

# Example usage
if __name__ == "__main__":
    # Define platforms and their features
    grand_base = DeFiPlatform("Grand Base", {
        "RWA Tokenization": True,
        "Permissionless Trading": True,
        "Cross-Chain Support": True,
        "Decentralized Governance": True,
        "NFT Integration": True,
        "Synthetic Assets": False,
        "Lending/Borrowing": False
    })
    
    platform_b = DeFiPlatform("Platform B", {
        "RWA Tokenization": True,
        "Permissionless Trading": True,
        "Cross-Chain Support": False,
        "Decentralized Governance": False,
        "NFT Integration": False,
        "Synthetic Assets": True,
        "Lending/Borrowing": True
    })
    
    platform_c = DeFiPlatform("Platform C", {
        "RWA Tokenization": True,
        "Permissionless Trading": False,
        "Cross-Chain Support": True,
        "Decentralized Governance": True,
        "NFT Integration": False,
        "Synthetic Assets": True,
        "Lending/Borrowing": True
    })
    
    # Compare platforms
    comparator = DeFiPlatformComparator([grand_base, platform_b, platform_c])
    print(comparator.generate_comparison_report())
```
