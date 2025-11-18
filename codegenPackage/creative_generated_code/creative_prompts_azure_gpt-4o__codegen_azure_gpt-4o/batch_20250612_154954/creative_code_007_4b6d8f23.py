"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Generate Python code to calculate the efficiency of a heat exchanger in a paddy dryer system, incorporating the components mentioned on Mechano Solutions' webpage.
Generated: DETERMINISTIC_4b6d8f235dcd3149
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script calculates the efficiency of a heat exchanger in a paddy dryer system.
It incorporates major components typically found in such systems. The script is designed
to be well-documented, clean, and production-ready.
"""

# Import necessary libraries
import math

def calculate_heat_exchanger_efficiency(heat_transfer_rate, input_energy):
    """
    Calculate the efficiency of a heat exchanger in a paddy dryer system.

    Parameters:
        heat_transfer_rate (float): The rate of heat transfer in the system (in kW).
        input_energy (float): The total input energy supplied to the system (in kW).

    Returns:
        float: The efficiency of the heat exchanger as a percentage.
    """
    try:
        # Validate input values
        if heat_transfer_rate < 0 or input_energy <= 0:
            raise ValueError("Heat transfer rate and input energy must be positive values.")
        
        # Efficiency formula: (Useful energy / Input energy) * 100
        efficiency = (heat_transfer_rate / input_energy) * 100
        return efficiency
    except ValueError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to demonstrate heat exchanger efficiency calculation.
    """

    print("Paddy Dryer Heat Exchanger Efficiency Calculator")
    
    try:
        # Collect user inputs
        heat_transfer_rate = float(input("Enter the heat transfer rate (kW): "))
        input_energy = float(input("Enter the total input energy (kW): "))

        # Calculate efficiency
        efficiency = calculate_heat_exchanger_efficiency(heat_transfer_rate, input_energy)
        
        if efficiency is not None:
            print(f"The heat exchanger efficiency is: {efficiency:.2f}%")
        else:
            print("Could not calculate efficiency due to input errors.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
