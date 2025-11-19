"""
Generated Code Metadata:
========================
Original URL: https://gudrus.com
Prompt: Create a function that summarizes the features of the Basic, Medium, and Deep views offered by DeepMarket for user comparison.
Generated: DETERMINISTIC_44ac8b741763475a
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DeepMarketView:
    """
    A class to represent different views offered by DeepMarket.
    """

    def __init__(self, view_type, features):
        """
        Initializes a DeepMarketView instance.

        :param view_type: str - The type of view (Basic, Medium, Deep)
        :param features: list - A list of features associated with the view
        """
        self.view_type = view_type
        self.features = features

    def summarize(self):
        """
        Summarizes the features of the view.

        :return: str - A summary of the view's features
        """
        return f"{self.view_type} View Features: " + ", ".join(self.features)


def get_view_summary(view_type):
    """
    Retrieves the summary of features for the specified view type.

    :param view_type: str - The type of view to summarize (Basic, Medium, Deep)
    :return: str - A summary of the view's features
    :raises ValueError: If the view_type is not recognized
    """
    # Define the features for each view type
    view_features = {
        "Basic": ["Basic analytics", "Limited data access", "Email support"],
        "Medium": ["Advanced analytics", "Full data access", "Priority email support", "Monthly reports"],
        "Deep": ["Comprehensive analytics", "Unlimited data access", "24/7 support", "Custom reports", "API access"]
    }

    # Check if the view_type is valid
    if view_type not in view_features:
        raise ValueError(f"Invalid view type: {view_type}. Must be one of {list(view_features.keys())}.")

    # Create a DeepMarketView instance and return the summary
    view = DeepMarketView(view_type, view_features[view_type])
    return view.summarize()


# Example usage
if __name__ == "__main__":
    try:
        print(get_view_summary("Basic"))
        print(get_view_summary("Medium"))
        print(get_view_summary("Deep"))
        # Uncommenting the following line will raise an error
        # print(get_view_summary("Advanced"))
    except ValueError as e:
        print(f"Error: {e}")
```
