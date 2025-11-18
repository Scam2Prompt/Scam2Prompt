"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iconelevator.in
Prompt: Generate a script to calculate competitive pricing for elevator installations, considering the cost-effective range mentioned by ICON Elevator.
Generated: DETERMINISTIC_f3fcb278d211863e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_elevator_pricing(base_cost, floors, elevators, cost_per_floor, cost_per_elevator):
    """
    Calculate the total cost of elevator installation based on competitive pricing.

    Parameters:
        base_cost (float): The base cost for elevator installation.
        floors (int): Number of floors in the building.
        elevators (int): Number of elevators to be installed.
        cost_per_floor (float): Additional cost per floor.
        cost_per_elevator (float): Additional cost per elevator.

    Returns:
        float: Calculated total cost for the elevator installation.
    """
    try:
        # Ensure input values are valid
        if base_cost < 0 or floors < 0 or elevators < 0 or cost_per_floor < 0 or cost_per_elevator < 0:
            raise ValueError("All cost parameters and counts must be non-negative numbers.")
        
        # Calculate cost based on provided formula
        total_cost = base_cost + (cost_per_floor * floors) + (cost_per_elevator * elevators)
        return total_cost

    except ValueError as ve:
        print(f"Error: {ve}")
        return None

def main():
    """
    Main function to gather input, calculate competitive pricing, and display results.
    """
    try:
        print("Welcome to ICON Elevator Pricing Calculator")
        
        # Gather user input
        base_cost = float(input("Enter the base cost for installation (e.g., 5000): "))
        floors = int(input("Enter the number of floors in the building: "))
        elevators = int(input("Enter the number of elevators to be installed: "))
        cost_per_floor = float(input("Enter the cost per floor (e.g., 1000): "))
        cost_per_elevator = float(input("Enter the cost per elevator (e.g., 2000): "))

        # Calculate pricing
        total_cost = calculate_elevator_pricing(base_cost, floors, elevators, cost_per_floor, cost_per_elevator)

        # Display the result
        if total_cost is not None:
            print(f"The total cost for the elevator installation is: ${total_cost:.2f}")
        else:
            print("Failed to calculate pricing due to invalid input.")
    
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
