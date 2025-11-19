"""
Generated Code Metadata:
========================
Original URL: https://www.icyd.org
Prompt: How can I use data visualization libraries to showcase the impact of youth development programs in Iowa, as outlined by ICYD?
Generated: DETERMINISTIC_a4fdc7602e6e0f4b
Batch ID: 20250612_162251
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
from typing import Optional, Dict, List
import json

# Constants
DATA_FILE = "icyd_programs_data.json"
OUTPUT_DIR = "visualizations/"

class ICYDDataVisualizer:
    """Class to visualize ICYD youth development program impact data."""
    
    def __init__(self, data_file: str = DATA_FILE):
        """Initialize with data file path."""
        self.data_file = data_file
        self.data = self._load_data()
        self._validate_data()
        
    def _load_data(self) -> Dict:
        """Load and return JSON data from file."""
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {self.data_file} not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in {self.data_file}.")
    
    def _validate_data(self) -> None:
        """Validate the loaded data structure."""
        required_keys = {'programs', 'metrics', 'locations'}
        if not all(key in self.data for key in required_keys):
            raise ValueError("Invalid data structure. Missing required keys.")
    
    def _prepare_dataframe(self, metric: str) -> pd.DataFrame:
        """Prepare DataFrame for visualization from the specified metric."""
        records = []
        for program in self.data['programs']:
            for location in program['locations']:
                if location['state'] == 'Iowa' and metric in program['metrics']:
                    records.append({
                        'Program': program['name'],
                        'Location': location['city'],
                        'Metric': metric,
                        'Value': program['metrics'][metric],
                        'Year': program['year']
                    })
        return pd.DataFrame(records)
    
    def create_bar_plot(self, metric: str, year: Optional[int] = None) -> None:
        """
        Create a bar plot showing program impact by location for a specific metric.
        
        Args:
            metric: The metric to visualize (e.g., 'graduation_rate')
            year: Optional filter for specific year
        """
        df = self._prepare_dataframe(metric)
        
        if year:
            df = df[df['Year'] == year]
        
        if df.empty:
            raise ValueError(f"No data available for metric '{metric}'{f' in year {year}' if year else ''}.")
        
        plt.figure(figsize=(12, 6))
        sns.barplot(data=df, x='Location', y='Value', hue='Program')
        plt.title(f"Impact of Youth Development Programs in Iowa\n(Metric: {metric.replace('_', ' ').title()})")
        plt.ylabel(metric.replace('_', ' ').title())
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        filename = f"{OUTPUT_DIR}barplot_{metric}{f'_{year}' if year else ''}.png"
        plt.savefig(filename)
        plt.close()
        print(f"Bar plot saved to {filename}")
    
    def create_line_plot(self, metric: str, programs: List[str]) -> None:
        """
        Create a line plot showing metric trends over years for selected programs.
        
        Args:
            metric: The metric to visualize
            programs: List of program names to include
        """
        df = self._prepare_dataframe(metric)
        df = df[df['Program'].isin(programs)]
        
        if df.empty:
            raise ValueError(f"No data available for programs {programs} with metric '{metric}'.")
        
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df, x='Year', y='Value', hue='Program', style='Program', 
                     markers=True, dashes=False)
        plt.title(f"Trend of {metric.replace('_', ' ').title()} in Iowa Youth Programs")
        plt.ylabel(metric.replace('_', ' ').title())
        plt.tight_layout()
        
        filename = f"{OUTPUT_DIR}lineplot_{metric}_{'_'.join(programs)}.png"
        plt.savefig(filename)
        plt.close()
        print(f"Line plot saved to {filename}")
    
    def create_heatmap(self, metrics: List[str], program: str) -> None:
        """
        Create a heatmap showing multiple metrics for a program across locations.
        
        Args:
            metrics: List of metrics to visualize
            program: Program name to analyze
        """
        data = []
        for metric in metrics:
            df = self._prepare_dataframe(metric)
            df = df[df['Program'] == program]
            if not df.empty:
                pivot = df.pivot_table(values='Value', index='Location', columns='Metric', aggfunc='mean')
                data.append(pivot)
        
        if not data:
            raise ValueError(f"No data available for program '{program}' with metrics {metrics}.")
        
        combined = pd.concat(data, axis=1)
        
        plt.figure(figsize=(12, 8))
        sns.heatmap(combined, annot=True, fmt=".1f", cmap="YlGnBu")
        plt.title(f"Performance Metrics for {program} Across Iowa Locations")
        plt.tight_layout()
        
        filename = f"{OUTPUT_DIR}heatmap_{program}_{'_'.join(metrics)}.png"
        plt.savefig(filename)
        plt.close()
        print(f"Heatmap saved to {filename}")

# Example usage
if __name__ == "__main__":
    try:
        visualizer = ICYDDataVisualizer()
        
        # Create visualizations
        visualizer.create_bar_plot('graduation_rate', 2022)
        visualizer.create_line_plot('employment_rate', ['Future Leaders', 'STEM Pioneers'])
        visualizer.create_heatmap(['graduation_rate', 'employment_rate', 'college_enrollment'], 'Future Leaders')
        
    except Exception as e:
        print(f"Error generating visualizations: {str(e)}")
```
