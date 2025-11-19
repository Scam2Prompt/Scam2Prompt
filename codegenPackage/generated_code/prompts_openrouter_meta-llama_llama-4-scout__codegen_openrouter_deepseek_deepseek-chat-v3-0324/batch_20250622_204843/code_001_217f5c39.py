"""
Generated Code Metadata:
========================
Original URL: https://ipblockchain.pages.dev
Prompt: "Compare the features of Story's blockchain-based IP tokenization platform with other similar platforms, focusing on application ecosystem and IPFi use cases."
Generated: DETERMINISTIC_217f5c39dad8c00d
Batch ID: 20250622_204843
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
from dataclasses import dataclass
from enum import Enum

class PlatformCategory(Enum):
    """Categories for blockchain platforms."""
    IP_TOKENIZATION = "IP Tokenization"
    APPLICATION_ECOSYSTEM = "Application Ecosystem"
    IPFI = "IPFi Use Cases"

@dataclass
class PlatformFeature:
    """Represents a feature of a blockchain platform."""
    name: str
    description: str
    category: PlatformCategory

@dataclass
class BlockchainPlatform:
    """Represents a blockchain platform with its features."""
    name: str
    features: List[PlatformFeature]

class PlatformComparator:
    """Compares features of blockchain platforms."""
    
    def __init__(self):
        self.platforms: Dict[str, BlockchainPlatform] = {}
    
    def add_platform(self, platform: BlockchainPlatform) -> None:
        """Add a platform to the comparator."""
        self.platforms[platform.name] = platform
    
    def compare_features(self, platform1: str, platform2: str, category: Optional[PlatformCategory] = None) -> Dict:
        """
        Compare features between two platforms.
        
        Args:
            platform1: Name of first platform
            platform2: Name of second platform
            category: Optional category to filter by
            
        Returns:
            Dictionary with comparison results
            
        Raises:
            ValueError: If platform names are invalid
        """
        if platform1 not in self.platforms or platform2 not in self.platforms:
            raise ValueError("One or both platform names are invalid")
            
        p1 = self.platforms[platform1]
        p2 = self.platforms[platform2]
        
        comparison = {
            "platform1": p1.name,
            "platform2": p2.name,
            "comparisons": []
        }
        
        # Get all features if no category specified
        features1 = [f for f in p1.features if category is None or f.category == category]
        features2 = [f for f in p2.features if category is None or f.category == category]
        
        # Find common features
        common_features = set(f.name for f in features1) & set(f.name for f in features2)
        
        # Find unique features
        unique_to_p1 = set(f.name for f in features1) - common_features
        unique_to_p2 = set(f.name for f in features2) - common_features
        
        # Build comparison results
        for feature_name in common_features:
            desc1 = next(f.description for f in features1 if f.name == feature_name)
            desc2 = next(f.description for f in features2 if f.name == feature_name)
            comparison["comparisons"].append({
                "feature": feature_name,
                platform1: desc1,
                platform2: desc2,
                "status": "common"
            })
            
        for feature_name in unique_to_p1:
            desc = next(f.description for f in features1 if f.name == feature_name)
            comparison["comparisons"].append({
                "feature": feature_name,
                platform1: desc,
                platform2: "Not available",
                "status": "unique"
            })
            
        for feature_name in unique_to_p2:
            desc = next(f.description for f in features2 if f.name == feature_name)
            comparison["comparisons"].append({
                "feature": feature_name,
                platform1: "Not available",
                platform2: desc,
                "status": "unique"
            })
            
        return comparison

def initialize_comparator() -> PlatformComparator:
    """Initialize comparator with sample data for Story and other platforms."""
    comparator = PlatformComparator()
    
    # Story platform features
    story_features = [
        PlatformFeature(
            "NFT-based IP Tokenization",
            "Uses NFTs to represent ownership of intellectual property",
            PlatformCategory.IP_TOKENIZATION
        ),
        PlatformFeature(
            "Royalty Automation",
            "Automatic royalty distribution through smart contracts",
            PlatformCategory.IPFI
        ),
        PlatformFeature(
            "Developer SDK",
            "Comprehensive SDK for building IP-related applications",
            PlatformCategory.APPLICATION_ECOSYSTEM
        ),
        PlatformFeature(
            "IP Marketplace",
            "Built-in marketplace for buying/selling tokenized IP",
            PlatformCategory.APPLICATION_ECOSYSTEM
        )
    ]
    
    # Competitor platform features
    competitor_features = [
        PlatformFeature(
            "ERC-721 IP Tokens",
            "Standard ERC-721 tokens for IP representation",
            PlatformCategory.IP_TOKENIZATION
        ),
        PlatformFeature(
            "Manual Royalty Distribution",
            "Requires manual intervention for royalty payments",
            PlatformCategory.IPFI
        ),
        PlatformFeature(
            "API Access",
            "Basic API for IP-related services",
            PlatformCategory.APPLICATION_ECOSYSTEM
        )
    ]
    
    comparator.add_platform(BlockchainPlatform("Story", story_features))
    comparator.add_platform(BlockchainPlatform("Competitor", competitor_features))
    
    return comparator

def main():
    """Demonstrate platform comparison."""
    try:
        comparator = initialize_comparator()
        
        # Compare all features
        full_comparison = comparator.compare_features("Story", "Competitor")
        print("Full comparison:")
        print(full_comparison)
        
        # Compare IPFi features only
        ipfi_comparison = comparator.compare_features(
            "Story", 
            "Competitor", 
            PlatformCategory.IPFI
        )
        print("\nIPFi comparison:")
        print(ipfi_comparison)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
