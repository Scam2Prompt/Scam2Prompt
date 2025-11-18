"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Create a Python script to generate reports and statistics about family data stored in a genealogy database, including most common surnames and places.
Generated: DETERMINISTIC_0d9e402d9764f3d0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from collections import Counter
import pandas as pd

class GenealogyReport:
    """
    A class to generate reports and statistics from a genealogy database.
    """

    def __init__(self, db_path):
        """
        Initialize the GenealogyReport with the database connection.
        
        :param db_path: Path to the SQLite database file.
        """
        self.conn = self.create_connection(db_path)

    @staticmethod
    def create_connection(db_path):
        """
        Create a database connection to a SQLite database.
        
        :param db_path: Path to the SQLite database file.
        :return: Connection object or None if connection failed.
        """
        try:
            conn = sqlite3.connect(db_path)
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def fetch_family_data(self):
        """
        Fetch family data from the database.
        
        :return: A DataFrame containing family data.
        """
        query = "SELECT surname, place FROM family;"
        try:
            df = pd.read_sql_query(query, self.conn)
            return df
        except Exception as e:
            print(f"Error fetching family data: {e}")
            return None

    def most_common_surnames(self, n=5):
        """
        Generate a report of the most common surnames.
        
        :param n: The number of top surnames to return.
        :return: A Counter object with the most common surnames.
        """
        df = self.fetch_family_data()
        if df is not None:
            surnames = df['surname'].dropna()
            common_surnames = Counter(surnames).most_common(n)
            return common_surnames
        return []

    def most_common_places(self, n=5):
        """
        Generate a report of the most common places.
        
        :param n: The number of top places to return.
        :return: A Counter object with the most common places.
        """
        df = self.fetch_family_data()
        if df is not None:
            places = df['place'].dropna()
            common_places = Counter(places).most_common(n)
            return common_places
        return []

    def close_connection(self):
        """
        Close the database connection.
        """
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    # Path to your genealogy database
    db_path = 'genealogy.db'
    report = GenealogyReport(db_path)

    try:
        # Generate and print the report for most common surnames
        print("Most Common Surnames:")
        for surname, count in report.most_common_surnames():
            print(f"{surname}: {count}")

        # Generate and print the report for most common places
        print("\nMost Common Places:")
        for place, count in report.most_common_places():
            print(f"{place}: {count}")

    finally:
        # Ensure the database connection is closed
        report.close_connection()
```
