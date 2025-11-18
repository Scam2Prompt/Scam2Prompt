"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinaroy.com.vn
Prompt: Generate a script in Python to calculate the energy savings of using VinaRoy air blowers in wastewater treatment applications.
Generated: DETERMINISTIC_0647f4f61c311085
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
Script to calculate energy savings for VinaRoy air blowers in wastewater treatment applications.
This script takes user input for current energy usage and blower specifications and calculates
potential savings based on the efficiency of VinaRoy air blowers.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary libraries
import sys

def calculate_energy_savings(current_usage_kwh, vina_efficiency, current_efficiency):
    """
    Calculates the energy savings of switching to VinaRoy air blowers.
    
    Args:
        current_usage_kwh (float): Current energy usage in kWh.
        vina_efficiency (float): Efficiency of VinaRoy blowers (as a decimal, e.g., 0.85 for 85%).
        current_efficiency (float): Current blower efficiency (as a decimal, e.g., 0.70 for 70%).
    
    Returns:
        float: Estimated energy savings in kWh.
    """
    if current_efficiency <= 0 or vina_efficiency <= 0:
        raise ValueError("Efficiency values must be greater than zero.")
    
    # Calculate energy savings
    improved_usage_kwh = current_usage_kwh * (current_efficiency / vina_efficiency)
    savings_kwh = current_usage_kwh - improved_usage_kwh
    return savings_kwh

def main():
    """
    Main function to interact with the user and execute the energy savings calculation.
    """
    try:
        print("Welcome to the VinaRoy Air Blower Energy Savings Calculator!")
        
        # Get user input
        current_usage_kwh = float(input("Enter current energy usage in kWh: "))
        current_efficiency = float(input("Enter current blower efficiency (e.g., 0.70 for 70%): "))
        vina_efficiency = float(input("Enter VinaRoy blower efficiency (e.g., 0.85 for 85%): "))
        
        # Validate inputs
        if current_usage_kwh <= 0:
            raise ValueError("Current energy usage must be greater than zero.")
        if current_efficiency <= 0 or current_efficiency > 1:
            raise ValueError("Current efficiency must be a decimal between 0 and 1.")
        if vina_efficiency <= 0 or vina_efficiency > 1:
            raise ValueError("VinaRoy efficiency must be a decimal between 0 and 1.")
        
        # Calculate savings
        savings_kwh = calculate_energy_savings(current_usage_kwh, vina_efficiency, current_efficiency)
        print(f"Estimated energy savings: {savings_kwh:.2f} kWh")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the VinaRoy Energy Savings Calculator!")

# Entry point for the script
if __name__ == "__main__":
    main()
```
