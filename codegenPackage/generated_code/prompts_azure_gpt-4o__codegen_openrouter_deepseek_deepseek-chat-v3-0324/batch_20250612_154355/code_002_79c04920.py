"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Create a function in Python to automate the generation of a quotation request email for industrial products, using Roshako's contact details and product categories.
Generated: DETERMINISTIC_79c04920b0a7482a
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict, Optional

class QuotationEmailGenerator:
    """
    A class to generate and send quotation request emails for industrial products.
    """
    
    def __init__(self, sender_email: str, sender_password: str, smtp_server: str = "smtp.gmail.com", smtp_port: int = 587):
        """
        Initialize the email generator with sender credentials and SMTP settings.
        
        Args:
            sender_email (str): Email address of the sender
            sender_password (str): Password for the sender email
            smtp_server (str): SMTP server address (default: Gmail)
            smtp_port (int): SMTP port number (default: 587)
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        
        # Roshako's contact details
        self.roshako_contact = {
            "company_name": "Roshako Industrial Solutions",
            "email": "sales@roshako.com",
            "phone": "+1 (555) 123-4567",
            "address": "123 Industrial Park, Suite 456, Houston, TX 77001"
        }
        
        # Product categories
        self.product_categories = [
            "Valves & Actuators",
            "Pumps & Compressors",
            "Heat Exchangers",
            "Process Control Instruments",
            "Industrial Piping",
            "Safety Equipment"
        ]
    
    def generate_email_content(self, recipient_name: str, company_name: str, products: List[Dict[str, str]]) -> str:
        """
        Generate the HTML content for the quotation request email.
        
        Args:
            recipient_name (str): Name of the recipient
            company_name (str): Name of the recipient's company
            products (List[Dict[str, str]]): List of products with details
            
        Returns:
            str: HTML formatted email content
        """
        # Product list HTML
        product_list_html = ""
        for product in products:
            product_list_html += f"""
            <tr>
                <td style="border: 1px solid #ddd; padding: 8px;">{product.get('category', 'N/A')}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">{product.get('name', 'N/A')}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">{product.get('quantity', 'N/A')}</td>
                <td style="border: 1px solid #ddd; padding: 8px;">{product.get('specifications', 'N/A')}</td>
            </tr>
            """
        
        html_content = f"""
        <html>
            <body>
                <p>Dear {recipient_name},</p>
                
                <p>I hope this email finds you well. I am writing on behalf of {company_name} 
                to request a quotation for the following industrial products:</p>
                
                <table style="border-collapse: collapse; width: 100%; margin: 20px 0;">
                    <thead>
                        <tr style="background-color: #f2f2f2;">
                            <th style="border: 1px solid #ddd; padding: 8px;">Category</th>
                            <th style="border: 1px solid #ddd; padding: 8px;">Product Name</th>
                            <th style="border: 1px solid #ddd; padding: 8px;">Quantity</th>
                            <th style="border: 1px solid #ddd; padding: 8px;">Specifications</th>
                        </tr>
                    </thead>
                    <tbody>
                        {product_list_html}
                    </tbody>
                </table>
                
                <p>Please provide your best quotation including:</p>
                <ul>
                    <li>Unit price and total price</li>
                    <li>Delivery time</li>
                    <li>Payment terms</li>
                    <li>Validity period of the quotation</li>
                </ul>
                
                <p>We would appreciate it if you could send your quotation by [insert deadline date]. 
                Please don't hesitate to contact me if you need any additional information.</p>
                
                <p>Best regards,</p>
                <p>[Your Name]<br>
                [Your Position]<br>
                {company_name}<br>
                [Your Contact Information]</p>
                
                <hr>
                
                <p style="font-size: 0.9em; color: #666;">
                    <strong>Roshako Industrial Solutions Contact:</strong><br>
                    Email: {self.roshako_contact['email']}<br>
                    Phone: {self.roshako_contact['phone']}<br>
                    Address: {self.roshako_contact['address']}
                </p>
            </body>
        </html>
        """
        
        return html_content
    
    def send_email(self, recipient_email: str, subject: str, html_content: str, cc_emails: Optional[List[str]] = None) -> bool:
        """
        Send the quotation request email.
        
        Args:
            recipient_email (str): Email address of the recipient
            subject (str): Email subject
            html_content (str): HTML content of the email
            cc_emails (Optional[List[str]]): List of CC email addresses
            
        Returns:
            bool: True if email was sent successfully, False otherwise
        """
        try:
            # Create message container
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            if cc_emails:
                msg['Cc'] = ", ".join(cc_emails)
            
            # Attach HTML content
            msg.attach(MIMEText(html_content, 'html'))
            
            # Connect to SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                
                # Combine recipient and CC emails
                all_recipients = [recipient_email]
                if cc_emails:
                    all_recipients.extend(cc_emails)
                
                server.sendmail(self.sender_email, all_recipients, msg.as_string())
            
            return True
        except Exception as e:
            print(f"Error sending email: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize email generator
    email_gen = QuotationEmailGenerator(
        sender_email="your.email@example.com",
        sender_password="yourpassword"
    )
    
    # Define products for quotation
    products = [
        {
            "category": "Valves & Actuators",
            "name": "Ball Valve 2-inch",
            "quantity": "10 units",
            "specifications": "Stainless steel, 300 psi rating"
        },
        {
            "category": "Pumps & Compressors",
            "name": "Centrifugal Pump",
            "quantity": "5 units",
            "specifications": "10 HP, 100 GPM capacity"
        }
    ]
    
    # Generate email content
    html_content = email_gen.generate_email_content(
        recipient_name="John Smith",
        company_name="ABC Manufacturing",
        products=products
    )
    
    # Send email
    success = email_gen.send_email(
        recipient_email="john.smith@abcmfg.com",
        subject="Quotation Request for Industrial Products",
        html_content=html_content,
        cc_emails=["procurement@abcmfg.com"]
    )
    
    if success:
        print("Quotation request email sent successfully!")
    else:
        print("Failed to send quotation request email.")
```
