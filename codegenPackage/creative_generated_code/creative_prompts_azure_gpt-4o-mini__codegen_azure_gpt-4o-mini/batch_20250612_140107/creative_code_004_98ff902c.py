"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdixchange.com
Prompt: Explain how to implement a CSV processor for handling bank statement templates available on fdixchange.com.
Generated: DETERMINISTIC_98ff902cad266cdb
Batch ID: 20250612_140107
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
from typing import List, Dict, Any

class CSVProcessor:
    """
    A class to process CSV files, specifically for bank statement templates.
    """

    def __init__(self, filename: str):
        """
        Initializes the CSVProcessor with a given filename.
        
        :param filename: The path to the CSV file to be processed.
        """
        self.filename = filename
        self.data = []

    def load_csv(self) -> None:
        """
        Loads the data from the CSV file into memory.
        
        Raises:
            FileNotFoundError: If the specified CSV file does not exist.
            csv.Error: If there is an error in reading the CSV file.
        """
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"The file {self.filename} does not exist.")
        
        try:
            with open(self.filename, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.data = [row for row in reader]
        except csv.Error as e:
            raise csv.Error(f"Error reading CSV file: {str(e)}")

    def filter_data(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Filters the loaded CSV data based on given criteria.
        
        :param criteria: A dictionary where the keys are column names and
                         the values are the desired values to filter by.
        :return: A list of dictionaries containing the filtered rows.
        """
        filtered_data = []
        for row in self.data:
            if all(row[key] == str(value) for key, value in criteria.items() if key in row):
                filtered_data.append(row)
        return filtered_data

    def save_to_csv(self, output_filename: str, data: List[Dict[str, Any]]) -> None:
        """
        Saves the given data to a new CSV file.
        
        :param output_filename: The path where the output CSV file will be saved.
        :param data: The data to save, as a list of dictionaries.
        
        Raises:
            IOError: If there is an error writing to the output file.
        """
        if not data:
            raise ValueError("No data to save.")

        try:
            with open(output_filename, mode='w', newline='', encoding='utf-8') as csvfile:
                if data:
                    fieldnames = data[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    writer.writeheader()
                    writer.writerows(data)
        except IOError as e:
            raise IOError(f"Error writing to CSV file: {str(e)}")

if __name__ == "__main__":
    # Example usage of the CSVProcessor
    try:
        processor = CSVProcessor('bank_statement_template.csv')
        processor.load_csv()
        criteria = {'TransactionType': 'Deposit'}
        filtered_data = processor.filter_data(criteria)
        processor.save_to_csv('filtered_transactions.csv', filtered_data)
        print(f"Filtered data saved to 'filtered_transactions.csv'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
