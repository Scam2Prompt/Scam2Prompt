"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landoparafusos.blogspot.com
Prompt: Develop a program to compare the corrosion resistance of "Suporte L em Inox 304" versus other materials for long-term solar panel installations.
Generated: DETERMINISTIC_96037d2aca029a59
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python program to compare the corrosion resistance of "Suporte L em Inox 304" versus other materials for long-term solar panel installations:

```python
import datetime
import csv


class Material:
    """
    Represents a material with its corrosion resistance data.
    """

    def __init__(self, name, corrosion_rate_mm_per_year):
        """
        Initialize a material.

        :param name: Name of the material
        :param corrosion_rate_mm_per_year: Corrosion rate in mm/year
        """
        self.name = name
        self.corrosion_rate = corrosion_rate_mm_per_year


class CorrosionResistanceComparison:
    """
    Handles the comparison of corrosion resistance for different materials.
    """

    def __init__(self):
        """
        Initialize the comparison object.
        """
        self.materials = []

    def add_material(self, material):
        """
        Add a material to the list for comparison.

        :param material: Material object to be added
        """
        self.materials.append(material)

    def compare(self, years=20):
        """
        Compare the corrosion resistance of materials over a given number of years.

        :param years: Number of years for corrosion comparison (default is 20 years)
        :return: A sorted list of materials based on their corrosion depth over the given years
        """
        comparison_results = []
        for material in self.materials:
            total_corrosion_depth = material.corrosion_rate * years
            comparison_results.append(
                {"Material": material.name, "Total Corrosion Depth (mm)": total_corrosion_depth}
            )

        # Sort results based on corrosion depth (ascending)
        return sorted(comparison_results, key=lambda x: x["Total Corrosion Depth (mm)"])

    def export_results_to_csv(self, results, filename="corrosion_comparison_results.csv"):
        """
        Export the comparison results to a CSV file.

        :param results: Results to export
        :param filename: Name of the CSV file (default is 'corrosion_comparison_results.csv')
        """
        try:
            with open(filename, mode="w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["Material", "Total Corrosion Depth (mm)"])
                writer.writeheader()
                writer.writerows(results)
            print(f"Results successfully exported to {filename}")
        except Exception as e:
            print(f"Error exporting results to CSV: {e}")


def main():
    """
    Main function to execute the program.
    """
    # Initialize materials
    inox_304 = Material("Suporte L em Inox 304", corrosion_rate_mm_per_year=0.01)  # Example rate
    aluminum = Material("Aluminum", corrosion_rate_mm_per_year=0.05)
    galvanized_steel = Material("Galvanized Steel", corrosion_rate_mm_per_year=0.1)

    # Initialize comparison object
    comparison = CorrosionResistanceComparison()

    # Add materials for comparison
    comparison.add_material(inox_304)
    comparison.add_material(aluminum)
    comparison.add_material(galvanized_steel)

    # Perform comparison over 20 years
    results = comparison.compare(years=20)

    # Print results
    print("Corrosion Resistance Comparison Results (over 20 years):")
    for result in results:
        print(f"{result['Material']}: {result['Total Corrosion Depth (mm)']} mm")

    # Export results to a CSV file
    comparison.export_results_to_csv(results)


if __name__ == "__main__":
    main()
```
