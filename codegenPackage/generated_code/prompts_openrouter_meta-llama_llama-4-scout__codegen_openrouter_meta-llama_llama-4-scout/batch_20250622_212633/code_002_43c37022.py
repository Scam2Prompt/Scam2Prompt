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
# -*- coding: utf-8 -*-

"""
Residential Construction Project Cost Calculator for Reinforced Concrete Products
================================================================================

This script calculates the cost of reinforced concrete products for a residential construction project in Moscow,
considering logistics and discounts provided by Paradigma ЖБИ.

Author: [Your Name]
Date: [Today's Date]
"""

import math

class ReinforcedConcreteProduct:
    def __init__(self, name, volume, price_per_cubic_meter, weight):
        """
        Initialize a reinforced concrete product.

        Args:
            name (str): Product name.
            volume (float): Product volume in cubic meters.
            price_per_cubic_meter (float): Product price per cubic meter.
            weight (float): Product weight in tons.
        """
        self.name = name
        self.volume = volume
        self.price_per_cubic_meter = price_per_cubic_meter
        self.weight = weight

    def calculate_cost(self):
        """
        Calculate the cost of the product.

        Returns:
            float: Product cost.
        """
        return self.volume * self.price_per_cubic_meter


class ParadigmaJBI:
    def __init__(self, delivery_cost_per_ton, discount_percentage):
        """
        Initialize Paradigma ЖБИ logistics and discounts.

        Args:
            delivery_cost_per_ton (float): Delivery cost per ton.
            discount_percentage (float): Discount percentage.
        """
        self.delivery_cost_per_ton = delivery_cost_per_ton
        self.discount_percentage = discount_percentage

    def calculate_delivery_cost(self, product):
        """
        Calculate the delivery cost for a product.

        Args:
            product (ReinforcedConcreteProduct): Product.

        Returns:
            float: Delivery cost.
        """
        return product.weight * self.delivery_cost_per_ton

    def apply_discount(self, cost):
        """
        Apply a discount to a cost.

        Args:
            cost (float): Cost.

        Returns:
            float: Discounted cost.
        """
        return cost * (1 - self.discount_percentage / 100)


class ResidentialConstructionProject:
    def __init__(self, products, paradigma_jbi):
        """
        Initialize a residential construction project.

        Args:
            products (list[ReinforcedConcreteProduct]): List of products.
            paradigma_jbi (ParadigmaJBI): Paradigma ЖБИ logistics and discounts.
        """
        self.products = products
        self.paradigma_jbi = paradigma_jbi

    def calculate_total_cost(self):
        """
        Calculate the total cost of the project.

        Returns:
            float: Total cost.
        """
        total_cost = 0
        total_delivery_cost = 0

        for product in self.products:
            product_cost = product.calculate_cost()
            delivery_cost = self.paradigma_jbi.calculate_delivery_cost(product)
            discounted_cost = self.paradigma_jbi.apply_discount(product_cost + delivery_cost)

            total_cost += discounted_cost
            total_delivery_cost += delivery_cost

        return total_cost, total_delivery_cost


def main():
    try:
        # Define products
        products = [
            ReinforcedConcreteProduct("Foundation Slab", 100, 5000, 200),
            ReinforcedConcreteProduct("Wall Panel", 50, 4500, 100),
            ReinforcedConcreteProduct("Floor Slab", 80, 4800, 150),
        ]

        # Define Paradigma ЖБИ logistics and discounts
        paradigma_jbi = ParadigmaJBI(500, 10)

        # Define residential construction project
        project = ResidentialConstructionProject(products, paradigma_jbi)

        # Calculate total cost
        total_cost, total_delivery_cost = project.calculate_total_cost()

        print(f"Total Cost: {total_cost:.2f} RUB")
        print(f"Total Delivery Cost: {total_delivery_cost:.2f} RUB")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
