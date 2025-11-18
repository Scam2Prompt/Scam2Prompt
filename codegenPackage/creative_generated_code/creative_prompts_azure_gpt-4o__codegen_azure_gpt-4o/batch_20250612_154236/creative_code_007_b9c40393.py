"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Generate a Python script to calculate printing and shipping costs for print-on-demand services, ensuring transparency as described by Penguin Books Publishers.
Generated: DETERMINISTIC_b9c40393b3bd6263
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class PrintOnDemandCostCalculator:
    def __init__(self, base_printing_cost_per_book, shipping_rate_per_kg, tax_rate_percent):
        """
        Initialize the calculator with given rates.

        :param base_printing_cost_per_book: Base printing cost for a single book (float).
        :param shipping_rate_per_kg: Cost of shipping per kilogram (float).
        :param tax_rate_percent: Tax rate as a percentage (float).
        """
        self.base_printing_cost_per_book = base_printing_cost_per_book
        self.shipping_rate_per_kg = shipping_rate_per_kg
        self.tax_rate = tax_rate_percent / 100  # Convert percentage to decimal

    def calculate_printing_cost(self, num_books):
        """
        Calculate total printing cost for the given number of books.

        :param num_books: Number of books to print (int).
        :return: Total printing cost (float).
        """
        if num_books <= 0:
            raise ValueError("Number of books must be greater than 0.")
        return self.base_printing_cost_per_book * num_books

    def calculate_shipping_cost(self, weight_per_book_kg, num_books):
        """
        Calculate total shipping cost based on weight per book and number of books.

        :param weight_per_book_kg: Weight of one book in kilograms (float).
        :param num_books: Number of books to ship (int).
        :return: Total shipping cost (float).
        """
        if weight_per_book_kg <= 0:
            raise ValueError("Weight per book must be greater than 0.")
        if num_books <= 0:
            raise ValueError("Number of books must be greater than 0.")
        total_weight = weight_per_book_kg * num_books
        return self.shipping_rate_per_kg * total_weight

    def calculate_total_cost(self, weight_per_book_kg, num_books):
        """
        Calculate the total cost including printing, shipping, and taxes.

        :param weight_per_book_kg: Weight of one book in kilograms (float).
        :param num_books: Number of books to ship (int).
        :return: Total cost including printing, shipping, and taxes (float).
        """
        try:
            printing_cost = self.calculate_printing_cost(num_books)
            shipping_cost = self.calculate_shipping_cost(weight_per_book_kg, num_books)
            subtotal = printing_cost + shipping_cost
            tax = subtotal * self.tax_rate
            total_cost = subtotal + tax

            return {
                "printing_cost": printing_cost,
                "shipping_cost": shipping_cost,
                "tax": tax,
                "total_cost": total_cost
            }
        except ValueError as e:
            print(f"Error: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Initialize the calculator with sample rates
    base_printing_cost_per_book = 5.0  # $5 per book
    shipping_rate_per_kg = 2.0        # $2 per kilogram
    tax_rate_percent = 10.0           # 10%

    calculator = PrintOnDemandCostCalculator(base_printing_cost_per_book, 
                                             shipping_rate_per_kg, 
                                             tax_rate_percent)

    # Parameters for calculation
    weight_per_book_kg = 0.5  # 0.5 kg per book
    num_books = 100           # 100 books to print and ship

    # Perform calculation
    result = calculator.calculate_total_cost(weight_per_book_kg, num_books)

    if result:
        print(f"Printing Cost: ${result['printing_cost']:.2f}")
        print(f"Shipping Cost: ${result['shipping_cost']:.2f}")
        print(f"Tax: ${result['tax']:.2f}")
        print(f"Total Cost: ${result['total_cost']:.2f}")
```
