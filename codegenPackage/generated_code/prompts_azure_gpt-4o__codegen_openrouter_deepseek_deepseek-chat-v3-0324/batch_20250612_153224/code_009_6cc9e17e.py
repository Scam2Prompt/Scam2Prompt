"""
Generated Code Metadata:
========================
Original URL: https://jusoor.ch
Prompt: Develop a program to visualize the impact of humanitarian interventions, using Jusoor International's reported statistics as a dataset.
Generated: DETERMINISTIC_6cc9e17e15c804b0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Optional

class HumanitarianInterventionVisualizer:
    """
    A class to visualize the impact of humanitarian interventions using Jusoor International's reported statistics.
    """

    def __init__(self, data_path: str):
        """
        Initialize the visualizer with data from a CSV file.

        Args:
            data_path (str): Path to the CSV file containing the intervention data.
        """
        try:
            self.data = pd.read_csv(data_path)
            self._validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found at path: {data_path}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")

    def _validate_data(self) -> None:
        """
        Validate the loaded data for required columns and data integrity.
        """
        required_columns = ['intervention', 'year', 'metric', 'value']
        for col in required_columns:
            if col not in self.data.columns:
                raise ValueError(f"Missing required column: {col}")

        if self.data.isnull().values.any():
            raise ValueError("Data contains missing values")

    def plot_intervention_impact(self, interventions: Optional[List[str]] = None) -> None:
        """
        Plot the impact of specified interventions over time.

        Args:
            interventions (List[str], optional): List of intervention names to plot. 
                If None, plots all interventions.
        """
        if interventions is None:
            interventions = self.data['intervention'].unique()

        plt.figure(figsize=(12, 8))
        sns.set_theme(style="whitegrid")

        for intervention in interventions:
            intervention_data = self.data[self.data['intervention'] == intervention]
            if intervention_data.empty:
                print(f"Warning: No data found for intervention '{intervention}'")
                continue

            sns.lineplot(
                data=intervention_data,
                x='year',
                y='value',
                hue='metric',
                style='metric',
                markers=True,
                dashes=False,
                label=intervention
            )

        plt.title('Impact of Humanitarian Interventions Over Time')
        plt.xlabel('Year')
        plt.ylabel('Impact Value')
        plt.legend(title='Intervention/Metric', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

    def plot_metric_comparison(self, metric: str) -> None:
        """
        Compare different interventions based on a specific metric.

        Args:
            metric (str): The metric to compare interventions by.
        """
        if metric not in self.data['metric'].unique():
            raise ValueError(f"Metric '{metric}' not found in data")

        metric_data = self.data[self.data['metric'] == metric]
        if metric_data.empty:
            raise ValueError(f"No data available for metric '{metric}'")

        plt.figure(figsize=(12, 8))
        sns.barplot(
            data=metric_data,
            x='value',
            y='intervention',
            hue='year',
            palette='viridis'
        )

        plt.title(f'Comparison of Interventions by {metric.capitalize()}')
        plt.xlabel(metric.capitalize())
        plt.ylabel('Intervention')
        plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()

    def save_plots(self, prefix: str = 'intervention_impact') -> None:
        """
        Save all generated plots to files.

        Args:
            prefix (str): Prefix for the saved plot filenames.
        """
        figures = [plt.figure(i) for i in plt.get_fignums()]
        for i, fig in enumerate(figures):
            fig.savefig(f"{prefix}_{i}.png", dpi=300, bbox_inches='tight')
        plt.close('all')

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your data path
        visualizer = HumanitarianInterventionVisualizer('jusoor_data.csv')
        
        # Plot all interventions
        visualizer.plot_intervention_impact()
        
        # Plot specific interventions
        visualizer.plot_intervention_impact(['Education Program', 'Healthcare Initiative'])
        
        # Compare by a specific metric
        visualizer.plot_metric_comparison('beneficiaries_reached')
        
        # Save all plots
        visualizer.save_plots()
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
