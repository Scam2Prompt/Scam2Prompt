"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Create a program to track and visualize the environmental sustainability metrics for a biotech company, inspired by CSL Seqirus UK's sustainability initiatives.
Generated: DETERMINISTIC_47f130a3c0eaa834
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class SustainabilityTracker:
    """
    A class to track and visualize environmental sustainability metrics for a biotech company.
    Metrics include energy consumption, waste production, water usage, and carbon emissions.
    """

    def __init__(self, data_file: str = "sustainability_data.json"):
        """
        Initialize the tracker with a data file.
        
        Args:
            data_file (str): Path to the JSON file storing sustainability data.
        """
        self.data_file = data_file
        self.metrics = {
            "energy_consumption": {"unit": "kWh", "data": {}},
            "waste_production": {"unit": "kg", "data": {}},
            "water_usage": {"unit": "liters", "data": {}},
            "carbon_emissions": {"unit": "kg CO2", "data": {}}
        }
        self._load_data()

    def _load_data(self) -> None:
        """Load sustainability data from the JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for metric in self.metrics:
                    if metric in data:
                        self.metrics[metric]["data"] = data[metric]
        except FileNotFoundError:
            print(f"Warning: Data file '{self.data_file}' not found. Starting with empty dataset.")
        except json.JSONDecodeError:
            print(f"Error: Data file '{self.data_file}' is corrupted. Starting with empty dataset.")

    def _save_data(self) -> None:
        """Save sustainability data to the JSON file."""
        data_to_save = {metric: self.metrics[metric]["data"] for metric in self.metrics}
        try:
            with open(self.data_file, 'w') as file:
                json.dump(data_to_save, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def add_metric_entry(self, metric_name: str, date: str, value: float) -> bool:
        """
        Add a new entry for a specific metric.
        
        Args:
            metric_name (str): Name of the metric (e.g., 'energy_consumption').
            date (str): Date in YYYY-MM-DD format.
            value (float): Value of the metric.
            
        Returns:
            bool: True if the entry was added successfully, False otherwise.
        """
        if metric_name not in self.metrics:
            print(f"Error: Metric '{metric_name}' not found.")
            return False
        
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            return False
        
        if value < 0:
            print("Error: Value cannot be negative.")
            return False
        
        self.metrics[metric_name]["data"][date] = value
        self._save_data()
        return True

    def get_metric_data(self, metric_name: str) -> Optional[Dict[str, float]]:
        """
        Retrieve all data for a specific metric.
        
        Args:
            metric_name (str): Name of the metric.
            
        Returns:
            Optional[Dict[str, float]]: Dictionary of dates and values, or None if metric not found.
        """
        if metric_name not in self.metrics:
            print(f"Error: Metric '{metric_name}' not found.")
            return None
        return self.metrics[metric_name]["data"]

    def plot_metric(self, metric_name: str, save_path: Optional[str] = None) -> bool:
        """
        Plot the data for a specific metric.
        
        Args:
            metric_name (str): Name of the metric to plot.
            save_path (Optional[str]): Path to save the plot image. If None, plot is displayed.
            
        Returns:
            bool: True if the plot was generated successfully, False otherwise.
        """
        if metric_name not in self.metrics:
            print(f"Error: Metric '{metric_name}' not found.")
            return False
        
        data = self.metrics[metric_name]["data"]
        if not data:
            print(f"Error: No data available for metric '{metric_name}'.")
            return False
        
        dates = sorted(data.keys())
        values = [data[date] for date in dates]
        
        plt.figure(figsize=(10, 6))
        plt.plot(dates, values, marker='o')
        plt.title(f"{metric_name.replace('_', ' ').title()} Over Time")
        plt.xlabel("Date")
        plt.ylabel(f"{self.metrics[metric_name]['unit']}")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        
        if save_path:
            try:
                plt.savefig(save_path)
                plt.close()
            except Exception as e:
                print(f"Error saving plot: {e}")
                return False
        else:
            plt.show()
        
        return True

    def generate_sustainability_report(self, save_path: Optional[str] = None) -> bool:
        """
        Generate a comprehensive sustainability report with all metrics.
        
        Args:
            save_path (Optional[str]): Path to save the report. If None, report is printed to console.
            
        Returns:
            bool: True if the report was generated successfully, False otherwise.
        """
        report_lines = ["Sustainability Report", "====================", ""]
        
        for metric in self.metrics:
            data = self.metrics[metric]["data"]
            if not data:
                report_lines.append(f"{metric.replace('_', ' ').title()}: No data available.")
                continue
            
            latest_date = max(data.keys())
            latest_value = data[latest_date]
            unit = self.metrics[metric]["unit"]
            
            report_lines.append(f"{metric.replace('_', ' ').title()}:")
            report_lines.append(f"  Latest ({latest_date}): {latest_value} {unit}")
            report_lines.append(f"  Total entries: {len(data)}")
            report_lines.append("")
        
        report = "\n".join(report_lines)
        
        if save_path:
            try:
                with open(save_path, 'w') as file:
                    file.write(report)
            except IOError as e:
                print(f"Error saving report: {e}")
                return False
        else:
            print(report)
        
        return True


# Example usage
if __name__ == "__main__":
    tracker = SustainabilityTracker()
    
    # Add some sample data
    tracker.add_metric_entry("energy_consumption", "2023-01-01", 1500.5)
    tracker.add_metric_entry("energy_consumption", "2023-02-01", 1450.2)
    tracker.add_metric_entry("waste_production", "2023-01-01", 200.0)
    tracker.add_metric_entry("waste_production", "2023-02-01", 180.5)
    
    # Generate plots and reports
    tracker.plot_metric("energy_consumption")
    tracker.generate_sustainability_report()
```
