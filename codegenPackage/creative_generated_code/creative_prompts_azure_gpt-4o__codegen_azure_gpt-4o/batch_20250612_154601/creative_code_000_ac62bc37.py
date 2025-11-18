"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Write Python code to calculate the energy efficiency (A++) of an air conditioning system based on the specifications provided for the Gree Bora A4 Silver series on the Frigoterm website.
Generated: DETERMINISTIC_ac62bc37a77328e6
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script calculates the energy efficiency rating (A++) of an air conditioning system.
The calculation is based on the specifications of the Gree Bora A4 Silver series.
Ensure that the data inputs match the specifications provided on the Frigoterm website.
"""

# Import necessary modules
import sys

def calculate_energy_efficiency(cooling_capacity, power_consumption):
    """
    Calculates the energy efficiency ratio (EER) for cooling and determines the rating.
    
    Parameters:
        cooling_capacity (float): Cooling capacity in watts (W).
        power_consumption (float): Power consumption in watts (W).
        
    Returns:
        str: Energy efficiency rating.
    """
    try:
        if cooling_capacity <= 0 or power_consumption <= 0:
            raise ValueError("Cooling capacity and power consumption must be greater than zero.")
        
        # Calculate EER (Energy Efficiency Ratio)
        eer = cooling_capacity / power_consumption
        
        # Determine the energy efficiency rating based on EER value
        if eer >= 3.2:
            return "A++"
        elif 2.6 <= eer < 3.2:
            return "A+"
        elif 2.0 <= eer < 2.6:
            return "A"
        else:
            return "B or lower (Not efficient)"
    except Exception as e:
        raise ValueError(f"Error calculating energy efficiency: {e}")

def main():
    """
    Main entry point of the program. Retrieves user input and calculates the energy efficiency rating.
    """
    try:
        # Prompt user for cooling capacity and power consumption
        print("Enter the specifications for the air conditioning system:")
        cooling_capacity = float(input("Cooling capacity (in watts): "))
        power_consumption = float(input("Power consumption (in watts): "))
        
        # Calculate energy efficiency rating
        rating = calculate_energy_efficiency(cooling_capacity, power_consumption)
        
        # Display the results
        print(f"The energy efficiency rating of the air conditioning system is: {rating}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Run the main program
    main()
```
