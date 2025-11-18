"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Write Python code to analyze website traffic data using cookies, referencing IT services that optimize user experience as described on uuip-hualdlugeen.
Generated: DETERMINISTIC_50fac5f1e49524ed
Batch ID: 20250612_154131
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
from urllib.parse import urlparse
from datetime import datetime

# Set up logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebsiteTrafficAnalyzer:
    """
    A class to analyze website traffic data based on cookies.
    This class provides methods to load data, clean it, and analyze user experience factors.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file path.

        :param data_file: str - Path to the website traffic data CSV file
        """
        self.data_file = data_file
        self.data = None

    def load_data(self):
        """Loads the website traffic data from a CSV file."""
        try:
            self.data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully.")
        except Exception as e:
            logging.error("Error loading data: %s", e)
            raise

    def clean_data(self):
        """Cleans the data by handling missing values and correcting data types."""
        if self.data is None:
            logging.error("Data not loaded. Please load data before cleaning.")
            raise ValueError("Data not loaded.")

        # Drop rows with missing values in critical columns
        initial_shape = self.data.shape
        self.data.dropna(subset=['user_id', 'session_id', 'timestamp'], inplace=True)
        logging.info("Cleaned data from %s to %s rows", initial_shape[0], self.data.shape[0])

        # Convert timestamp to datetime
        self.data['timestamp'] = pd.to_datetime(self.data['timestamp'], errors='coerce')
        self.data.dropna(subset=['timestamp'], inplace=True)

    def analyze_traffic(self):
        """Analyzes the traffic data to provide insights on user experience."""
        if self.data is None:
            logging.error("Data not loaded. Please load and clean data before analysis.")
            raise ValueError("Data not loaded.")
        
        # Group by session and count visits
        session_counts = self.data.groupby('session_id').size().reset_index(name='visit_count')
        logging.info("Session visit counts calculated.")

        # Analyze cookie usage
        cookie_usage = self.data['cookie_present'].value_counts(normalize=True)
        logging.info("Cookie usage analysis completed.")

        return session_counts, cookie_usage

    def generate_report(self, session_counts, cookie_usage):
        """Generates a report of the analysis results."""
        report = {
            'total_sessions': session_counts['visit_count'].count(),
            'avg_visits_per_session': session_counts['visit_count'].mean(),
            'cookie_usage': cookie_usage.to_dict()
        }
        logging.info("Report generated: %s", report)
        return report

def main():
    # Example usage of the WebsiteTrafficAnalyzer class
    try:
        analyzer = WebsiteTrafficAnalyzer(data_file='traffic_data.csv')
        analyzer.load_data()
        analyzer.clean_data()
        session_counts, cookie_usage = analyzer.analyze_traffic()
        report = analyzer.generate_report(session_counts, cookie_usage)
        print(report)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

if __name__ == "__main__":
    main()
```

### Note:
- This code assumes that the CSV file `traffic_data.csv` contains relevant columns like `user_id`, `session_id`, `timestamp`, and `cookie_present`.
- Logging is implemented to track the flow and catch errors.
- The report includes total sessions, average visits per session, and cookie usage distribution.
- Ensure to replace the `data_file` with the correct path to your CSV data file.
