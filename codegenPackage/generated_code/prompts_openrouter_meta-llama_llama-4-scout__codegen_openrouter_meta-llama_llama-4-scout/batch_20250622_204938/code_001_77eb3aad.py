"""
Generated Code Metadata:
========================
Original URL: https://sonic-labs.vercel.app
Prompt: "Recommend a suitable blockchain platform for a decentralized application that requires high scalability, low latency, and EVM compatibility, considering Sonic's features."
Generated: DETERMINISTIC_77eb3aad6891505a
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blockchain_recommender.py

from enum import Enum

class BlockchainPlatform(Enum):
    """Enum for blockchain platforms."""
    POLYGON = "Polygon"
    BSC = "Binance Smart Chain"
    AVALANCHE = "Avalanche"
    SONIC = "Sonic"

class BlockchainFeatures:
    """Class to hold blockchain features."""
    def __init__(self, platform, scalability, latency, evm_compatibility):
        """
        Initialize blockchain features.

        Args:
        - platform (BlockchainPlatform): The blockchain platform.
        - scalability (str): The scalability of the platform.
        - latency (str): The latency of the platform.
        - evm_compatibility (bool): Whether the platform is EVM compatible.
        """
        self.platform = platform
        self.scalability = scalability
        self.latency = latency
        self.evm_compatibility = evm_compatibility

def get_blockchain_features(platform):
    """
    Get features of a blockchain platform.

    Args:
    - platform (BlockchainPlatform): The blockchain platform.

    Returns:
    - BlockchainFeatures: The features of the blockchain platform.
    """
    features = {
        BlockchainPlatform.POLYGON: BlockchainFeatures(
            BlockchainPlatform.POLYGON, 
            "High", 
            "Low", 
            True
        ),
        BlockchainPlatform.BSC: BlockchainFeatures(
            BlockchainPlatform.BSC, 
            "High", 
            "Low", 
            True
        ),
        BlockchainPlatform.AVALANCHE: BlockchainFeatures(
            BlockchainPlatform.AVALANCHE, 
            "High", 
            "Low", 
            True
        ),
        BlockchainPlatform.SONIC: BlockchainFeatures(
            BlockchainPlatform.SONIC, 
            "Very High", 
            "Very Low", 
            True
        ),
    }
    return features.get(platform, None)

def recommend_blockchain_platform(scalability_requirement, latency_requirement, evm_compatibility_requirement):
    """
    Recommend a suitable blockchain platform.

    Args:
    - scalability_requirement (str): The required scalability.
    - latency_requirement (str): The required latency.
    - evm_compatibility_requirement (bool): Whether EVM compatibility is required.

    Returns:
    - BlockchainPlatform: The recommended blockchain platform.
    """
    platforms = [
        BlockchainPlatform.SONIC,
        BlockchainPlatform.POLYGON,
        BlockchainPlatform.BSC,
        BlockchainPlatform.AVALANCHE,
    ]

    recommended_platform = None
    best_match = 0

    for platform in platforms:
        features = get_blockchain_features(platform)
        if features:
            match = 0
            if features.scalability == scalability_requirement:
                match += 1
            if features.latency == latency_requirement:
                match += 1
            if features.evm_compatibility == evm_compatibility_requirement:
                match += 1

            if match > best_match:
                best_match = match
                recommended_platform = platform

    return recommended_platform

def main():
    try:
        scalability_requirement = "Very High"
        latency_requirement = "Very Low"
        evm_compatibility_requirement = True

        recommended_platform = recommend_blockchain_platform(
            scalability_requirement, 
            latency_requirement, 
            evm_compatibility_requirement
        )

        if recommended_platform:
            print(f"Recommended blockchain platform: {recommended_platform.value}")
        else:
            print("No matching blockchain platform found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
