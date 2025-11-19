"""
Generated Code Metadata:
========================
Original URL: https://id.stromkonto.net
Prompt: Write a script to calculate the energy factor (Wh/kg) for a given set of energy generation and usage data, using the formulas provided by Stromkonto Grünstrom Konto.
Generated: DETERMINISTIC_a4e1b596723128d5
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class EnergyFactorCalculator:
    """
    A class to calculate the energy factor (Wh/kg) based on energy generation and usage data.
    """

    def __init__(self, generation_data: pd.DataFrame, usage_data: pd.DataFrame):
        """
        Initializes the EnergyFactorCalculator with generation and usage data.

        :param generation_data: DataFrame containing energy generation data with 'energy_generated' column (in Wh)
        :param usage_data: DataFrame containing energy usage data with 'energy_used' column (in Wh)
        """
        self.generation_data = generation_data
        self.usage_data = usage_data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the required columns and data types.
        Raises ValueError if validation fails.
        """
        required_columns = ['energy_generated', 'energy_used']
        for column in required_columns:
            if column not in self.generation_data.columns or column not in self.usage_data.columns:
                raise ValueError(f"Missing required column: {column}")

        if not all(pd.api.types.is_numeric_dtype(self.generation_data[column]) for column in required_columns):
            raise ValueError("All required columns must be numeric.")

    def calculate_energy_factor(self) -> float:
        """
        Calculates the energy factor (Wh/kg) based on the provided generation and usage data.

        :return: The calculated energy factor (Wh/kg)
        """
        self.validate_data()

        total_generated = self.generation_data['energy_generated'].sum()
        total_used = self.usage_data['energy_used'].sum()

        if total_used == 0:
            raise ValueError("Total energy used cannot be zero to avoid division by zero.")

        energy_factor = total_generated / total_used
        return energy_factor

def main():
    """
    Main function to execute the energy factor calculation.
    """
    # Sample data for demonstration purposes
    generation_data = pd.DataFrame({
        'energy_generated': [1000, 2000, 1500]  # in Wh
    })

    usage_data = pd.DataFrame({
        'energy_used': [800, 1200, 1000]  # in Wh
    })

    try:
        calculator = EnergyFactorCalculator(generation_data, usage_data)
        energy_factor = calculator.calculate_energy_factor()
        print(f"Calculated Energy Factor: {energy_factor:.2f} Wh/kg")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
