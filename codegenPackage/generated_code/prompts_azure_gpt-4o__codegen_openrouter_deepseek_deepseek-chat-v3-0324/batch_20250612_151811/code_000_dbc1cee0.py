"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: Write Python code to automate the process of generating quotes for wire mesh products, including fields for name, email, phone number, address, subject, and message, as described on the Baochuan Wire Mesh website.
Generated: DETERMINISTIC_dbc1cee0bc83d8a7
Batch ID: 20250612_151811
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
import json
import os
from datetime import datetime
from typing import Dict, Optional

class QuoteGenerator:
    """
    A class to handle the generation and sending of wire mesh product quotes.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the QuoteGenerator with configuration.
        
        Args:
            config_path: Path to the configuration file.
        """
        self.config = self._load_config(config_path)
        self.quotes_dir = "quotes"
        os.makedirs(self.quotes_dir, exist_ok=True)
        
    def _load_config(self, config_path: str) -> Dict:
        """
        Load configuration from JSON file.
        
        Args:
            config_path: Path to the configuration file.
            
        Returns:
            Dictionary containing configuration.
            
        Raises:
            FileNotFoundError: If config file doesn't exist.
            json.JSONDecodeError: If config file is malformed.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {config_path}")
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in configuration file: {e}", e.doc, e.pos)
    
    def generate_quote(
        self,
        name: str,
        email: str,
        phone: str,
        address: str,
        subject: str,
        message: str,
        products: Optional[Dict] = None
    ) -> str:
        """
        Generate a quote document and save it to disk.
        
        Args:
            name: Customer name.
            email: Customer email.
            phone: Customer phone number.
            address: Customer address.
            subject: Quote subject.
            message: Customer message.
            products: Dictionary of products and quantities (optional).
            
        Returns:
            Path to the generated quote file.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"quote_{timestamp}.txt"
        filepath = os.path.join(self.quotes_dir, filename)
        
        quote_content = self._build_quote_content(
            name, email, phone, address, subject, message, products
        )
        
        with open(filepath, 'w') as f:
            f.write(quote_content)
            
        return filepath
    
    def _build_quote_content(
        self,
        name: str,
        email: str,
        phone: str,
        address: str,
        subject: str,
        message: str,
        products: Optional[Dict] = None
    ) -> str:
        """
        Build the content of the quote document.
        
        Args:
            name: Customer name.
            email: Customer email.
            phone: Customer phone number.
            address: Customer address.
            subject: Quote subject.
            message: Customer message.
            products: Dictionary of products and quantities (optional).
            
        Returns:
            Formatted quote content as string.
        """
        content = [
            f"Quote Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            "\nCustomer Information:",
            f"Name: {name}",
            f"Email: {email}",
            f"Phone: {phone}",
            f"Address: {address}",
            "\nQuote Details:",
            f"Subject: {subject}",
            f"Message: {message}",
        ]
        
        if products:
            content.append("\nProducts Requested:")
            for product, quantity in products.items():
                content.append(f"- {product}: {quantity}")
        
        content.append("\nThank you for your inquiry!")
        content.append("Baochuan Wire Mesh Team")
        
        return "\n".join(content)
    
    def send_quote_email(self, quote_path: str, recipient_email: str) -> bool:
        """
        Send the generated quote via email.
        
        Args:
            quote_path: Path to the quote file.
            recipient_email: Email address of the recipient.
            
        Returns:
            True if email was sent successfully, False otherwise.
        """
        try:
            with open(quote_path, 'r') as f:
                quote_content = f.read()
            
            msg = MIMEMultipart()
            msg['From'] = self.config['email']['sender']
            msg['To'] = recipient_email
            msg['Subject'] = "Your Wire Mesh Product Quote"
            
            body = (
                "Dear Customer,\n\n"
                "Please find attached your wire mesh product quote.\n\n"
                "Best regards,\n"
                "Baochuan Wire Mesh Team"
            )
            
            msg.attach(MIMEText(body, 'plain'))
            msg.attach(MIMEText(quote_content, 'plain'))
            
            with smtplib.SMTP(
                self.config['email']['smtp_server'],
                self.config['email']['smtp_port']
            ) as server:
                server.starttls()
                server.login(
                    self.config['email']['sender'],
                    self.config['email']['password']
                )
                server.send_message(msg)
            
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

# Example usage
if __name__ == "__main__":
    try:
        # Initialize quote generator
        generator = QuoteGenerator()
        
        # Customer information
        customer_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890",
            "address": "123 Main St, Anytown, USA",
            "subject": "Wire Mesh Fence Quote",
            "message": "I need a quote for 100m of 2m high wire mesh fence.",
            "products": {
                "Wire Mesh Fence (2m height)": "100 meters",
                "Installation": "Included"
            }
        }
        
        # Generate quote
        quote_path = generator.generate_quote(**customer_data)
        print(f"Quote generated at: {quote_path}")
        
        # Send quote via email
        if generator.send_quote_email(quote_path, customer_data["email"]):
            print("Quote email sent successfully!")
        else:
            print("Failed to send quote email.")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
