"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fenceguys4u.com
Prompt: Write a Python script to calculate the cost of installing a custom fence based on the dimensions, material type, and labor rates provided by "The Fence Guys" in Savannah, GA.
Generated: DETERMINISTIC_58d41207e9710238
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# fence_calculator.py
# A script to calculate the cost of installing a custom fence based on dimensions, material type, and labor rates.

# Constants for material costs (per linear foot)
MATERIAL_COSTS = {
    "wood": 25.0,         # Cost per foot for wood fencing
    "vinyl": 40.0,        # Cost per foot for vinyl fencing
    "chain_link": 15.0    # Cost per foot for chain-link fencing
}

# Labor cost per linear foot
LABOR_COST_PER_FOOT = 10.0

def calculate_fence_cost(length, width, material_type):
    """
    Calculate the total cost of installing a custom fence.
    
    Parameters:
        - length (float): The length of the fence in feet.
        - width (float): The width of the fence in feet.
        - material_type (str): The type of material used ("wood", "vinyl", "chain_link").
        
    Returns:
        - float: The total cost of installation, or None if invalid input is provided.
    """
    try:
        # Ensure inputs are valid
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers.")
        if material_type not in MATERIAL_COSTS:
            raise ValueError(f"Invalid material type. Choose one of: {', '.join(MATERIAL_COSTS.keys())}.")

        # Calculate the perimeter of the fence
        perimeter = 2 * (length + width)

        # Get the material cost per foot
        material_cost_per_foot = MATERIAL_COSTS[material_type]

        # Calculate total cost
        material_cost = perimeter * material_cost_per_foot
        labor_cost = perimeter * LABOR_COST_PER_FOOT
        total_cost = material_cost + labor_cost

        return total_cost

    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    """
    Main function to get user input and calculate the fence installation cost.
    """
    print("Welcome to The Fence Guys Fence Installation Cost Calculator!")
    try:
        # Get user input for dimensions and material type
        length = float(input("Enter the length of the fence (in feet): "))
        width = float(input("Enter the width of the fence (in feet): "))
        material_type = input("Enter the material type (wood, vinyl, chain_link): ").strip().lower()

        # Calculate the cost
        total_cost = calculate_fence_cost(length, width, material_type)

        # Display the result
        if total_cost is not None:
            print(f"The total cost of installing the fence is: ${total_cost:.2f}")
        else:
            print("Unable to calculate the cost due to invalid input.")

    except ValueError:
        print("Error: Please enter valid numeric values for the dimensions.")

if __name__ == "__main__":
    main()
```
