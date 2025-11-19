"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jusoor.ch
Prompt: Develop a data visualization tool that displays the impact of humanitarian interventions, similar to the metrics provided by Jusoor International.
Generated: DETERMINISTIC_a38ea387d182ed46
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for a data visualization tool based on the request. It uses `matplotlib` for visualization and includes error handling for input data and file operations.

```python
import pandas as pd
import matplotlib.pyplot as plt
import os

class HumanitarianImpactVisualizer:
    """
    A tool to visualize the impact of humanitarian interventions.
    Metrics are displayed in bar charts and pie charts to show distributions.
    """

    def __init__(self, data_file):
        """
        Initialize the visualizer with the data file.

        :param data_file: Path to the CSV file containing intervention data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Load data from a CSV file.

        Ensures the file exists and handles errors during loading.
        """
        if not os.path.exists(self.data_file):
            raise FileNotFoundError(f"Data file not found: {self.data_file}")

        try:
            self.data = pd.read_csv(self.data_file)
        except Exception as e:
            raise ValueError(f"Failed to load data: {e}")

        # Validate essential columns exist
        required_columns = ['Intervention', 'Impact', 'Region']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def visualize_impact_by_intervention(self):
        """
        Generate a bar chart to show the impact of each intervention.
        """
        try:
            intervention_data = self.data.groupby('Intervention')['Impact'].sum()
            plt.figure(figsize=(10, 6))
            intervention_data.plot(kind='bar', color='skyblue')
            plt.title("Impact by Intervention", fontsize=16)
            plt.xlabel("Intervention", fontsize=14)
            plt.ylabel("Impact", fontsize=14)
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error visualizing impact by intervention: {e}")

    def visualize_impact_distribution_by_region(self):
        """
        Generate a pie chart to show the distribution of impacts across regions.
        """
        try:
            region_data = self.data.groupby('Region')['Impact'].sum()
            plt.figure(figsize=(8, 8))
            region_data.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
            plt.title("Impact Distribution by Region", fontsize=16)
            plt.ylabel("")
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error visualizing impact distribution by region: {e}")

def main():
    """
    Main function to run the visualization tool.
    """
    # Specify the path to the CSV file containing intervention data
    data_file = 'intervention_data.csv'

    # Create the visualizer instance
    visualizer = HumanitarianImpactVisualizer(data_file)

    try:
        # Load the data
        visualizer.load_data()

        # Generate visualizations
        print("Generating visualizations...")
        visualizer.visualize_impact_by_intervention()
        visualizer.visualize_impact_distribution_by_region()
        print("Visualizations completed.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Features:
- **Input CSV File Format**: The tool expects a CSV file with columns `Intervention`, `Impact`, and `Region`.
- **Error Handling**: Includes checks for file existence, readable format, and mandatory columns.
- **Visualization**: Uses bar and pie charts to represent intervention impacts and regional distributions.
- **Scalability**: Designed for extensibility and easy integration with other tools.

Ensure you install necessary dependencies:
```bash
pip install pandas matplotlib
```
