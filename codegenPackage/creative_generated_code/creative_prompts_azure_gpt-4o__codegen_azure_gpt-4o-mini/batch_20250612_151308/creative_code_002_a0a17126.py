"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Create a script to automate the generation of business cards using client-provided data, ensuring compatibility with digital offset printing processes described on Ram Digi's website.
Generated: DETERMINISTIC_a0a17126aefd18a7
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF

class BusinessCardGenerator:
    def __init__(self, output_dir):
        """
        Initializes the BusinessCardGenerator with an output directory.
        
        Args:
            output_dir (str): The directory where generated business cards will be stored.
        """
        self.output_dir = output_dir
        self.verify_output_directory()

    def verify_output_directory(self):
        """
        Verifies if the output directory exists and creates it if it doesn't.
        Raises:
            OSError: If the directory cannot be created or accessed.
        """
        try:
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
        except OSError as e:
            raise OSError(f"Error creating output directory: {e}")

    def create_business_card(self, client_data):
        """
        Generates a business card PDF using client-provided data.

        Args:
            client_data (dict): A dictionary containing client information such as name, title, phone, email, and address.
        
        Raises:
            ValueError: If any required field is missing from client_data.
        """
        required_fields = ['name', 'title', 'phone', 'email', 'address']
        for field in required_fields:
            if field not in client_data:
                raise ValueError(f"Missing required field: {field}")

        # Create a PDF object
        pdf = FPDF()
        pdf.add_page()

        # Set font for the business card
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, client_data['name'], ln=True)
        
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(0, 10, client_data['title'], ln=True)
        
        pdf.set_font("Arial", '', 12)
        pdf.cell(0, 10, f"Phone: {client_data['phone']}", ln=True)
        pdf.cell(0, 10, f"Email: {client_data['email']}", ln=True)
        pdf.cell(0, 10, f"Address: {client_data['address']}", ln=True)

        # Filename based on client name
        filename = f"{client_data['name'].replace(' ', '_').lower()}_business_card.pdf"
        output_file_path = os.path.join(self.output_dir, filename)

        # Save the PDF to the specified output directory
        pdf.output(output_file_path)
        print(f"Business card generated: {output_file_path}")

if __name__ == "__main__":
    # Example usage
    output_directory = "./business_cards"
    generator = BusinessCardGenerator(output_directory)

    # Example client data
    client_info = {
        'name': 'John Doe',
        'title': 'Software Engineer',
        'phone': '+1-234-567-8901',
        'email': 'john.doe@example.com',
        'address': '1234 Elm Street, Springfield, IL, 62701'
    }

    try:
        generator.create_business_card(client_info)
    except Exception as e:
        print(f"An error occurred: {e}")
```
