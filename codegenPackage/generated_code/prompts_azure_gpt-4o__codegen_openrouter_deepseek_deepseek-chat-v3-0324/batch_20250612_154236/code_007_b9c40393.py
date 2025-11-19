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
"""
Print-on-Demand Cost Calculator for Penguin Books Publishers

This script calculates the total cost of printing and shipping for print-on-demand services.
It provides transparent cost breakdowns for different book specifications and shipping options.

Features:
- Calculate printing cost based on page count and book type
- Calculate shipping cost based on destination and weight
- Provide itemized cost breakdown
- Validate inputs to ensure realistic values
"""

import enum
from dataclasses import dataclass
from typing import Optional, Tuple, Dict


class BookType(enum.Enum):
    """Enumeration of supported book types"""
    PAPERBACK = "paperback"
    HARDCOVER = "hardcover"
    SPIRAL_BOUND = "spiral_bound"


class ShippingZone(enum.Enum):
    """Enumeration of shipping zones with their base costs"""
    DOMESTIC = "domestic"
    INTERNATIONAL_EU = "international_eu"
    INTERNATIONAL_OTHER = "international_other"


@dataclass
class CostBreakdown:
    """Dataclass to hold cost breakdown information"""
    printing_cost: float
    shipping_cost: float
    total_cost: float
    details: Dict[str, float]


class PrintOnDemandCalculator:
    """Main calculator class for print-on-demand services"""
    
    # Printing cost constants (per page)
    PRINTING_COSTS = {
        BookType.PAPERBACK: 0.02,
        BookType.HARDCOVER: 0.05,
        BookType.SPIRAL_BOUND: 0.03
    }
    
    # Base costs for different book types
    BASE_COSTS = {
        BookType.PAPERBACK: 2.00,
        BookType.HARDCOVER: 5.00,
        BookType.SPIRAL_BOUND: 3.00
    }
    
    # Shipping costs per weight unit (kg) by zone
    SHIPPING_COSTS = {
        ShippingZone.DOMESTIC: 1.50,
        ShippingZone.INTERNATIONAL_EU: 3.00,
        ShippingZone.INTERNATIONAL_OTHER: 4.50
    }
    
    # Weight per page in kg
    WEIGHT_PER_PAGE = 0.005
    
    def __init__(self):
        """Initialize the calculator with default values"""
        self._validate_cost_tables()
    
    def _validate_cost_tables(self):
        """Internal method to validate that all cost tables are properly configured"""
        for book_type in BookType:
            if book_type not in self.PRINTING_COSTS:
                raise ValueError(f"Missing printing cost for {book_type}")
            if book_type not in self.BASE_COSTS:
                raise ValueError(f"Missing base cost for {book_type}")
        
        for zone in ShippingZone:
            if zone not in self.SHIPPING_COSTS:
                raise ValueError(f"Missing shipping cost for {zone}")
    
    def calculate_weight(self, page_count: int) -> float:
        """
        Calculate the book weight based on page count
        
        Args:
            page_count: Number of pages in the book
            
        Returns:
            Calculated weight in kilograms
            
        Raises:
            ValueError: If page_count is not positive
        """
        if page_count <= 0:
            raise ValueError("Page count must be a positive integer")
        return page_count * self.WEIGHT_PER_PAGE
    
    def calculate_printing_cost(self, book_type: BookType, page_count: int) -> float:
        """
        Calculate the printing cost for a book
        
        Args:
            book_type: Type of the book (from BookType enum)
            page_count: Number of pages in the book
            
        Returns:
            Total printing cost
            
        Raises:
            ValueError: If page_count is not positive
        """
        if page_count <= 0:
            raise ValueError("Page count must be a positive integer")
        
        base_cost = self.BASE_COSTS[book_type]
        per_page_cost = self.PRINTING_COSTS[book_type]
        return base_cost + (per_page_cost * page_count)
    
    def calculate_shipping_cost(self, zone: ShippingZone, weight: float) -> float:
        """
        Calculate the shipping cost
        
        Args:
            zone: Shipping zone (from ShippingZone enum)
            weight: Weight of the package in kilograms
            
        Returns:
            Shipping cost
            
        Raises:
            ValueError: If weight is not positive
        """
        if weight <= 0:
            raise ValueError("Weight must be a positive number")
        
        return self.SHIPPING_COSTS[zone] * weight
    
    def calculate_total_cost(
        self,
        book_type: BookType,
        page_count: int,
        zone: ShippingZone,
        quantity: int = 1
    ) -> CostBreakdown:
        """
        Calculate the total cost including printing and shipping
        
        Args:
            book_type: Type of the book (from BookType enum)
            page_count: Number of pages in the book
            zone: Shipping zone (from ShippingZone enum)
            quantity: Number of copies (default: 1)
            
        Returns:
            CostBreakdown object with detailed costs
            
        Raises:
            ValueError: If any parameter is invalid
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        weight = self.calculate_weight(page_count)
        printing_cost = self.calculate_printing_cost(book_type, page_count) * quantity
        shipping_cost = self.calculate_shipping_cost(zone, weight * quantity)
        
        return CostBreakdown(
            printing_cost=printing_cost,
            shipping_cost=shipping_cost,
            total_cost=printing_cost + shipping_cost,
            details={
                "printing_cost_per_unit": printing_cost / quantity,
                "shipping_cost_per_unit": shipping_cost / quantity,
                "weight_per_unit": weight,
                "total_weight": weight * quantity
            }
        )


# Example usage
if __name__ == "__main__":
    calculator = PrintOnDemandCalculator()
    
    try:
        # Example calculation
        breakdown = calculator.calculate_total_cost(
            book_type=BookType.PAPERBACK,
            page_count=200,
            zone=ShippingZone.DOMESTIC,
            quantity=5
        )
        
        print("Cost Breakdown:")
        print(f"Printing Cost: ${breakdown.printing_cost:.2f}")
        print(f"Shipping Cost: ${breakdown.shipping_cost:.2f}")
        print(f"Total Cost: ${breakdown.total_cost:.2f}")
        print("\nDetails:")
        for key, value in breakdown.details.items():
            print(f"{key.replace('_', ' ').title()}: {value:.2f}")
    
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
