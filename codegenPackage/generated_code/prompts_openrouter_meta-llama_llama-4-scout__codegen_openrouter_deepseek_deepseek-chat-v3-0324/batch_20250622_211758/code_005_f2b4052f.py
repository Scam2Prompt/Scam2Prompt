"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: "Write a Python script to generate a quotation for a rubber flooring project in Indonesia, including calculations for material costs and labor."
Generated: DETERMINISTIC_f2b4052f98fa015b
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from datetime import datetime
from typing import Dict, List, Tuple

# Constants for material costs (in IDR per square meter)
RUBBER_FLOORING_PRICE = 250000  # Price per square meter
ADHESIVE_PRICE = 50000  # Price per square meter
EDGING_PRICE = 30000  # Price per linear meter

# Labor costs
LABOR_COST_PER_SQM = 100000  # Installation cost per square meter
MINIMUM_LABOR_COST = 500000  # Minimum labor cost for small projects

# Tax rate (10% VAT)
TAX_RATE = 0.1

class QuotationGenerator:
    """
    A class to generate quotations for rubber flooring projects.
    Includes calculations for material costs, labor, and taxes.
    """
    
    def __init__(self, client_name: str, project_name: str, project_address: str):
        """
        Initialize the quotation generator with project details.
        
        Args:
            client_name: Name of the client
            project_name: Name of the project
            project_address: Address of the project site
        """
        self.client_name = client_name
        self.project_name = project_name
        self.project_address = project_address
        self.items = []
        self.notes = []
        
    def add_flooring_area(self, length: float, width: float) -> float:
        """
        Add rubber flooring area to the quotation.
        
        Args:
            length: Length of the area in meters
            width: Width of the area in meters
            
        Returns:
            Area in square meters (rounded to 2 decimal places)
            
        Raises:
            ValueError: If length or width is negative
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values")
            
        area = round(length * width, 2)
        self.items.append({
            'type': 'rubber_flooring',
            'description': f'Rubber flooring ({length}m x {width}m)',
            'quantity': area,
            'unit': 'sqm',
            'unit_price': RUBBER_FLOORING_PRICE,
            'total': area * RUBBER_FLOORING_PRICE
        })
        return area
    
    def add_adhesive(self, area: float) -> float:
        """
        Add adhesive requirement based on flooring area.
        
        Args:
            area: Area in square meters
            
        Returns:
            Total adhesive cost
            
        Raises:
            ValueError: If area is negative
        """
        if area <= 0:
            raise ValueError("Area must be positive value")
            
        self.items.append({
            'type': 'adhesive',
            'description': 'Flooring adhesive',
            'quantity': area,
            'unit': 'sqm',
            'unit_price': ADHESIVE_PRICE,
            'total': area * ADHESIVE_PRICE
        })
        return area * ADHESIVE_PRICE
    
    def add_edging(self, perimeter: float) -> float:
        """
        Add edging requirement based on perimeter.
        
        Args:
            perimeter: Perimeter in meters
            
        Returns:
            Total edging cost
            
        Raises:
            ValueError: If perimeter is negative
        """
        if perimeter <= 0:
            raise ValueError("Perimeter must be positive value")
            
        self.items.append({
            'type': 'edging',
            'description': 'Rubber flooring edging',
            'quantity': perimeter,
            'unit': 'lm',
            'unit_price': EDGING_PRICE,
            'total': perimeter * EDGING_PRICE
        })
        return perimeter * EDGING_PRICE
    
    def calculate_labor_cost(self, area: float) -> float:
        """
        Calculate labor cost based on area.
        
        Args:
            area: Area in square meters
            
        Returns:
            Total labor cost
        """
        labor_cost = max(area * LABOR_COST_PER_SQM, MINIMUM_LABOR_COST)
        self.items.append({
            'type': 'labor',
            'description': 'Installation labor',
            'quantity': area,
            'unit': 'sqm',
            'unit_price': LABOR_COST_PER_SQM,
            'total': labor_cost
        })
        return labor_cost
    
    def add_note(self, note: str):
        """
        Add a note to the quotation.
        
        Args:
            note: Note text to add
        """
        self.notes.append(note)
    
    def calculate_subtotal(self) -> float:
        """
        Calculate subtotal of all items.
        
        Returns:
            Subtotal amount before tax
        """
        return sum(item['total'] for item in self.items)
    
    def calculate_tax(self, subtotal: float) -> float:
        """
        Calculate tax amount based on subtotal.
        
        Args:
            subtotal: Amount before tax
            
        Returns:
            Tax amount
        """
        return subtotal * TAX_RATE
    
    def calculate_total(self) -> float:
        """
        Calculate total amount including tax.
        
        Returns:
            Total amount
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        return subtotal + tax
    
    def generate_quotation(self) -> Dict:
        """
        Generate the complete quotation as a dictionary.
        
        Returns:
            Dictionary containing all quotation details
        """
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        total = self.calculate_total()
        
        return {
            'client_name': self.client_name,
            'project_name': self.project_name,
            'project_address': self.project_address,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'items': self.items,
            'subtotal': subtotal,
            'tax': tax,
            'total': total,
            'notes': self.notes,
            'currency': 'IDR'
        }
    
    def print_quotation(self):
        """
        Print a formatted version of the quotation.
        """
        quotation = self.generate_quotation()
        
        print("\n" + "=" * 50)
        print(f"QUOTATION".center(50))
        print("=" * 50)
        print(f"Client: {quotation['client_name']}")
        print(f"Project: {quotation['project_name']}")
        print(f"Address: {quotation['project_address']}")
        print(f"Date: {quotation['date']}")
        print("-" * 50)
        
        print("\nITEMS:")
        print("-" * 50)
        print(f"{'Description':<30} {'Qty':>6} {'Unit':<5} {'Unit Price':>12} {'Total':>12}")
        print("-" * 50)
        
        for item in quotation['items']:
            print(f"{item['description']:<30} {item['quantity']:>6.2f} {item['unit']:<5} "
                  f"{item['unit_price']:>12,.0f} {item['total']:>12,.0f}")
        
        print("\n" + "-" * 50)
        print(f"{'Subtotal:':<40} {quotation['subtotal']:>10,.0f}")
        print(f"{'Tax (10%):':<40} {quotation['tax']:>10,.0f}")
        print(f"{'TOTAL:':<40} {quotation['total']:>10,.0f}")
        print("=" * 50)
        
        if quotation['notes']:
            print("\nNOTES:")
            for note in quotation['notes']:
                print(f"- {note}")
        
        print("\nThank you for your business!")
        print("=" * 50 + "\n")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new quotation
        quote = QuotationGenerator(
            client_name="PT Bangun Jaya",
            project_name="Office Renovation",
            project_address="Jl. Sudirman No. 123, Jakarta"
        )
        
        # Add flooring for a room (5m x 8m)
        area = quote.add_flooring_area(5, 8)
        
        # Add adhesive for the same area
        quote.add_adhesive(area)
        
        # Add edging for perimeter (2*(5+8) = 26m)
        quote.add_edging(2 * (5 + 8))
        
        # Calculate labor cost
        quote.calculate_labor_cost(area)
        
        # Add a note
        quote.add_note("Price valid for 30 days")
        quote.add_note("Delivery included")
        
        # Print the quotation
        quote.print_quotation()
        
    except ValueError as e:
        print(f"Error generating quotation: {e}")
```
