"""
Generated Code Metadata:
========================
Original URL: https://aave-v3.github.io
Prompt: Recommend a suitable blockchain network for integrating Aave's protocol, considering factors such as scalability, security, and community support.
Generated: DETERMINISTIC_ec9314c17f694c89
Batch ID: 20250622_212302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List, Tuple

class BlockchainNetwork:
    """Represents a blockchain network with its attributes."""
    
    def __init__(self, name: str, scalability: float, security: float, 
                 community_support: float, aave_integration: bool):
        """
        Initialize a blockchain network.
        
        Args:
            name: Name of the blockchain network
            scalability: Scalability score (0-1)
            security: Security score (0-1)
            community_support: Community support score (0-1)
            aave_integration: Whether Aave is already integrated
        """
        self.name = name
        self.scalability = scalability
        self.security = security
        self.community_support = community_support
        self.aave_integration = aave_integration
    
    def calculate_score(self, weights: Dict[str, float]) -> float:
        """
        Calculate weighted score based on given weights.
        
        Args:
            weights: Dictionary of weights for each factor
            
        Returns:
            Weighted score
            
        Raises:
            ValueError: If weights don't sum to 1 or contain invalid keys
        """
        if abs(sum(weights.values()) - 1.0) > 0.0001:
            raise ValueError("Weights must sum to 1")
        
        valid_keys = {'scalability', 'security', 'community_support'}
        if not set(weights.keys()).issubset(valid_keys):
            raise ValueError(f"Invalid weight keys. Must be one of {valid_keys}")
            
        score = 0
        for factor, weight in weights.items():
            score += getattr(self, factor) * weight
            
        return score

def recommend_network(networks: List[BlockchainNetwork], 
                     weights: Dict[str, float] = None) -> Tuple[str, float]:
    """
    Recommend the best blockchain network for Aave integration.
    
    Args:
        networks: List of BlockchainNetwork objects to evaluate
        weights: Optional weights for scoring (default: equal weighting)
        
    Returns:
        Tuple of (best_network_name, highest_score)
        
    Raises:
        ValueError: If networks list is empty
    """
    if not networks:
        raise ValueError("No networks provided for evaluation")
    
    # Default weights if not provided
    if weights is None:
        weights = {
            'scalability': 0.4,
            'security': 0.4,
            'community_support': 0.2
        }
    
    # Calculate scores for each network
    scored_networks = []
    for network in networks:
        try:
            score = network.calculate_score(weights)
            scored_networks.append((network.name, score, network.aave_integration))
        except ValueError as e:
            print(f"Error calculating score for {network.name}: {str(e)}")
            continue
    
    if not scored_networks:
        raise ValueError("No valid networks could be scored")
    
    # Sort by score (descending) and prioritize non-integrated networks
    scored_networks.sort(key=lambda x: (-x[1], x[2]))
    
    return scored_networks[0][0], scored_networks[0][1]

# Example usage
if __name__ == "__main__":
    # Sample blockchain networks data
    networks = [
        BlockchainNetwork("Ethereum", 0.7, 0.9, 0.9, True),
        BlockchainNetwork("Polygon", 0.8, 0.8, 0.7, True),
        BlockchainNetwork("Avalanche", 0.85, 0.85, 0.8, True),
        BlockchainNetwork("Arbitrum", 0.9, 0.85, 0.75, False),
        BlockchainNetwork("Optimism", 0.88, 0.82, 0.7, False),
    ]
    
    try:
        best_network, score = recommend_network(networks)
        print(f"Recommended network: {best_network} with score: {score:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")
```
