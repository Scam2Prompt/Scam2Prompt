"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Create a Python script to compare the energy consumption of the XT400 and XT500 EPS foam densifiers based on their power requirements and processing capacities.
Generated: DETERMINISTIC_860e48c5aff64bd0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_energy_consumption(power_kw, processing_capacity_kg_per_hour, hours_of_operation):
    """
    Calculate energy consumption based on power requirement, processing capacity, and hours of operation.

    Parameters:
        power_kw (float): Power requirement in kilowatts (kW).
        processing_capacity_kg_per_hour (float): Processing capacity in kilograms per hour (kg/h).
        hours_of_operation (float): Total hours of operation.

    Returns:
        float: Total energy consumption in kilowatt-hours (kWh) per kilogram of foam processed.
    """
    try:
        # Total energy consumed (kWh)
        total_energy_consumed = power_kw * hours_of_operation

        # Energy consumption per kilogram of foam processed (kWh/kg)
        energy_per_kg = total_energy_consumed / (processing_capacity_kg_per_hour * hours_of_operation)
        return energy_per_kg

    except ZeroDivisionError:
        raise ValueError("Processing capacity and hours of operation must be greater than 0.")

def main():
    """
    Main function to compare the energy consumption of XT400 and XT500 EPS foam densifiers.
    """
    try:
        # Specifications for XT400
        xt400_power_kw = 15.0  # Power requirement in kW
        xt400_processing_capacity_kg_per_hour = 300.0  # Processing capacity in kg/h

        # Specifications for XT500
        xt500_power_kw = 20.0  # Power requirement in kW
        xt500_processing_capacity_kg_per_hour = 400.0  # Processing capacity in kg/h

        # User input for hours of operation
        hours_of_operation = float(input("Enter the hours of operation: "))
        if hours_of_operation <= 0:
            raise ValueError("Hours of operation must be greater than 0.")

        # Calculate energy consumption for XT400
        xt400_energy_per_kg = calculate_energy_consumption(
            xt400_power_kw, xt400_processing_capacity_kg_per_hour, hours_of_operation
        )

        # Calculate energy consumption for XT500
        xt500_energy_per_kg = calculate_energy_consumption(
            xt500_power_kw, xt500_processing_capacity_kg_per_hour, hours_of_operation
        )

        # Display results
        print("\nEnergy Consumption Comparison:")
        print(f"XT400: {xt400_energy_per_kg:.4f} kWh/kg")
        print(f"XT500: {xt500_energy_per_kg:.4f} kWh/kg")

        # Determine the more energy-efficient model
        if xt400_energy_per_kg < xt500_energy_per_kg:
            print("The XT400 is more energy-efficient.")
        elif xt500_energy_per_kg < xt400_energy_per_kg:
            print("The XT500 is more energy-efficient.")
        else:
            print("Both models have the same energy efficiency.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
