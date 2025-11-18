"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerafricasolar.com
Prompt: Generate a program to calculate the environmental benefits of switching to solar energy, using Power Africa Solar's focus on clean and sustainable energy solutions.
Generated: DETERMINISTIC_d5615899d786c952
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to calculate the environmental benefits of switching to solar energy.
This program uses Power Africa Solar's focus on clean and sustainable energy solutions 
to estimate CO2 emissions saved and equivalent environmental impacts.
"""

# Import necessary libraries
import sys

def calculate_solar_benefits(energy_consumption_kwh, co2_emission_rate, solar_emission_rate):
    """
    Calculate the environmental benefits of switching to solar energy.

    Args:
        energy_consumption_kwh (float): Annual energy consumption in kilowatt-hours (kWh).
        co2_emission_rate (float): CO2 emissions per kWh for traditional energy sources (in kg CO2/kWh).
        solar_emission_rate (float): CO2 emissions per kWh for solar energy (in kg CO2/kWh).

    Returns:
        dict: A dictionary containing the total CO2 emissions saved and equivalent metrics.
    """
    # Validate input
    if energy_consumption_kwh < 0 or co2_emission_rate < 0 or solar_emission_rate < 0:
        raise ValueError("Energy consumption and emission rates must be non-negative numbers.")

    # Calculate the CO2 emissions for traditional energy sources
    co2_emissions_traditional = energy_consumption_kwh * co2_emission_rate

    # Calculate the CO2 emissions for solar energy sources
    co2_emissions_solar = energy_consumption_kwh * solar_emission_rate

    # Calculate the CO2 emissions saved
    co2_emissions_saved = co2_emissions_traditional - co2_emissions_solar

    # Calculate equivalent environmental metrics
    # For example, trees planted: 1 tree absorbs approximately 21 kg of CO2 per year
    trees_planted_equivalent = co2_emissions_saved / 21

    # Return results as a dictionary
    return {
        "co2_emissions_saved_kg": co2_emissions_saved,
        "trees_planted_equivalent": trees_planted_equivalent,
    }

def main():
    """
    Main function to interact with the user and calculate environmental benefits.
    """
    print("Welcome to the Solar Energy Environmental Benefits Calculator!")
    
    try:
        # Get user input
        energy_consumption_kwh = float(input("Enter annual energy consumption in kWh: "))
        co2_emission_rate = float(input("Enter CO2 emissions rate for traditional energy sources (kg CO2/kWh): "))
        solar_emission_rate = float(input("Enter CO2 emissions rate for solar energy (kg CO2/kWh): "))

        # Calculate the benefits
        benefits = calculate_solar_benefits(energy_consumption_kwh, co2_emission_rate, solar_emission_rate)

        # Display results
        print("\nEnvironmental Benefits of Switching to Solar Energy:")
        print(f"Total CO2 Emissions Saved: {benefits['co2_emissions_saved_kg']:.2f} kg")
        print(f"Equivalent Trees Planted: {benefits['trees_planted_equivalent']:.2f} trees")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Solar Energy Environmental Benefits Calculator. Goodbye!")

# Entry point of the program
if __name__ == "__main__":
    main()
```
