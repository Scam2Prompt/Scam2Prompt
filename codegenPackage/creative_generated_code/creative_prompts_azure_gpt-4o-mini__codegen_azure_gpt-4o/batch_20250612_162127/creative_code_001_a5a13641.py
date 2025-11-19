"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.giselabravo.com
Prompt: What are some effective ways to automate invoice generation and improve internal communication based on Gisela Bravo's marketing automation services?
Generated: DETERMINISTIC_a5a13641aa3ccfaa
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automate invoice generation and send notifications to improve internal communication.
This Python script uses the `reportlab` library for PDF invoice generation and `smtplib` for email notifications.
Ensure dependencies are installed: `pip install reportlab`.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Path to save the generated invoices
INVOICE_DIRECTORY = 'invoices'
os.makedirs(INVOICE_DIRECTORY, exist_ok=True)

# Email configurations
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your-email@example.com'
SMTP_PASSWORD = 'your-email-password'
NOTIFICATION_EMAIL = 'recipient@example.com'

# Function to generate invoice
def generate_invoice(invoice_id, client_name, items, total_amount):
    """
    Generate a PDF invoice with given details.

    Args:
        invoice_id (str): Unique identifier for the invoice.
        client_name (str): Name of the client.
        items (list): List of tuples (item_name, price) representing the invoice items.
        total_amount (float): Total amount to be charged.

    Returns:
        str: Path to the generated invoice file.
    """
    invoice_path = os.path.join(INVOICE_DIRECTORY, f"invoice_{invoice_id}.pdf")
    c = canvas.Canvas(invoice_path, pagesize=letter)
    c.setFont("Helvetica", 12)
    
    # Header
    c.drawString(50, 750, f"Invoice ID: {invoice_id}")
    c.drawString(50, 735, f"Client Name: {client_name}")
    c.drawString(50, 720, "Date: YYYY-MM-DD")
    c.drawString(50, 705, "----------------------------------------")
    
    # Body - Itemized list
    y = 670
    for item_name, price in items:
        c.drawString(50, y, f"{item_name}: ${price:.2f}")
        y -= 20
    
    # Footer
    c.drawString(50, y - 20, "----------------------------------------")
    c.drawString(50, y - 40, f"Total: ${total_amount:.2f}")
    
    # Finalize and save the PDF
    c.save()
    return invoice_path

# Function to send email notification
def send_email_notification(subject, body, attachment_path=None):
    """
    Send an email notification with optional attachment.

    Args:
        subject (str): Email subject.
        body (str): Email body.
        attachment_path (str): Path to the file to be attached (optional).
    """
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = SMTP_USERNAME
        msg['To'] = NOTIFICATION_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach the file if provided
        if attachment_path:
            with open(attachment_path, 'rb') as attachment:
                part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                msg.attach(part)
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
            print(f"Notification email sent successfully to {NOTIFICATION_EMAIL}.")
    
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    # Invoice details
    invoice_id = "12345"
    client_name = "Acme Corporation"
    items = [("Marketing Campaign - Social Media", 500.00),
             ("SEO Optimization", 300.00)]
    total_amount = sum(price for _, price in items)
    
    # Generate the invoice
    invoice_path = generate_invoice(invoice_id, client_name, items, total_amount)
    print(f"Invoice generated: {invoice_path}")
    
    # Send email notification with the invoice attached
    subject = f"Invoice #{invoice_id} for {client_name}"
    body = f"Hello {client_name},\n\nPlease find attached your invoice #{invoice_id}.\nTotal Due: ${total_amount:.2f}\n\nRegards,\nYour Company"
    send_email_notification(subject, body, invoice_path)
```
