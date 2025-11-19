"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Write code to automate the generation of branded stationery items, such as calendars, yearbooks, and document holders, using the stationery list provided by Sanuri Supplies.
Generated: DETERMINISTIC_0290ce2b67a073d6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from fpdf import FPDF

class StationeryGenerator:
    def __init__(self, stationery_list_file):
        """
        Initializes the StationeryGenerator with a list of stationery items.

        :param stationery_list_file: Path to the JSON file containing stationery items.
        """
        self.stationery_list_file = stationery_list_file
        self.stationery_items = self.load_stationery_items()

    def load_stationery_items(self):
        """
        Loads the stationery items from a JSON file.

        :return: A list of stationery items.
        """
        try:
            with open(self.stationery_list_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Stationery list file not found: {self.stationery_list_file}")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the stationery list file.")

    def create_calendar(self, year):
        """
        Generates a calendar for the specified year.

        :param year: The year for which the calendar is to be generated.
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"Calendar for {year}", ln=True, align='C')

        # Placeholder for calendar generation logic
        for month in range(1, 13):
            pdf.cell(0, 10, f"Month {month}", ln=True)

        output_file = f"calendar_{year}.pdf"
        pdf.output(output_file)
        print(f"Calendar for {year} generated: {output_file}")

    def create_yearbook(self, title):
        """
        Generates a yearbook with the specified title.

        :param title: The title of the yearbook.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, title, ln=True, align='C')

        # Placeholder for yearbook content
        for item in self.stationery_items:
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 10, item, ln=True)

        output_file = f"yearbook_{title.replace(' ', '_')}.pdf"
        pdf.output(output_file)
        print(f"Yearbook '{title}' generated: {output_file}")

    def create_document_holder(self, title):
        """
        Generates a document holder with the specified title.

        :param title: The title of the document holder.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, title, ln=True, align='C')

        # Placeholder for document holder content
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, "Document Holder Content", ln=True)

        output_file = f"document_holder_{title.replace(' ', '_')}.pdf"
        pdf.output(output_file)
        print(f"Document holder '{title}' generated: {output_file}")

if __name__ == "__main__":
    # Path to the stationery list JSON file
    stationery_list_path = "stationery_list.json"

    # Create an instance of the StationeryGenerator
    generator = StationeryGenerator(stationery_list_path)

    # Generate a calendar for the year 2023
    generator.create_calendar(2023)

    # Generate a yearbook with a specific title
    generator.create_yearbook("2023 Yearbook")

    # Generate a document holder with a specific title
    generator.create_document_holder("2023 Document Holder")
```

Make sure to have the `fpdf` library installed in your Python environment. You can install it using pip:

```bash
pip install fpdf
```

Also, ensure that the `stationery_list.json` file exists in the same directory as the script or provide the correct path to it. The JSON file should contain a list of stationery items.
