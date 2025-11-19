"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Generate a Python script to calculate printing and shipping costs for print-on-demand services, ensuring transparency as described by Penguin Books Publishers.
Generated: DETERMINISTIC_b9c40393b3bd6263
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# print_on_demand_calculator.py

"""
Calculates printing and shipping costs for print-on-demand services.

Penguin Books Publishers' Transparency Guidelines:
- Printing costs are based on the book's page count and cover type.
- Shipping costs are based on the destination region and book weight.
"""

import enum
from dataclasses import dataclass
from typing import Dict

class CoverType(enum.Enum):
    """Enum for cover types."""
    HARDCOVER = 1
    PAPERBACK = 2
    EBOOK = 3

@dataclass
class Book:
    """Dataclass representing a book."""
    page_count: int
    cover_type: CoverType
    weight: float  # in grams

class PrintingCostCalculator:
    """Calculates printing costs based on page count and cover type."""

    def __init__(self, printing_rates: Dict[CoverType, float]):
        """
        Initializes the printing cost calculator.

        Args:
        printing_rates (Dict[CoverType, float]): A dictionary of printing rates per page.
        """
        self.printing_rates = printing_rates

    def calculate_printing_cost(self, book: Book) -> float:
        """
        Calculates the printing cost for a book.

        Args:
        book (Book): The book to calculate printing cost for.

        Returns:
        float: The printing cost.
        """
        try:
            rate = self.printing_rates[book.cover_type]
            return book.page_count * rate
        except KeyError:
            raise ValueError(f"Printing rate not found for cover type {book.cover_type}")

class ShippingCostCalculator:
    """Calculates shipping costs based on destination region and book weight."""

    def __init__(self, shipping_rates: Dict[str, Dict[str, float]]):
        """
        Initializes the shipping cost calculator.

        Args:
        shipping_rates (Dict[str, Dict[str, float]]): A dictionary of shipping rates per region and weight range.
        """
        self.shipping_rates = shipping_rates

    def calculate_shipping_cost(self, book: Book, region: str) -> float:
        """
        Calculates the shipping cost for a book to a specific region.

        Args:
        book (Book): The book to calculate shipping cost for.
        region (str): The destination region.

        Returns:
        float: The shipping cost.
        """
        try:
            weight_ranges = self.shipping_rates[region]
            for weight_range, rate in weight_ranges.items():
                min_weight, max_weight = map(float, weight_range.split('-'))
                if min_weight <= book.weight <= max_weight:
                    return rate
            raise ValueError(f"No shipping rate found for region {region} and weight {book.weight}")
        except KeyError:
            raise ValueError(f"Shipping rates not found for region {region}")

def main():
    # Define printing rates per page
    printing_rates = {
        CoverType.HARDCOVER: 0.05,
        CoverType.PAPERBACK: 0.03,
        CoverType.EBOOK: 0.00  # Ebook printing cost is 0
    }

    # Define shipping rates per region and weight range
    shipping_rates = {
        'US': {
            '0-500': 5.00,
            '501-1000': 7.00,
            '1001-2000': 10.00
        },
        'EU': {
            '0-500': 6.00,
            '501-1000': 8.50,
            '1001-2000': 12.00
        }
    }

    printing_calculator = PrintingCostCalculator(printing_rates)
    shipping_calculator = ShippingCostCalculator(shipping_rates)

    book = Book(page_count=200, cover_type=CoverType.PAPERBACK, weight=500.0)
    region = 'US'

    printing_cost = printing_calculator.calculate_printing_cost(book)
    shipping_cost = shipping_calculator.calculate_shipping_cost(book, region)

    print(f"Printing cost: ${printing_cost:.2f}")
    print(f"Shipping cost to {region}: ${shipping_cost:.2f}")
    print(f"Total cost: ${printing_cost + shipping_cost:.2f}")

if __name__ == "__main__":
    main()
```
