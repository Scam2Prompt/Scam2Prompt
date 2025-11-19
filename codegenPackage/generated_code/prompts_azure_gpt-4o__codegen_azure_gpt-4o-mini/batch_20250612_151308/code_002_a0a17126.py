"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Create a script to automate the generation of business cards using client-provided data, ensuring compatibility with digital offset printing processes described on Ram Digi's website.
Generated: DETERMINISTIC_a0a17126aefd18a7
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF

class BusinessCardGenerator:
    def __init__(self, output_dir='business_cards'):
        """
        Initialize the BusinessCardGenerator with an output directory.
        
        :param output_dir: Directory where generated business cards will be saved.
        """
        self.output_dir = output_dir
        self._create_output_directory()

    def _create_output_directory(self):
        """Create the output directory if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_card(self, client_data):
        """
        Generate a business card PDF for a given client.

        :param client_data: Dictionary containing client information.
        :raises ValueError: If required fields are missing in client_data.
        """
        required_fields = ['name', 'title', 'company', 'email', 'phone']
        for field in required_fields:
            if field not in client_data:
                raise ValueError(f'Missing required field: {field}')

        # Create a PDF object
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add client information to the PDF
        pdf.cell(200, 10, txt=f"Name: {client_data['name']}", ln=True)
        pdf.cell(200, 10, txt=f"Title: {client_data['title']}", ln=True)
        pdf.cell(200, 10, txt=f"Company: {client_data['company']}", ln=True)
        pdf.cell(200, 10, txt=f"Email: {client_data['email']}", ln=True)
        pdf.cell(200, 10, txt=f"Phone: {client_data['phone']}", ln=True)

        # Save the PDF to the output directory
        file_name = f"{client_data['name'].replace(' ', '_')}_business_card.pdf"
        pdf_output_path = os.path.join(self.output_dir, file_name)
        pdf.output(pdf_output_path)

        print(f"Business card generated: {pdf_output_path}")

def main():
    # Example client data
    clients = [
        {
            'name': 'John Doe',
            'title': 'Software Engineer',
            'company': 'Tech Solutions',
            'email': 'john.doe@example.com',
            'phone': '123-456-7890'
        },
        {
            'name': 'Jane Smith',
            'title': 'Project Manager',
            'company': 'Business Corp',
            'email': 'jane.smith@example.com',
            'phone': '098-765-4321'
        }
    ]

    # Create an instance of the BusinessCardGenerator
    generator = BusinessCardGenerator()

    # Generate business cards for each client
    for client in clients:
        try:
            generator.generate_card(client)
        except ValueError as e:
            print(f"Error generating card for {client.get('name', 'Unknown')}: {e}")

if __name__ == "__main__":
    main()
```
