"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Generate code to analyze success stories of research projects, using ORIC's approach to academia-industry linkages as a model.
Generated: DETERMINISTIC_6ce9723c5f58f1d7
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

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ResearchProjectAnalyzer:
    """
    A class to analyze success stories of research projects using ORIC's approach.
    """

    def __init__(self, data_file):
        """
        Initializes the ResearchProjectAnalyzer with the given data file.

        :param data_file: Path to the CSV file containing research project data
        """
        self.data_file = data_file
        self.data = None
        self.success_stories = []

    def load_data(self):
        """
        Loads the research project data from the specified CSV file.
        Handles errors in file loading and data parsing.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info(f'Data loaded successfully from {self.data_file}.')
        except FileNotFoundError:
            logging.error(f'File not found: {self.data_file}')
            raise
        except pd.errors.EmptyDataError:
            logging.error('No data found in the file.')
            raise
        except Exception as e:
            logging.error(f'An error occurred while loading data: {e}')
            raise

    def analyze_success_stories(self):
        """
        Analyzes the loaded data to extract success stories based on specific criteria.
        A success story is defined as having a positive impact and strong industry linkages.
        """
        if self.data is None:
            logging.warning('Data not loaded. Please call load_data() first.')
            return

        # Define criteria for success stories
        try:
            success_criteria = (self.data['impact'] == 'positive') & (self.data['industry_linkage'] == 'strong')
            self.success_stories = self.data[success_criteria]
            logging.info(f'Found {len(self.success_stories)} success stories.')
        except KeyError as e:
            logging.error(f'Missing expected column in data: {e}')
            raise
        except Exception as e:
            logging.error(f'An error occurred during analysis: {e}')
            raise

    def get_success_stories(self):
        """
        Returns the analyzed success stories.

        :return: DataFrame containing the success stories
        """
        return self.success_stories

    def save_success_stories(self, output_file):
        """
        Saves the success stories to a specified CSV file.

        :param output_file: Path to the output CSV file
        """
        if len(self.success_stories) == 0:
            logging.warning('No success stories to save.')
            return

        try:
            self.success_stories.to_csv(output_file, index=False)
            logging.info(f'Success stories saved to {output_file}.')
        except Exception as e:
            logging.error(f'An error occurred while saving the success stories: {e}')
            raise


if __name__ == "__main__":
    # Initialize the analyzer with the path to the data file
    analyzer = ResearchProjectAnalyzer("research_projects.csv")
    
    # Load the data
    analyzer.load_data()
    
    # Analyze the success stories
    analyzer.analyze_success_stories()
    
    # Retrieve and save success stories
    success_stories_df = analyzer.get_success_stories()
    analyzer.save_success_stories("success_stories.csv")
```
