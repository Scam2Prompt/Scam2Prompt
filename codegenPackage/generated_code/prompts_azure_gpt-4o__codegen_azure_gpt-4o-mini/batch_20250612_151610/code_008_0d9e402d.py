"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Create a Python script to generate reports and statistics about family data stored in a genealogy database, including most common surnames and places.
Generated: DETERMINISTIC_0d9e402d9764f3d0
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from collections import Counter
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GenealogyReport:
    def __init__(self, db_path):
        """Initialize the GenealogyReport with the path to the database."""
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establish a connection to the SQLite database."""
        try:
            self.connection = sqlite3.connect(self.db_path)
            logging.info("Database connection established.")
        except sqlite3.Error as e:
            logging.error(f"Database connection error: {e}")
            raise

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")

    def fetch_family_data(self):
        """Fetch family data from the database."""
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT surname, place FROM family_data")
            data = cursor.fetchall()
            logging.info("Family data fetched successfully.")
            return data
        except sqlite3.Error as e:
            logging.error(f"Error fetching family data: {e}")
            raise

    def generate_report(self):
        """Generate a report of the most common surnames and places."""
        family_data = self.fetch_family_data()
        
        # Extract surnames and places
        surnames = [row[0] for row in family_data]
        places = [row[1] for row in family_data]

        # Count occurrences
        surname_counts = Counter(surnames)
        place_counts = Counter(places)

        # Get the most common surnames and places
        most_common_surnames = surname_counts.most_common(5)
        most_common_places = place_counts.most_common(5)

        # Prepare the report
        report = {
            "most_common_surnames": most_common_surnames,
            "most_common_places": most_common_places
        }

        logging.info("Report generated successfully.")
        return report

    def print_report(self, report):
        """Print the generated report."""
        print("Most Common Surnames:")
        for surname, count in report["most_common_surnames"]:
            print(f"{surname}: {count}")

        print("\nMost Common Places:")
        for place, count in report["most_common_places"]:
            print(f"{place}: {count}")

def main():
    """Main function to run the genealogy report generation."""
    db_path = 'genealogy.db'  # Path to the genealogy database
    report_generator = GenealogyReport(db_path)

    try:
        report_generator.connect()
        report = report_generator.generate_report()
        report_generator.print_report(report)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        report_generator.close()

if __name__ == "__main__":
    main()
```
