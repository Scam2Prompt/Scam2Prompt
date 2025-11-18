"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mctsummit.org
Prompt: Develop a script to analyze attendee data for networking events at the MCT Summit, including metrics like registered candidates and global speakers.
Generated: DETERMINISTIC_23d0b3f874f12323
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import logging

# Set up logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EventAnalytics:
    def __init__(self, data_file):
        """
        Initialize the EventAnalytics class.

        :param data_file: str - Path to the CSV file containing attendee data
        """
        self.data_file = data_file
        self.attendee_data = None

    def load_data(self):
        """
        Load attendee data from a CSV file into a pandas DataFrame.
        Handles file-related errors.
        """
        try:
            self.attendee_data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully from %s", self.data_file)
        except FileNotFoundError:
            logging.error("File not found: %s", self.data_file)
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data found in the file: %s", self.data_file)
            raise
        except pd.errors.ParserError:
            logging.error("Error parsing data in the file: %s", self.data_file)
            raise

    def analyze_attendees(self):
        """
        Analyze the attendee data and return key metrics.
        
        :return: dict - A dictionary containing metrics on registered candidates and global speakers
        """
        if self.attendee_data is None:
            logging.error("Attendee data is not loaded. Please call load_data() first.")
            raise ValueError("Attendee data not loaded")

        try:
            # Count registered candidates
            total_candidates = self.attendee_data['Candidate'].notnull().sum()
            # Count unique global speakers
            total_speakers = self.attendee_data['Speaker'].nunique()

            metrics = {
                'total_candidates': total_candidates,
                'total_speakers': total_speakers
            }
            logging.info("Analysis complete: %s", metrics)
            return metrics
        except KeyError as e:
            logging.error("Missing expected column in data: %s", e)
            raise

def main():
    """
    Main function to execute the event analytics.
    """
    # Path to the CSV file containing event data
    data_file_path = 'attendee_data.csv'

    # Create an instance of EventAnalytics
    analytics = EventAnalytics(data_file_path)

    # Load the attendee data
    analytics.load_data()

    # Analyze the attendee data
    try:
        results = analytics.analyze_attendees()
        print("Total Registered Candidates:", results['total_candidates'])
        print("Total Global Speakers:", results['total_speakers'])
    except Exception as e:
        logging.error("An error occurred during analysis: %s", e)

if __name__ == "__main__":
    main()
```
