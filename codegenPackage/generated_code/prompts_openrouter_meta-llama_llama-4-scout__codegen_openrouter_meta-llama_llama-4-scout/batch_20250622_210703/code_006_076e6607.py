"""
Generated Code Metadata:
========================
Original URL: https://feresplast.com
Prompt: Develop a code snippet to integrate a shipping and handling calculator into an e-commerce platform, considering factors like location and package weight, similar to Feresplast's shipping features.
Generated: DETERMINISTIC_076e66076c39bbdb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shipping_calculator.py

class ShippingCalculator:
    """
    A class used to calculate shipping costs based on location and package weight.

    Attributes:
    ----------
    rates : dict
        A dictionary containing shipping rates per unit of weight for different locations.

    Methods:
    -------
    calculate_shipping(location, weight)
        Calculates the shipping cost based on the location and package weight.
    """

    def __init__(self):
        # Define shipping rates per unit of weight for different locations
        self.rates = {
            'local': 0.05,  # $0.05 per unit of weight for local shipping
            'national': 0.10,  # $0.10 per unit of weight for national shipping
            'international': 0.20  # $0.20 per unit of weight for international shipping
        }

    def calculate_shipping(self, location, weight):
        """
        Calculates the shipping cost based on the location and package weight.

        Parameters:
        ----------
        location : str
            The location of the shipment (local, national, international).
        weight : float
            The weight of the package.

        Returns:
        -------
        float
            The calculated shipping cost.

        Raises:
        ------
        ValueError
            If the location or weight is invalid.
        """

        # Validate location
        if location not in self.rates:
            raise ValueError("Invalid location")

        # Validate weight
        if weight <= 0:
            raise ValueError("Weight must be greater than zero")

        # Calculate shipping cost
        shipping_cost = self.rates[location] * weight

        return shipping_cost


class HandlingCalculator:
    """
    A class used to calculate handling costs based on package weight.

    Attributes:
    ----------
    handling_rates : dict
        A dictionary containing handling rates for different weight ranges.

    Methods:
    -------
    calculate_handling(weight)
        Calculates the handling cost based on the package weight.
    """

    def __init__(self):
        # Define handling rates for different weight ranges
        self.handling_rates = {
            (0, 1): 5.00,  # $5.00 handling for packages weighing 0-1 unit
            (1, 5): 10.00,  # $10.00 handling for packages weighing 1-5 units
            (5, float('inf')): 15.00  # $15.00 handling for packages weighing over 5 units
        }

    def calculate_handling(self, weight):
        """
        Calculates the handling cost based on the package weight.

        Parameters:
        ----------
        weight : float
            The weight of the package.

        Returns:
        -------
        float
            The calculated handling cost.

        Raises:
        ------
        ValueError
            If the weight is invalid.
        """

        # Validate weight
        if weight <= 0:
            raise ValueError("Weight must be greater than zero")

        # Find the applicable handling rate
        handling_cost = next((rate for (low, high), rate in self.handling_rates.items() if low <= weight <= high), None)

        # Raise an error if no applicable handling rate is found
        if handling_cost is None:
            raise ValueError("No handling rate found for the given weight")

        return handling_cost


def main():
    try:
        # Create instances of the shipping and handling calculators
        shipping_calculator = ShippingCalculator()
        handling_calculator = HandlingCalculator()

        # Example usage
        location = 'national'
        weight = 3.0

        shipping_cost = shipping_calculator.calculate_shipping(location, weight)
        handling_cost = handling_calculator.calculate_handling(weight)

        total_cost = shipping_cost + handling_cost

        print(f"Shipping Cost: ${shipping_cost:.2f}")
        print(f"Handling Cost: ${handling_cost:.2f}")
        print(f"Total Cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
