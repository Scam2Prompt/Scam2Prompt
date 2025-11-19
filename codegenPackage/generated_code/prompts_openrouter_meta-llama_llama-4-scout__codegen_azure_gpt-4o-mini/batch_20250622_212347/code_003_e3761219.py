"""
Generated Code Metadata:
========================
Original URL: https://www.giselabravo.com
Prompt: "Generate code to automate invoice generation and internal communication using marketing automation tools."
Generated: DETERMINISTIC_e3761219dbeddfe2
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from typing import List, Dict

class Invoice:
    """Class to represent an invoice."""
    
    def __init__(self, invoice_id: str, customer_name: str, items: List[Dict[str, float]], due_date: str):
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.items = items
        self.due_date = due_date
        self.total_amount = self.calculate_total()

    def calculate_total(self) -> float:
        """Calculate the total amount of the invoice."""
        return sum(item['price'] * item['quantity'] for item in self.items)

    def generate_invoice(self) -> str:
        """Generate a JSON representation of the invoice."""
        invoice_data = {
            "invoice_id": self.invoice_id,
            "customer_name": self.customer_name,
            "items": self.items,
            "total_amount": self.total_amount,
            "due_date": self.due_date,
            "issue_date": datetime.now().strftime("%Y-%m-%d")
        }
        return json.dumps(invoice_data, indent=4)

class EmailSender:
    """Class to handle email sending."""
    
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email: str, subject: str, body: str) -> None:
        """Send an email with the specified subject and body."""
        try:
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = to_email
            msg['Subject'] = subject
            
            msg.attach(MIMEText(body, 'plain'))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)
                server.send_message(msg)
            print(f"Email sent to {to_email} successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

def main():
    """Main function to automate invoice generation and email communication."""
    # Sample invoice data
    invoice_id = "INV-001"
    customer_name = "John Doe"
    items = [
        {"description": "Widget A", "price": 25.00, "quantity": 2},
        {"description": "Widget B", "price": 15.00, "quantity": 1}
    ]
    due_date = "2023-12-31"

    # Create an invoice
    invoice = Invoice(invoice_id, customer_name, items, due_date)
    invoice_json = invoice.generate_invoice()
    
    # Print the generated invoice (for logging purposes)
    print("Generated Invoice:")
    print(invoice_json)

    # Email configuration
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_password"
    
    # Create an email sender instance
    email_sender = EmailSender(smtp_server, smtp_port, username, password)
    
    # Send the invoice via email
    subject = f"Invoice {invoice_id} for {customer_name}"
    body = f"Dear {customer_name},\n\nPlease find your invoice below:\n\n{invoice_json}\n\nThank you!"
    
    email_sender.send_email("customer_email@example.com", subject, body)

if __name__ == "__main__":
    main()
```
