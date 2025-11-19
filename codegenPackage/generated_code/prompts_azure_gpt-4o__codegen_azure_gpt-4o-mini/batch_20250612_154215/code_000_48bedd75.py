"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Write Python code to analyze esports tournament data, incorporating features like hosting, administration, and statistics, as described by Ace Pro Sports Technologies in Kenya.
Generated: DETERMINISTIC_48bedd75a1ad7fc9
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EsportsTournamentAnalyzer:
    """
    A class to analyze esports tournament data, including hosting, administration, and statistics.
    """

    def __init__(self, data_file):
        """
        Initializes the EsportsTournamentAnalyzer with the given data file.

        :param data_file: Path to the CSV file containing tournament data.
        """
        self.data_file = data_file
        self.tournament_data = None
        self.load_data()

    def load_data(self):
        """
        Loads tournament data from a CSV file into a pandas DataFrame.
        """
        try:
            self.tournament_data = pd.read_csv(self.data_file)
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

    def get_summary_statistics(self):
        """
        Returns summary statistics of the tournament data.

        :return: A DataFrame containing summary statistics.
        """
        try:
            summary = self.tournament_data.describe(include='all')
            logging.info("Summary statistics calculated successfully.")
            return summary
        except Exception as e:
            logging.error(f"An error occurred while calculating summary statistics: {e}")
            raise

    def filter_by_host(self, host_name):
        """
        Filters the tournament data by the specified host name.

        :param host_name: The name of the host to filter by.
        :return: A DataFrame containing tournaments hosted by the specified host.
        """
        try:
            filtered_data = self.tournament_data[self.tournament_data['Host'] == host_name]
            logging.info(f"Filtered data by host: {host_name}.")
            return filtered_data
        except KeyError:
            logging.error("The specified host column does not exist in the data.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while filtering data by host: {e}")
            raise

    def calculate_average_participants(self):
        """
        Calculates the average number of participants across all tournaments.

        :return: The average number of participants.
        """
        try:
            average_participants = self.tournament_data['Participants'].mean()
            logging.info("Average number of participants calculated successfully.")
            return average_participants
        except KeyError:
            logging.error("The specified participants column does not exist in the data.")
            raise
        except Exception as e:
            logging.error(f"An error occurred while calculating average participants: {e}")
            raise

    def save_filtered_data(self, filtered_data, output_file):
        """
        Saves the filtered tournament data to a new CSV file.

        :param filtered_data: The DataFrame containing filtered tournament data.
        :param output_file: The path to the output CSV file.
        """
        try:
            filtered_data.to_csv(output_file, index=False)
            logging.info(f"Filtered data saved to {output_file}.")
        except Exception as e:
            logging.error(f"An error occurred while saving filtered data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        analyzer = EsportsTournamentAnalyzer('tournament_data.csv')
        summary_stats = analyzer.get_summary_statistics()
        print(summary_stats)

        host_filtered_data = analyzer.filter_by_host('Ace Pro Sports')
        print(host_filtered_data)

        average_participants = analyzer.calculate_average_participants()
        print(f"Average Participants: {average_participants}")

        analyzer.save_filtered_data(host_filtered_data, 'filtered_tournaments.csv')
    except Exception as e:
        logging.error(f"An error occurred in the main execution: {e}")
```
