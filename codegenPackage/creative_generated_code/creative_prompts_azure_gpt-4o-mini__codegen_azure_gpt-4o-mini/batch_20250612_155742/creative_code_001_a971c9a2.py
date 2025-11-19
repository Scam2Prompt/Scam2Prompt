"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a Python script that calculates potential energy savings from installing commercial spray foam insulation based on user input for building size and energy costs.
Generated: DETERMINISTIC_a971c9a2b70b80dc
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# potential_energy_savings.py

def calculate_energy_savings(building_size, energy_cost, insulation_efficiency):
    """
    Calculate potential energy savings from installing commercial spray foam insulation.

    Parameters:
    building_size (float): Size of the building in square feet.
    energy_cost (float): Cost of energy per kilowatt-hour.
    insulation_efficiency (float): Estimated percentage of energy savings from insulation (0-100).

    Returns:
    float: Estimated annual energy savings in dollars.
    """
    # Validate inputs
    if building_size <= 0:
        raise ValueError("Building size must be greater than zero.")
    if energy_cost < 0:
        raise ValueError("Energy cost cannot be negative.")
    if insulation_efficiency < 0 or insulation_efficiency > 100:
        raise ValueError("Insulation efficiency must be between 0 and 100.")

    # Constant: estimated energy consumption per square foot per year for uninsulated building
    energy_consumption_per_sqft = 15  # kWh/sqft/year

    # Calculate total energy consumption
    total_energy_consumption = building_size * energy_consumption_per_sqft

    # Calculate potential energy savings
    annual_savings = total_energy_consumption * (insulation_efficiency / 100) * energy_cost

    return annual_savings


def main():
    """
    Main function to execute the energy savings calculation based on user input.
    """
    try:
        # User input for building size
        building_size = float(input("Enter the building size in square feet: "))

        # User input for energy cost
        energy_cost = float(input("Enter the energy cost per kilowatt-hour: $"))

        # User input for insulation efficiency
        insulation_efficiency = float(input("Enter estimated insulation efficiency (0-100%): "))

        # Calculate potential energy savings
        savings = calculate_energy_savings(building_size, energy_cost, insulation_efficiency)

        # Display the results
        print(f"Estimated annual energy savings: ${savings:.2f}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
