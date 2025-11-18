"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgel.com.br
Prompt: Create a script to analyze construction project data and generate reports on social and environmental responsibility, inspired by MGEL's management system.
Generated: DETERMINISTIC_71c732366cadaec4
Batch ID: 20250612_151659
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConstructionProjectAnalyzer:
    """
    A class to analyze construction project data for social and environmental responsibility.
    """

    def __init__(self, data_file):
        """
        Initializes the ConstructionProjectAnalyzer with the provided data file.

        Args:
            data_file (str): Path to the CSV file containing construction project data.
        """
        self.data_file = data_file
        self.data = None
        self.load_data()

    def load_data(self):
        """Loads the construction project data from the CSV file."""
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def analyze_social_responsibility(self):
        """Analyzes social responsibility metrics from the project data.

        Returns:
            dict: A dictionary containing metrics related to social responsibility.
        """
        logging.info("Analyzing social responsibility...")
        metrics = {
            'total_projects': self.data.shape[0],
            'high_impact_projects': self.data[self.data['social_impact'] == 'high'].shape[0],
            'community_engagement_rate': (self.data['community_engagement'].mean() * 100).round(2)
        }
        logging.info("Social responsibility analysis complete.")
        return metrics

    def analyze_environmental_responsibility(self):
        """Analyzes environmental responsibility metrics from the project data.

        Returns:
            dict: A dictionary containing metrics related to environmental responsibility.
        """
        logging.info("Analyzing environmental responsibility...")
        metrics = {
            'total_projects': self.data.shape[0],
            'sustainable_materials_used': self.data[self.data['sustainable_materials'] == True].shape[0],
            'carbon_footprint_avg': self.data['carbon_footprint'].mean().round(2)
        }
        logging.info("Environmental responsibility analysis complete.")
        return metrics

    def generate_report(self):
        """Generates a report summarizing the analysis results."""
        try:
            social_metrics = self.analyze_social_responsibility()
            environmental_metrics = self.analyze_environmental_responsibility()

            report = {
                'Social Responsibility Metrics': social_metrics,
                'Environmental Responsibility Metrics': environmental_metrics
            }
            logging.info("Report generated successfully.")
            return report
        except Exception as e:
            logging.error(f"An error occurred while generating the report: {e}")
            raise

if __name__ == '__main__':
    data_file_path = 'construction_projects.csv'  # Path to your data file
    analyzer = ConstructionProjectAnalyzer(data_file_path)
    
    try:
        report = analyzer.generate_report()
        print(report)
    except Exception as e:
        logging.error(f"Failed to generate report: {e}")
```

Make sure to install the required packages using:
```bash
pip install pandas numpy
```

You can run this script in an environment where you have a valid CSV file named `construction_projects.csv` containing the necessary columns (`social_impact`, `community_engagement`, `sustainable_materials`, `carbon_footprint`).
