"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Write a script to calculate CO2 emissions savings based on energy usage and generation data, using the emission factor (g/kWh) provided by Stromkonto Grünstrom Konto.
Generated: DETERMINISTIC_3c374437944c6d4a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse

def calculate_co2_savings(energy_usage, energy_generation, emission_factor):
    """
    Calculate CO2 emissions savings based on energy usage, generation, and emission factor.

    Parameters:
    energy_usage (float): Total energy usage in kWh.
    energy_generation (float): Total green energy generation in kWh.
    emission_factor (float): CO2 emission factor in grams per kWh.

    Returns:
    float: CO2 emissions savings in grams.
    """
    # Ensure energy generation does not exceed energy usage
    green_energy_used = min(energy_usage, energy_generation)
    co2_savings = green_energy_used * emission_factor
    return co2_savings

def main():
    """
    Main function for handling input and calculating CO2 emissions savings.
    """
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Calculate CO2 emissions savings based on energy data and emission factor.")
    parser.add_argument("energy_usage", type=float, help="Total energy usage in kWh")
    parser.add_argument("energy_generation", type=float, help="Total green energy generation in kWh")
    parser.add_argument("emission_factor", type=float, help="CO2 emission factor (grams per kWh) provided by Stromkonto Grünstrom Konto")

    args = parser.parse_args()

    # Input validation
    if args.energy_usage < 0 or args.energy_generation < 0 or args.emission_factor < 0:
        print("Error: All input values must be non-negative.")
        return

    try:
        # Calculate CO2 savings
        savings = calculate_co2_savings(args.energy_usage, args.energy_generation, args.emission_factor)
        print(f"CO2 Emissions Savings: {savings:.2f} grams")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
