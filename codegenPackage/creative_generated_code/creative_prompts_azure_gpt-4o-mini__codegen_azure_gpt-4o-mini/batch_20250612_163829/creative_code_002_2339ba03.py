"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somnial.pages.dev
Prompt: What are the key features of the Somnia® blockchain that enable seamless NFT integration across different virtual worlds?
Generated: DETERMINISTIC_2339ba035a4cd4a4
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SomniaBlockchain:
    """
    A class to represent the key features of the Somnia® blockchain 
    that enable seamless NFT integration across different virtual worlds.
    """

    def __init__(self):
        """
        Initializes the SomniaBlockchain with default feature set.
        """
        self.features = {
            "Interoperability": True,
            "Scalability": True,
            "Low Latency": True,
            "Smart Contracts": True,
            "Decentralized Governance": True,
            "Cross-Chain Compatibility": True,
        }

    def check_feature(self, feature_name):
        """
        Checks if a given feature is supported by the Somnia blockchain.

        Args:
            feature_name (str): The name of the feature to check.

        Returns:
            bool: True if the feature is supported, False otherwise.
        """
        return self.features.get(feature_name, False)

    def list_features(self):
        """
        Lists all the features of the Somnia blockchain.

        Returns:
            dict: A dictionary of features and their support status.
        """
        return self.features

# Error handling example usage
if __name__ == "__main__":
    try:
        somnia = SomniaBlockchain()

        # Display all features of the Somnia blockchain
        print("Somnia Blockchain Features:")
        for feature, supported in somnia.list_features().items():
            status = "Supported" if supported else "Not Supported"
            print(f"- {feature}: {status}")

        # Check specific feature
        feature_to_check = "Interoperability"
        if somnia.check_feature(feature_to_check):
            print(f"{feature_to_check} is supported.")
        else:
            print(f"{feature_to_check} is not supported.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
