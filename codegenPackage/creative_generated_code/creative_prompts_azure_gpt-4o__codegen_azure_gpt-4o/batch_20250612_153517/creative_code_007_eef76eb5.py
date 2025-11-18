"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Generate code for calculating the efficiency of a CCHP (Combined Cooling, Heat, and Power) system, incorporating the technical specifications provided by پایش نیرو.
Generated: DETERMINISTIC_eef76eb55f66ea97
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module to calculate the efficiency of a CCHP (Combined Cooling, Heat, and Power) system.

This script uses the technical specifications provided by پایش نیرو to calculate
the overall system efficiency based on input energy and output energies (electricity, heat, and cooling).
"""

# Import necessary libraries
import sys

def calculate_cchp_efficiency(input_energy, electricity_output, heat_output, cooling_output):
    """
    Calculate the efficiency of a CCHP system based on input energy and output energies.

    Args:
        input_energy (float): Total input energy to the CCHP system (in kWh).
        electricity_output (float): Electricity generation output (in kWh).
        heat_output (float): Heat generation output (in kWh).
        cooling_output (float): Cooling generation output (in kWh).
    
    Returns:
        float: Overall efficiency of the CCHP system as a percentage.
    
    Raises:
        ValueError: If any energy value is negative.
    """
    # Validate inputs
    if any(value < 0 for value in [input_energy, electricity_output, heat_output, cooling_output]):
        raise ValueError("Energy values must be non-negative.")
    if input_energy == 0:
        raise ValueError("Input energy must be greater than zero to calculate efficiency.")
    
    # Calculate total useful output energy
    total_output_energy = electricity_output + heat_output + cooling_output
    
    # Calculate efficiency as a percentage
    efficiency = (total_output_energy / input_energy) * 100
    return efficiency

def main():
    """
    Main function to interact with the user and calculate CCHP system efficiency.
    """
    print("CCHP System Efficiency Calculator")
    print("Please provide the following energy values in kWh.")
    try:
        # Get user input
        input_energy = float(input("Enter total input energy to the system: "))
        electricity_output = float(input("Enter electricity generation output: "))
        heat_output = float(input("Enter heat generation output: "))
        cooling_output = float(input("Enter cooling generation output: "))
        
        # Calculate efficiency
        efficiency = calculate_cchp_efficiency(input_energy, electricity_output, heat_output, cooling_output)
        print(f"The overall efficiency of the CCHP system is: {efficiency:.2f}%")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
