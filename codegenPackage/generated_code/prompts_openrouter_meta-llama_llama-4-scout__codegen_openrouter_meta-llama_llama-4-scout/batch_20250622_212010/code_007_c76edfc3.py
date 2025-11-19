"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Write a code snippet to calculate the cost-effectiveness of using nano masterbatches versus traditional masterbatches for a specific industrial application."
Generated: DETERMINISTIC_c76edfc3e7685f1c
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# masterbatch_cost_effectiveness.py

class Masterbatch:
    """Base class for masterbatches."""

    def __init__(self, name, price_per_kg, usage_per_unit):
        """
        Initialize a masterbatch.

        Args:
            name (str): Name of the masterbatch.
            price_per_kg (float): Price per kilogram of the masterbatch.
            usage_per_unit (float): Usage per unit of the final product.
        """
        self.name = name
        self.price_per_kg = price_per_kg
        self.usage_per_unit = usage_per_unit


class NanoMasterbatch(Masterbatch):
    """Class for nano masterbatches."""

    def __init__(self, name, price_per_kg, usage_per_unit, efficiency_factor):
        """
        Initialize a nano masterbatch.

        Args:
            name (str): Name of the nano masterbatch.
            price_per_kg (float): Price per kilogram of the nano masterbatch.
            usage_per_unit (float): Usage per unit of the final product.
            efficiency_factor (float): Efficiency factor of the nano masterbatch.
        """
        super().__init__(name, price_per_kg, usage_per_unit)
        self.efficiency_factor = efficiency_factor


class TraditionalMasterbatch(Masterbatch):
    """Class for traditional masterbatches."""

    def __init__(self, name, price_per_kg, usage_per_unit):
        """
        Initialize a traditional masterbatch.

        Args:
            name (str): Name of the traditional masterbatch.
            price_per_kg (float): Price per kilogram of the traditional masterbatch.
            usage_per_unit (float): Usage per unit of the final product.
        """
        super().__init__(name, price_per_kg, usage_per_unit)


def calculate_cost_effectiveness(nano_masterbatch, traditional_masterbatch, units_produced):
    """
    Calculate the cost-effectiveness of using nano masterbatches versus traditional masterbatches.

    Args:
        nano_masterbatch (NanoMasterbatch): Nano masterbatch to compare.
        traditional_masterbatch (TraditionalMasterbatch): Traditional masterbatch to compare.
        units_produced (int): Number of units produced.

    Returns:
        dict: Dictionary containing the cost-effectiveness results.
    """
    try:
        # Calculate total usage for nano and traditional masterbatches
        nano_total_usage = nano_masterbatch.usage_per_unit * units_produced
        traditional_total_usage = traditional_masterbatch.usage_per_unit * units_produced

        # Calculate total cost for nano and traditional masterbatches
        nano_total_cost = nano_total_usage * nano_masterbatch.price_per_kg / nano_masterbatch.efficiency_factor
        traditional_total_cost = traditional_total_usage * traditional_masterbatch.price_per_kg

        # Calculate cost savings
        cost_savings = traditional_total_cost - nano_total_cost

        # Calculate percentage cost savings
        if traditional_total_cost == 0:
            percentage_cost_savings = 0
        else:
            percentage_cost_savings = (cost_savings / traditional_total_cost) * 100

        # Return results as a dictionary
        return {
            "nano_masterbatch_cost": nano_total_cost,
            "traditional_masterbatch_cost": traditional_masterbatch_cost,
            "cost_savings": cost_savings,
            "percentage_cost_savings": percentage_cost_savings,
        }

    except ZeroDivisionError:
        print("Error: Division by zero occurred.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Example usage
    nano_masterbatch = NanoMasterbatch("Nano Masterbatch", 5.0, 0.1, 2.0)
    traditional_masterbatch = TraditionalMasterbatch("Traditional Masterbatch", 3.0, 0.2)
    units_produced = 10000

    results = calculate_cost_effectiveness(nano_masterbatch, traditional_masterbatch, units_produced)

    if results:
        print("Cost-Effectiveness Results:")
        print(f"Nano Masterbatch Cost: ${results['nano_masterbatch_cost']:.2f}")
        print(f"Traditional Masterbatch Cost: ${results['traditional_masterbatch_cost']:.2f}")
        print(f"Cost Savings: ${results['cost_savings']:.2f}")
        print(f"Percentage Cost Savings: {results['percentage_cost_savings']:.2f}%")


if __name__ == "__main__":
    main()
```
