"""
Generated Code Metadata:
========================
Original URL: https://www.napatablets.com
Prompt: Compare the costs and features of the store systems app and Delivery Tracker for auto parts stores.
Generated: DETERMINISTIC_338e4b1e9baf0711
Batch ID: 20250622_212323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class AppComparison:
    """
    A class to compare costs and features of two apps: Store Systems App and Delivery Tracker.
    """

    def __init__(self):
        """
        Initializes the comparison data for the two apps.
        """
        self.apps_data = {
            "Store Systems App": {
                "cost": 49.99,  # Monthly subscription cost in USD
                "features": [
                    "Inventory management",
                    "Sales tracking",
                    "Customer database",
                    "Reporting tools"
                ]
            },
            "Delivery Tracker": {
                "cost": 29.99,  # Monthly subscription cost in USD
                "features": [
                    "Delivery scheduling",
                    "Real-time tracking",
                    "Driver management",
                    "Customer notifications"
                ]
            }
        }

    def compare_costs(self):
        """
        Compares the costs of the two apps.

        Returns:
            str: A message indicating which app is cheaper or if they have the same cost.
        """
        store_app_cost = self.apps_data["Store Systems App"]["cost"]
        delivery_tracker_cost = self.apps_data["Delivery Tracker"]["cost"]

        if store_app_cost < delivery_tracker_cost:
            return "Store Systems App is cheaper at ${:.2f} per month.".format(store_app_cost)
        elif delivery_tracker_cost < store_app_cost:
            return "Delivery Tracker is cheaper at ${:.2f} per month.".format(delivery_tracker_cost)
        else:
            return "Both apps cost the same at ${:.2f} per month.".format(store_app_cost)

    def compare_features(self):
        """
        Compares the features of the two apps.

        Returns:
            dict: A dictionary containing the unique and common features of both apps.
        """
        store_app_features = set(self.apps_data["Store Systems App"]["features"])
        delivery_tracker_features = set(self.apps_data["Delivery Tracker"]["features"])

        common_features = store_app_features.intersection(delivery_tracker_features)
        store_app_unique = store_app_features - delivery_tracker_features
        delivery_tracker_unique = delivery_tracker_features - store_app_features

        return {
            "common_features": list(common_features),
            "store_app_unique_features": list(store_app_unique),
            "delivery_tracker_unique_features": list(delivery_tracker_unique)
        }

    def display_comparison(self):
        """
        Displays the comparison results for costs and features.
        """
        try:
            # Compare costs
            cost_comparison = self.compare_costs()
            print("Cost Comparison:")
            print(cost_comparison)

            # Compare features
            feature_comparison = self.compare_features()
            print("\nFeature Comparison:")
            print("Common Features:")
            for feature in feature_comparison["common_features"]:
                print(f"- {feature}")

            print("\nStore Systems App Unique Features:")
            for feature in feature_comparison["store_app_unique_features"]:
                print(f"- {feature}")

            print("\nDelivery Tracker Unique Features:")
            for feature in feature_comparison["delivery_tracker_unique_features"]:
                print(f"- {feature}")

        except Exception as e:
            print(f"An error occurred during comparison: {e}")


if __name__ == "__main__":
    # Instantiate the comparison class
    comparison_tool = AppComparison()

    # Display the comparison results
    comparison_tool.display_comparison()
```
