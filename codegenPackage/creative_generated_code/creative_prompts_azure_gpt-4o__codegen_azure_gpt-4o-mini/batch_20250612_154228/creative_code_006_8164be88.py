"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Write a program to analyze user activity on BaxBet and generate reports on popular casino games and betting trends.
Generated: DETERMINISTIC_8164be881256b55a
Batch ID: 20250612_154228
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
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UserActivityAnalyzer:
    def __init__(self, data_file):
        """
        Initializes the UserActivityAnalyzer with a data file.

        :param data_file: Path to the CSV file containing user activity data.
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """
        Loads user activity data from the specified CSV file.
        """
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except FileNotFoundError:
            logging.error("File not found. Please check the file path.")
            raise
        except pd.errors.EmptyDataError:
            logging.error("The provided CSV file is empty.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while loading the data: {e}")
            raise

    def preprocess_data(self):
        """
        Preprocesses the data for analysis.
        - Converts timestamps to datetime objects
        - Handles missing values
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data before preprocessing.")
            raise ValueError("Data not loaded.")

        # Convert 'timestamp' column to datetime
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'], errors='coerce')

        # Drop rows with any missing values
        self.data.dropna(inplace=True)
        logging.info("Data preprocessed successfully.")

    def generate_reports(self):
        """
        Generates reports on popular casino games and betting trends.
        :return: A dictionary containing reports.
        """
        if self.data is None:
            logging.error("Data not loaded. Please load the data before generating reports.")
            raise ValueError("Data not loaded.")

        # Analyzing popular games
        popular_games = self.data['game'].value_counts().head(10)

        # Analyzing betting trends
        self.data['date'] = self.data['timestamp'].dt.date
        betting_trends = self.data.groupby('date')['bet_amount'].sum()

        reports = {
            "popular_games": popular_games,
            "betting_trends": betting_trends
        }

        logging.info("Reports generated successfully.")
        return reports

    def save_reports(self, reports, output_file):
        """
        Saves the generated reports to a specified output file.

        :param reports: The reports dictionary to save.
        :param output_file: Path to the output CSV file.
        """
        try:
            pd.DataFrame(reports['popular_games']).to_csv('popular_games_report.csv')
            reports['betting_trends'].to_csv('betting_trends_report.csv')
            logging.info("Reports saved successfully.")
        except Exception as e:
            logging.error(f"An error occurred while saving reports: {e}")
            raise

def main():
    # Path to user activity data CSV file
    data_file = 'user_activity.csv'

    # Create an instance of UserActivityAnalyzer
    analyzer = UserActivityAnalyzer(data_file)

    # Load, preprocess data, generate, and save reports
    try:
        analyzer.load_data()
        analyzer.preprocess_data()
        reports = analyzer.generate_reports()
        analyzer.save_reports(reports, 'output_reports/')
    except Exception as e:
        logging.error(f"An error occurred during the analysis: {e}")

if __name__ == "__main__":
    main()
```
