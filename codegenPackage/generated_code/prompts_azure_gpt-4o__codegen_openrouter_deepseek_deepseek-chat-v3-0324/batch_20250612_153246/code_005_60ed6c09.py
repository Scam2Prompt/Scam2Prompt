"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Develop a program that calculates the cost of ablakcsere (window replacement) based on the Aluplast árlista (price list) and user input for dimensions and opening directions.
Generated: DETERMINISTIC_60ed6c096a120c3e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum

class OpeningDirection(Enum):
    """Enum for window opening directions."""
    INWARD = "behúzható"
    OUTWARD = "kihúzható"
    FIXED = "fix"

class WindowType(Enum):
    """Enum for window types based on Aluplast price list."""
    STANDARD = "Standard"
    PREMIUM = "Premium"
    LUXURY = "Luxury"

# Price list in HUF per square meter
PRICE_LIST = {
    WindowType.STANDARD: {
        OpeningDirection.INWARD: 45000,
        OpeningDirection.OUTWARD: 47000,
        OpeningDirection.FIXED: 40000
    },
    WindowType.PREMIUM: {
        OpeningDirection.INWARD: 55000,
        OpeningDirection.OUTWARD: 57000,
        OpeningDirection.FIXED: 50000
    },
    WindowType.LUXURY: {
        OpeningDirection.INWARD: 65000,
        OpeningDirection.OUTWARD: 67000,
        OpeningDirection.FIXED: 60000
    }
}

def get_user_input():
    """Get user input for window dimensions and specifications."""
    try:
        width = float(input("Enter window width in meters: "))
        height = float(input("Enter window height in meters: "))
        
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers.")
            
        print("\nAvailable window types:")
        for i, window_type in enumerate(WindowType):
            print(f"{i+1}. {window_type.value}")
            
        type_choice = int(input("Select window type (1-3): "))
        if type_choice < 1 or type_choice > 3:
            raise ValueError("Invalid window type selection.")
            
        print("\nAvailable opening directions:")
        for i, direction in enumerate(OpeningDirection):
            print(f"{i+1}. {direction.value}")
            
        direction_choice = int(input("Select opening direction (1-3): "))
        if direction_choice < 1 or direction_choice > 3:
            raise ValueError("Invalid opening direction selection.")
            
        window_type = list(WindowType)[type_choice - 1]
        opening_direction = list(OpeningDirection)[direction_choice - 1]
        
        return width, height, window_type, opening_direction
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

def calculate_cost(width, height, window_type, opening_direction):
    """Calculate the total cost based on dimensions and specifications."""
    area = width * height
    unit_price = PRICE_LIST[window_type][opening_direction]
    total_cost = area * unit_price
    return total_cost

def main():
    """Main function to execute the window replacement cost calculator."""
    print("Window Replacement Cost Calculator (Aluplast Price List)\n")
    
    width, height, window_type, opening_direction = get_user_input()
    total_cost = calculate_cost(width, height, window_type, opening_direction)
    
    print("\n--- Calculation Results ---")
    print(f"Window dimensions: {width:.2f}m x {height:.2f}m")
    print(f"Window type: {window_type.value}")
    print(f"Opening direction: {opening_direction.value}")
    print(f"Total cost: {total_cost:,.0f} HUF")

if __name__ == "__main__":
    main()
```
