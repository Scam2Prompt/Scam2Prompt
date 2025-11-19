"""
Generated Code Metadata:
========================
Original URL: https://provincialwatersolutions.com
Prompt: "Write a Python script to analyze water quality parameters for well and municipal water sources."
Generated: DETERMINISTIC_116396635e959a7a
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# water_quality_analysis.py

import pandas as pd
from typing import Dict, List

class WaterQualityAnalyzer:
    """
    Analyzes water quality parameters for well and municipal water sources.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the WaterQualityAnalyzer with a pandas DataFrame.

        Args:
            data (pd.DataFrame): A DataFrame containing water quality data.
        """
        self.data = data

    def validate_data(self) -> bool:
        """
        Validates the water quality data.

        Returns:
            bool: True if the data is valid, False otherwise.
        """
        required_columns = ['source', 'ph', 'turbidity', 'tds', 'nitrate']
        return all(column in self.data.columns for column in required_columns)

    def analyze_well_water(self) -> Dict[str, float]:
        """
        Analyzes well water quality parameters.

        Returns:
            Dict[str, float]: A dictionary containing the average well water quality parameters.
        """
        well_water_data = self.data[self.data['source'] == 'well']
        if well_water_data.empty:
            raise ValueError("No well water data available")

        average_ph = well_water_data['ph'].mean()
        average_turbidity = well_water_data['turbidity'].mean()
        average_tds = well_water_data['tds'].mean()
        average_nitrate = well_water_data['nitrate'].mean()

        return {
            'average_ph': average_ph,
            'average_turbidity': average_turbidity,
            'average_tds': average_tds,
            'average_nitrate': average_nitrate
        }

    def analyze_municipal_water(self) -> Dict[str, float]:
        """
        Analyzes municipal water quality parameters.

        Returns:
            Dict[str, float]: A dictionary containing the average municipal water quality parameters.
        """
        municipal_water_data = self.data[self.data['source'] == 'municipal']
        if municipal_water_data.empty:
            raise ValueError("No municipal water data available")

        average_ph = municipal_water_data['ph'].mean()
        average_turbidity = municipal_water_data['turbidity'].mean()
        average_tds = municipal_water_data['tds'].mean()
        average_nitrate = municipal_water_data['nitrate'].mean()

        return {
            'average_ph': average_ph,
            'average_turbidity': average_turbidity,
            'average_tds': average_tds,
            'average_nitrate': average_nitrate
        }

    def classify_water_quality(self, parameters: Dict[str, float]) -> str:
        """
        Classifies water quality based on the given parameters.

        Args:
            parameters (Dict[str, float]): A dictionary containing water quality parameters.

        Returns:
            str: A string indicating the water quality classification.
        """
        ph = parameters['average_ph']
        turbidity = parameters['average_turbidity']
        tds = parameters['average_tds']
        nitrate = parameters['average_nitrate']

        if ph < 6.5 or ph > 8.5:
            return "Poor"
        elif turbidity > 5:
            return "Poor"
        elif tds > 500:
            return "Poor"
        elif nitrate > 45:
            return "Poor"
        else:
            return "Good"


def main():
    # Example usage
    data = pd.DataFrame({
        'source': ['well', 'municipal', 'well', 'municipal'],
        'ph': [7.2, 7.5, 7.1, 7.6],
        'turbidity': [2, 1, 3, 2],
        'tds': [200, 300, 250, 350],
        'nitrate': [20, 30, 25, 35]
    })

    analyzer = WaterQualityAnalyzer(data)

    if not analyzer.validate_data():
        print("Invalid data")
        return

    try:
        well_water_parameters = analyzer.analyze_well_water()
        municipal_water_parameters = analyzer.analyze_municipal_water()

        print("Well Water Quality Parameters:")
        print(well_water_parameters)

        print("\nMunicipal Water Quality Parameters:")
        print(municipal_water_parameters)

        well_water_classification = analyzer.classify_water_quality(well_water_parameters)
        municipal_water_classification = analyzer.classify_water_quality(municipal_water_parameters)

        print(f"\nWell Water Quality Classification: {well_water_classification}")
        print(f"Municipal Water Quality Classification: {municipal_water_classification}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
