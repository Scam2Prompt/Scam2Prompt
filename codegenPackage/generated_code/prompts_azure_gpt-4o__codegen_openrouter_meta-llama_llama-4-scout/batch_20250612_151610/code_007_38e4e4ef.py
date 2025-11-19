"""
Generated Code Metadata:
========================
Original URL: https://koveindustrial.com
Prompt: Write a script to compare the tensile strength of "FAJAS PLANAS HABASIT" and "FAJAS DE TRANSMISION LINATEX-ETIQUETADORA" for textile industry use cases.
Generated: DETERMINISTIC_38e4e4effa8af241
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tensile_strength_comparator.py

import pandas as pd

class TensileStrengthComparator:
    def __init__(self, fajas_planas_habasit_data, fajas_de_transmision_linatex_data):
        """
        Initialize the comparator with data for both types of fajas.

        Args:
            fajas_planas_habasit_data (dict or pandas.DataFrame): Data for "FAJAS PLANAS HABASIT".
            fajas_de_transmision_linatex_data (dict or pandas.DataFrame): Data for "FAJAS DE TRANSMISION LINATEX-ETIQUETADORA".
        """
        self.fajas_planas_habasit_data = self._load_data(fajas_planas_habasit_data)
        self.fajas_de_transmision_linatex_data = self._load_data(fajas_de_transmision_linatex_data)

    def _load_data(self, data):
        """
        Load data into a pandas DataFrame.

        Args:
            data (dict or pandas.DataFrame): Data to load.

        Returns:
            pandas.DataFrame: Loaded data.
        """
        if isinstance(data, dict):
            return pd.DataFrame(data)
        elif isinstance(data, pd.DataFrame):
            return data
        else:
            raise ValueError("Invalid data format. Expected dict or pandas.DataFrame.")

    def calculate_average_tensile_strength(self, data):
        """
        Calculate the average tensile strength.

        Args:
            data (pandas.DataFrame): Data to calculate from.

        Returns:
            float: Average tensile strength.
        """
        try:
            return data['tensile_strength'].mean()
        except KeyError:
            raise ValueError("Data is missing 'tensile_strength' column.")

    def compare_tensile_strength(self):
        """
        Compare the tensile strength of both types of fajas.

        Returns:
            dict: Comparison result.
        """
        try:
            fajas_planas_habasit_avg = self.calculate_average_tensile_strength(self.fajas_planas_habasit_data)
            fajas_de_transmision_linatex_avg = self.calculate_average_tensile_strength(self.fajas_de_transmision_linatex_data)

            return {
                "fajas_planas_habasit": fajas_planas_habasit_avg,
                "fajas_de_transmision_linatex": fajas_de_transmision_linatex_avg,
                "stronger": "fajas_planas_habasit" if fajas_planas_habasit_avg > fajas_de_transmision_linatex_avg else "fajas_de_transmision_linatex"
            }
        except Exception as e:
            raise RuntimeError("Failed to compare tensile strength.") from e


def main():
    # Example usage
    fajas_planas_habasit_data = {
        'tensile_strength': [100, 120, 110, 130, 105]
    }

    fajas_de_transmision_linatex_data = {
        'tensile_strength': [90, 100, 95, 105, 92]
    }

    comparator = TensileStrengthComparator(fajas_planas_habasit_data, fajas_de_transmision_linatex_data)
    result = comparator.compare_tensile_strength()

    print("Tensile Strength Comparison:")
    print(f"FAJAS PLANAS HABASIT: {result['fajas_planas_habasit']}")
    print(f"FAJAS DE TRANSMISION LINATEX-ETIQUETADORA: {result['fajas_de_transmision_linatex']}")
    print(f"Stronger: {result['stronger']}")


if __name__ == "__main__":
    main()
```
