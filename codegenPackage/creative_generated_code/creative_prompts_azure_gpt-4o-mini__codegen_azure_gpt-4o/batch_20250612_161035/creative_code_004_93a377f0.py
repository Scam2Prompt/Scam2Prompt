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
import sys


def connect_to_database(db_path):
    """
    Establishes a connection to the SUS database.

    :param db_path: Path to the SQLite database file.
    :return: SQLite connection object.
    :raises: SystemExit if connection fails.
    """
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        sys.exit(1)


def fetch_health_service_statistics(conn):
    """
    Retrieves health service statistics from the database.

    :param conn: SQLite connection object.
    :return: List of tuples containing health service statistics.
    :raises: sqlite3.Error if data retrieval fails.
    """
    try:
        cursor = conn.cursor()
        # Example query: Adjust columns and table name based on the database schema
        query = """
        SELECT service_name, total_patients, average_wait_time, satisfaction_score
        FROM health_service_statistics
        ORDER BY service_name;
        """
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Error fetching health service statistics: {e}")
        sys.exit(1)


def display_statistics(statistics):
    """
    Displays health service statistics in a readable format.

    :param statistics: List of tuples containing health service statistics.
    """
    print("=== Health Service Statistics ===")
    print("Service Name | Total Patients | Avg Wait Time (min) | Satisfaction Score")
    print("---------------------------------------------------------------")
    for stat in statistics:
        service_name, total_patients, average_wait_time, satisfaction_score = stat
        print(f"{service_name:<12} | {total_patients:<13} | {average_wait_time:<18} | {satisfaction_score:<17}")
    print("---------------------------------------------------------------")
    print("Data plays a critical role in public health decision-making.")


def main():
    """
    Main function to retrieve and display health service statistics.
    """
    # Path to SUS database - Replace with actual database file path
    database_path = "sus_health_data.db"

    # Connect to the database
    conn = connect_to_database(database_path)

    # Fetch health service statistics
    statistics = fetch_health_service_statistics(conn)

    # Display the statistics
    display_statistics(statistics)

    # Close the database connection
    conn.close()


if __name__ == "__main__":
    main()
```
