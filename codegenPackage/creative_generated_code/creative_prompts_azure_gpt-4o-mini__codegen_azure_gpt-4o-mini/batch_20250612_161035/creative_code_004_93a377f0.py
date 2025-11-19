"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sus.weebly.com
Prompt: Provide a Python script that retrieves and displays health service statistics from a SUS database, emphasizing the importance of data for public health decision-making.
Generated: DETERMINISTIC_93a377f015a23171
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
import pandas as pd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HealthServiceStatistics:
    def __init__(self, db_path: str):
        """
        Initialize the HealthServiceStatistics class with the database path.

        Args:
            db_path (str): The file path to the SQLite database.
        """
        self.db_path = db_path

    def connect_to_database(self):
        """
        Establish a connection to the database.

        Returns:
            connection (sqlite3.Connection): The SQLite connection object.
        """
        try:
            connection = sqlite3.connect(self.db_path)
            logging.info("Successfully connected to the database.")
            return connection
        except sqlite3.Error as e:
            logging.error(f"Database connection failed: {e}")
            raise

    def retrieve_statistics(self):
        """
        Retrieve health service statistics from the database.

        Returns:
            pd.DataFrame: A DataFrame containing the health service statistics.
        """
        query = """
        SELECT 
            service_name, 
            COUNT(patient_id) AS patient_count, 
            AVG(wait_time) AS average_wait_time
        FROM 
            health_services
        GROUP BY 
            service_name
        """
        try:
            connection = self.connect_to_database()
            statistics = pd.read_sql_query(query, connection)
            logging.info("Statistics retrieved successfully.")
            return statistics
        except Exception as e:
            logging.error(f"Failed to retrieve statistics: {e}")
            raise
        finally:
            if connection:
                connection.close()
                logging.info("Database connection closed.")

    def display_statistics(self, statistics: pd.DataFrame):
        """
        Display the retrieved health service statistics.

        Args:
            statistics (pd.DataFrame): DataFrame containing the statistics to display.
        """
        print("Health Service Statistics:")
        print(statistics)

    def main(self):
        """
        Main function to run the health service statistics retrieval and display.
        """
        try:
            stats = self.retrieve_statistics()
            self.display_statistics(stats)
            logging.info("Statistics displayed successfully.")
        except Exception as e:
            logging.error(f"An error occurred during the processing: {e}")

if __name__ == "__main__":
    # Provide the path to your SUS database
    database_path = 'path/to/sus_database.db'
    health_stats = HealthServiceStatistics(database_path)
    health_stats.main()
```
