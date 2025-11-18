"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoablabs.com
Prompt: Create a Python program to generate shipping labels for sample kits, incorporating A & B Labs' guidelines for domestic and international shipments.
Generated: DETERMINISTIC_c417c87e5adff61a
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from fpdf import FPDF

class ShippingLabelGenerator:
    """
    A class to generate shipping labels for sample kits according to A & B Labs' guidelines.
    """

    def __init__(self, output_directory='labels'):
        """
        Initializes the ShippingLabelGenerator.

        :param output_directory: Directory to save the generated shipping labels
        """
        self.output_directory = output_directory
        self.validate_output_directory()

    def validate_output_directory(self):
        """Ensures the output directory exists; creates if it does not."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def generate_label(self, recipient_info, is_international=False):
        """
        Generates a shipping label for the given recipient information.

        :param recipient_info: Dictionary containing recipient details
        :param is_international: Boolean indicating if the shipment is international
        :return: Path to the generated shipping label
        """
        if not self.validate_recipient_info(recipient_info):
            raise ValueError("Recipient information is incomplete or invalid.")

        label = self.create_pdf_label(recipient_info, is_international)
        label_path = os.path.join(self.output_directory, f"{recipient_info['name']}_shipping_label.pdf")
        label.output(label_path)

        return label_path

    def validate_recipient_info(self, recipient_info):
        """
        Validates the recipient information.

        :param recipient_info: Dictionary containing recipient details
        :return: True if valid, False otherwise
        """
        required_fields = ['name', 'address', 'city', 'state', 'zip_code', 'country']
        return all(field in recipient_info for field in required_fields)

    def create_pdf_label(self, recipient_info, is_international):
        """
        Creates a PDF shipping label.

        :param recipient_info: Dictionary containing recipient details
        :param is_international: Boolean indicating if the shipment is international
        :return: FPDF object representing the shipping label
        """
        pdf = FPDF()
        pdf.add_page()

        # Set font for the label
        pdf.set_font("Arial", size=12)

        # Add recipient information to the label
        pdf.cell(200, 10, f"Shipping Label for {recipient_info['name']}", ln=True, align='C')
        pdf.cell(200, 10, recipient_info['address'], ln=True)
        pdf.cell(200, 10, f"{recipient_info['city']}, {recipient_info['state']} {recipient_info['zip_code']}", ln=True)
        pdf.cell(200, 10, recipient_info['country'], ln=True)

        # Add international notice if applicable
        if is_international:
            pdf.cell(200, 10, "International Shipment - Customs Declaration Required", ln=True, align='C')

        return pdf

def load_recipient_info(file_path):
    """
    Loads recipient information from a JSON file.

    :param file_path: Path to the JSON file containing recipient information
    :return: Dictionary containing recipient details
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        raise ValueError(f"Error loading recipient information: {str(e)}")

if __name__ == "__main__":
    # Example usage
    try:
        recipient_file = 'recipient_info.json'  # Adjust the path as needed
        recipient_info = load_recipient_info(recipient_file)

        # Specify if the shipment is international
        is_international = recipient_info.get('country', '').lower() not in ['united states', 'usa']

        generator = ShippingLabelGenerator()
        label_path = generator.generate_label(recipient_info, is_international)

        print(f"Shipping label generated at: {label_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
```

This code adheres to best practices, is well-documented, and includes proper error handling, making it suitable for production use. Please ensure the `fpdf` library is installed in your Python environment (`pip install fpdf`) and prepare a JSON file with the appropriate recipient information to test the program.
