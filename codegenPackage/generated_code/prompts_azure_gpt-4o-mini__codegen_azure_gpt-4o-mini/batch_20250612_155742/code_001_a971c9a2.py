"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a Python script that calculates potential energy savings from installing commercial spray foam insulation based on user input for building size and energy costs.
Generated: DETERMINISTIC_a971c9a2b70b80dc
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sys

def calculate_energy_savings(building_size, energy_cost, insulation_thickness):
    """
    Calculate potential energy savings from installing spray foam insulation.

    Parameters:
    building_size (float): The size of the building in square feet.
    energy_cost (float): The cost of energy per kilowatt-hour.
    insulation_thickness (float): The thickness of the insulation in inches.

    Returns:
    float: Estimated annual energy savings in dollars.
    """
    # Constants for energy savings calculation
    R_VALUE_PER_INCH = 6.5  # R-value per inch of spray foam insulation
    HEATING_DEGREE_DAYS = 5000  # Average heating degree days for a commercial building
    ENERGY_USE_PER_SQFT = 1.5  # Energy use per square foot in kWh

    # Calculate total R-value based on insulation thickness
    total_r_value = insulation_thickness * R_VALUE_PER_INCH

    # Calculate energy savings in kWh
    energy_savings_kwh = (HEATING_DEGREE_DAYS / total_r_value) * building_size * ENERGY_USE_PER_SQFT

    # Calculate cost savings
    cost_savings = energy_savings_kwh * energy_cost

    return cost_savings

def main():
    """
    Main function to execute the energy savings calculation based on user input.
    """
    try:
        # User input for building size, energy cost, and insulation thickness
        building_size = float(input("Enter the building size in square feet: "))
        energy_cost = float(input("Enter the energy cost per kWh: "))
        insulation_thickness = float(input("Enter the insulation thickness in inches: "))

        # Validate inputs
        if building_size <= 0 or energy_cost <= 0 or insulation_thickness <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Calculate potential energy savings
        savings = calculate_energy_savings(building_size, energy_cost, insulation_thickness)

        # Display the results
        print(f"Estimated annual energy savings: ${savings:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
