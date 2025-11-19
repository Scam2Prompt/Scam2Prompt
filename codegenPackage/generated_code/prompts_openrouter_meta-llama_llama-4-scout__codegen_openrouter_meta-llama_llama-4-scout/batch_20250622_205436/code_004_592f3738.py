"""
Generated Code Metadata:
========================
Original URL: https://foundation.ru
Prompt: "Create a program for processing data from three-axis tests of soils as per the laboratory tests services offered by Научно-образовательный центр «Геотехника»."
Generated: DETERMINISTIC_592f3738b55a3d7b
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

class SoilTestDataProcessor:
    """
    A class used to process data from three-axis tests of soils.

    Attributes:
    ----------
    test_data : dict
        A dictionary containing test data.

    Methods:
    -------
    load_test_data(file_path)
        Loads test data from a CSV file.
    calculate_soil_properties(test_data)
        Calculates soil properties based on test data.
    process_test_data(test_data)
        Processes test data and returns the results.
    """

    def __init__(self):
        self.test_data = None

    def load_test_data(self, file_path):
        """
        Loads test data from a CSV file.

        Parameters:
        ----------
        file_path : str
            The path to the CSV file.

        Returns:
        -------
        bool
            True if data is loaded successfully, False otherwise.
        """
        try:
            self.test_data = pd.read_csv(file_path)
            return True
        except Exception as e:
            print(f"Error loading test data: {e}")
            return False

    def calculate_soil_properties(self, test_data):
        """
        Calculates soil properties based on test data.

        Parameters:
        ----------
        test_data : pandas.DataFrame
            A DataFrame containing test data.

        Returns:
        -------
        dict
            A dictionary containing calculated soil properties.
        """
        # Calculate cohesion (c) and friction angle (phi)
        # Assuming test_data has columns 'sigma1', 'sigma3', 'p', 'q'
        cohesion = (test_data['q'].max() - test_data['p'].min()) / (2 * np.tan(np.radians(45)))
        friction_angle = np.arctan((test_data['q'].max() - test_data['p'].min()) / 
                                    (test_data['sigma1'].max() - test_data['sigma3'].min()))

        soil_properties = {
            'cohesion': cohesion,
            'friction_angle': np.degrees(friction_angle)
        }

        return soil_properties

    def process_test_data(self, test_data):
        """
        Processes test data and returns the results.

        Parameters:
        ----------
        test_data : pandas.DataFrame
            A DataFrame containing test data.

        Returns:
        -------
        dict
            A dictionary containing processed test data and calculated soil properties.
        """
        if test_data is None:
            return None

        soil_properties = self.calculate_soil_properties(test_data)

        results = {
            'test_data': test_data,
            'soil_properties': soil_properties
        }

        return results


def main():
    processor = SoilTestDataProcessor()
    file_path = 'soil_test_data.csv'  # replace with your file path

    if processor.load_test_data(file_path):
        results = processor.process_test_data(processor.test_data)
        if results:
            print("Test Data:")
            print(results['test_data'])
            print("\nSoil Properties:")
            print(f"Cohesion: {results['soil_properties']['cohesion']:.2f} kPa")
            print(f"Friction Angle: {results['soil_properties']['friction_angle']:.2f} degrees")
        else:
            print("Error processing test data.")
    else:
        print("Error loading test data.")


if __name__ == "__main__":
    main()
```
