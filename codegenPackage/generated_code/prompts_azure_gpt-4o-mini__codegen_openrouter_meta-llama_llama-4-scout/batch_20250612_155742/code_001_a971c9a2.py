"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a Python script that calculates potential energy savings from installing commercial spray foam insulation based on user input for building size and energy costs.
Generated: DETERMINISTIC_a971c9a2b70b80dc
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Calculates potential energy savings from installing commercial spray foam insulation.

Author: [Your Name]
Date: [Today's Date]
"""

def get_user_input():
    """
    Gets user input for building size and energy costs.

    Returns:
        tuple: Building size in square feet, current energy cost per square foot, 
               and proposed energy cost per square foot after insulation.
    """
    try:
        building_size_sf = float(input("Enter building size in square feet: "))
        current_energy_cost_sf = float(input("Enter current energy cost per square foot: $"))
        proposed_energy_cost_sf = float(input("Enter proposed energy cost per square foot after insulation: $"))
        return building_size_sf, current_energy_cost_sf, proposed_energy_cost_sf
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()


def calculate_energy_savings(building_size_sf, current_energy_cost_sf, proposed_energy_cost_sf):
    """
    Calculates potential energy savings.

    Args:
        building_size_sf (float): Building size in square feet.
        current_energy_cost_sf (float): Current energy cost per square foot.
        proposed_energy_cost_sf (float): Proposed energy cost per square foot after insulation.

    Returns:
        tuple: Current annual energy cost, proposed annual energy cost, and potential annual energy savings.
    """
    # Assume 12 months of energy usage per year
    current_annual_energy_cost = building_size_sf * current_energy_cost_sf * 12
    proposed_annual_energy_cost = building_size_sf * proposed_energy_cost_sf * 12
    potential_annual_energy_savings = current_annual_energy_cost - proposed_annual_energy_cost
    return current_annual_energy_cost, proposed_annual_energy_cost, potential_annual_energy_savings


def main():
    building_size_sf, current_energy_cost_sf, proposed_energy_cost_sf = get_user_input()
    current_annual_energy_cost, proposed_annual_energy_cost, potential_annual_energy_savings = calculate_energy_savings(
        building_size_sf, current_energy_cost_sf, proposed_energy_cost_sf)

    print("\nEnergy Savings Analysis:")
    print("-------------------------")
    print(f"Building Size: {building_size_sf:.2f} sqft")
    print(f"Current Energy Cost: ${current_energy_cost_sf:.2f}/sqft/month")
    print(f"Proposed Energy Cost: ${proposed_energy_cost_sf:.2f}/sqft/month")
    print(f"Current Annual Energy Cost: ${current_annual_energy_cost:.2f}")
    print(f"Proposed Annual Energy Cost: ${proposed_annual_energy_cost:.2f}")
    print(f"Potential Annual Energy Savings: ${potential_annual_energy_savings:.2f}")


if __name__ == "__main__":
    main()
```
