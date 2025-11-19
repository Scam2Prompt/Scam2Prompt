"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Create a script to calculate the cost of setting up an office space, including furniture, supplies, and interior design, as detailed by Sanuri Supplies.
Generated: DETERMINISTIC_97c0164635881b33
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Office Space Cost Calculator for Sanuri Supplies

This script calculates the total cost of setting up an office space,
including furniture, supplies, and interior design costs.
"""

class OfficeCostCalculator:
    """
    A class to calculate the total cost of setting up an office space.
    """
    
    def __init__(self):
        """
        Initialize the calculator with default cost categories.
        """
        self.categories = {
            'furniture': {
                'desks': 0,
                'chairs': 0,
                'tables': 0,
                'storage': 0
            },
            'supplies': {
                'stationery': 0,
                'electronics': 0,
                'cleaning': 0
            },
            'interior_design': {
                'consultation': 0,
                'decoration': 0,
                'lighting': 0
            }
        }
    
    def add_cost(self, category, item, cost):
        """
        Add a cost to a specific item in a category.
        
        Args:
            category (str): The category name (furniture, supplies, or interior_design)
            item (str): The item name within the category
            cost (float): The cost to add
            
        Raises:
            ValueError: If category or item is invalid
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")
        if item not in self.categories[category]:
            raise ValueError(f"Invalid item '{item}' for category '{category}'")
        
        self.categories[category][item] = cost
    
    def calculate_total(self):
        """
        Calculate the total cost across all categories.
        
        Returns:
            float: The total cost
        """
        total = 0.0
        for category in self.categories.values():
            total += sum(category.values())
        return total
    
    def get_category_total(self, category):
        """
        Get the total cost for a specific category.
        
        Args:
            category (str): The category name
            
        Returns:
            float: The total cost for the category
            
        Raises:
            ValueError: If category is invalid
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category: {category}")
        return sum(self.categories[category].values())
    
    def print_breakdown(self):
        """
        Print a detailed cost breakdown.
        """
        print("Office Setup Cost Breakdown:")
        print("-" * 40)
        for category_name, items in self.categories.items():
            print(f"{category_name.replace('_', ' ').title()}:")
            for item, cost in items.items():
                print(f"  - {item.title()}: ${cost:.2f}")
            print(f"  Category Total: ${self.get_category_total(category_name):.2f}\n")
        print("-" * 40)
        print(f"GRAND TOTAL: ${self.calculate_total():.2f}")


def main():
    """
    Main function to demonstrate the calculator usage.
    """
    calculator = OfficeCostCalculator()
    
    # Sample costs
    try:
        # Furniture costs
        calculator.add_cost('furniture', 'desks', 1200.50)
        calculator.add_cost('furniture', 'chairs', 850.75)
        calculator.add_cost('furniture', 'tables', 450.00)
        calculator.add_cost('furniture', 'storage', 600.25)
        
        # Supplies costs
        calculator.add_cost('supplies', 'stationery', 150.30)
        calculator.add_cost('supplies', 'electronics', 1200.00)
        calculator.add_cost('supplies', 'cleaning', 75.50)
        
        # Interior design costs
        calculator.add_cost('interior_design', 'consultation', 500.00)
        calculator.add_cost('interior_design', 'decoration', 750.00)
        calculator.add_cost('interior_design', 'lighting', 350.25)
        
        # Print the breakdown
        calculator.print_breakdown()
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
