"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alu-air.com
Prompt: Write code to simulate the environmental impact reduction achieved by using alu-air© devices compared to traditional plastic-based solutions.
Generated: DETERMINISTIC_90a64955a469d3cd
Batch ID: 20250612_155002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class EnvironmentalImpactSimulator:
    """
    A class to simulate the environmental impact reduction achieved by using alu-air© devices
    compared to traditional plastic-based solutions.
    """

    def __init__(self, alu_air_emissions, plastic_emissions, items_replaced):
        """
        Initialize the simulator with emission data and the number of items replaced.

        :param alu_air_emissions: Emissions per alu-air© device (kg CO2 equivalent).
        :param plastic_emissions: Emissions per plastic-based item (kg CO2 equivalent).
        :param items_replaced: Number of plastic items replaced with alu-air© devices.
        """
        self.alu_air_emissions = alu_air_emissions
        self.plastic_emissions = plastic_emissions
        self.items_replaced = items_replaced

    def calculate_environmental_savings(self):
        """
        Calculate the environmental savings in terms of reduced emissions.

        :return: A dictionary containing total emissions for alu-air©,
                 total emissions for plastic-based solutions, and net savings.
        """
        try:
            alu_air_total = self.alu_air_emissions * self.items_replaced
            plastic_total = self.plastic_emissions * self.items_replaced
            savings = plastic_total - alu_air_total

            return {
                "alu_air_total_emissions": alu_air_total,
                "plastic_total_emissions": plastic_total,
                "net_savings": savings,
            }
        except Exception as e:
            raise ValueError(f"Error calculating environmental savings: {e}")

    def display_results(self, results):
        """
        Display the environmental impact comparison results.

        :param results: A dictionary containing the calculated results.
        """
        try:
            print("Environmental Impact Comparison:")
            print(f"Total emissions (alu-air© devices): {results['alu_air_total_emissions']} kg CO2")
            print(f"Total emissions (plastic-based items): {results['plastic_total_emissions']} kg CO2")
            print(f"Net savings: {results['net_savings']} kg CO2")
        except KeyError as e:
            raise ValueError(f"Missing key in results: {e}")

    def export_results_to_json(self, results, file_path):
        """
        Export the results to a JSON file.

        :param results: A dictionary containing the calculated results.
        :param file_path: Path to the JSON file where results will be saved.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(results, file, indent=4)
            print(f"Results successfully exported to {file_path}")
        except Exception as e:
            raise ValueError(f"Error exporting results to JSON: {e}")


if __name__ == "__main__":
    # Example values for emissions (kg CO2 equivalent per item)
    ALU_AIR_EMISSIONS = 1.5  # Example value for alu-air© devices
    PLASTIC_EMISSIONS = 5.0  # Example value for plastic-based items
    ITEMS_REPLACED = 1000    # Example number of plastic items replaced

    # Initialize simulator
    simulator = EnvironmentalImpactSimulator(ALU_AIR_EMISSIONS, PLASTIC_EMISSIONS, ITEMS_REPLACED)

    # Calculate savings
    results = simulator.calculate_environmental_savings()

    # Display results
    simulator.display_results(results)

    # Export results to JSON file
    OUTPUT_FILE_PATH = "environmental_savings.json"
    simulator.export_results_to_json(results, OUTPUT_FILE_PATH)
```
