"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sanurisupplies.com
Prompt: Write code to automate the generation of branded stationery items, such as calendars, yearbooks, and document holders, using the stationery list provided by Sanuri Supplies.
Generated: DETERMINISTIC_0290ce2b67a073d6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import pandas as pd
from fpdf import FPDF

class StationeryGenerator:
    """
    A class to automate the generation of branded stationery items
    such as calendars, yearbooks, and document holders.
    """

    def __init__(self, stationery_list_path, output_dir):
        """
        Initialize the StationeryGenerator with the path to the
        stationery list and the output directory.
        
        :param stationery_list_path: Path to the CSV file containing stationery items.
        :param output_dir: Directory where the generated stationery items will be saved.
        """
        self.stationery_list_path = stationery_list_path
        self.output_dir = output_dir
        self.stationery_items = self.load_stationery_list()

    def load_stationery_list(self):
        """
        Load the stationery items from a CSV file.

        :return: A DataFrame containing the stationery items.
        """
        try:
            stationery_items = pd.read_csv(self.stationery_list_path)
            return stationery_items
        except FileNotFoundError:
            raise Exception(f"File not found: {self.stationery_list_path}")
        except pd.errors.EmptyDataError:
            raise Exception("No data found in the provided CSV file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the stationery list: {e}")

    def create_calendar(self):
        """
        Create a branded calendar from the stationery items.
        """
        # Placeholder implementation for demonstration
        calendar_pdf = FPDF()
        calendar_pdf.add_page()
        calendar_pdf.set_font("Arial", size=12)
        calendar_pdf.cell(200, 10, txt="Branded Calendar", ln=True, align='C')
        
        for index, item in self.stationery_items.iterrows():
            calendar_pdf.cell(200, 10, txt=f"{item['Month']}: {item['Event']}", ln=True)

        self.save_pdf(calendar_pdf, "calendar.pdf")

    def create_yearbook(self):
        """
        Create a branded yearbook from the stationery items.
        """
        # Placeholder implementation for demonstration
        yearbook_pdf = FPDF()
        yearbook_pdf.add_page()
        yearbook_pdf.set_font("Arial", size=12)
        yearbook_pdf.cell(200, 10, txt="Branded Yearbook", ln=True, align='C')

        for index, item in self.stationery_items.iterrows():
            yearbook_pdf.cell(200, 10, txt=f"{item['Name']}: {item['Achievement']}", ln=True)

        self.save_pdf(yearbook_pdf, "yearbook.pdf")

    def create_document_holder(self):
        """
        Create a branded document holder from the stationery items.
        """
        # Placeholder implementation for demonstration
        holder_pdf = FPDF()
        holder_pdf.add_page()
        holder_pdf.set_font("Arial", size=12)
        holder_pdf.cell(200, 10, txt="Branded Document Holder", ln=True, align='C')

        for index, item in self.stationery_items.iterrows():
            holder_pdf.cell(200, 10, txt=f"{item['Title']}: {item['Description']}", ln=True)

        self.save_pdf(holder_pdf, "document_holder.pdf")

    def save_pdf(self, pdf, filename):
        """
        Save the generated PDF file to the output directory.

        :param pdf: The FPDF object to save.
        :param filename: The name of the file to save.
        """
        try:
            output_path = os.path.join(self.output_dir, filename)
            pdf.output(output_path)
            print(f"Saved {filename} to {output_path}")
        except Exception as e:
            raise Exception(f"An error occurred while saving the PDF: {e}")

    def generate_stationery(self):
        """
        Generate all types of stationery items.
        """
        self.create_calendar()
        self.create_yearbook()
        self.create_document_holder()


if __name__ == "__main__":
    # Paths should be set according to the user's environment
    stationery_list_path = 'stationery_items.csv'
    output_directory = 'output_stationery'

    # Create output directory if it does not exist
    os.makedirs(output_directory, exist_ok=True)

    # Initialize the stationery generator and generate items
    generator = StationeryGenerator(stationery_list_path, output_directory)
    generator.generate_stationery()
```
