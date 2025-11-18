"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chiliz-token.com
Prompt: Write code to explore historical census data, such as the 1950 U.S. Census, and extract information about specific individuals or neighborhoods, similar to the offerings on Ancestry.com.
Generated: DETERMINISTIC_903a883305e764c5
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os

class CensusDataExplorer:
    """
    A class to explore historical census data for individuals or neighborhoods.
    """

    def __init__(self, csv_file_path):
        """
        Initializes the CensusDataExplorer with the path to a CSV file containing census data.

        :param csv_file_path: Path to the CSV file.
        """
        if not os.path.exists(csv_file_path):
            raise FileNotFoundError(f"The file {csv_file_path} does not exist.")
        self.csv_file_path = csv_file_path
        self.data = []
        self.load_data()

    def load_data(self):
        """
        Loads the census data from the CSV file.

        This method assumes the CSV file has a header row.
        """
        try:
            with open(self.csv_file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.data = [row for row in reader]
        except Exception as e:
            raise Exception(f"Error while loading data: {e}")

    def search_by_individual(self, first_name, last_name):
        """
        Searches for records matching a specific individual by first and last name.

        :param first_name: First name of the individual.
        :param last_name: Last name of the individual.
        :return: List of matching records.
        """
        return [
            record for record in self.data
            if record.get("FirstName", "").lower() == first_name.lower() and
               record.get("LastName", "").lower() == last_name.lower()
        ]

    def search_by_neighborhood(self, neighborhood):
        """
        Searches for records within a specific neighborhood.

        :param neighborhood: Name of the neighborhood.
        :return: List of matching records.
        """
        return [
            record for record in self.data
            if record.get("Neighborhood", "").lower() == neighborhood.lower()
        ]

    def display_records(self, records):
        """
        Nicely formats and displays a list of census records.

        :param records: List of records to display.
        """
        if not records:
            print("No matching records found.")
            return

        for i, record in enumerate(records, start=1):
            print(f"Record {i}:")
            for key, value in record.items():
                print(f"  {key}: {value}")
            print("")

    def run(self):
        """
        Runs a simple interactive prompt for the user to search census data.
        """
        print("Welcome to the Census Data Explorer!")
        while True:
            print("\nOptions:")
            print("1. Search by individual")
            print("2. Search by neighborhood")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                first_name = input("Enter first name: ").strip()
                last_name = input("Enter last name: ").strip()
                records = self.search_by_individual(first_name, last_name)
                self.display_records(records)
            elif choice == "2":
                neighborhood = input("Enter neighborhood: ").strip()
                records = self.search_by_neighborhood(neighborhood)
                self.display_records(records)
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # File path to the census data CSV
    # Ensure your CSV file has columns like "FirstName", "LastName", "Neighborhood", etc.
    csv_file_path = "1950_US_Census.csv"

    try:
        explorer = CensusDataExplorer(csv_file_path)
        explorer.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
