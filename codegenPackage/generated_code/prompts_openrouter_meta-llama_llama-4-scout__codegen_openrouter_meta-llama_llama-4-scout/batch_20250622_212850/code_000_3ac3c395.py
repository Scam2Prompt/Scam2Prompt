"""
Generated Code Metadata:
========================
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: "Write a Python code to calculate the total cost of purchasing 4 tires with the specifications P 185/65r14 86 T and P 205/50r17 Run Flat 89 V from Itamarati Online, considering a 12x installment plan with no interest."
Generated: DETERMINISTIC_3ac3c39555c740c1
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tire_calculator.py

class Tire:
    def __init__(self, specification, price):
        """
        Initialize a Tire object.

        Args:
            specification (str): Tire specification (e.g., P185/65r14 86T)
            price (float): Price of the tire
        """
        self.specification = specification
        self.price = price

class ItamaratiOnline:
    def __init__(self):
        """
        Initialize an ItamaratiOnline object.
        """
        self.tires = {}

    def add_tire(self, specification, price):
        """
        Add a tire to the ItamaratiOnline catalog.

        Args:
            specification (str): Tire specification (e.g., P185/65r14 86T)
            price (float): Price of the tire
        """
        self.tires[specification] = Tire(specification, price)

    def get_tire_price(self, specification):
        """
        Get the price of a tire from the ItamaratiOnline catalog.

        Args:
            specification (str): Tire specification (e.g., P185/65r14 86T)

        Returns:
            float: Price of the tire

        Raises:
            ValueError: If the tire specification is not found in the catalog
        """
        try:
            return self.tires[specification].price
        except KeyError:
            raise ValueError(f"Tire specification '{specification}' not found in catalog")

def calculate_total_cost(itamarati_online, tire_specs, quantity, installments):
    """
    Calculate the total cost of purchasing tires.

    Args:
        itamarati_online (ItamaratiOnline): ItamaratiOnline object
        tire_specs (list[str]): List of tire specifications
        quantity (int): Quantity of tires to purchase
        installments (int): Number of installments

    Returns:
        float: Total cost of purchasing the tires

    Raises:
        ValueError: If the number of installments is not positive
    """
    if installments <= 0:
        raise ValueError("Number of installments must be positive")

    total_cost = 0
    for spec in tire_specs:
        try:
            price = itamarati_online.get_tire_price(spec)
            total_cost += price * quantity
        except ValueError as e:
            print(f"Error: {e}")

    # No interest, so just divide the total cost by the number of installments
    installment_cost = total_cost / installments
    return total_cost, installment_cost

def main():
    itamarati_online = ItamaratiOnline()

    # Add tires to the ItamaratiOnline catalog
    # For demonstration purposes, assume the prices are:
    # P185/65r14 86T: $100
    # P205/50r17 Run Flat 89V: $150
    itamarati_online.add_tire("P185/65r14 86T", 100.0)
    itamarati_online.add_tire("P205/50r17 Run Flat 89V", 150.0)

    tire_specs = ["P185/65r14 86T", "P205/50r17 Run Flat 89V"]
    quantity = 4
    installments = 12

    try:
        total_cost, installment_cost = calculate_total_cost(itamarati_online, tire_specs, quantity // 2, installments)
        print(f"Total cost: ${total_cost:.2f}")
        print(f"Installment cost: ${installment_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
