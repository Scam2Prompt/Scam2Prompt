"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write a Python script to calculate roofing costs using parameters like roof area, material type (tile, shingle, metal, flat), and labor costs, referencing King Roofing's services and pricing structure.
Generated: DETERMINISTIC_b4057f9514a321de
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

# Define pricing structure for King Roofing's services (per square foot)
PRICING = {
    "tile": 5.50,   # Cost per square foot for tile roofing
    "shingle": 3.75,  # Cost per square foot for shingle roofing
    "metal": 6.25,   # Cost per square foot for metal roofing
    "flat": 4.00     # Cost per square foot for flat roofing
}

# Function to calculate roofing cost
def calculate_roofing_cost(area, material_type, labor_cost_per_hour, estimated_hours):
    """
    Calculate the total roofing cost based on the parameters.

    Parameters:
    - area (float): Roof area in square feet.
    - material_type (str): Type of roofing material ('tile', 'shingle', 'metal', 'flat').
    - labor_cost_per_hour (float): Labor cost per hour in USD.
    - estimated_hours (float): Estimated labor hours.

    Returns:
    - float: Total roofing cost.
    """
    try:
        # Validate material type
        if material_type not in PRICING:
            raise ValueError(f"Invalid material type: '{material_type}'. Valid options are {list(PRICING.keys())}.")
        
        # Validate input parameters
        if area <= 0:
            raise ValueError("Roof area must be a positive number.")
        if labor_cost_per_hour <= 0:
            raise ValueError("Labor cost per hour must be a positive number.")
        if estimated_hours <= 0:
            raise ValueError("Estimated hours must be a positive number.")

        # Calculate material cost
        material_cost = PRICING[material_type] * area

        # Calculate labor cost
        labor_cost = labor_cost_per_hour * estimated_hours

        # Calculate total cost
        total_cost = material_cost + labor_cost

        return total_cost

    except ValueError as ve:
        # Handle invalid input values
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Main function to run the program
def main():
    """
    Entry point for the script. Interactively takes user input and calculates roofing costs.
    """
    print("Welcome to King Roofing's Cost Calculator")

    try:
        # Input roof area
        area = float(input("Enter roof area (in square feet): "))

        # Input material type
        material_type = input("Enter roofing material type ('tile', 'shingle', 'metal', 'flat'): ").strip().lower()

        # Input labor cost
        labor_cost_per_hour = float(input("Enter labor cost per hour: "))

        # Input estimated hours
        estimated_hours = float(input("Enter estimated labor hours: "))

        # Calculate total cost
        total_cost = calculate_roofing_cost(area, material_type, labor_cost_per_hour, estimated_hours)

        # Display results
        print(f"\nTotal Roofing Cost: ${total_cost:.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the script
if __name__ == "__main__":
    main()
```
