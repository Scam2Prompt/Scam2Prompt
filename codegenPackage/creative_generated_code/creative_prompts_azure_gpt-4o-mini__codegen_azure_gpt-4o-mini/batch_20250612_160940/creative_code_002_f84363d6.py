"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6873801772-3yp.pages.dev
Prompt: What are the key features of CCleaner that contribute to making a computer faster and more secure?
Generated: DETERMINISTIC_f84363d6e6fe998e
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CCleaner:
    """
    A class representing the key features of CCleaner that contribute to making a computer faster and more secure.
    """

    def __init__(self):
        """
        Initializes the CCleaner with default feature values.
        """
        self.features = {
            "Junk File Cleaner": False,
            "Registry Cleaner": False,
            "Startup Manager": False,
            "Uninstall Manager": False,
            "Browser Cleaner": False,
            "Privacy Protector": False,
            "Disk Analyzer": False,
            "System Restore": False,
        }

    def enable_feature(self, feature):
        """
        Enables a feature of CCleaner.

        Args:
            feature (str): The name of the feature to enable.

        Raises:
            ValueError: If the feature is not recognized.
        """
        if feature in self.features:
            self.features[feature] = True
            print(f"{feature} has been enabled.")
        else:
            raise ValueError(f"Feature '{feature}' is not recognized.")

    def disable_feature(self, feature):
        """
        Disables a feature of CCleaner.

        Args:
            feature (str): The name of the feature to disable.

        Raises:
            ValueError: If the feature is not recognized.
        """
        if feature in self.features:
            self.features[feature] = False
            print(f"{feature} has been disabled.")
        else:
            raise ValueError(f"Feature '{feature}' is not recognized.")

    def list_features(self):
        """
        Lists all features of CCleaner with their current status.

        Returns:
            dict: A dictionary with feature names and their statuses (enabled/disabled).
        """
        return self.features

    def clean_system(self):
        """
        Runs the cleaning process based on enabled features.
        
        Raises:
            RuntimeError: If no cleaning features are enabled.
        """
        active_features = [feature for feature, enabled in self.features.items() if enabled]
        
        if not active_features:
            raise RuntimeError("No cleaning features are enabled. Please enable at least one feature.")
        
        print("Starting system cleaning with the following features enabled:")
        for feature in active_features:
            print(f"- {feature}")
        # Simulate cleaning process
        print("Cleaning process completed successfully.")

# Example usage:
if __name__ == "__main__":
    try:
        ccleaner = CCleaner()
        ccleaner.enable_feature("Junk File Cleaner")
        ccleaner.enable_feature("Registry Cleaner")
        ccleaner.clean_system()
        print(ccleaner.list_features())
    except (ValueError, RuntimeError) as e:
        print(f"Error: {e}")
```
