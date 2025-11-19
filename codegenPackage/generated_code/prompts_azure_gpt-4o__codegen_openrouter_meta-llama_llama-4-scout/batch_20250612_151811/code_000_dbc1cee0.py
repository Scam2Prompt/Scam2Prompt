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
# Import required libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

class WireMeshQuoteGenerator:
    def __init__(self, 
                 name: str, 
                 email: str, 
                 phone_number: str, 
                 address: str, 
                 subject: str, 
                 message: str):
        """
        Initialize the WireMeshQuoteGenerator class.

        Args:
        - name (str): The name of the user requesting the quote.
        - email (str): The email address of the user requesting the quote.
        - phone_number (str): The phone number of the user requesting the quote.
        - address (str): The address of the user requesting the quote.
        - subject (str): The subject of the quote request.
        - message (str): The message or description of the quote request.
        """
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.subject = subject
        self.message = message

    def generate_quote_request(self) -> str:
        """
        Generate a formatted string for the quote request.

        Returns:
        - str: A formatted string containing the user's information and message.
        """
        quote_request = f"""
        Name: {self.name}
        Email: {self.email}
        Phone Number: {self.phone_number}
        Address: {self.address}
        Subject: {self.subject}
        Message: {self.message}
        """
        return quote_request

    def send_quote_request(self, 
                          sender_email: str, 
                          sender_password: str, 
                          recipient_email: str, 
                          smtp_server: str = "smtp.gmail.com", 
                          smtp_port: int = 587) -> bool:
        """
        Send the quote request via email.

        Args:
        - sender_email (str): The email address of the sender.
        - sender_password (str): The password of the sender's email account.
        - recipient_email (str): The email address of the recipient.
        - smtp_server (str): The SMTP server to use. Defaults to "smtp.gmail.com".
        - smtp_port (int): The SMTP port to use. Defaults to 587.

        Returns:
        - bool: True if the email was sent successfully, False otherwise.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient_email
            msg['Subject'] = self.subject

            body = self.generate_quote_request()
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, recipient_email, text)
            server.quit()
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False


def load_config(file_path: str) -> dict:
    """
    Load configuration from a JSON file.

    Args:
    - file_path (str): The path to the JSON file.

    Returns:
    - dict: A dictionary containing the configuration.
    """
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
            return config
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return {}

def main():
    # Load configuration from JSON file
    config = load_config('config.json')

    # Create a WireMeshQuoteGenerator instance
    quote_generator = WireMeshQuoteGenerator(
        name=config['name'],
        email=config['email'],
        phone_number=config['phone_number'],
        address=config['address'],
        subject=config['subject'],
        message=config['message']
    )

    # Send the quote request
    sender_email = config['sender_email']
    sender_password = config['sender_password']
    recipient_email = config['recipient_email']

    success = quote_generator.send_quote_request(
        sender_email, 
        sender_password, 
        recipient_email
    )

    if success:
        print("Quote request sent successfully!")
    else:
        print("Failed to send quote request.")

if __name__ == "__main__":
    main()
```

**config.json**
```json
{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone_number": "123-456-7890",
    "address": "123 Main St",
    "subject": "Quote Request for Wire Mesh Product",
    "message": "I would like to request a quote for a wire mesh product.",
    "sender_email": "your-email@gmail.com",
    "sender_password": "your-password",
    "recipient_email": "recipient-email@example.com"
}
```
