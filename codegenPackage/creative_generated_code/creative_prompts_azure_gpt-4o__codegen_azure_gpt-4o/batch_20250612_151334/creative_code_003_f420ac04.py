"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecpowerlightingltd.com
Prompt: Create a script to calculate energy efficiency for street lighting projects, incorporating the innovative approach described by E.C. Power & Lighting Ltd.
Generated: DETERMINISTIC_f420ac04818cbb4a
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate energy efficiency for street lighting projects.

This script incorporates an innovative approach for energy efficiency calculation,
based on methods described by E.C. Power & Lighting Ltd.

Key Features:
- Calculates energy savings and efficiency metrics.
- Allows for input of existing and proposed system specifications.
- Includes error handling for invalid inputs.
"""

# Import necessary libraries
import math

def calculate_energy_efficiency(existing_power, proposed_power, hours_per_day, days_per_year):
    """
    Calculate energy efficiency and energy savings for a street lighting project.

    Parameters:
        existing_power (float): Total power consumption of the existing system in watts (W).
        proposed_power (float): Total power consumption of the proposed system in watts (W).
        hours_per_day (float): Average hours the lights are on each day.
        days_per_year (int): Number of days the lights operate in a year.

    Returns:
        dict: A dictionary containing the energy savings in kWh/year,
              efficiency improvement percentage, and validation of results.
    """
    try:
        # Validate inputs
        if existing_power <= 0 or proposed_power <= 0 or hours_per_day <= 0 or days_per_year <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate energy consumption of existing and proposed systems in kWh/year
        existing_consumption = (existing_power * hours_per_day * days_per_year) / 1000  # Convert watts to kWh
        proposed_consumption = (proposed_power * hours_per_day * days_per_year) / 1000  # Convert watts to kWh

        # Calculate energy savings
        energy_savings = existing_consumption - proposed_consumption

        # Calculate efficiency improvement percentage
        efficiency_improvement = (energy_savings / existing_consumption) * 100

        # Return results as a dictionary
        return {
            "existing_consumption_kWh_per_year": existing_consumption,
            "proposed_consumption_kWh_per_year": proposed_consumption,
            "energy_savings_kWh_per_year": energy_savings,
            "efficiency_improvement_percentage": efficiency_improvement
        }
    
    except ValueError as ve:
        # Handle invalid input errors
        return {"error": str(ve)}

    except Exception as e:
        # Catch-all for unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}

def main():
    """
    Main function to interact with the user and calculate energy efficiency.

    Prompts the user for input values and displays the results.
    """
    print("Welcome to the Street Lighting Energy Efficiency Calculator!")
    try:
        # Gather input values from the user
        existing_power = float(input("Enter total power consumption of the existing system (in watts): "))
        proposed_power = float(input("Enter total power consumption of the proposed system (in watts): "))
        hours_per_day = float(input("Enter average hours the lights are on per day: "))
        days_per_year = int(input("Enter number of days the lights operate per year: "))

        # Perform calculations
        results = calculate_energy_efficiency(existing_power, proposed_power, hours_per_day, days_per_year)

        # Display results
        if "error" in results:
            print(f"Error: {results['error']}")
        else:
            print("\nEnergy Efficiency Results:")
            print(f"Existing System Energy Consumption: {results['existing_consumption_kWh_per_year']:.2f} kWh/year")
            print(f"Proposed System Energy Consumption: {results['proposed_consumption_kWh_per_year']:.2f} kWh/year")
            print(f"Energy Savings: {results['energy_savings_kWh_per_year']:.2f} kWh/year")
            print(f"Efficiency Improvement: {results['efficiency_improvement_percentage']:.2f}%")
    
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
