"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Write Python code to calculate the cost of UDIZINE's modular display systems based on user-selected components, such as shelf type (glass/wood), hanging rails, and display units.
Generated: DETERMINISTIC_fd0b81c4407b4794
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ModularDisplaySystem:
    """
    A class to represent a modular display system for UDIZINE.
    
    Attributes:
        shelf_type (str): Type of shelf ('glass' or 'wood').
        hanging_rails (int): Number of hanging rails.
        display_units (int): Number of display units.
    """

    # Pricing constants
    SHELF_PRICES = {
        'glass': 150.0,
        'wood': 100.0
    }
    
    HANGING_RAIL_PRICE = 20.0
    DISPLAY_UNIT_PRICE = 50.0

    def __init__(self, shelf_type, hanging_rails, display_units):
        """
        Initializes the ModularDisplaySystem with selected components.
        
        Parameters:
            shelf_type (str): Type of shelf ('glass' or 'wood').
            hanging_rails (int): Number of hanging rails.
            display_units (int): Number of display units.
            
        Raises:
            ValueError: If shelf_type is not valid, or hanging_rails/display_units are negative.
        """
        if shelf_type not in self.SHELF_PRICES:
            raise ValueError(f"Invalid shelf type. Choose from {list(self.SHELF_PRICES.keys())}.")
        
        if hanging_rails < 0 or display_units < 0:
            raise ValueError("Number of hanging rails and display units must be non-negative.")
        
        self.shelf_type = shelf_type
        self.hanging_rails = hanging_rails
        self.display_units = display_units

    def calculate_total_cost(self):
        """
        Calculates the total cost of the modular display system based on selected components.
        
        Returns:
            float: Total cost of the display system.
        """
        shelf_cost = self.SHELF_PRICES[self.shelf_type]
        total_cost = (shelf_cost +
                      (self.HANGING_RAIL_PRICE * self.hanging_rails) +
                      (self.DISPLAY_UNIT_PRICE * self.display_units))
        return total_cost

def main():
    """
    Main function to demonstrate the calculation of the modular display system cost.
    Handles user input and provides error handling for invalid inputs.
    """
    try:
        # User input for components
        shelf_type = input("Enter shelf type (glass/wood): ").strip().lower()
        hanging_rails = int(input("Enter number of hanging rails: "))
        display_units = int(input("Enter number of display units: "))
        
        # Create a ModularDisplaySystem instance
        display_system = ModularDisplaySystem(shelf_type, hanging_rails, display_units)
        
        # Calculate and display the total cost
        total_cost = display_system.calculate_total_cost()
        print(f"The total cost of the modular display system is: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
