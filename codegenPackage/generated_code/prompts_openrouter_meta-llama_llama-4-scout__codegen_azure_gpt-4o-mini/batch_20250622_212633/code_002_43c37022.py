"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Generate a code snippet to calculate the cost of reinforced concrete products for a residential construction project in Moscow, considering the logistics and discounts provided by Paradigma ЖБИ.
Generated: DETERMINISTIC_43c370224b7bb753
Batch ID: 20250622_212633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ConcreteProduct:
    """
    A class to represent a reinforced concrete product.
    """

    def __init__(self, name, unit_price, quantity):
        """
        Initializes a new concrete product.

        :param name: str - The name of the concrete product.
        :param unit_price: float - The price per unit of the product.
        :param quantity: int - The quantity of the product required.
        """
        self.name = name
        self.unit_price = unit_price
        self.quantity = quantity

    def total_cost(self):
        """
        Calculates the total cost for the concrete product.

        :return: float - The total cost for the product.
        """
        return self.unit_price * self.quantity


class Logistics:
    """
    A class to handle logistics costs.
    """

    def __init__(self, base_cost, distance):
        """
        Initializes logistics with base cost and distance.

        :param base_cost: float - The base cost of logistics.
        :param distance: float - The distance to the construction site in km.
        """
        self.base_cost = base_cost
        self.distance = distance

    def calculate_logistics_cost(self):
        """
        Calculates the logistics cost based on distance.

        :return: float - The total logistics cost.
        """
        cost_per_km = 10  # Cost per km
        return self.base_cost + (cost_per_km * self.distance)


class Discount:
    """
    A class to handle discounts on the total cost.
    """

    def __init__(self, discount_rate):
        """
        Initializes a discount with a discount rate.

        :param discount_rate: float - The discount rate as a percentage (0-100).
        """
        self.discount_rate = discount_rate

    def apply_discount(self, total_cost):
        """
        Applies the discount to the total cost.

        :param total_cost: float - The total cost before discount.
        :return: float - The total cost after applying the discount.
        """
        if not (0 <= self.discount_rate <= 100):
            raise ValueError("Discount rate must be between 0 and 100.")
        discount_amount = (self.discount_rate / 100) * total_cost
        return total_cost - discount_amount


def calculate_total_cost(products, logistics, discount):
    """
    Calculates the total cost of the construction project.

    :param products: list - A list of ConcreteProduct instances.
    :param logistics: Logistics - An instance of the Logistics class.
    :param discount: Discount - An instance of the Discount class.
    :return: float - The total cost after logistics and discount.
    """
    try:
        # Calculate total product cost
        total_product_cost = sum(product.total_cost() for product in products)

        # Calculate logistics cost
        total_logistics_cost = logistics.calculate_logistics_cost()

        # Calculate total cost before discount
        total_cost = total_product_cost + total_logistics_cost

        # Apply discount
        final_cost = discount.apply_discount(total_cost)

        return final_cost

    except Exception as e:
        print(f"An error occurred while calculating total cost: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define concrete products
    products = [
        ConcreteProduct("Reinforced Slab", 5000, 10),
        ConcreteProduct("Concrete Beam", 3000, 5)
    ]

    # Define logistics
    logistics = Logistics(base_cost=2000, distance=15)

    # Define discount
    discount = Discount(discount_rate=10)  # 10% discount

    # Calculate total cost
    total_cost = calculate_total_cost(products, logistics, discount)

    if total_cost is not None:
        print(f"The total cost of the construction project is: {total_cost:.2f} RUB")
```
