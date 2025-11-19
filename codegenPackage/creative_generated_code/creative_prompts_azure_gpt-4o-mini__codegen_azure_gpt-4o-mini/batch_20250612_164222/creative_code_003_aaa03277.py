"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gifts.sparklingz.nl
Prompt: Create a sample code snippet for sending a contact message to the Sparklingz customer service email.
Generated: DETERMINISTIC_aaa032776152e20e
Batch ID: 20250612_164222
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

def send_contact_message(name, email, message):
    """
    Sends a contact message to the Sparklingz customer service email.

    Args:
        name (str): The name of the sender.
        email (str): The email address of the sender.
        message (str): The contact message to be sent.

    Raises:
        ValueError: If any of the input fields are empty.
        Exception: If there is an error in sending the email.
    """
    # Validate input
    if not name or not email or not message:
        raise ValueError("All fields are required: name, email, and message.")

    # Email configuration
    sender_email = "your_email@example.com"
    recipient_email = "customerservice@sparklingz.com"
    subject = "Contact Message from {}".format(name)

    # Create the email content
    email_body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'plain'))

    try:
        # Set up the server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade to a secure connection
            server.login(sender_email, 'your_password')  # Login to your email account
            server.send_message(msg)  # Send the email

        print("Message sent successfully.")

    except smtplib.SMTPException as e:
        # Handle SMTP exceptions
        print("Failed to send email:", e)
        raise

# Example usage
if __name__ == "__main__":
    try:
        send_contact_message("John Doe", "john.doe@example.com", "I have a question about your services.")
    except ValueError as ve:
        print("Input error:", ve)
    except Exception as e:
        print("An error occurred:", e)
```
