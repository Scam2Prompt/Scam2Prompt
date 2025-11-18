"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renovation-globale-maprimerenov.aides-gouv-fr.info
Prompt: Write code to estimate the increase in property value after energy-efficient renovations, using data points mentioned in the Ma Prime Renov' program (e.g., 15%-25% increase).
Generated: DETERMINISTIC_57684720046f7e66
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class PropertyValueEstimator:
    """
    A class to estimate the increase in property value after energy-efficient renovations.
    """

    def __init__(self, base_property_value: float):
        """
        Initialize the estimator with the base property value.

        :param base_property_value: The original property value before renovations (in euros).
        """
        if base_property_value <= 0:
            raise ValueError("Base property value must be a positive number.")
        self.base_property_value = base_property_value

    def estimate_increase(self, percentage_increase: float) -> float:
        """
        Estimate the new property value after renovations based on the percentage increase.

        :param percentage_increase: Percentage increase in property value (e.g., 15 for 15%).
        :return: The new estimated property value after renovations (in euros).
        """
        if not (0 <= percentage_increase <= 100):
            raise ValueError("Percentage increase must be between 0 and 100.")
        return self.base_property_value * (1 + percentage_increase / 100)

    def estimate_range(self, min_percentage: float, max_percentage: float) -> dict:
        """
        Estimate the range of possible new property values based on a range of percentage increases.

        :param min_percentage: Minimum percentage increase in property value (e.g., 15 for 15%).
        :param max_percentage: Maximum percentage increase in property value (e.g., 25 for 25%).
        :return: A dictionary with the minimum and maximum estimated property values.
        """
        if min_percentage > max_percentage:
            raise ValueError("Minimum percentage increase cannot be greater than maximum percentage increase.")

        min_value = self.estimate_increase(min_percentage)
        max_value = self.estimate_increase(max_percentage)

        return {"min_value": min_value, "max_value": max_value}


def main():
    """
    Main function to interact with the PropertyValueEstimator and demonstrate its usage.
    """
    try:
        # Example data points from Ma Prime Renov' program
        base_value = float(input("Enter the current property value in euros: "))
        min_percentage = 15  # Example minimum increase percentage
        max_percentage = 25  # Example maximum increase percentage

        # Create an instance of PropertyValueEstimator
        estimator = PropertyValueEstimator(base_property_value=base_value)

        # Estimate the increase range
        range_estimation = estimator.estimate_range(min_percentage, max_percentage)

        # Output the results in JSON format
        print("Estimated property value range after renovations:")
        print(json.dumps(range_estimation, indent=4))

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
