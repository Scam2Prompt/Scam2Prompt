"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clibiya.com
Prompt: Generate code to calculate the environmental impact of recycling organic waste into protein, using Clibiya's recycling model as a reference.
Generated: DETERMINISTIC_356e78a455874afd
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math


class OrganicWasteRecyclingCalculator:
    """
    A class to calculate the environmental impact of recycling organic waste into protein
    using Clibiya's recycling model as a reference.
    """

    def __init__(self, waste_amount_kg, conversion_efficiency=0.4):
        """
        Initialize the calculator with waste amount and conversion efficiency.

        Args:
            waste_amount_kg (float): Amount of organic waste in kilograms.
            conversion_efficiency (float): Efficiency of converting waste to protein (default is 40%).
        """
        if waste_amount_kg <= 0:
            raise ValueError("Waste amount must be greater than 0.")
        if not (0 <= conversion_efficiency <= 1):
            raise ValueError("Conversion efficiency must be between 0 and 1.")

        self.waste_amount_kg = waste_amount_kg
        self.conversion_efficiency = conversion_efficiency

    def calculate_protein_output(self):
        """
        Calculate the amount of protein produced from recycling the waste.

        Returns:
            float: Protein output in kilograms.
        """
        return self.waste_amount_kg * self.conversion_efficiency

    def calculate_carbon_footprint_saved(self):
        """
        Calculate the carbon footprint saved by recycling organic waste into protein
        instead of disposing of it in a landfill.

        Returns:
            float: Carbon footprint saved in kilograms of CO2 equivalent.
        """
        landfill_emissions_per_kg = 0.25  # CO2 equivalent emitted per kg of organic waste in a landfill
        recycling_emissions_per_kg = 0.05  # CO2 equivalent emitted per kg of organic waste recycled

        landfill_emissions = self.waste_amount_kg * landfill_emissions_per_kg
        recycling_emissions = self.waste_amount_kg * recycling_emissions_per_kg

        return landfill_emissions - recycling_emissions

    def calculate_water_saved(self):
        """
        Calculate the amount of water saved by recycling organic waste into protein
        compared to traditional protein production methods.

        Returns:
            float: Water saved in liters.
        """
        traditional_protein_water_usage_per_kg = 15000  # Liters of water used per kg of traditional protein production
        recycled_protein_water_usage_per_kg = 300  # Liters of water used per kg of recycled protein production

        protein_output_kg = self.calculate_protein_output()
        traditional_water_usage = protein_output_kg * traditional_protein_water_usage_per_kg
        recycled_water_usage = protein_output_kg * recycled_protein_water_usage_per_kg

        return traditional_water_usage - recycled_water_usage

    def generate_report(self):
        """
        Generate a report summarizing the environmental impact.

        Returns:
            dict: Report containing protein output, carbon footprint saved, and water saved.
        """
        return {
            "Protein Output (kg)": self.calculate_protein_output(),
            "Carbon Footprint Saved (kg CO2 eq)": self.calculate_carbon_footprint_saved(),
            "Water Saved (liters)": self.calculate_water_saved(),
        }


def main():
    try:
        # Example values
        waste_amount_kg = float(input("Enter the amount of organic waste in kilograms: "))
        conversion_efficiency = float(input("Enter the conversion efficiency (0-1, default is 0.4): ") or 0.4)
        
        # Create an instance of the calculator
        calculator = OrganicWasteRecyclingCalculator(waste_amount_kg, conversion_efficiency)
        
        # Generate the environmental impact report
        report = calculator.generate_report()
        
        # Print the report
        print("\nEnvironmental Impact Report:")
        for key, value in report.items():
            print(f"{key}: {value}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
