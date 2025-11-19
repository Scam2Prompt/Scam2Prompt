"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Recommend a suitable blockchain platform for building a decentralized social media/martech platform that rewards users for digital engagement and contributes to environmental conservation.
Generated: DETERMINISTIC_8ddd2e777acda824
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_platform_recommender.py

from enum import Enum, auto
from typing import List, Dict, Optional

class BlockchainPlatform(Enum):
    """Enum representing different blockchain platforms."""
    ETHEREUM = auto()
    POLKADOT = auto()
    SOLANA = auto()
    ALGORAND = auto()
    TEZOS = auto()
    FLOW = auto()
    HEDERA = auto()
    NEAR = auto()

class PlatformCriteria(Enum):
    """Enum representing evaluation criteria for blockchain platforms."""
    SCALABILITY = auto()
    TRANSACTION_SPEED = auto()
    ENERGY_EFFICIENCY = auto()
    SMART_CONTRACT_SUPPORT = auto()
    COMMUNITY_ECOSYSTEM = auto()
    INTEROPERABILITY = auto()
    TRANSACTION_COSTS = auto()

class BlockchainPlatformRecommender:
    """Recommends suitable blockchain platforms based on specified requirements."""
    
    def __init__(self):
        self.platform_scores = {
            BlockchainPlatform.ETHEREUM: {
                PlatformCriteria.SCALABILITY: 3,
                PlatformCriteria.TRANSACTION_SPEED: 2,
                PlatformCriteria.ENERGY_EFFICIENCY: 1,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 5,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 5,
                PlatformCriteria.INTEROPERABILITY: 3,
                PlatformCriteria.TRANSACTION_COSTS: 2
            },
            BlockchainPlatform.POLKADOT: {
                PlatformCriteria.SCALABILITY: 5,
                PlatformCriteria.TRANSACTION_SPEED: 4,
                PlatformCriteria.ENERGY_EFFICIENCY: 4,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 4,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 4,
                PlatformCriteria.INTEROPERABILITY: 5,
                PlatformCriteria.TRANSACTION_COSTS: 3
            },
            BlockchainPlatform.SOLANA: {
                PlatformCriteria.SCALABILITY: 5,
                PlatformCriteria.TRANSACTION_SPEED: 5,
                PlatformCriteria.ENERGY_EFFICIENCY: 3,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 4,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 3,
                PlatformCriteria.INTEROPERABILITY: 2,
                PlatformCriteria.TRANSACTION_COSTS: 4
            },
            BlockchainPlatform.ALGORAND: {
                PlatformCriteria.SCALABILITY: 4,
                PlatformCriteria.TRANSACTION_SPEED: 4,
                PlatformCriteria.ENERGY_EFFICIENCY: 5,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 4,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 3,
                PlatformCriteria.INTEROPERABILITY: 3,
                PlatformCriteria.TRANSACTION_COSTS: 4
            },
            BlockchainPlatform.TEZOS: {
                PlatformCriteria.SCALABILITY: 3,
                PlatformCriteria.TRANSACTION_SPEED: 3,
                PlatformCriteria.ENERGY_EFFICIENCY: 4,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 4,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 3,
                PlatformCriteria.INTEROPERABILITY: 3,
                PlatformCriteria.TRANSACTION_COSTS: 3
            },
            BlockchainPlatform.FLOW: {
                PlatformCriteria.SCALABILITY: 4,
                PlatformCriteria.TRANSACTION_SPEED: 4,
                PlatformCriteria.ENERGY_EFFICIENCY: 4,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 4,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 3,
                PlatformCriteria.INTEROPERABILITY: 2,
                PlatformCriteria.TRANSACTION_COSTS: 3
            },
            BlockchainPlatform.HEDERA: {
                PlatformCriteria.SCALABILITY: 5,
                PlatformCriteria.TRANSACTION_SPEED: 5,
                PlatformCriteria.ENERGY_EFFICIENCY: 5,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 4,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 3,
                PlatformCriteria.INTEROPERABILITY: 3,
                PlatformCriteria.TRANSACTION_COSTS: 5
            },
            BlockchainPlatform.NEAR: {
                PlatformCriteria.SCALABILITY: 4,
                PlatformCriteria.TRANSACTION_SPEED: 4,
                PlatformCriteria.ENERGY_EFFICIENCY: 4,
                PlatformCriteria.SMART_CONTRACT_SUPPORT: 4,
                PlatformCriteria.COMMUNITY_ECOSYSTEM: 3,
                PlatformCriteria.INTEROPERABILITY: 3,
                PlatformCriteria.TRANSACTION_COSTS: 4
            }
        }
        
        # Weightings for a social media/martech platform with environmental focus
        self.criteria_weights = {
            PlatformCriteria.SCALABILITY: 0.2,
            PlatformCriteria.TRANSACTION_SPEED: 0.15,
            PlatformCriteria.ENERGY_EFFICIENCY: 0.25,
            PlatformCriteria.SMART_CONTRACT_SUPPORT: 0.15,
            PlatformCriteria.COMMUNITY_ECOSYSTEM: 0.1,
            PlatformCriteria.INTEROPERABILITY: 0.1,
            PlatformCriteria.TRANSACTION_COSTS: 0.05
        }
    
    def recommend_platforms(self, top_n: int = 3) -> List[Dict]:
        """
        Recommends the top blockchain platforms based on weighted criteria.
        
        Args:
            top_n: Number of top platforms to return (default: 3)
            
        Returns:
            List of dictionaries containing platform and score, sorted by score
        """
        if not isinstance(top_n, int) or top_n <= 0:
            raise ValueError("top_n must be a positive integer")
            
        platform_scores = []
        
        for platform, criteria_scores in self.platform_scores.items():
            total_score = 0.0
            for criteria, weight in self.criteria_weights.items():
                total_score += criteria_scores[criteria] * weight
            
            platform_scores.append({
                "platform": platform.name,
                "score": round(total_score, 2)
            })
        
        # Sort by score in descending order
        platform_scores.sort(key=lambda x: x["score"], reverse=True)
        
        return platform_scores[:top_n]

if __name__ == "__main__":
    try:
        recommender = BlockchainPlatformRecommender()
        recommendations = recommender.recommend_platforms()
        
        print("Top Recommended Blockchain Platforms:")
        for idx, rec in enumerate(recommendations, 1):
            print(f"{idx}. {rec['platform']} (Score: {rec['score']})")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
