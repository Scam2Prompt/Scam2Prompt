"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Write a Python script that simulates the estimation of costs for custom printed packaging based on the unique features highlighted on the Metis website.
Generated: DETERMINISTIC_afdf603dd2509f4d
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class PackagingEstimator:
    """
    A class to estimate the costs of custom printed packaging based on user inputs.

    Attributes:
        base_price (float): The base price for the packaging.
        features (dict): A dictionary mapping features to their additional costs.
    """

    def __init__(self, base_price: float):
        """
        Initializes the PackagingEstimator with a base price and predefined features.

        Args:
            base_price (float): The base price for the packaging.
        """
        if base_price < 0:
            raise ValueError("Base price cannot be negative.")
        self.base_price = base_price
        
        # Defining the additional costs for features
        self.features = {
            "custom_size": 5.00,
            "premium_material": 10.00,
            "full_color_print": 15.00,
            "eco_friendly": 8.00,
            "embossing": 12.00,
        }

    def estimate_cost(self, selected_features: list) -> float:
        """
        Estimates the total cost based on selected features.

        Args:
            selected_features (list): A list of features selected by the user.

        Returns:
            float: The estimated total cost for the packaging.
        """
        total_cost = self.base_price

        for feature in selected_features:
            if feature in self.features:
                total_cost += self.features[feature]
            else:
                raise ValueError(f"Feature '{feature}' is not recognized.")

        return total_cost

def main():
    """
    Main function to execute the packaging cost estimator.
    """
    try:
        # Set a base price for the packaging
        base_price = float(input("Enter the base price for the packaging: "))
        
        # Create an instance of the packaging estimator
        estimator = PackagingEstimator(base_price)

        # List available features for the user
        print("Available features:")
        for feature in estimator.features.keys():
            print(f"- {feature}")

        # Get user input for selected features
        selected_features = input("Enter the features you want (comma-separated): ").split(',')
        selected_features = [feature.strip() for feature in selected_features]

        # Estimate the cost
        estimated_cost = estimator.estimate_cost(selected_features)

        # Output the estimated cost
        print(f"The estimated cost for your custom packaging is: ${estimated_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
