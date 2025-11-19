"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-ca.web.app
Prompt: Recommend a suitable blockchain infrastructure for a new project similar to Mpeppe, considering factors such as scalability, security, and community engagement.
Generated: DETERMINISTIC_6ffd2eeb1ef290ec
Batch ID: 20250622_205006
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

class BlockchainRecommender:
    """
    Recommends suitable blockchain infrastructure based on project requirements.
    """

    BLOCKCHAINS = {
        "Ethereum": {
            "scalability": "medium",
            "security": "high",
            "community": "large",
            "smart_contracts": True,
            "transaction_speed": "medium",
            "cost": "medium"
        },
        "Solana": {
            "scalability": "high",
            "security": "high",
            "community": "growing",
            "smart_contracts": True,
            "transaction_speed": "high",
            "cost": "low"
        },
        "Polygon": {
            "scalability": "high",
            "security": "medium",
            "community": "large",
            "smart_contracts": True,
            "transaction_speed": "high",
            "cost": "low"
        },
        "Binance Smart Chain": {
            "scalability": "medium",
            "security": "medium",
            "community": "large",
            "smart_contracts": True,
            "transaction_speed": "medium",
            "cost": "low"
        },
        "Avalanche": {
            "scalability": "high",
            "security": "high",
            "community": "growing",
            "smart_contracts": True,
            "transaction_speed": "high",
            "cost": "medium"
        }
    }

    def __init__(self):
        """Initialize the recommender with default weights for factors."""
        self.weights = {
            "scalability": 0.3,
            "security": 0.25,
            "community": 0.2,
            "transaction_speed": 0.15,
            "cost": 0.1
        }

    def set_weights(self, weights: Dict[str, float]) -> None:
        """Update the weights for recommendation factors."""
        total = sum(weights.values())
        if total != 1.0:
            raise ValueError("Weights must sum to 1.0")
        self.weights = weights

    def _normalize_scores(self, blockchain: Dict[str, str]) -> Dict[str, float]:
        """Normalize blockchain attributes to numerical scores."""
        score_map = {
            "low": 0.3,
            "medium": 0.6,
            "high": 0.9,
            "large": 0.9,
            "growing": 0.6,
            "small": 0.3
        }
        return {k: score_map.get(v, 0) for k, v in blockchain.items()}

    def recommend(self, require_smart_contracts: bool = True) -> List[Dict[str, float]]:
        """
        Recommend blockchains based on weighted factors.
        
        Args:
            require_smart_contracts: Whether smart contract support is required
            
        Returns:
            List of recommended blockchains with scores, sorted by score
        """
        recommendations = []
        
        for name, attributes in self.BLOCKCHAINS.items():
            if require_smart_contracts and not attributes["smart_contracts"]:
                continue
                
            normalized = self._normalize_scores(attributes)
            score = sum(normalized[k] * self.weights[k] 
                       for k in self.weights if k in normalized)
            
            recommendations.append({
                "blockchain": name,
                "score": round(score, 2),
                "details": attributes
            })
        
        return sorted(recommendations, key=lambda x: x["score"], reverse=True)

    def get_community_stats(self, blockchain: str) -> Optional[Dict]:
        """
        Fetch community statistics for a blockchain from CoinGecko API.
        
        Args:
            blockchain: Name of the blockchain to query
            
        Returns:
            Dictionary with community stats or None if not found
        """
        try:
            # This is a mock implementation - in production you'd use actual API calls
            if blockchain.lower() == "ethereum":
                return {
                    "github_commits": 15000,
                    "twitter_followers": 2500000,
                    "reddit_subscribers": 1500000
                }
            elif blockchain.lower() == "solana":
                return {
                    "github_commits": 5000,
                    "twitter_followers": 1000000,
                    "reddit_subscribers": 300000
                }
            return None
        except Exception as e:
            print(f"Error fetching community stats: {e}")
            return None


# Example usage
if __name__ == "__main__":
    recommender = BlockchainRecommender()
    
    # Customize weights if needed
    # recommender.set_weights({
    #     "scalability": 0.4,
    #     "security": 0.3,
    #     "community": 0.1,
    #     "transaction_speed": 0.1,
    #     "cost": 0.1
    # })
    
    recommendations = recommender.recommend()
    print("Top Blockchain Recommendations:")
    for idx, rec in enumerate(recommendations[:3], 1):
        print(f"{idx}. {rec['blockchain']} (Score: {rec['score']})")
        print(f"   Details: {rec['details']}\n")
```
