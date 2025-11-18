"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Write code to calculate the cost of manufacturing flip-flops based on material type (rigid or expanded), design complexity, and quantity ordered.
Generated: DETERMINISTIC_744369376d807a4c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready Python code:

```python
# Import necessary modules
import sys

# Define constants for material type costs (cost per flip-flop)
RIGID_COST = 5.00       # Cost for rigid material flip-flop
EXPANDED_COST = 7.50    # Cost for expanded material flip-flop

# Define constants for design complexity costs (additional cost per flip-flop)
SIMPLE_DESIGN_COST = 0.00    # No additional cost for simple design
MODERATE_DESIGN_COST = 2.50  # Additional cost for moderate design
COMPLEX_DESIGN_COST = 5.00   # Additional cost for complex design

def calculate_cost(material_type, design_complexity, quantity):
    """
    Calculate the total manufacturing cost of flip-flops.

    Parameters:
    material_type (str): Type of material ('rigid' or 'expanded')
    design_complexity (str): Design complexity ('simple', 'moderate', or 'complex')
    quantity (int): Number of flip-flops to be produced

    Returns:
    float: Total manufacturing cost
    """
    # Validate material type
    if material_type not in ['rigid', 'expanded']:
        raise ValueError("Invalid material type. Must be 'rigid' or 'expanded'.")
    
    # Validate design complexity
    if design_complexity not in ['simple', 'moderate', 'complex']:
        raise ValueError("Invalid design complexity. Must be 'simple', 'moderate', or 'complex'.")
    
    # Validate quantity
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    
    # Determine cost based on material type
    if material_type == 'rigid':
        material_cost = RIGID_COST
    else: # material_type == 'expanded'
        material_cost = EXPANDED_COST
    
    # Determine cost based on design complexity
    if design_complexity == 'simple':
        design_cost = SIMPLE_DESIGN_COST
    elif design_complexity == 'moderate':
        design_cost = MODERATE_DESIGN_COST
    else: # design_complexity == 'complex'
        design_cost = COMPLEX_DESIGN_COST
    
    # Calculate total cost per flip-flop
    cost_per_flip_flop = material_cost + design_cost
    
    # Calculate total cost for the order
    total_cost = cost_per_flip_flop * quantity
    
    return total_cost

def main():
    """
    Main function to get user input and calculate the manufacturing cost.
    """
    try:
        # Get user input
        material_type = input("Enter material type (rigid or expanded): ").strip().lower()
        design_complexity = input("Enter design complexity (simple, moderate, or complex): ").strip().lower()
        quantity = int(input("Enter quantity of flip-flops to be ordered: ").strip())
        
        # Calculate the cost
        total_cost = calculate_cost(material_type, design_complexity, quantity)
        
        # Display the result
        print(f"The total manufacturing cost for {quantity} flip-flops is: ${total_cost:.2f}")
    
    except ValueError as ve:
        # Handle invalid input or calculation errors
        print(f"Error: {ve}")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the program
if __name__ == "__main__":
    main()
```
