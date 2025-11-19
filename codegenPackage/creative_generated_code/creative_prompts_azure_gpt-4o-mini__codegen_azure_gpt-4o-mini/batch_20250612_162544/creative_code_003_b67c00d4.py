"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aydinspirate.com
Prompt: Create a function that calculates the total cost for a customer ordering multiple types of window treatments, including options for printed and motorized blinds.
Generated: DETERMINISTIC_b67c00d44e38392d
Batch ID: 20250612_162544
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WindowTreatment:
    """
    Class to represent a window treatment product.
    """

    def __init__(self, name: str, base_price: float, is_motorized: bool = False):
        """
        Initializes a new window treatment product.

        :param name: The name of the window treatment.
        :param base_price: The base price of the window treatment.
        :param is_motorized: Flag indicating if the product is motorized.
        """
        self.name = name
        self.base_price = base_price
        self.is_motorized = is_motorized

    def get_cost(self) -> float:
        """
        Returns the total cost of the window treatment, including motorization cost if applicable.

        :return: The total cost of the window treatment.
        """
        motorized_cost = 100.0 if self.is_motorized else 0.0
        return self.base_price + motorized_cost


class Order:
    """
    Class to represent a customer's order of window treatments.
    """

    def __init__(self):
        """
        Initializes a new order with an empty list of window treatments.
        """
        self.window_treatments = []

    def add_window_treatment(self, treatment: WindowTreatment):
        """
        Adds a window treatment to the order.

        :param treatment: The window treatment to be added.
        """
        if not isinstance(treatment, WindowTreatment):
            raise ValueError("Invalid window treatment object.")
        self.window_treatments.append(treatment)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of all window treatments in the order.

        :return: The total cost of the order.
        """
        total_cost = sum(treatment.get_cost() for treatment in self.window_treatments)
        return total_cost


def main():
    """
    Main function to demonstrate the window treatment ordering system.
    """
    try:
        # Create an order
        order = Order()

        # Create window treatments
        blinds = WindowTreatment("Printed Blinds", 50.0)
        motorized_blinds = WindowTreatment("Motorized Blinds", 70.0, is_motorized=True)

        # Add window treatments to the order
        order.add_window_treatment(blinds)
        order.add_window_treatment(motorized_blinds)

        # Calculate the total cost
        total_cost = order.calculate_total_cost()

        print(f"Total cost of the order: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
