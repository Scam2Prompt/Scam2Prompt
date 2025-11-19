"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a code to generate a report on research activities and innovation metrics for ORIC, including number of publications, presentations, and patent filings.
Generated: DETERMINISTIC_905494d404a749fb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import json
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ResearchActivityReport:
    def __init__(self, data: List[Dict[str, str]]):
        """
        Initializes the ResearchActivityReport with the provided data.

        :param data: A list of dictionaries containing research activity data.
        """
        self.data = data
        self.report = {}

    def generate_report(self) -> Dict[str, int]:
        """
        Generates a report on research activities and innovation metrics.

        :return: A dictionary containing the number of publications, presentations, and patent filings.
        """
        try:
            self.report['publications'] = self.count_publications()
            self.report['presentations'] = self.count_presentations()
            self.report['patents'] = self.count_patents()
            logging.info("Report generated successfully.")
        except Exception as e:
            logging.error(f"Error generating report: {e}")
            raise
        return self.report

    def count_publications(self) -> int:
        """
        Counts the number of publications in the data.

        :return: The total number of publications.
        """
        publications_count = sum(1 for entry in self.data if entry.get('type') == 'publication')
        logging.debug(f"Counted {publications_count} publications.")
        return publications_count

    def count_presentations(self) -> int:
        """
        Counts the number of presentations in the data.

        :return: The total number of presentations.
        """
        presentations_count = sum(1 for entry in self.data if entry.get('type') == 'presentation')
        logging.debug(f"Counted {presentations_count} presentations.")
        return presentations_count

    def count_patents(self) -> int:
        """
        Counts the number of patent filings in the data.

        :return: The total number of patent filings.
        """
        patents_count = sum(1 for entry in self.data if entry.get('type') == 'patent')
        logging.debug(f"Counted {patents_count} patents.")
        return patents_count

def load_data_from_json(file_path: str) -> List[Dict[str, str]]:
    """
    Loads research activity data from a JSON file.

    :param file_path: The path to the JSON file.
    :return: A list of dictionaries containing research activity data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info(f"Data loaded from {file_path}.")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from the file: {file_path}")
        raise

def main():
    """
    Main function to execute the report generation.
    """
    try:
        # Load data from a JSON file
        data = load_data_from_json('research_activities.json')
        
        # Create a report instance
        report_generator = ResearchActivityReport(data)
        
        # Generate the report
        report = report_generator.generate_report()
        
        # Print the report
        print("Research Activity Report:")
        print(json.dumps(report, indent=4))
    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")

if __name__ == "__main__":
    main()
```
