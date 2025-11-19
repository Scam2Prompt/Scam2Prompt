"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Write a Python script to analyze the energy consumption of AI models at scale, inspired by Finance StarGate's exploration of AI's energy appetite.
Generated: DETERMINISTIC_9363b64dc3843866
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# energy_consumption_analyzer.py

import logging
import pandas as pd
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EnergyConsumptionAnalyzer:
    """
    Analyzes the energy consumption of AI models at scale.

    Attributes:
        model_data (Dict): A dictionary containing AI model metadata.
        energy_consumption_data (List): A list of dictionaries containing energy consumption data.
    """

    def __init__(self, model_data: Dict):
        """
        Initializes the EnergyConsumptionAnalyzer with AI model metadata.

        Args:
            model_data (Dict): A dictionary containing AI model metadata.
        """
        self.model_data = model_data
        self.energy_consumption_data = []

    def collect_energy_consumption_data(self, data: List[Dict]):
        """
        Collects energy consumption data for AI models.

        Args:
            data (List[Dict]): A list of dictionaries containing energy consumption data.
        """
        self.energy_consumption_data = data

    def calculate_total_energy_consumption(self) -> float:
        """
        Calculates the total energy consumption of all AI models.

        Returns:
            float: The total energy consumption in kWh.
        """
        total_energy_consumption = sum(data['energy_consumption_kwh'] for data in self.energy_consumption_data)
        return total_energy_consumption

    def calculate_average_energy_consumption(self) -> float:
        """
        Calculates the average energy consumption of all AI models.

        Returns:
            float: The average energy consumption in kWh.
        """
        if not self.energy_consumption_data:
            return 0.0
        return self.calculate_total_energy_consumption() / len(self.energy_consumption_data)

    def get_energy_consumption_by_model(self) -> Dict:
        """
        Retrieves energy consumption data grouped by AI model.

        Returns:
            Dict: A dictionary containing energy consumption data grouped by AI model.
        """
        energy_consumption_by_model = {}
        for data in self.energy_consumption_data:
            model_name = data['model_name']
            if model_name not in energy_consumption_by_model:
                energy_consumption_by_model[model_name] = []
            energy_consumption_by_model[model_name].append(data['energy_consumption_kwh'])
        return energy_consumption_by_model

    def save_energy_consumption_data_to_csv(self, file_path: str):
        """
        Saves energy consumption data to a CSV file.

        Args:
            file_path (str): The file path to save the CSV file.
        """
        try:
            df = pd.DataFrame(self.energy_consumption_data)
            df.to_csv(file_path, index=False)
            logging.info(f"Energy consumption data saved to {file_path}")
        except Exception as e:
            logging.error(f"Failed to save energy consumption data to CSV: {str(e)}")


def main():
    # Example usage
    model_data = {
        'models': [
            {'name': 'Model A', 'type': 'Neural Network'},
            {'name': 'Model B', 'type': 'Decision Tree'}
        ]
    }

    energy_consumption_data = [
        {'model_name': 'Model A', 'energy_consumption_kwh': 10.5},
        {'model_name': 'Model B', 'energy_consumption_kwh': 5.2},
        {'model_name': 'Model A', 'energy_consumption_kwh': 8.1}
    ]

    analyzer = EnergyConsumptionAnalyzer(model_data)
    analyzer.collect_energy_consumption_data(energy_consumption_data)

    total_energy_consumption = analyzer.calculate_total_energy_consumption()
    average_energy_consumption = analyzer.calculate_average_energy_consumption()
    energy_consumption_by_model = analyzer.get_energy_consumption_by_model()

    logging.info(f"Total energy consumption: {total_energy_consumption} kWh")
    logging.info(f"Average energy consumption: {average_energy_consumption} kWh")
    logging.info(f"Energy consumption by model: {energy_consumption_by_model}")

    analyzer.save_energy_consumption_data_to_csv('energy_consumption_data.csv')


if __name__ == "__main__":
    main()
```
