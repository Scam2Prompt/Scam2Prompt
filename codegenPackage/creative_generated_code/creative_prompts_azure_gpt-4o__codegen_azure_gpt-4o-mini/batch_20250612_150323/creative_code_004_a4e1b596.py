"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: Write a script to calculate the energy factor (Wh/kg) for a given set of energy generation and usage data, using the formulas provided by Stromkonto Grünstrom Konto.
Generated: DETERMINISTIC_a4e1b596723128d5
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class EnergyFactorCalculator:
    """
    A class to calculate the energy factor (Wh/kg) based on energy generation 
    and usage data.
    """

    def __init__(self, generation_data, usage_data):
        """
        Initializes the EnergyFactorCalculator with generation and usage data.

        :param generation_data: DataFrame containing energy generation data.
        :param usage_data: DataFrame containing energy usage data.
        """
        self.generation_data = generation_data
        self.usage_data = usage_data

    def validate_data(self):
        """
        Validates the input data to ensure it contains necessary columns.

        :raises ValueError: If data is missing required columns.
        """
        required_gen_columns = {'date', 'energy_generated_wh', 'weight_kg'}
        required_usage_columns = {'date', 'energy_used_wh'}

        if not required_gen_columns.issubset(self.generation_data.columns):
            raise ValueError(f"Generation data must contain columns: {required_gen_columns}")
        if not required_usage_columns.issubset(self.usage_data.columns):
            raise ValueError(f"Usage data must contain columns: {required_usage_columns}")

    def calculate_energy_factor(self):
        """
        Calculates the energy factor (Wh/kg) for the given generation and usage data.

        :return: DataFrame containing date, energy factor (Wh/kg)
        """
        self.validate_data()

        # Merge generation and usage data on date
        merged_data = pd.merge(self.generation_data, self.usage_data, on='date', how='inner')

        # Calculate energy factor
        merged_data['energy_factor_wh_per_kg'] = (
            merged_data['energy_generated_wh'] / merged_data['weight_kg']
        ).clip(lower=0)  # Ensure non-negative values

        # Select relevant columns for output
        result = merged_data[['date', 'energy_factor_wh_per_kg']]
        return result

def main():
    # Example data for energy generation and usage
    generation_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'energy_generated_wh': [1000, 1500, 1200],
        'weight_kg': [50, 75, 60]
    })

    usage_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
        'energy_used_wh': [800, 1300, 1100]
    })

    # Instantiate the calculator
    calculator = EnergyFactorCalculator(generation_data, usage_data)
    
    try:
        # Calculate and print the energy factor
        energy_factor_result = calculator.calculate_energy_factor()
        print(energy_factor_result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
