"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Provide a Python implementation to calculate the cost-effectiveness of using VinaRoy FB200 air blowers in cement production processes.
Generated: DETERMINISTIC_fff473b73e9cd7d2
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
Module to calculate the cost-effectiveness of using VinaRoy FB200 air blowers 
in cement production processes. The program calculates the cost-effectiveness 
based on user-provided inputs such as energy consumption, production output, 
and cost per unit energy.
"""

# Import necessary modules
import sys

def calculate_cost_effectiveness(energy_consumption, production_output, cost_per_unit_energy):
    """
    Calculate the cost-effectiveness of using VinaRoy FB200 air blowers.

    :param energy_consumption: Energy consumed by the air blower in kilowatt-hours (kWh).
    :param production_output: Cement production output in metric tons.
    :param cost_per_unit_energy: Cost per unit energy in currency per kilowatt-hour.
    :return: Cost-effectiveness metric as cost per metric ton of cement produced.
    """
    try:
        # Validate inputs
        if energy_consumption <= 0:
            raise ValueError("Energy consumption must be greater than zero.")
        if production_output <= 0:
            raise ValueError("Production output must be greater than zero.")
        if cost_per_unit_energy <= 0:
            raise ValueError("Cost per unit energy must be greater than zero.")
        
        # Calculate total energy cost
        total_energy_cost = energy_consumption * cost_per_unit_energy
        
        # Calculate cost-effectiveness
        cost_effectiveness = total_energy_cost / production_output
        return cost_effectiveness

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to interact with the user and calculate the cost-effectiveness.
    """
    print("VinaRoy FB200 Air Blower Cost-Effectiveness Calculator")
    try:
        # Get user inputs
        energy_consumption = float(input("Enter the energy consumption in kWh: "))
        production_output = float(input("Enter the cement production output in metric tons: "))
        cost_per_unit_energy = float(input("Enter the cost per unit energy in currency/kWh: "))
        
        # Calculate cost-effectiveness
        result = calculate_cost_effectiveness(energy_consumption, production_output, cost_per_unit_energy)
        
        if result is not None:
            print(f"Cost-effectiveness: {result:.2f} currency/ton of cement.")
        else:
            print("Failed to calculate cost-effectiveness due to invalid inputs.")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Entry point of the program
    main()
```
