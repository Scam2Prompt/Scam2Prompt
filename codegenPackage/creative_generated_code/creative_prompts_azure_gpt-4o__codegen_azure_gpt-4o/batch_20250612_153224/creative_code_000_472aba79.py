"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karenfixing.com
Prompt: Write a Python script to calculate the load-bearing capacity of aluminum runners used in dry facade systems, referencing the specifications of "رانر آلومینیومی" from Karen Fixing's product catalog.
Generated: DETERMINISTIC_472aba79ffd92bcd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to calculate the load-bearing capacity of aluminum runners 
used in dry facade systems based on specifications provided in Karen Fixing's product catalog.

This script assumes you have access to the product catalog data and provides 
a way to calculate the load-bearing capacity based on user input and material properties.
"""

# Import necessary modules
import sys

def get_aluminum_runner_properties():
    """
    Mock function to retrieve aluminum runner properties from Karen Fixing's product catalog.
    In production, this would query a database or read from an API/file.
    
    Returns:
        dict: Material properties of the aluminum runner.
    """
    # Example properties (replace with real data from Karen Fixing's catalog)
    return {
        "density": 2.7,  # g/cm^3 (density of aluminum)
        "yield_strength": 80,  # MPa (example yield strength of aluminum runner)
        "modulus_of_elasticity": 69,  # GPa (modulus of elasticity for aluminum)
        "cross_section_area": 10,  # cm^2 (example cross-sectional area of the runner)
        "length": 300,  # cm (example length of the runner)
        "safety_factor": 1.5  # Safety factor for load calculations
    }

def calculate_load_capacity(properties):
    """
    Calculate the load-bearing capacity of the aluminum runner.

    Args:
        properties (dict): Material properties of the aluminum runner.

    Returns:
        float: Maximum load-bearing capacity in kilograms.
    """
    try:
        # Extract necessary properties
        yield_strength = properties["yield_strength"]  # MPa
        cross_section_area = properties["cross_section_area"]  # cm^2
        safety_factor = properties["safety_factor"]

        # Convert yield strength from MPa to N/cm^2 (1 MPa = 10 N/cm^2)
        yield_strength_n_cm2 = yield_strength * 10
        
        # Calculate load capacity without safety factor
        load_capacity_n = yield_strength_n_cm2 * cross_section_area
        
        # Adjust for safety factor
        load_capacity_n_safe = load_capacity_n / safety_factor

        # Convert load capacity from N to kilograms (1 N = 0.10197 kg)
        load_capacity_kg = load_capacity_n_safe * 0.10197

        return round(load_capacity_kg, 2)  # Return rounded value for readability
    
    except KeyError as e:
        print(f"Error: Missing required property in input data - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the load-bearing capacity calculation.
    """
    print("Calculating load-bearing capacity of aluminum runners...\n")
    
    # Get runner properties
    runner_properties = get_aluminum_runner_properties()

    # Calculate load capacity
    load_capacity = calculate_load_capacity(runner_properties)

    # Output the result
    print(f"Load-bearing capacity (with safety factor): {load_capacity} kg")
    print("\nCalculation complete.")

# Run the script
if __name__ == "__main__":
    main()
```
