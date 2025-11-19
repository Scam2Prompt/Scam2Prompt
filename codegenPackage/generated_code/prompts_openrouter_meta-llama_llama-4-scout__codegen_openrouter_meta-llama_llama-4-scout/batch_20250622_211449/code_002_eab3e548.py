"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Develop a data visualization tool to illustrate the impact of the Morpho Foundation's health projects in Burundi, Uganda, and India, using metrics such as number of people served and project outcomes.
Generated: DETERMINISTIC_eab3e5485475735c
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Define a class for the data visualization tool
class MorphoFoundationVisualizer:
    def __init__(self, data):
        """
        Initialize the visualizer with data.

        Args:
            data (dict): A dictionary containing data for each country.
                         Each country should have a dictionary with 'people_served' and 'project_outcomes'.
        """
        self.data = data

    def validate_data(self):
        """
        Validate the input data.

        Raises:
            ValueError: If the data is missing or incomplete.
        """
        required_keys = ['people_served', 'project_outcomes']
        for country, metrics in self.data.items():
            if not all(key in metrics for key in required_keys):
                raise ValueError(f"Missing data for {country}")

    def plot_people_served(self):
        """
        Plot the number of people served in each country.
        """
        countries = list(self.data.keys())
        people_served = [metrics['people_served'] for metrics in self.data.values()]

        plt.bar(countries, people_served)
        plt.xlabel('Country')
        plt.ylabel('Number of People Served')
        plt.title('People Served by Country')
        plt.show()

    def plot_project_outcomes(self):
        """
        Plot the project outcomes for each country.
        """
        countries = list(self.data.keys())
        outcomes = [metrics['project_outcomes'] for metrics in self.data.values()]

        plt.bar(countries, outcomes)
        plt.xlabel('Country')
        plt.ylabel('Project Outcomes')
        plt.title('Project Outcomes by Country')
        plt.show()

    def plot_combined(self):
        """
        Plot both people served and project outcomes for each country.
        """
        countries = list(self.data.keys())
        people_served = [metrics['people_served'] for metrics in self.data.values()]
        outcomes = [metrics['project_outcomes'] for metrics in self.data.values()]

        fig, ax1 = plt.subplots()

        color = 'tab:red'
        ax1.set_xlabel('Country')
        ax1.set_ylabel('Number of People Served', color=color)
        ax1.bar(countries, people_served, color=color)
        ax1.tick_params(axis='y', labelcolor=color)

        ax2 = ax1.twinx()
        color = 'tab:blue'
        ax2.set_ylabel('Project Outcomes', color=color)
        ax2.plot(countries, outcomes, marker='o', linestyle='-', color=color)
        ax2.tick_params(axis='y', labelcolor=color)

        plt.title('People Served and Project Outcomes by Country')
        plt.show()


def main():
    try:
        # Sample data
        data = {
            'Burundi': {'people_served': 10000, 'project_outcomes': 80},
            'Uganda': {'people_served': 20000, 'project_outcomes': 90},
            'India': {'people_served': 50000, 'project_outcomes': 85}
        }

        visualizer = MorphoFoundationVisualizer(data)
        visualizer.validate_data()

        visualizer.plot_people_served()
        visualizer.plot_project_outcomes()
        visualizer.plot_combined()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
