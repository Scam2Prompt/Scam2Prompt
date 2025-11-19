"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: Create a Python script that sends an email inquiry about a property, using the contact details format seen on the 2ms.pt website.
Generated: DETERMINISTIC_b1d113d4707cc509
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_inquiry(property_name, property_address, inquiry_message, 
                        sender_name, sender_email, sender_phone, 
                        recipient_email, recipient_name, smtp_server, smtp_port, password):
    """
    Send an email inquiry about a property.

    Args:
        property_name (str): Name of the property.
        property_address (str): Address of the property.
        inquiry_message (str): Message of the inquiry.
        sender_name (str): Name of the sender.
        sender_email (str): Email of the sender.
        sender_phone (str): Phone number of the sender.
        recipient_email (str): Email of the recipient.
        recipient_name (str): Name of the recipient.
        smtp_server (str): SMTP server to use.
        smtp_port (int): Port of the SMTP server.
        password (str): Password of the sender's email account.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """

    # Create the message
    message = MIMEMultipart()
    message['From'] = f"{sender_name} <{sender_email}>"
    message['To'] = f"{recipient_name} <{recipient_email}>"
    message['Subject'] = f"Inquiry about {property_name}"

    # Format the message body
    body = f"""
    Name: {sender_name}\n
    Email: {sender_email}\n
    Phone: {sender_phone}\n\n
    Property: {property_name}\n
    Address: {property_address}\n\n
    Message: {inquiry_message}
    """

    # Attach the message body
    message.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        return True

    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Check your email and password.")
        return False

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
        return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    property_name = "Example Property"
    property_address = "Example Address"
    inquiry_message = "This is an example inquiry message."
    sender_name = "John Doe"
    sender_email = "john@example.com"
    sender_phone = "123456789"
    recipient_email = "recipient@example.com"
    recipient_name = "Recipient"
    smtp_server = "smtp.example.com"
    smtp_port = 587
    password = "password"

    success = send_email_inquiry(property_name, property_address, inquiry_message, 
                                  sender_name, sender_email, sender_phone, 
                                  recipient_email, recipient_name, smtp_server, smtp_port, password)

    if success:
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
```
