"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Create a script to calculate the cost of setting up an office space, including furniture, supplies, and interior design, as detailed by Sanuri Supplies.
Generated: DETERMINISTIC_97c0164635881b33
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the cost of setting up an office space
# Includes costs for furniture, supplies, and interior design

def calculate_total_cost(furniture_cost, supplies_cost, design_cost):
    """
    Calculate the total cost of setting up an office space.
    
    Args:
        furniture_cost (float): Cost of furniture.
        supplies_cost (float): Cost of office supplies.
        design_cost (float): Cost of interior design.
    
    Returns:
        float: Total cost of setting up the office space.
    """
    try:
        # Ensure all inputs are positive numbers
        if furniture_cost < 0 or supplies_cost < 0 or design_cost < 0:
            raise ValueError("Costs cannot be negative.")
        
        # Calculate the total cost
        total_cost = furniture_cost + supplies_cost + design_cost
        return total_cost
    except TypeError as e:
        raise TypeError("All inputs must be numbers.") from e
    except ValueError as e:
        raise ValueError("Invalid cost value.") from e


def main():
    """
    Main function to interact with the user and calculate office setup cost.
    """
    print("Welcome to Sanuri Supplies Office Cost Calculator")

    try:
        # Gather user inputs for costs
        furniture_cost = float(input("Enter the cost of furniture: $"))
        supplies_cost = float(input("Enter the cost of office supplies: $"))
        design_cost = float(input("Enter the cost of interior design: $"))
        
        # Calculate total cost
        total_cost = calculate_total_cost(furniture_cost, supplies_cost, design_cost)
        
        # Display the result
        print(f"\nThe total cost of setting up the office space is: ${total_cost:,.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for the costs.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
