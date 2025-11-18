"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cartoansurperu.com
Prompt: Generate a script to simulate the environmental impact of using 100% recycled corrugated cardboard for packaging, as described in the Cartonerías Andinas del Sur product specifications.
Generated: DETERMINISTIC_458f72e84df7fd50
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Constants representing environmental factors
CARBON_EMISSIONS_PER_TON = 1.5  # Metric tons of CO2 produced per ton of production
WATER_USAGE_PER_TON = 5000     # Liters of water used per ton of production
ENERGY_USAGE_PER_TON = 3000    # kWh used per ton of production

# Factors for 100% recycled cardboard (reduced metrics vs new production)
CARBON_EMISSIONS_REDUCED_PERCENTAGE = 70  # 70% reduction in emissions
WATER_USAGE_REDUCED_PERCENTAGE = 50      # 50% reduction in water usage
ENERGY_USAGE_REDUCED_PERCENTAGE = 60     # 60% reduction in energy usage

def simulate_environmental_impact(weight_in_tons):
    """
    Simulates the environmental impact of using 100% recycled corrugated cardboard packaging.
    :param weight_in_tons: The weight of the recycled cardboard produced in tons.
    :return: A dictionary containing environmental statistics for the recycled cardboard production.
    """
    try:
        # Validate input
        if weight_in_tons <= 0:
            raise ValueError("Weight in tons must be a positive number.")

        # Calculate metrics for new cardboard production
        carbon_emissions_new = weight_in_tons * CARBON_EMISSIONS_PER_TON
        water_usage_new = weight_in_tons * WATER_USAGE_PER_TON
        energy_usage_new = weight_in_tons * ENERGY_USAGE_PER_TON

        # Calculate metrics for 100% recycled cardboard production
        carbon_emissions_recycled = carbon_emissions_new * (1 - CARBON_EMISSIONS_REDUCED_PERCENTAGE / 100)
        water_usage_recycled = water_usage_new * (1 - WATER_USAGE_REDUCED_PERCENTAGE / 100)
        energy_usage_recycled = energy_usage_new * (1 - ENERGY_USAGE_REDUCED_PERCENTAGE / 100)

        # Calculate savings
        carbon_savings = carbon_emissions_new - carbon_emissions_recycled
        water_savings = water_usage_new - water_usage_recycled
        energy_savings = energy_usage_new - energy_usage_recycled

        # Compile results
        results = {
            "new_production": {
                "carbon_emissions": carbon_emissions_new,
                "water_usage": water_usage_new,
                "energy_usage": energy_usage_new
            },
            "recycled_production": {
                "carbon_emissions": carbon_emissions_recycled,
                "water_usage": water_usage_recycled,
                "energy_usage": energy_usage_recycled
            },
            "savings": {
                "carbon_emissions_saved": carbon_savings,
                "water_usage_saved": water_savings,
                "energy_usage_saved": energy_savings
            }
        }

        return results
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function to execute the simulation and display results.
    """
    try:
        # Input weight of recycled cardboard in tons
        weight_in_tons = float(input("Enter the weight of recycled cardboard in tons: "))

        # Simulate environmental impact
        impact_results = simulate_environmental_impact(weight_in_tons)

        if impact_results:
            # Format and display results
            print("\nEnvironmental Impact Simulation Results:")
            print(json.dumps(impact_results, indent=4))
    except ValueError:
        print("Please enter a valid numeric value for the weight.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
