"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wiraukur.com
Prompt: Provide Python code for managing construction survey data and generating analytics reports, inspired by Wira Survey Consultants' project management solutions.
Generated: DETERMINISTIC_c8dcccf953ccac24
Batch ID: 20250612_154444
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
from typing import List, Dict, Any, Optional

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SurveyDataManager:
    """
    A class to manage construction survey data and generate analytics reports.
    """

    def __init__(self, data_file: str):
        """
        Initialize the SurveyDataManager with a data file.

        :param data_file: Path to the CSV file containing survey data.
        """
        self.data_file = data_file
        self.survey_data = None
        self.load_data()

    def load_data(self):
        """
        Load the survey data from the specified CSV file.
        """
        try:
            self.survey_data = pd.read_csv(self.data_file)
            logging.info("Survey data loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the CSV file.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading data: {e}")
            raise

    def generate_report(self, report_type: str) -> Optional[Dict[str, Any]]:
        """
        Generate an analytics report based on the type specified.

        :param report_type: Type of report to generate ('summary' or 'detailed').
        :return: A dictionary containing the report data.
        """
        if report_type == 'summary':
            return self._generate_summary_report()
        elif report_type == 'detailed':
            return self._generate_detailed_report()
        else:
            logging.error("Invalid report type specified.")
            raise ValueError("Report type must be 'summary' or 'detailed'.")

    def _generate_summary_report(self) -> Dict[str, Any]:
        """
        Generate a summary report of the survey data.

        :return: A dictionary with summary statistics.
        """
        try:
            summary_stats = {
                'total_surveys': self.survey_data.shape[0],
                'average_accuracy': self.survey_data['accuracy'].mean(),
                'max_height_difference': self.survey_data['height_difference'].max(),
                'min_height_difference': self.survey_data['height_difference'].min(),
            }
            logging.info("Summary report generated successfully.")
            return summary_stats
        except KeyError as e:
            logging.error(f"Missing expected column in survey data: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while generating the summary report: {e}")
            raise

    def _generate_detailed_report(self) -> pd.DataFrame:
        """
        Generate a detailed report of the survey data.

        :return: A DataFrame containing the detailed survey data.
        """
        try:
            detailed_report = self.survey_data.copy()
            detailed_report['height_difference'] = detailed_report['height_end'] - detailed_report['height_start']
            logging.info("Detailed report generated successfully.")
            return detailed_report
        except KeyError as e:
            logging.error(f"Missing expected column in survey data: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while generating the detailed report: {e}")
            raise

if __name__ == '__main__':
    # Example usage
    try:
        manager = SurveyDataManager('survey_data.csv')
        summary_report = manager.generate_report('summary')
        print("Summary Report:", summary_report)

        detailed_report = manager.generate_report('detailed')
        print("Detailed Report:\n", detailed_report)
    except Exception as e:
        logging.error(f"An error occurred in the SurveyDataManager: {e}")
```
