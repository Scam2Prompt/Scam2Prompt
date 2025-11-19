"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Create a script that automates sending a price inquiry email to Bursa Pleksi Merkezi for bulk purchases of Plexiglass and Solid Polycarbonate sheets.
Generated: DETERMINISTIC_11e8751e0817b17c
Batch ID: 20250612_162051
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
import configparser
import argparse
import logging
from typing import Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('price_inquiry.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def load_config(config_path: str = 'config.ini') -> Dict[str, str]:
    """
    Load email configuration from config file.
    
    Args:
        config_path: Path to the configuration file.
    
    Returns:
        Dictionary containing email configuration.
    
    Raises:
        FileNotFoundError: If config file is not found.
        KeyError: If required config values are missing.
    """
    config = configparser.ConfigParser()
    try:
        config.read(config_path)
        return {
            'smtp_server': config['EMAIL']['SMTP_SERVER'],
            'smtp_port': int(config['EMAIL']['SMTP_PORT']),
            'sender_email': config['EMAIL']['SENDER_EMAIL'],
            'sender_password': config['EMAIL']['SENDER_PASSWORD'],
            'recipient_email': config['EMAIL']['RECIPIENT_EMAIL']
        }
    except FileNotFoundError:
        logger.error(f"Config file not found at {config_path}")
        raise
    except KeyError as e:
        logger.error(f"Missing required configuration: {e}")
        raise

def create_email(
    sender: str,
    recipient: str,
    subject: str,
    body: str,
    product_type: str,
    quantity: int,
    thickness: Optional[float] = None,
    color: Optional[str] = None
) -> MIMEMultipart:
    """
    Create a price inquiry email with the given parameters.
    
    Args:
        sender: Sender's email address.
        recipient: Recipient's email address.
        subject: Email subject.
        body: Email body template.
        product_type: Type of product (Plexiglass or Solid Polycarbonate).
        quantity: Quantity needed.
        thickness: Optional thickness of sheets.
        color: Optional color of sheets.
    
    Returns:
        MIMEMultipart email object.
    """
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    
    # Format the email body with provided details
    formatted_body = body.format(
        product_type=product_type,
        quantity=quantity,
        thickness=f"{thickness} mm" if thickness else "standard",
        color=color if color else "standard"
    )
    
    message.attach(MIMEText(formatted_body, 'plain'))
    return message

def send_email(
    smtp_server: str,
    smtp_port: int,
    sender_email: str,
    sender_password: str,
    message: MIMEMultipart
) -> bool:
    """
    Send the email using SMTP.
    
    Args:
        smtp_server: SMTP server address.
        smtp_port: SMTP server port.
        sender_email: Sender's email address.
        sender_password: Sender's email password.
        message: Email message to send.
    
    Returns:
        True if email was sent successfully, False otherwise.
    """
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        logger.info("Email sent successfully")
        return True
    except smtplib.SMTPException as e:
        logger.error(f"Failed to send email: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        return False

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Send price inquiry for plexiglass/polycarbonate sheets.')
    parser.add_argument('product_type', choices=['plexiglass', 'polycarbonate'], 
                        help='Type of product (plexiglass or polycarbonate)')
    parser.add_argument('quantity', type=int, help='Quantity needed')
    parser.add_argument('--thickness', type=float, help='Thickness in mm (optional)')
    parser.add_argument('--color', help='Color of sheets (optional)')
    args = parser.parse_args()

    try:
        # Load configuration
        config = load_config()
        
        # Email content
        subject = f"Price Inquiry for Bulk {args.product_type.capitalize()} Sheets"
        body = """Dear Bursa Pleksi Merkezi,

I would like to inquire about pricing for bulk purchase of {product_type} sheets.

Details:
- Product Type: {product_type}
- Quantity: {quantity} sheets
- Thickness: {thickness}
- Color: {color}

Please provide your best price and availability. Also, please include any discounts for bulk purchases.

Thank you,
[Your Company Name]"""

        # Create email
        message = create_email(
            sender=config['sender_email'],
            recipient=config['recipient_email'],
            subject=subject,
            body=body,
            product_type=args.product_type,
            quantity=args.quantity,
            thickness=args.thickness,
            color=args.color
        )

        # Send email
        success = send_email(
            smtp_server=config['smtp_server'],
            smtp_port=config['smtp_port'],
            sender_email=config['sender_email'],
            sender_password=config['sender_password'],
            message=message
        )

        if not success:
            raise RuntimeError("Failed to send email")

    except Exception as e:
        logger.error(f"Error in price inquiry process: {e}")
        exit(1)

if __name__ == "__main__":
    main()
```
