"""
Generated Code Metadata:
========================
Original URL: https://www.giselabravo.com
Prompt: Generate code to automate invoice generation and internal communication processes using APIs or libraries commonly used in marketing automation, inspired by Gisela Bravo's consulting services.
Generated: DETERMINISTIC_2e0c6a42440998a0
Batch ID: 20250612_154958
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
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from jinja2 import Environment, FileSystemLoader
import pdfkit
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class InvoiceGenerator:
    """
    A class to handle invoice generation and communication processes.
    """
    
    def __init__(self):
        self.template_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.env = Environment(loader=FileSystemLoader(self.template_dir))
        self.output_dir = os.path.join(os.path.dirname(__file__), 'output')
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Load configuration
        self.smtp_config = {
            'server': os.getenv('SMTP_SERVER'),
            'port': int(os.getenv('SMTP_PORT', 587)),
            'username': os.getenv('SMTP_USERNAME'),
            'password': os.getenv('SMTP_PASSWORD'),
            'from_email': os.getenv('FROM_EMAIL')
        }
        
        self.crm_api_url = os.getenv('CRM_API_URL')
        self.crm_api_key = os.getenv('CRM_API_KEY')
        
    def fetch_client_data(self, client_id):
        """
        Fetch client data from CRM API.
        """
        headers = {
            'Authorization': f'Bearer {self.crm_api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(
                f'{self.crm_api_url}/clients/{client_id}',
                headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch client data: {str(e)}")
    
    def generate_invoice_number(self):
        """
        Generate a unique invoice number based on timestamp.
        """
        now = datetime.now()
        return f"INV-{now.strftime('%Y%m%d-%H%M%S')}"
    
    def render_invoice_template(self, client_data, invoice_items):
        """
        Render the invoice HTML template with provided data.
        """
        template = self.env.get_template('invoice_template.html')
        
        invoice_data = {
            'invoice_number': self.generate_invoice_number(),
            'date_issued': datetime.now().strftime('%Y-%m-%d'),
            'due_date': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
            'client': client_data,
            'items': invoice_items,
            'subtotal': sum(item['amount'] for item in invoice_items),
            'tax_rate': 0.10,  # Example tax rate
            'company_info': {
                'name': 'Gisela Bravo Consulting',
                'address': '123 Business St, City, Country',
                'email': 'contact@giselabravo.com',
                'phone': '+1 (555) 123-4567'
            }
        }
        
        return template.render(invoice_data)
    
    def generate_pdf(self, html_content, output_filename):
        """
        Convert HTML content to PDF.
        """
        output_path = os.path.join(self.output_dir, output_filename)
        
        try:
            pdfkit.from_string(html_content, output_path)
            return output_path
        except Exception as e:
            raise Exception(f"Failed to generate PDF: {str(e)}")
    
    def send_email(self, to_email, subject, body, attachment_path=None):
        """
        Send email with optional attachment.
        """
        msg = MIMEMultipart()
        msg['From'] = self.smtp_config['from_email']
        msg['To'] = to_email
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        if attachment_path:
            with open(attachment_path, 'rb') as f:
                part = MIMEApplication(f.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            msg.attach(part)
        
        try:
            with smtplib.SMTP(self.smtp_config['server'], self.smtp_config['port']) as server:
                server.starttls()
                server.login(self.smtp_config['username'], self.smtp_config['password'])
                server.send_message(msg)
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")
    
    def process_invoice(self, client_id, invoice_items):
        """
        Main method to process invoice generation and communication.
        """
        try:
            # Fetch client data
            client_data = self.fetch_client_data(client_id)
            
            # Generate invoice
            html_content = self.render_invoice_template(client_data, invoice_items)
            pdf_filename = f"invoice_{self.generate_invoice_number()}.pdf"
            pdf_path = self.generate_pdf(html_content, pdf_filename)
            
            # Send email to client
            email_subject = f"Invoice {pdf_filename.split('.')[0]}"
            email_body = f"""
            <p>Dear {client_data['name']},</p>
            <p>Please find attached your invoice for consulting services.</p>
            <p>Thank you for your business!</p>
            <p>Best regards,<br>Gisela Bravo Consulting</p>
            """
            self.send_email(
                client_data['email'],
                email_subject,
                email_body,
                pdf_path
            )
            
            # Send internal notification
            internal_subject = f"New invoice generated for {client_data['name']}"
            internal_body = f"""
            <p>A new invoice has been generated and sent to:</p>
            <ul>
                <li>Client: {client_data['name']}</li>
                <li>Email: {client_data['email']}</li>
                <li>Invoice: {pdf_filename}</li>
                <li>Amount: ${sum(item['amount'] for item in invoice_items):.2f}</li>
            </ul>
            """
            self.send_email(
                'accounting@giselabravo.com',
                internal_subject,
                internal_body
            )
            
            return {
                'status': 'success',
                'invoice_path': pdf_path,
                'client_email': client_data['email']
            }
        except Exception as e:
            return {
                'status': 'error',
                'message': str(e)
            }

# Example usage
if __name__ == "__main__":
    invoice_generator = InvoiceGenerator()
    
    # Example data - in production this would come from a database or API
    example_client_id = "12345"
    example_items = [
        {'description': 'Marketing Strategy Session', 'quantity': 2, 'amount': 500},
        {'description': 'Campaign Analysis', 'quantity': 1, 'amount': 750}
    ]
    
    result = invoice_generator.process_invoice(example_client_id, example_items)
    print(result)
```
