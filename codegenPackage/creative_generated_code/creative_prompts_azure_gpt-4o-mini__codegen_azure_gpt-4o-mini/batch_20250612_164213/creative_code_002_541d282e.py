"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacerealestatevt.com
Prompt: Create a code snippet that sends an email inquiry to Danica Rolfe at Pace Real Estate, including fields for the user's name and property interests.
Generated: DETERMINISTIC_541d282e5a21d711
Batch ID: 20250612_164213
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

# Function to send an email inquiry
def send_email_inquiry(user_name, property_interest, sender_email, sender_password):
    """
    Sends an email inquiry to Danica Rolfe at Pace Real Estate.

    Args:
        user_name (str): The name of the user sending the inquiry.
        property_interest (str): The user's property interests.
        sender_email (str): The email address of the sender.
        sender_password (str): The sender's email account password.
    """
    try:
        # Email configuration
        recipient_email = "danica.rolfe@pacerealestate.com"
        subject = "Property Inquiry"
        body = f"Hello Danica,\n\nMy name is {user_name}.\nI am interested in the following properties: {property_interest}.\n\nThank you!"

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body to the email
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS
            server.login(sender_email, sender_password)  # Login to the email account
            server.send_message(msg)  # Send the email

        print("Email sent successfully!")

    except smtplib.SMTPException as e:
        # Handle SMTP exceptions
        print(f"Error occurred while sending email: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")

# Sample usage (uncomment and replace with actual credentials to use)
# send_email_inquiry("John Doe", "3-bedroom house in downtown", "your_email@gmail.com", "your_password")
```
