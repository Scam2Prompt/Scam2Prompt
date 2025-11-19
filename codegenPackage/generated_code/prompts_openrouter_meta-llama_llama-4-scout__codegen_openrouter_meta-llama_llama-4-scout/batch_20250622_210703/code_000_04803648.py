"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: "Write a Python code to compare prices of different Gree ducted split models, such as GU36T/AK and GKH36T, considering their BTU and inverter features."
Generated: DETERMINISTIC_04803648949011ce
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gree_ducted_split_comparator.py

class GreeDuctedSplit:
    """Represents a Gree ducted split model."""

    def __init__(self, model, btu, inverter, price):
        """
        Initializes a Gree ducted split model.

        Args:
            model (str): The model number of the Gree ducted split.
            btu (int): The BTU rating of the Gree ducted split.
            inverter (bool): Whether the Gree ducted split has an inverter feature.
            price (float): The price of the Gree ducted split.
        """
        self.model = model
        self.btu = btu
        self.inverter = inverter
        self.price = price

    def __str__(self):
        """Returns a string representation of the Gree ducted split model."""
        inverter_feature = "Yes" if self.inverter else "No"
        return f"Model: {self.model}, BTU: {self.btu}, Inverter: {inverter_feature}, Price: ${self.price:.2f}"


class GreeDuctedSplitComparator:
    """Compares prices of different Gree ducted split models."""

    def __init__(self):
        """Initializes a Gree ducted split comparator."""
        self.models = []

    def add_model(self, model):
        """
        Adds a Gree ducted split model to the comparator.

        Args:
            model (GreeDuctedSplit): The Gree ducted split model to add.
        """
        self.models.append(model)

    def compare_prices(self):
        """
        Compares prices of the Gree ducted split models.

        Returns:
            list: A list of Gree ducted split models sorted by price.
        """
        try:
            # Sort the models by price
            sorted_models = sorted(self.models, key=lambda x: x.price)
            return sorted_models
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def compare_by_btu_and_inverter(self):
        """
        Compares prices of the Gree ducted split models considering their BTU and inverter features.

        Returns:
            dict: A dictionary with BTU and inverter feature as keys and a list of corresponding models and prices as values.
        """
        try:
            # Group the models by BTU and inverter feature
            models_grouped = {}
            for model in self.models:
                btu_key = model.btu
                inverter_key = "Inverter" if model.inverter else "Non-Inverter"
                if btu_key not in models_grouped:
                    models_grouped[btu_key] = {}
                if inverter_key not in models_grouped[btu_key]:
                    models_grouped[btu_key][inverter_key] = []
                models_grouped[btu_key][inverter_key].append((model.model, model.price))
            return models_grouped
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}


def main():
    # Create Gree ducted split models
    model1 = GreeDuctedSplit("GU36T/AK", 36000, True, 1200.0)
    model2 = GreeDuctedSplit("GKH36T", 36000, False, 900.0)
    model3 = GreeDuctedSplit("GU48T/AK", 48000, True, 1800.0)
    model4 = GreeDuctedSplit("GKH48T", 48000, False, 1400.0)

    # Create a comparator and add models
    comparator = GreeDuctedSplitComparator()
    comparator.add_model(model1)
    comparator.add_model(model2)
    comparator.add_model(model3)
    comparator.add_model(model4)

    # Compare prices
    print("Price Comparison:")
    for model in comparator.compare_prices():
        print(model)

    # Compare prices considering BTU and inverter features
    print("\nComparison by BTU and Inverter:")
    comparison_result = comparator.compare_by_btu_and_inverter()
    for btu, inverter_models in comparison_result.items():
        print(f"BTU: {btu}")
        for inverter, models in inverter_models.items():
            print(f"  {inverter}:")
            for model, price in models:
                print(f"    {model}: ${price:.2f}")


if __name__ == "__main__":
    main()
```
