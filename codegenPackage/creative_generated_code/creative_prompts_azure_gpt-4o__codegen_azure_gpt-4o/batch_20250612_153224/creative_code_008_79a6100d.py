"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elagrocorrentino.com.ar
Prompt: Develop a script to track the import of agricultural machinery, such as cotton harvesters, into Argentina, as mentioned in "El Agro Correntino."
Generated: DETERMINISTIC_79a6100dd689f949
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import logging
from datetime import datetime

# Configure logging settings
logging.basicConfig(
    filename='machinery_imports.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class MachineryImportTracker:
    """
    A class to track the import of agricultural machinery into Argentina.
    """

    def __init__(self, data_file):
        """
        Initialize the tracker with a data file.
        
        Args:
            data_file (str): Path to the CSV file containing machinery import data.
        """
        self.data_file = data_file

    def log_import(self, machinery_type, brand, origin_country, import_date=None):
        """
        Log a machinery import entry in the CSV file.
        
        Args:
            machinery_type (str): Type of agricultural machinery (e.g., Cotton Harvester).
            brand (str): Brand of the machinery.
            origin_country (str): Country of origin.
            import_date (str, optional): Date of import in 'YYYY-MM-DD' format. Defaults to today.
        """
        try:
            if import_date is None:
                import_date = datetime.now().strftime('%Y-%m-%d')

            # Validate the date format
            datetime.strptime(import_date, '%Y-%m-%d')

            # Append the new import record to the CSV file
            with open(self.data_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([machinery_type, brand, origin_country, import_date])

            logging.info(f"Successfully logged: {machinery_type}, {brand}, {origin_country}, {import_date}")
        except ValueError as ve:
            logging.error(f"Invalid date format provided: {import_date}. Error: {ve}")
        except Exception as e:
            logging.error(f"An error occurred while logging import: {e}")

    def display_imports(self):
        """
        Display all logged machinery imports from the CSV file.
        """
        try:
            # Read and display content from the CSV file
            with open(self.data_file, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                print("Machinery Imports:")
                print(f"{'Type':<20} {'Brand':<20} {'Origin Country':<20} {'Import Date':<12}")
                print("=" * 75)
                for row in reader:
                    print(f"{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<12}")
        except FileNotFoundError:
            logging.error(f"The file {self.data_file} does not exist.")
        except Exception as e:
            logging.error(f"An error occurred while displaying imports: {e}")

# Entry point for the script
if __name__ == "__main__":
    # Initialize the tracker with the file name
    tracker = MachineryImportTracker("agricultural_machinery_imports.csv")

    # Example usage (Uncomment to test)
    # tracker.log_import("Cotton Harvester", "John Deere", "USA")
    # tracker.log_import("Tractor", "Massey Ferguson", "UK", import_date="2023-10-15")
    # tracker.display_imports()
```
