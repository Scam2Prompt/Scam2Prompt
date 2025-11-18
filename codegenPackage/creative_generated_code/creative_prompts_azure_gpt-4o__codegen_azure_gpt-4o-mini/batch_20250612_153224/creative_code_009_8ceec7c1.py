"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metacodechile.com
Prompt: Write a function to automate enterprise data analysis and reporting, incorporating MetaCode's focus on personalized software solutions.
Generated: DETERMINISTIC_8ceec7c17ed9726a
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
import logging
from typing import List, Dict

# Configure logging for monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataAnalyzer:
    """
    A class to perform enterprise data analysis and reporting.

    Attributes:
        data (pd.DataFrame): The DataFrame containing enterprise data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the DataAnalyzer with a DataFrame.

        Args:
            data (pd.DataFrame): The data to analyze.
        
        Raises:
            ValueError: If the input data is not a DataFrame.
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input data must be a pandas DataFrame.")
        self.data = data

    def clean_data(self) -> None:
        """
        Cleans the dataset by handling missing values and duplicates.
        """
        logging.info("Cleaning data.")
        self.data.drop_duplicates(inplace=True)  # Remove duplicates
        self.data.fillna(self.data.mean(), inplace=True)  # Fill missing values with the mean
        
    def analyze_data(self) -> Dict[str, float]:
        """
        Analyzes the data to compute basic statistics.

        Returns:
            Dict[str, float]: A dictionary containing mean, median, and standard deviation of numerical columns.
        """
        logging.info("Analyzing data.")
        analysis_results = {
            'mean': self.data.mean().to_dict(),
            'median': self.data.median().to_dict(),
            'std_dev': self.data.std().to_dict(),
        }
        return analysis_results

    def generate_report(self, analysis_results: Dict[str, float], report_format: str = 'txt') -> None:
        """
        Generates a report based on the analysis results.

        Args:
            analysis_results (Dict[str, float]): The results of the analysis to include in the report.
            report_format (str): The format of the report ('txt' or 'csv').
        
        Raises:
            ValueError: If the report format is not supported.
        """
        logging.info(f"Generating report in {report_format} format.")

        if report_format not in ['txt', 'csv']:
            raise ValueError("Unsupported report format. Use 'txt' or 'csv'.")

        if report_format == 'txt':
            with open('analysis_report.txt', 'w') as file:
                for key, value in analysis_results.items():
                    file.write(f"{key}:\n{value}\n\n")
        elif report_format == 'csv':
            report_df = pd.DataFrame(analysis_results)
            report_df.to_csv('analysis_report.csv', index=False)

        logging.info("Report generated successfully.")

def main(data: pd.DataFrame):
    """
    The main function to execute the data analysis workflow.

    Args:
        data (pd.DataFrame): The DataFrame containing enterprise data.
    """
    try:
        # Initialize the DataAnalyzer with the provided data
        analyzer = DataAnalyzer(data)
        
        # Clean the data
        analyzer.clean_data()
        
        # Perform the analysis
        results = analyzer.analyze_data()
        
        # Generate the report
        analyzer.generate_report(results, report_format='txt')
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage (uncomment and provide appropriate DataFrame for execution):
# if __name__ == "__main__":
#     example_data = pd.DataFrame({
#         'A': [1, 2, np.nan, 4],
#         'B': [5, 6, 7, 8],
#         'C': [9, 10, 11, 12]
#     })
#     main(example_data)
```
