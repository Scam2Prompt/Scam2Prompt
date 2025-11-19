"""
Generated Code Metadata:
========================
Original URL: https://brosbel.pe
Prompt: Develop a program to track the performance of Brosbel Agro's bioestimulantes, such as "Algakelp," in improving the health of orange and avocado crops, based on field data.
Generated: DETERMINISTIC_732bdc83667efafc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
import numpy as np
from datetime import datetime

class CropPerformanceTracker:
    """
    A class to track the performance of bioestimulantes in improving crop health.

    Attributes:
    ----------
    crop_data : dict
        A dictionary to store crop data with crop name as key and a list of dictionaries as value.
        Each dictionary in the list contains 'date', 'health_score', and 'bioestimulante' used.

    Methods:
    -------
    add_crop_data(crop_name, date, health_score, bioestimulante)
        Adds data for a specific crop.
    get_crop_data(crop_name)
        Retrieves data for a specific crop.
    calculate_improvement(crop_name, bioestimulante)
        Calculates the average improvement in health score for a crop using a specific bioestimulante.
    """

    def __init__(self):
        self.crop_data = {}

    def add_crop_data(self, crop_name, date, health_score, bioestimulante):
        """
        Adds data for a specific crop.

        Parameters:
        ----------
        crop_name : str
            The name of the crop.
        date : str
            The date of data collection in 'YYYY-MM-DD' format.
        health_score : float
            The health score of the crop.
        bioestimulante : str
            The bioestimulante used.

        Raises:
        ------
        ValueError
            If the date is not in 'YYYY-MM-DD' format.
        """
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Date must be in 'YYYY-MM-DD' format")

        if crop_name not in self.crop_data:
            self.crop_data[crop_name] = []

        self.crop_data[crop_name].append({
            'date': date,
            'health_score': health_score,
            'bioestimulante': bioestimulante
        })

    def get_crop_data(self, crop_name):
        """
        Retrieves data for a specific crop.

        Parameters:
        ----------
        crop_name : str
            The name of the crop.

        Returns:
        -------
        list
            A list of dictionaries containing data for the specified crop.

        Raises:
        ------
        KeyError
            If the crop name is not found.
        """
        try:
            return self.crop_data[crop_name]
        except KeyError:
            raise KeyError("Crop not found")

    def calculate_improvement(self, crop_name, bioestimulante):
        """
        Calculates the average improvement in health score for a crop using a specific bioestimulante.

        Parameters:
        ----------
        crop_name : str
            The name of the crop.
        bioestimulante : str
            The bioestimulante used.

        Returns:
        -------
        float
            The average improvement in health score.

        Raises:
        ------
        KeyError
            If the crop name is not found.
        ValueError
            If no data is found for the specified crop and bioestimulante.
        """
        try:
            crop_data = self.crop_data[crop_name]
        except KeyError:
            raise KeyError("Crop not found")

        bioestimulante_data = [data for data in crop_data if data['bioestimulante'] == bioestimulante]

        if not bioestimulante_data:
            raise ValueError("No data found for the specified crop and bioestimulante")

        health_scores = [data['health_score'] for data in bioestimulante_data]
        average_health_score = np.mean(health_scores)

        # Assuming the baseline health score is 50
        baseline_health_score = 50
        average_improvement = average_health_score - baseline_health_score

        return average_improvement


def main():
    tracker = CropPerformanceTracker()

    # Add data for orange crops
    tracker.add_crop_data('orange', '2022-01-01', 70, 'Algakelp')
    tracker.add_crop_data('orange', '2022-02-01', 80, 'Algakelp')
    tracker.add_crop_data('orange', '2022-03-01', 90, 'Algakelp')

    # Add data for avocado crops
    tracker.add_crop_data('avocado', '2022-01-01', 60, 'Algakelp')
    tracker.add_crop_data('avocado', '2022-02-01', 75, 'Algakelp')
    tracker.add_crop_data('avocado', '2022-03-01', 85, 'Algakelp')

    # Calculate improvement for orange crops using Algakelp
    try:
        improvement = tracker.calculate_improvement('orange', 'Algakelp')
        print(f"The average improvement in health score for orange crops using Algakelp is {improvement}")
    except (KeyError, ValueError) as e:
        print(e)

    # Calculate improvement for avocado crops using Algakelp
    try:
        improvement = tracker.calculate_improvement('avocado', 'Algakelp')
        print(f"The average improvement in health score for avocado crops using Algakelp is {improvement}")
    except (KeyError, ValueError) as e:
        print(e)


if __name__ == "__main__":
    main()
```
