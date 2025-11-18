"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sun-almamlaka.com
Prompt: Write code to calculate the cost-effectiveness of thermal and waterproof insulation for residential buildings, using the materials and methods discussed on the "شمس المملكة" website.
Generated: DETERMINISTIC_662a6db3e977b288
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class InsulationCostEffectiveness:
    """
    A class to calculate the cost-effectiveness of thermal and waterproof insulation
    for residential buildings based on user-defined parameters.
    """

    def __init__(self, thermal_cost_per_sqm, waterproof_cost_per_sqm, area_sqm):
        """
        Initializes the cost-effectiveness calculator with insulation costs and area.
        
        :param thermal_cost_per_sqm: Cost of thermal insulation per square meter
        :param waterproof_cost_per_sqm: Cost of waterproof insulation per square meter
        :param area_sqm: Area of the building in square meters
        """
        self.thermal_cost_per_sqm = thermal_cost_per_sqm
        self.waterproof_cost_per_sqm = waterproof_cost_per_sqm
        self.area_sqm = area_sqm

    def calculate_total_cost(self):
        """
        Calculates the total cost for thermal and waterproof insulation.
        
        :return: Total cost of both thermal and waterproof insulation
        """
        thermal_cost = self.thermal_cost_per_sqm * self.area_sqm
        waterproof_cost = self.waterproof_cost_per_sqm * self.area_sqm
        total_cost = thermal_cost + waterproof_cost
        return total_cost

    def calculate_cost_effectiveness(self):
        """
        Calculates the cost-effectiveness ratio for insulation materials.
        
        :return: Cost-effectiveness ratio (total cost / area)
        """
        total_cost = self.calculate_total_cost()
        cost_effectiveness = total_cost / self.area_sqm
        return cost_effectiveness

def main():
    """
    Main function to execute the cost-effectiveness calculation.
    """
    try:
        # User inputs for insulation costs and area
        thermal_cost_per_sqm = float(input("Enter the cost of thermal insulation per square meter: "))
        waterproof_cost_per_sqm = float(input("Enter the cost of waterproof insulation per square meter: "))
        area_sqm = float(input("Enter the area of the building in square meters: "))

        # Create an instance of InsulationCostEffectiveness
        insulation_calculator = InsulationCostEffectiveness(thermal_cost_per_sqm, waterproof_cost_per_sqm, area_sqm)

        # Calculate and display results
        total_cost = insulation_calculator.calculate_total_cost()
        cost_effectiveness = insulation_calculator.calculate_cost_effectiveness()

        print(f"Total Cost of Insulation: {total_cost:.2f} currency units")
        print(f"Cost-Effectiveness Ratio: {cost_effectiveness:.2f} currency units per square meter")

    except ValueError as e:
        print("Invalid input. Please enter numeric values for costs and area.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
