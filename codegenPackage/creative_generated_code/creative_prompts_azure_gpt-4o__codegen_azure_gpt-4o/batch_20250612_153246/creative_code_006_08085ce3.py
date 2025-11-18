"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supplymarinebr.com.br
Prompt: Recommend Python libraries for handling customer data and communication, specifically for maritime supply companies like Supply Marine that offer direct WhatsApp and email contact options.
Generated: DETERMINISTIC_08085ce338a7bc9d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script recommends Python libraries for handling customer data and communication 
for maritime supply companies like Supply Marine. It includes options for WhatsApp and 
email communication, demonstrating basic usage for each library.
"""

# Import required libraries
import smtplib  # For sending emails
from email.mime.text import MIMEText  # For constructing email messages
from email.mime.multipart import MIMEMultipart  # For handling attachments
from twilio.rest import Client  # For WhatsApp communication via Twilio
import sqlite3  # For storing customer data in a local database (SQL)

# Database setup function for customer information
def setup_database(database_path="customer_data.db"):
    """
    Sets up a SQLite database to store customer information.
    :param database_path: Path to the database file
    """
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                whatsapp_number TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
        print("Database setup complete.")
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")


# Function to send an email
def send_email(sender_email, sender_password, recipient_email, subject, message):
    """
    Sends an email using the SMTP protocol.
    :param sender_email: The sender's email address
    :param sender_password: The sender's email password
    :param recipient_email: The recipient's email address
    :param subject: The subject of the email
    :param message: The email message content
    """
    try:
        # Construct email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to SMTP server and send message
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail's SMTP server
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")


# Function to send WhatsApp message
def send_whatsapp(account_sid, auth_token, whatsapp_number, recipient_number, message):
    """
    Sends a WhatsApp message using Twilio's API.
    :param account_sid: Twilio account SID
    :param auth_token: Twilio authentication token
    :param whatsapp_number: The sender's Twilio WhatsApp-enabled number
    :param recipient_number: The recipient's WhatsApp number
    :param message: The WhatsApp message content
    """
    try:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=message,
            from_=f'whatsapp:{whatsapp_number}',
            to=f'whatsapp:{recipient_number}'
        )
        print("WhatsApp message sent successfully. Message SID:", message.sid)
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")


# Example usage
if __name__ == "__main__":
    # Setup database for customer information
    setup_database()

    # Sample email sending
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    recipient_email = "customer@example.com"
    subject = "Order Confirmation"
    message = "Thank you for your order with Supply Marine. Your order has been confirmed."
    send_email(sender_email, sender_password, recipient_email, subject, message)

    # Sample WhatsApp message sending
    account_sid = "your_twilio_account_sid"
    auth_token = "your_twilio_auth_token"
    whatsapp_number = "+14155238886"  # Twilio's WhatsApp sandbox number
    recipient_number = "+1234567890"  # Customer's WhatsApp number
    message = "Thank you for choosing Supply Marine! Please let us know if you have any questions."
    send_whatsapp(account_sid, auth_token, whatsapp_number, recipient_number, message)
```
