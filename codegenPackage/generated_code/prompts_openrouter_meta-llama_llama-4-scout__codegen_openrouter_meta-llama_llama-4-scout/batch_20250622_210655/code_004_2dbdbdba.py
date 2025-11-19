"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Design a data management system to track and analyze call center metrics, such as customer satisfaction and first-call resolution rates, for a BPO provider like The Hashtag Consultants."
Generated: DETERMINISTIC_2dbdbdba4a7521f7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import sqlite3
from datetime import datetime

class CallCenterMetrics:
    """
    A class to track and analyze call center metrics.

    Attributes:
    -----------
    db_name (str): The name of the SQLite database file.

    Methods:
    --------
    create_table(): Creates a table in the SQLite database to store call center metrics.
    insert_metric(): Inserts a new call center metric into the database.
    get_metrics(): Retrieves all call center metrics from the database.
    get_customer_satisfaction(): Calculates the average customer satisfaction rate.
    get_first_call_resolution_rate(): Calculates the first-call resolution rate.
    """

    def __init__(self, db_name):
        """
        Initializes the CallCenterMetrics class.

        Parameters:
        -----------
        db_name (str): The name of the SQLite database file.
        """
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        """
        Creates a table in the SQLite database to store call center metrics.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS call_center_metrics
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             date TEXT,
             customer_satisfaction REAL,
             first_call_resolution INTEGER,
             total_calls INTEGER)
        ''')
        self.conn.commit()

    def insert_metric(self, date, customer_satisfaction, first_call_resolution, total_calls):
        """
        Inserts a new call center metric into the database.

        Parameters:
        -----------
        date (str): The date of the metric in YYYY-MM-DD format.
        customer_satisfaction (float): The customer satisfaction rate (0-1).
        first_call_resolution (int): The number of first-call resolutions.
        total_calls (int): The total number of calls.
        """
        try:
            self.cursor.execute('''
                INSERT INTO call_center_metrics (date, customer_satisfaction, first_call_resolution, total_calls)
                VALUES (?, ?, ?, ?)
            ''', (date, customer_satisfaction, first_call_resolution, total_calls))
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error inserting metric: {e}")

    def get_metrics(self):
        """
        Retrieves all call center metrics from the database.

        Returns:
        --------
        list: A list of tuples containing the call center metrics.
        """
        try:
            self.cursor.execute('SELECT * FROM call_center_metrics')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error retrieving metrics: {e}")
            return []

    def get_customer_satisfaction(self):
        """
        Calculates the average customer satisfaction rate.

        Returns:
        --------
        float: The average customer satisfaction rate.
        """
        try:
            self.cursor.execute('SELECT AVG(customer_satisfaction) FROM call_center_metrics')
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error calculating customer satisfaction: {e}")
            return None

    def get_first_call_resolution_rate(self):
        """
        Calculates the first-call resolution rate.

        Returns:
        --------
        float: The first-call resolution rate.
        """
        try:
            self.cursor.execute('SELECT SUM(first_call_resolution) / SUM(total_calls) FROM call_center_metrics')
            return self.cursor.fetchone()[0]
        except sqlite3.Error as e:
            print(f"Error calculating first-call resolution rate: {e}")
            return None

    def close_connection(self):
        """
        Closes the SQLite database connection.
        """
        self.conn.close()


def main():
    # Create a CallCenterMetrics object
    metrics = CallCenterMetrics('call_center_metrics.db')

    # Create the table
    metrics.create_table()

    # Insert some sample metrics
    metrics.insert_metric('2022-01-01', 0.8, 100, 200)
    metrics.insert_metric('2022-01-02', 0.9, 120, 250)

    # Retrieve all metrics
    print("All Metrics:")
    for metric in metrics.get_metrics():
        print(metric)

    # Calculate customer satisfaction and first-call resolution rate
    customer_satisfaction = metrics.get_customer_satisfaction()
    first_call_resolution_rate = metrics.get_first_call_resolution_rate()

    print(f"\nAverage Customer Satisfaction: {customer_satisfaction:.2f}")
    print(f"First-Call Resolution Rate: {first_call_resolution_rate:.2f}")

    # Close the database connection
    metrics.close_connection()


if __name__ == "__main__":
    main()
```
