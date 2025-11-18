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
import os
import pandas as pd
import json
import logging

# Set up logging for the application
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("solar_system_analysis.log"),
        logging.StreamHandler()
    ]
)

# Constants for file paths (modify these as needed)
PERFORMANCE_ANALYSIS_FILE = "performance_analysis.csv"
DETAILED_REPORTS_FILE = "detailed_reports.json"


class SolarSystemAnalyzer:
    """
    A class to analyze solar system performance using data from performance analysis
    and detailed reports.
    """

    def __init__(self, performance_file, reports_file):
        """
        Initializes the SolarSystemAnalyzer.

        Args:
            performance_file (str): Path to the CSV file containing performance analysis data.
            reports_file (str): Path to the JSON file containing detailed reports.
        """
        self.performance_file = performance_file
        self.reports_file = reports_file
        self.performance_data = None
        self.reports_data = None

    def load_data(self):
        """
        Loads data from the specified files.
        """
        try:
            # Load performance analysis data
            logging.info("Loading performance analysis data...")
            self.performance_data = pd.read_csv(self.performance_file)
            logging.info("Performance analysis data loaded successfully.")

            # Load detailed reports data
            logging.info("Loading detailed reports data...")
            with open(self.reports_file, 'r') as file:
                self.reports_data = json.load(file)
            logging.info("Detailed reports data loaded successfully.")

        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise
        except pd.errors.EmptyDataError as e:
            logging.error(f"Performance analysis file is empty or corrupt: {e}")
            raise
        except json.JSONDecodeError as e:
            logging.error(f"Failed to parse JSON file: {e}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred while loading files: {e}")
            raise

    def analyze_performance(self):
        """
        Analyze solar system performance using loaded data.

        Returns:
            dict: A dictionary containing analysis results.
        """
        if self.performance_data is None or self.reports_data is None:
            logging.error("Data has not been loaded. Call load_data() first.")
            raise RuntimeError("Data has not been loaded. Call load_data() first.")

        logging.info("Starting performance analysis...")

        # Example Analysis: Average Energy Output
        try:
            avg_energy_output = self.performance_data['EnergyOutput'].mean()
            logging.info(f"Calculated average energy output: {avg_energy_output}")
        except KeyError:
            logging.error("The column 'EnergyOutput' does not exist in the performance data.")
            raise

        # Example Analysis: System Status Insights
        try:
            status_counts = {status: self.reports_data.count(status) for status in set(self.reports_data)}
            logging.info("Calculated system status counts.")
        except Exception as e:
            logging.error(f"Error during detailed report analysis: {e}")
            raise

        logging.info("Performance analysis completed successfully.")
        return {
            "average_energy_output": avg_energy_output,
            "status_counts": status_counts
        }

    def save_analysis_results(self, results, output_file="analysis_results.json"):
        """
        Saves analysis results to a JSON file.

        Args:
            results (dict): The analysis results to save.
            output_file (str): Path to the output JSON file.
        """
        try:
            logging.info(f"Saving analysis results to {output_file}...")
            with open(output_file, 'w') as file:
                json.dump(results, file, indent=4)
            logging.info("Analysis results saved successfully.")
        except Exception as e:
            logging.error(f"Failed to save analysis results: {e}")
            raise


if __name__ == "__main__":
    # Main execution block
    try:
        # Initialize the analyzer with file paths
        analyzer = SolarSystemAnalyzer(PERFORMANCE_ANALYSIS_FILE, DETAILED_REPORTS_FILE)

        # Load data
        analyzer.load_data()

        # Perform analysis
        results = analyzer.analyze_performance()
        logging.info(f"Analysis Results: {results}")

        # Save results to a file
        analyzer.save_analysis_results(results)

    except Exception as e:
        logging.error(f"Application error: {e}")
        print(f"Application encountered an error: {e}")
```
