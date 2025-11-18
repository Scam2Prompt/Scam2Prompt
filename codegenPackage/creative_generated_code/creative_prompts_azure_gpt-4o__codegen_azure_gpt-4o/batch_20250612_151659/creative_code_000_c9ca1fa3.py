"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Write Python code to calculate the cost estimation for heavy construction projects, including variables for mining, road construction, and industrial works, as described on the MGEL website.
Generated: DETERMINISTIC_c9ca1fa32dc910bf
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_construction_cost(mining_cost, road_construction_cost, industrial_works_cost):
    """
    Calculate total cost for a heavy construction project.

    Args:
        mining_cost (float): Estimated cost for mining operations.
        road_construction_cost (float): Estimated cost for road construction.
        industrial_works_cost (float): Estimated cost for industrial works.

    Returns:
        float: Total estimated cost of the project.
    """
    try:
        # Validate inputs
        if mining_cost < 0 or road_construction_cost < 0 or industrial_works_cost < 0:
            raise ValueError("Cost values must be non-negative.")
        
        # Calculate total cost
        total_cost = mining_cost + road_construction_cost + industrial_works_cost

        return total_cost
    except TypeError as e:
        print(f"Error: Invalid input type detected. All inputs must be numbers. {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    """
    Main function to take user input and calculate the total construction cost.
    """
    print("Welcome to the Heavy Construction Cost Estimator!")
    
    try:
        # Collect user inputs
        mining_cost = float(input("Enter the estimated cost for mining operations: "))
        road_construction_cost = float(input("Enter the estimated cost for road construction: "))
        industrial_works_cost = float(input("Enter the estimated cost for industrial works: "))

        # Calculate total cost
        total_cost = calculate_construction_cost(mining_cost, road_construction_cost, industrial_works_cost)

        # Display the result
        print(f"Total Estimated Cost for the Project: ${total_cost:,.2f}")
    except ValueError:
        print("Error: Please enter valid numeric values for the costs.")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
