"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Write a Python script that automates the preparation of tax forms for immigrants, referencing the services offered by Hispanic Services.
Generated: DETERMINISTIC_6067d0363bd35d1f
Batch ID: 20250612_164222
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
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, filename='tax_form_preparation.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class TaxFormPreparation:
    def __init__(self, input_file: str, output_dir: str):
        """
        Initializes the TaxFormPreparation instance.

        :param input_file: Path to the input CSV file containing immigrant data.
        :param output_dir: Directory where the generated tax forms will be saved.
        """
        self.input_file = input_file
        self.output_dir = output_dir

        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def read_data(self):
        """
        Reads immigrant data from a CSV file.

        :return: List of dictionaries containing immigrant data.
        """
        try:
            with open(self.input_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                data = [row for row in reader]
            logging.info("Data read successfully from %s", self.input_file)
            return data
        except FileNotFoundError:
            logging.error("Input file not found: %s", self.input_file)
            raise
        except Exception as e:
            logging.error("An error occurred while reading data: %s", e)
            raise

    def generate_tax_forms(self, immigrant_data):
        """
        Generates tax forms for each immigrant in the provided data.

        :param immigrant_data: List of dictionaries containing immigrant data.
        """
        for person in immigrant_data:
            try:
                # Create a tax form content
                tax_form_content = self.create_tax_form(person)
                
                # Define output file name
                output_file = os.path.join(self.output_dir, f"{person['name'].replace(' ', '_')}_tax_form.txt")

                # Write tax form to a file
                with open(output_file, mode='w', encoding='utf-8') as file:
                    file.write(tax_form_content)

                logging.info("Tax form generated for %s", person['name'])
            except Exception as e:
                logging.error("Failed to generate tax form for %s: %s", person['name'], e)

    def create_tax_form(self, person):
        """
        Creates the content of the tax form based on immigrant data.

        :param person: Dictionary containing data for a single immigrant.
        :return: String content for the tax form.
        """
        return (f"Tax Form for {person['name']}\n"
                f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
                f"Address: {person['address']}\n"
                f"SSN: {person['ssn']}\n"
                f"Income: {person['income']}\n"
                f"Tax Guidelines provided by Hispanic Services.\n")

    def run(self):
        """
        Executes the tax form preparation process.
        """
        try:
            immigrant_data = self.read_data()
            self.generate_tax_forms(immigrant_data)
            logging.info("Tax form preparation completed successfully.")
        except Exception as e:
            logging.error("An error occurred during tax form preparation: %s", e)

if __name__ == "__main__":
    # Example usage
    input_csv = 'immigrant_data.csv'  # Path to the input CSV file
    output_directory = 'tax_forms'     # Directory to save generated tax forms

    tax_form_preparation = TaxFormPreparation(input_csv, output_directory)
    tax_form_preparation.run()
```
