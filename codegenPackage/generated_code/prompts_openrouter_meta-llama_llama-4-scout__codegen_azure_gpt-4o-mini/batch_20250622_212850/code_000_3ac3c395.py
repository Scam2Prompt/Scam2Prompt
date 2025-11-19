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
class Tire:
    """
    A class to represent a tire with its specifications and price.
    """

    def __init__(self, specification: str, price: float):
        """
        Initializes a Tire instance.

        :param specification: The specification of the tire (e.g., 'P 185/65r14 86 T').
        :param price: The price of the tire.
        """
        self.specification = specification
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the tire.
        """
        return f"{self.specification}: ${self.price:.2f}"


class TirePurchase:
    """
    A class to handle the purchase of tires.
    """

    def __init__(self):
        """
        Initializes the TirePurchase instance with an empty list of tires.
        """
        self.tires = []

    def add_tire(self, tire: Tire):
        """
        Adds a tire to the purchase list.

        :param tire: An instance of Tire to be added.
        """
        self.tires.append(tire)

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the tires.

        :return: Total cost of all tires.
        """
        return sum(tire.price for tire in self.tires)

    def calculate_installment_plan(self, total_cost: float, installments: int) -> float:
        """
        Calculates the amount per installment.

        :param total_cost: Total cost of the purchase.
        :param installments: Number of installments.
        :return: Amount per installment.
        """
        if installments <= 0:
            raise ValueError("Number of installments must be greater than zero.")
        return total_cost / installments


def main():
    """
    Main function to execute the tire purchase calculation.
    """
    try:
        # Define tire specifications and prices
        tire1 = Tire("P 185/65r14 86 T", 100.00)  # Example price
        tire2 = Tire("P 205/50r17 Run Flat 89 V", 150.00)  # Example price

        # Create a tire purchase instance
        purchase = TirePurchase()

        # Add tires to the purchase
        purchase.add_tire(tire1)
        purchase.add_tire(tire2)

        # Calculate total cost
        total_cost = purchase.calculate_total_cost()
        print(f"Total cost for 4 tires: ${total_cost:.2f}")

        # Calculate installment plan
        installments = 12
        installment_amount = purchase.calculate_installment_plan(total_cost, installments)
        print(f"Amount per installment for {installments} months: ${installment_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
