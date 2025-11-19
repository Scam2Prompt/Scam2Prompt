"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: "Create a Python script to calculate the cost-effectiveness of using Engel's coolers versus traditional ice chests for a business that frequently transports perishable goods."
Generated: DETERMINISTIC_3b0df2e63a3877d8
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_cost_effectiveness(engel_cost, engel_lifespan, engel_energy_cost, 
                                  ice_chest_cost, ice_chest_lifespan, ice_cost, trips_per_year):
    """
    Calculate the cost-effectiveness of Engel's coolers vs traditional ice chests.

    Parameters:
    - engel_cost (float): Initial cost of an Engel cooler.
    - engel_lifespan (int): Lifespan of an Engel cooler in years.
    - engel_energy_cost (float): Annual energy cost of using an Engel cooler.
    - ice_chest_cost (float): Initial cost of a traditional ice chest.
    - ice_chest_lifespan (int): Lifespan of a traditional ice chest in years.
    - ice_cost (float): Cost of ice per trip for a traditional ice chest.
    - trips_per_year (int): Number of trips per year.

    Returns:
    - dict: A dictionary containing the total cost for each option and the more cost-effective option.
    """
    try:
        # Calculate annualized cost for Engel cooler
        engel_annualized_cost = engel_cost / engel_lifespan
        engel_total_annual_cost = engel_annualized_cost + engel_energy_cost

        # Calculate annualized cost for traditional ice chest
        ice_chest_annualized_cost = ice_chest_cost / ice_chest_lifespan
        ice_chest_total_annual_cost = ice_chest_annualized_cost + (ice_cost * trips_per_year)

        # Determine the more cost-effective option
        if engel_total_annual_cost < ice_chest_total_annual_cost:
            more_cost_effective = "Engel Cooler"
        elif engel_total_annual_cost > ice_chest_total_annual_cost:
            more_cost_effective = "Traditional Ice Chest"
        else:
            more_cost_effective = "Both options are equally cost-effective"

        # Return results as a dictionary
        return {
            "engel_total_annual_cost": round(engel_total_annual_cost, 2),
            "ice_chest_total_annual_cost": round(ice_chest_total_annual_cost, 2),
            "more_cost_effective": more_cost_effective
        }
    except Exception as e:
        print(f"An error occurred during calculation: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to gather user input and calculate cost-effectiveness.
    """
    try:
        print("Enter the details for Engel's cooler:")
        engel_cost = float(input("Initial cost of Engel cooler ($): "))
        engel_lifespan = int(input("Lifespan of Engel cooler (years): "))
        engel_energy_cost = float(input("Annual energy cost of Engel cooler ($): "))

        print("\nEnter the details for the traditional ice chest:")
        ice_chest_cost = float(input("Initial cost of traditional ice chest ($): "))
        ice_chest_lifespan = int(input("Lifespan of traditional ice chest (years): "))
        ice_cost = float(input("Cost of ice per trip ($): "))
        trips_per_year = int(input("Number of trips per year: "))

        # Calculate cost-effectiveness
        result = calculate_cost_effectiveness(
            engel_cost, engel_lifespan, engel_energy_cost,
            ice_chest_cost, ice_chest_lifespan, ice_cost, trips_per_year
        )

        if result:
            print("\nCost-Effectiveness Analysis:")
            print(f"Total Annual Cost (Engel Cooler): ${result['engel_total_annual_cost']}")
            print(f"Total Annual Cost (Traditional Ice Chest): ${result['ice_chest_total_annual_cost']}")
            print(f"More Cost-Effective Option: {result['more_cost_effective']}")
        else:
            print("Failed to calculate cost-effectiveness. Please check your inputs.")
    except ValueError:
        print("Invalid input. Please enter numeric values where required.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
