"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m2bob.shop
Prompt: What are the key features of M2Bob that enhance gameplay on servers such as SG and others?
Generated: DETERMINISTIC_e7e9b34db044705e
Batch ID: 20250612_155813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class M2BobFeatures:
    """
    Class to represent the key features of M2Bob that enhance gameplay on servers like SG.
    """

    def __init__(self):
        """Initialize the M2Bob features with default values."""
        self.features = {
            "AutoFarm": True,
            "SpeedHack": True,
            "NoFallDamage": True,
            "AntiCheat": True,
            "ESP": True,
            "Fly": False,
            "AutoClicker": True,
            "CustomMacros": True
        }

    def get_features(self):
        """
        Get the list of features and their status.
        
        Returns:
            dict: A dictionary with feature names as keys and their statuses as values.
        """
        return self.features

    def toggle_feature(self, feature_name):
        """
        Toggle the status of a specific feature.
        
        Args:
            feature_name (str): The name of the feature to toggle.
        
        Raises:
            ValueError: If the feature does not exist.
        """
        if feature_name in self.features:
            self.features[feature_name] = not self.features[feature_name]
        else:
            raise ValueError(f"Feature '{feature_name}' does not exist.")

    def is_feature_enabled(self, feature_name):
        """
        Check if a specific feature is enabled.
        
        Args:
            feature_name (str): The name of the feature to check.
        
        Returns:
            bool: True if the feature is enabled, False otherwise.
        
        Raises:
            ValueError: If the feature does not exist.
        """
        if feature_name in self.features:
            return self.features[feature_name]
        else:
            raise ValueError(f"Feature '{feature_name}' does not exist.")

if __name__ == "__main__":
    # Example usage of the M2BobFeatures class
    try:
        m2bob = M2BobFeatures()
        print("M2Bob Features:", m2bob.get_features())

        # Toggle a feature
        m2bob.toggle_feature("Fly")
        print("Fly feature enabled:", m2bob.is_feature_enabled("Fly"))

        # Attempt to toggle a non-existing feature
        m2bob.toggle_feature("NonExistentFeature")

    except ValueError as e:
        print(f"Error: {e}")
```
