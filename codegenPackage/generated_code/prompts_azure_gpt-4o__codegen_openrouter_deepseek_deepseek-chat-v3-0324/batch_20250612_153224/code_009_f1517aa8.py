"""
Generated Code Metadata:
========================
Original URL: https://karenfixing.com
Prompt: Generate a script to calculate the cost of facade installation using Karen Fixing's products, including payment terms like "پرداخت توافقی."
Generated: DETERMINISTIC_f1517aa86a3f416c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Facade Installation Cost Calculator for Karen Fixing's Products

This script calculates the total cost of facade installation using Karen Fixing's products,
including optional payment terms like "پرداخت توافقی" (negotiable payment).

Features:
- Calculate material costs based on area and product type
- Add labor costs
- Apply discounts if applicable
- Support for negotiable payment terms
"""

class FacadeCostCalculator:
    """
    A class to calculate the total cost of facade installation.
    """

    def __init__(self):
        """Initialize the calculator with default values."""
        self.product_prices = {
            'standard': 500000,  # per square meter (IRR)
            'premium': 800000,
            'luxury': 1200000
        }
        self.labor_cost = 300000  # per square meter (IRR)
        self.discount_rate = 0.0
        self.payment_terms = 'full'  # default is full payment

    def set_product_type(self, product_type):
        """
        Set the product type for calculation.
        
        Args:
            product_type (str): One of 'standard', 'premium', or 'luxury'
        
        Raises:
            ValueError: If product type is invalid
        """
        if product_type not in self.product_prices:
            raise ValueError(f"Invalid product type. Must be one of {list(self.product_prices.keys())}")
        self.product_type = product_type

    def set_area(self, area):
        """
        Set the installation area in square meters.
        
        Args:
            area (float): Area in square meters (must be positive)
        
        Raises:
            ValueError: If area is not positive
        """
        if area <= 0:
            raise ValueError("Area must be a positive number")
        self.area = area

    def set_discount(self, discount_rate):
        """
        Set discount rate (0-100%).
        
        Args:
            discount_rate (float): Discount percentage (0-100)
        
        Raises:
            ValueError: If discount is not between 0 and 100
        """
        if not 0 <= discount_rate <= 100:
            raise ValueError("Discount must be between 0 and 100 percent")
        self.discount_rate = discount_rate / 100

    def set_payment_terms(self, terms):
        """
        Set payment terms ('full' or 'negotiable').
        
        Args:
            terms (str): Payment terms ('full' or 'negotiable')
        
        Raises:
            ValueError: If terms are invalid
        """
        valid_terms = ['full', 'negotiable']
        if terms.lower() not in valid_terms:
            raise ValueError(f"Invalid payment terms. Must be one of {valid_terms}")
        self.payment_terms = terms.lower()

    def calculate_cost(self):
        """
        Calculate the total installation cost.
        
        Returns:
            dict: A dictionary containing cost breakdown and total
        """
        if not hasattr(self, 'product_type') or not hasattr(self, 'area'):
            raise ValueError("Product type and area must be set before calculation")

        material_cost = self.product_prices[self.product_type] * self.area
        labor_cost = self.labor_cost * self.area
        subtotal = material_cost + labor_cost
        discount_amount = subtotal * self.discount_rate
        total = subtotal - discount_amount

        return {
            'material_cost': material_cost,
            'labor_cost': labor_cost,
            'subtotal': subtotal,
            'discount_amount': discount_amount,
            'total': total,
            'payment_terms': self.payment_terms,
            'currency': 'IRR'
        }

def main():
    """Main function to demonstrate the calculator usage."""
    try:
        calculator = FacadeCostCalculator()
        
        # Get user input
        area = float(input("Enter the facade area in square meters: "))
        product_type = input("Enter product type (standard/premium/luxury): ").lower()
        discount = float(input("Enter discount percentage (0-100): "))
        payment_terms = input("Enter payment terms (full/negotiable): ").lower()

        # Set calculator values
        calculator.set_area(area)
        calculator.set_product_type(product_type)
        calculator.set_discount(discount)
        calculator.set_payment_terms(payment_terms)

        # Calculate and display results
        result = calculator.calculate_cost()
        
        print("\nCost Breakdown:")
        print(f"Material Cost: {result['material_cost']:,} IRR")
        print(f"Labor Cost: {result['labor_cost']:,} IRR")
        print(f"Subtotal: {result['subtotal']:,} IRR")
        print(f"Discount: {result['discount_amount']:,} IRR")
        print(f"Total Cost: {result['total']:,} IRR")
        print(f"Payment Terms: {result['payment_terms']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
