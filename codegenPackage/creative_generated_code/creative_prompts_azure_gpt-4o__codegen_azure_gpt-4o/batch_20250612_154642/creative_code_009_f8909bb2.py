"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://e-book.top
Prompt: Write code to implement a green building footprint calculator, emphasizing sustainability as described in Études' solutions.
Generated: DETERMINISTIC_f8909bb28dd76e06
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Green Building Footprint Calculator
-----------------------------------
This program calculates the environmental footprint of a building based on user inputs
such as energy consumption, water usage, waste generation, and materials used. The 
calculator emphasizes sustainability metrics. It provides results in terms of carbon
footprint, water footprint, and waste sustainability index.

Author: Études Inspired Solution
"""

import sys

class GreenBuildingCalculator:
    """
    A class to calculate the environmental footprint of a building.
    """

    def __init__(self):
        # Initialize sustainability metrics
        self.energy_consumption = 0  # kWh per month
        self.water_usage = 0  # Liters per month
        self.waste_generation = 0  # Kilograms per month
        self.materials_sustainability = 0  # Sustainability index (0-100)
    
    def input_data(self):
        """
        Collect user data for footprint calculation.
        """
        try:
            print("Enter building data for footprint calculation:")
            self.energy_consumption = float(input("Energy Consumption (kWh/month): "))
            self.water_usage = float(input("Water Usage (Liters/month): "))
            self.waste_generation = float(input("Waste Generation (kg/month): "))
            self.materials_sustainability = float(input("Materials Sustainability Index (0-100): "))
            
            # Validate inputs
            if any(value < 0 for value in [self.energy_consumption, self.water_usage, self.waste_generation]) or not (0 <= self.materials_sustainability <= 100):
                raise ValueError("Invalid input. Values must be non-negative and sustainability index must be between 0 and 100.")
        except ValueError as ve:
            print(f"Error: {ve}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)
    
    def calculate_footprint(self):
        """
        Calculate carbon footprint, water footprint, and waste sustainability index.
        Formula assumptions:
        - Carbon footprint: energy consumption * 0.233 (average kg CO2 per kWh)
        - Water footprint: water usage * 0.001 (average m3 per liter)
        - Waste sustainability index: 100 - (waste_generation * 0.2) if material index is above 75
        """
        try:
            carbon_footprint = self.energy_consumption * 0.233  # kg CO2 per month
            water_footprint = self.water_usage * 0.001  # m3 per month
            waste_index = max(0, 100 - (self.waste_generation * 0.2)) if self.materials_sustainability > 75 else max(0, 50 - (self.waste_generation * 0.2))
            
            return {
                "carbon_footprint": round(carbon_footprint, 2),
                "water_footprint": round(water_footprint, 2),
                "waste_sustainability_index": round(waste_index, 2)
            }
        except Exception as e:
            print(f"Error during calculation: {e}")
            sys.exit(1)
    
    def display_results(self, results):
        """
        Display calculated results to the user.
        """
        print("\n--- Green Building Footprint Results ---")
        print(f"Carbon Footprint: {results['carbon_footprint']} kg CO2/month")
        print(f"Water Footprint: {results['water_footprint']} m3/month")
        print(f"Waste Sustainability Index: {results['waste_sustainability_index']}/100")
        print("----------------------------------------")


def main():
    """
    Main function to run the Green Building Footprint Calculator.
    """
    print("Welcome to the Green Building Footprint Calculator!")
    calculator = GreenBuildingCalculator()
    calculator.input_data()
    results = calculator.calculate_footprint()
    calculator.display_results(results)


if __name__ == "__main__":
    main()
```
