"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munasimkullakita.org
Prompt: Write code to generate reports on the impact of social programs, such as the percentage of beneficiaries reintegrated into education or independent living, based on the data model described on Fundación Munasim Kullakita's webpage.
Generated: DETERMINISTIC_dc2a706bb913a98c
Batch ID: 20250612_153224
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
from typing import Dict, Any, List

class SocialProgramReportGenerator:
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the report generator with the provided data.
        
        :param data: A DataFrame containing the social program beneficiaries data.
        """
        self.data = data

    def calculate_reintegration_percentage(self, column_name: str) -> float:
        """
        Calculate the percentage of beneficiaries who have been reintegrated into a specified program.
        
        :param column_name: The name of the column to analyze for reintegration status.
        :return: The percentage of beneficiaries reintegrated.
        """
        try:
            total_beneficiaries = self.data.shape[0]
            reintegrated_count = self.data[column_name].value_counts().get('Reintegrated', 0)
            percentage = (reintegrated_count / total_beneficiaries) * 100 if total_beneficiaries > 0 else 0.0
            return percentage
        except KeyError as e:
            raise ValueError(f"Column '{column_name}' not found in data.") from e
        except Exception as e:
            raise RuntimeError("An error occurred while calculating reintegration percentage.") from e

    def generate_report(self) -> Dict[str, Any]:
        """
        Generate a report summarizing the impact of social programs.
        
        :return: A dictionary containing the report data.
        """
        report = {}
        try:
            report['reintegration_into_education'] = self.calculate_reintegration_percentage('Education_Status')
            report['reintegration_into_independent_living'] = self.calculate_reintegration_percentage('Living_Status')
            report['total_beneficiaries'] = self.data.shape[0]
        except Exception as e:
            raise RuntimeError("Failed to generate report.") from e
        
        return report

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file into a DataFrame.
    
    :param file_path: The path to the CSV file.
    :return: A DataFrame containing the loaded data.
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        raise ValueError("The provided CSV file is empty.")
    except Exception as e:
        raise RuntimeError("An error occurred while loading the data.") from e

if __name__ == "__main__":
    try:
        # Load data from a CSV file
        data_file_path = 'path_to_your_data_file.csv'  # Update this path
        beneficiaries_data = load_data(data_file_path)

        # Create a report generator instance
        report_generator = SocialProgramReportGenerator(beneficiaries_data)

        # Generate and print the impact report
        impact_report = report_generator.generate_report()
        print("Social Program Impact Report:")
        print(impact_report)

    except Exception as e:
        print(f"An error occurred: {e}")
```
