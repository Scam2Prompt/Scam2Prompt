"""
Generated Code Metadata:
========================
Original URL: https://salesstudios.com
Prompt: Generate a sample email campaign that could help convert leads into loyal customers, based on the strategies outlined by Sales Studios.
Generated: DETERMINISTIC_c3ae9e0dfe4a90ed
Batch ID: 20250612_163424
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

class EmailCampaign:
    """
    A class to generate a sample email campaign to convert leads into loyal customers.
    """

    def __init__(self, sender_email, sender_password, recipient_emails):
        """
        Initialize the EmailCampaign class.

        Args:
            sender_email (str): The email address of the sender.
            sender_password (str): The password of the sender's email account.
            recipient_emails (list): A list of recipient email addresses.
        """
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_emails = recipient_emails

    def create_email_content(self, lead_name, product_name):
        """
        Create the content of the email.

        Args:
            lead_name (str): The name of the lead.
            product_name (str): The name of the product.

        Returns:
            str: The content of the email.
        """
        # Create a personalized email content
        email_content = f"""
        Subject: Exclusive Offer for {lead_name}

        Dear {lead_name},

        We hope this email finds you well. As a valued lead, we would like to offer you an exclusive deal on our best-selling product, {product_name}.

        For a limited time, you can get 20% off your first purchase. Don't miss out on this amazing opportunity to experience the benefits of our product.

        Click the link below to redeem your offer:
        [Insert link]

        Best regards,
        [Your Name]
        """
        return email_content

    def send_email(self, lead_name, product_name):
        """
        Send an email to a lead.

        Args:
            lead_name (str): The name of the lead.
            product_name (str): The name of the product.
        """
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = self.recipient_emails[0]
            msg['Subject'] = f"Exclusive Offer for {lead_name}"

            # Create the email content
            email_content = self.create_email_content(lead_name, product_name)

            # Attach the email content
            msg.attach(MIMEText(email_content, 'plain'))

            # Set up the SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.sender_email, self.sender_password)

            # Send the email
            text = msg.as_string()
            server.sendmail(self.sender_email, self.recipient_emails[0], text)
            server.quit()

            print(f"Email sent to {self.recipient_emails[0]} successfully.")

        except smtplib.SMTPAuthenticationError:
            print("Failed to send email: Authentication error.")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

def load_config(file_path):
    """
    Load configuration from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The configuration.
    """
    try:
        with open(file_path, 'r') as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        print("Configuration file not found.")
        return None
    except json.JSONDecodeError:
        print("Invalid configuration file.")
        return None

def main():
    # Load configuration
    config = load_config('config.json')

    if config:
        # Initialize the EmailCampaign class
        email_campaign = EmailCampaign(
            config['sender_email'],
            config['sender_password'],
            config['recipient_emails']
        )

        # Send emails to leads
        leads = config['leads']
        product_name = config['product_name']

        for lead in leads:
            email_campaign.send_email(lead['name'], product_name)

if __name__ == "__main__":
    main()
```

**config.json**
```json
{
    "sender_email": "your-email@gmail.com",
    "sender_password": "your-password",
    "recipient_emails": ["recipient-email@example.com"],
    "leads": [
        {
            "name": "John Doe"
        },
        {
            "name": "Jane Doe"
        }
    ],
    "product_name": "Example Product"
}
```
