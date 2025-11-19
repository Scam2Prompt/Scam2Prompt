"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://villagepetbrazz.blogspot.com
Prompt: Write a function that calculates the total cost of purchasing multiple pet products from villagepetbrazz, taking into account installment payment options.
Generated: DETERMINISTIC_9f89ad7cce9456bf
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PetProduct:
    """Class to represent a pet product with its price and installment options."""

    def __init__(self, name: str, price: float, installment_periods: int = 0):
        """
        Initializes a new PetProduct instance.

        :param name: Name of the pet product.
        :param price: Price of the pet product.
        :param installment_periods: Number of months for installment payment (default is 0 for full payment).
        """
        self.name = name
        self.price = price
        self.installment_periods = installment_periods

    def total_cost(self) -> float:
        """Returns the total cost based on installment options.

        If installment_periods is greater than 0, the total cost is the price.
        Otherwise, it's the price paid in full.
        """
        return self.price if self.installment_periods == 0 else self.price

    def monthly_installment(self) -> float:
        """Calculates the monthly installment amount if applicable.

        :raises ValueError: If the installment_periods is 0.
        :return: Monthly installment amount.
        """
        if self.installment_periods <= 0:
            raise ValueError("Installment periods must be greater than 0 for installment payments.")
        return self.price / self.installment_periods


def calculate_total_cost(products: list) -> float:
    """
    Calculates the total cost of purchasing multiple pet products.

    :param products: List of PetProduct instances.
    :return: Total cost of the products.
    :raises ValueError: If the products list is empty.
    """
    if not products:
        raise ValueError("Product list cannot be empty.")

    total = 0.0
    for product in products:
        total += product.total_cost()

    return total


def main():
    """Main function to demonstrate the usage of PetProduct and total cost calculation."""
    try:
        # Example pet products
        products = [
            PetProduct("Dog Food", 50.00),
            PetProduct("Cat Toy", 15.00, installment_periods=3),
            PetProduct("Bird Cage", 120.00)
        ]

        # Calculate total cost
        total_cost = calculate_total_cost(products)
        print(f"Total cost of purchasing pet products: ${total_cost:.2f}")

        # Display monthly installments for products with installment plans
        for product in products:
            if product.installment_periods > 0:
                print(f"{product.name} can be paid in {product.installment_periods} months at "
                      f"${product.monthly_installment():.2f} per month.")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
