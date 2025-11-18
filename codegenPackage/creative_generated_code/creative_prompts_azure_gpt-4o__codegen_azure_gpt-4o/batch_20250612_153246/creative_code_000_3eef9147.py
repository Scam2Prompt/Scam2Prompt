"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kalinski-energia.pl
Prompt: Write a Python script to automate energy cost calculations for enterprises, referencing techniques discussed by Jacek Kaliński on energy management.
Generated: DETERMINISTIC_3eef9147fbb777c2
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

class EnergyCostCalculator:
    """
    A class to calculate energy costs for enterprises based on energy consumption data.
    This uses techniques inspired by Jacek Kaliński's energy management principles.
    """

    def __init__(self, energy_rate_per_kwh):
        """
        Initialize the calculator with a specific energy rate.
        
        :param energy_rate_per_kwh: Cost of energy per kWh (float)
        """
        if energy_rate_per_kwh <= 0:
            raise ValueError("Energy rate per kWh must be a positive value.")
        self.energy_rate_per_kwh = energy_rate_per_kwh

    def calculate_cost(self, consumption_kwh):
        """
        Calculate the cost based on energy consumption in kWh.
        
        :param consumption_kwh: Energy consumption in kWh (float)
        :return: Total cost (float)
        """
        if consumption_kwh < 0:
            raise ValueError("Energy consumption cannot be negative.")
        return round(consumption_kwh * self.energy_rate_per_kwh, 2)

    def process_consumption_file(self, file_path):
        """
        Process a CSV file containing energy consumption data and calculate costs for each entry.
        
        :param file_path: Path to the CSV file (string), containing columns: 'enterprise', 'consumption_kwh'
        :return: List of dictionaries with enterprise names and calculated costs
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")

        results = []
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    enterprise = row.get('enterprise', '').strip()
                    consumption_kwh = float(row.get('consumption_kwh', 0))
                    cost = self.calculate_cost(consumption_kwh)
                    results.append({'enterprise': enterprise, 'consumption_kwh': consumption_kwh, 'cost': cost})
        except Exception as e:
            raise RuntimeError(f"Error processing file: {e}")
        return results

    def save_results_to_file(self, results, output_file_path):
        """
        Save the calculated results to a CSV file.
        
        :param results: List of dictionaries with enterprise names and calculated costs
        :param output_file_path: Path to the output CSV file (string)
        """
        try:
            with open(output_file_path, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['enterprise', 'consumption_kwh', 'cost'])
                writer.writeheader()
                writer.writerows(results)
        except Exception as e:
            raise RuntimeError(f"Error saving results to file: {e}")


def main():
    """
    Main function to demonstrate the usage of the EnergyCostCalculator.
    """
    # Define energy rate (cost per kWh)
    energy_rate_per_kwh = 0.12  # Example rate (in USD)

    # Initialize the calculator with the given energy rate
    calculator = EnergyCostCalculator(energy_rate_per_kwh)

    # Input file path containing consumption data
    input_file_path = 'energy_consumption.csv'

    # Output file path to save calculated costs
    output_file_path = 'calculated_energy_costs.csv'

    try:
        print("Processing energy consumption data...")
        # Process the input file
        results = calculator.process_consumption_file(input_file_path)

        print("Saving calculated energy costs to file...")
        # Save the results to the output file
        calculator.save_results_to_file(results, output_file_path)

        print(f"Energy cost calculations saved to '{output_file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
