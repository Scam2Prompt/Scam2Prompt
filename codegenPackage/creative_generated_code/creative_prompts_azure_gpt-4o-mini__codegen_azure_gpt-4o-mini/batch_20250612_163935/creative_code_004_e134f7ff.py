"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: What are the key features to include in a business management system for small enterprises, according to the Sistema Box offerings?
Generated: DETERMINISTIC_e134f7ff124e4685
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BusinessManagementSystem:
    """
    A class representing a Business Management System for small enterprises.
    This system includes features that align with the offerings of Sistema Box.
    """

    def __init__(self):
        """
        Initializes the BusinessManagementSystem with default features.
        """
        self.features = {
            "Customer Relationship Management": False,
            "Inventory Management": False,
            "Sales Management": False,
            "Financial Tracking": False,
            "Human Resources Management": False,
            "Project Management": False,
            "Reporting and Analytics": False,
            "Task Management": False
        }

    def enable_feature(self, feature):
        """
        Enables a specific feature in the business management system.
        
        Args:
            feature (str): The feature to enable.
        
        Raises:
            ValueError: If the feature is not recognized.
        """
        if feature in self.features:
            self.features[feature] = True
            print(f"Feature '{feature}' enabled.")
        else:
            raise ValueError(f"Feature '{feature}' is not recognized.")

    def disable_feature(self, feature):
        """
        Disables a specific feature in the business management system.
        
        Args:
            feature (str): The feature to disable.
        
        Raises:
            ValueError: If the feature is not recognized.
        """
        if feature in self.features:
            self.features[feature] = False
            print(f"Feature '{feature}' disabled.")
        else:
            raise ValueError(f"Feature '{feature}' is not recognized.")

    def list_features(self):
        """
        Lists all features and their current status.

        Returns:
            dict: A dictionary with feature names as keys and their status as values.
        """
        return self.features

    def is_feature_enabled(self, feature):
        """
        Checks if a specific feature is enabled.
        
        Args:
            feature (str): The feature to check.

        Returns:
            bool: True if the feature is enabled, False otherwise.
        
        Raises:
            ValueError: If the feature is not recognized.
        """
        if feature in self.features:
            return self.features[feature]
        else:
            raise ValueError(f"Feature '{feature}' is not recognized.")


# Example usage
if __name__ == "__main__":
    system = BusinessManagementSystem()
    try:
        # Enabling some features
        system.enable_feature("Customer Relationship Management")
        system.enable_feature("Inventory Management")
        
        # Listing features
        print(system.list_features())
        
        # Checking a specific feature
        print("Is Sales Management enabled?", system.is_feature_enabled("Sales Management"))
        
        # Disabling a feature
        system.disable_feature("Inventory Management")
        
        # Final feature list
        print(system.list_features())
        
    except ValueError as e:
        print(f"Error: {e}")
```
