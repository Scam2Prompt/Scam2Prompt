"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigskyenergy.com.au
Prompt: Provide a Python script to analyze solar system performance using data from "performance analysis" and "detailed written reports" as described in Big Sky Energy's solar inspection services.
Generated: DETERMINISTIC_4dcaf3d0c7cdc536
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SolarSystemPerformanceAnalyzer:
    def __init__(self, performance_data_path, report_data_path):
        """
        Initialize the SolarSystemPerformanceAnalyzer with paths to the performance and report data.

        :param performance_data_path: Path to the CSV file containing performance analysis data
        :param report_data_path: Path to the CSV file containing detailed written reports
        """
        self.performance_data_path = performance_data_path
        self.report_data_path = report_data_path
        self.performance_data = None
        self.report_data = None

    def load_data(self):
        """Load the performance and report data from the specified CSV files."""
        try:
            self.performance_data = pd.read_csv(self.performance_data_path)
            logging.info("Performance data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading performance data: {e}")
            raise

        try:
            self.report_data = pd.read_csv(self.report_data_path)
            logging.info("Report data loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading report data: {e}")
            raise

    def analyze_performance(self):
        """Analyze the solar system performance based on loaded data."""
        if self.performance_data is None:
            logging.error("Performance data is not loaded. Please load the data first.")
            return

        try:
            # Calculate efficiency as a new column
            self.performance_data['Efficiency'] = (
                self.performance_data['EnergyProduced'] / self.performance_data['EnergyPotential']
            ) * 100  # Convert to percentage

            # Basic statistics on efficiency
            efficiency_mean = self.performance_data['Efficiency'].mean()
            efficiency_std = self.performance_data['Efficiency'].std()
            logging.info(f"Mean Efficiency: {efficiency_mean:.2f}%")
            logging.info(f"Efficiency Standard Deviation: {efficiency_std:.2f}%")

            return efficiency_mean, efficiency_std
        except Exception as e:
            logging.error(f"Error during performance analysis: {e}")
            raise

    def visualize_performance(self):
        """Visualize the performance data."""
        if self.performance_data is None:
            logging.error("Performance data is not loaded. Please load the data first.")
            return

        try:
            plt.figure(figsize=(10, 5))
            plt.plot(self.performance_data['Date'], self.performance_data['Efficiency'], marker='o')
            plt.title("Solar System Efficiency Over Time")
            plt.xlabel("Date")
            plt.ylabel("Efficiency (%)")
            plt.xticks(rotation=45)
            plt.grid()
            plt.tight_layout()
            plt.show()
            logging.info("Performance visualization displayed successfully.")
        except Exception as e:
            logging.error(f"Error during visualization: {e}")
            raise

    def generate_report(self, efficiency_mean, efficiency_std):
        """Generate a summary report of the performance analysis.

        :param efficiency_mean: Mean efficiency of the solar system
        :param efficiency_std: Standard deviation of the efficiency
        """
        report = (
            f"Solar System Performance Analysis Report\n"
            f"-----------------------------------------\n"
            f"Mean Efficiency: {efficiency_mean:.2f}%\n"
            f"Efficiency Standard Deviation: {efficiency_std:.2f}%\n"
            f"Total Records Analyzed: {len(self.performance_data)}\n"
        )
        with open("performance_report.txt", "w") as f:
            f.write(report)
            logging.info("Performance report generated and saved as 'performance_report.txt'.")

if __name__ == "__main__":
    # Example usage:
    analyzer = SolarSystemPerformanceAnalyzer('performance_analysis.csv', 'detailed_reports.csv')
    analyzer.load_data()
    mean_efficiency, std_efficiency = analyzer.analyze_performance()
    analyzer.visualize_performance()
    analyzer.generate_report(mean_efficiency, std_efficiency)
```
