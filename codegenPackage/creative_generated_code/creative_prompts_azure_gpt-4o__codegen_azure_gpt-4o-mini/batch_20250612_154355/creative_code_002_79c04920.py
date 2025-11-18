"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roshako.com
Prompt: Create a function in Python to automate the generation of a quotation request email for industrial products, using Roshako's contact details and product categories.
Generated: DETERMINISTIC_79c04920b0a7482a
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List, Dict

# Define contact details for Roshako
ROSHKO_CONTACT = {
    "name": "Roshako Sales Team",
    "email": "sales@roshako.com",
    "phone": "+123456789",
    "address": "123 Industrial Rd, Manufacturing City, ST 12345"
}

def generate_quotation_request_email(recipient_email: str, product_categories: List[str]) -> str:
    """
    Generate the body of a quotation request email for industrial products.

    Parameters:
    recipient_email (str): The email address of the recipient.
    product_categories (List[str]): List of product categories for which the quote is requested.

    Returns:
    str: The formatted email body.
    """
    # Validate the recipient email
    if not validate_email(recipient_email):
        raise ValueError("Invalid recipient email address.")

    # Construct the email body
    email_body = f"""
    Dear {ROSHKO_CONTACT['name']},

    I hope this message finds you well.

    We are interested in receiving a quotation for the following product categories:
    {', '.join(product_categories)}

    Please include pricing, availability, and any additional information you may have.

    Thank you for your assistance.

    Best regards,
    [Your Name]
    [Your Company]
    Email: {recipient_email}
    Phone: {ROSHKO_CONTACT['phone']}
    Address: {ROSHKO_CONTACT['address']}
    """
    return email_body

def validate_email(email: str) -> bool:
    """
    Validate the email address format.

    Parameters:
    email (str): The email address to validate.

    Returns:
    bool: True if valid, False otherwise.
    """
    import re
    # Basic regex for email validation
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return re.match(email_regex, email) is not None

def send_email(subject: str, body: str, recipient_email: str) -> None:
    """
    Send an email using SMTP.

    Parameters:
    subject (str): The subject of the email.
    body (str): The body content of the email.
    recipient_email (str): The email address of the recipient.
    
    Raises:
    Exception: If the email could not be sent.
    """
    try:
        # Configure SMTP server (example using Gmail)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        sender_email = ROSHKO_CONTACT['email']
        password = "YOUR_EMAIL_PASSWORD"  # Update with the actual password or use environment variables for security

        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body to the message
        msg.attach(MIMEText(body, 'plain'))

        # Establish a secure session with SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(sender_email, password)  # Log in to the email account
            server.send_message(msg)  # Send the email

    except Exception as e:
        raise Exception(f"Failed to send email: {str(e)}")

# Example usage
if __name__ == "__main__":
    recipient = "client@example.com"
    categories = ["Machinery", "Tools", "Raw Materials"]

    try:
        email_body = generate_quotation_request_email(recipient, categories)
        send_email("Quotation Request", email_body, recipient)
        print("Quotation request email sent successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")
```
