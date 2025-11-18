"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axos-management.com
Prompt: Generate code to analyze target audience groups and create goal-oriented reports, as outlined in Axos Management's influencer management process.
Generated: DETERMINISTIC_99676e8817e3841e
Batch ID: 20250612_145153
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
from typing import List, Dict
import logging

# Setting up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AudienceAnalyzer:
    def __init__(self, data_file: str):
        """
        Initialize the AudienceAnalyzer with a data file.

        :param data_file: Path to the CSV file containing audience data.
        """
        self.data_file = data_file
        self.audience_data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Load audience data from a CSV file.

        :return: DataFrame containing audience data.
        """
        try:
            data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
            return data
        except FileNotFoundError:
            logging.error(f"File not found: {self.data_file}. Please check the file path.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file.")
            raise
        except pd.errors.ParserError:
            logging.error("Error parsing the data file.")
            raise

    def analyze_audience_groups(self) -> Dict[str, float]:
        """
        Analyze the audience groups based on engagement metrics.

        :return: Dictionary with the average engagement per group.
        """
        try:
            # Grouping by 'audience_group' and calculating mean engagement
            analysis = self.audience_data.groupby('audience_group')['engagement'].mean().to_dict()
            logging.info("Audience group analysis completed.")
            return analysis
        except KeyError as e:
            logging.error(f"Missing expected column in data: {e}")
            raise
        except Exception as e:
            logging.error(f"An error occurred during analysis: {e}")
            raise

    def create_reports(self, analysis: Dict[str, float]) -> None:
        """
        Create and save reports based on the audience analysis.

        :param analysis: Dictionary containing audience group analysis results.
        """
        try:
            # Convert analysis to DataFrame for easier manipulation
            report_df = pd.DataFrame(list(analysis.items()), columns=['Audience Group', 'Average Engagement'])
            report_df.to_csv('audience_analysis_report.csv', index=False)
            logging.info("Report created successfully and saved as 'audience_analysis_report.csv'")
        except Exception as e:
            logging.error(f"An error occurred while creating the report: {e}")
            raise

    def visualize_data(self, analysis: Dict[str, float]) -> None:
        """
        Visualize the analysis results using a bar chart.

        :param analysis: Dictionary containing audience group analysis results.
        """
        try:
            plt.bar(analysis.keys(), analysis.values(), color='skyblue')
            plt.title('Average Engagement per Audience Group')
            plt.xlabel('Audience Group')
            plt.ylabel('Average Engagement')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('audience_analysis_visualization.png')
            plt.show()
            logging.info("Visualization created successfully and saved as 'audience_analysis_visualization.png'")
        except Exception as e:
            logging.error(f"An error occurred during visualization: {e}")
            raise


if __name__ == "__main__":
    # The main entry point of the script
    try:
        # Initialize the AudienceAnalyzer with the specified data file
        analyzer = AudienceAnalyzer('audience_data.csv')

        # Analyze audience groups
        audience_analysis = analyzer.analyze_audience_groups()

        # Create reports from the analysis
        analyzer.create_reports(audience_analysis)

        # Visualize the analysis
        analyzer.visualize_data(audience_analysis)

    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")
```

**Note**: Ensure `audience_data.csv` exists in the same directory as this script or provide the correct path to it. The CSV file should contain at least the columns `audience_group` and `engagement`.
