"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2ms.pt
Prompt: Create a Python script that sends an email inquiry about a property, using the contact details format seen on the 2ms.pt website.
Generated: DETERMINISTIC_b1d113d4707cc509
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage

def send_property_inquiry(sender_email, sender_password, recipient_email, subject, property_details, inquiry_message):
    """
    Sends an email inquiry about a property using SMTP.

    Args:
        sender_email (str): Email address of the sender.
        sender_password (str): Password for the sender's email account.
        recipient_email (str): Email address of the recipient (e.g., property contact).
        subject (str): Subject of the email.
        property_details (str): Details about the property being inquired about.
        inquiry_message (str): The body message of the inquiry.

    Returns:
        None
    """
    try:
        # Create the email message
        email = EmailMessage()
        email['From'] = sender_email
        email['To'] = recipient_email
        email['Subject'] = subject
        
        # Construct the email content
        email_content = f"""
        Dear Property Contact,

        I am interested in the property listed below:
        {property_details}

        {inquiry_message}

        Please let me know if the property is still available or provide further details. I look forward to your response.

        Best regards,
        [Your Name]
        """
        email.set_content(email_content)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, sender_password)
            smtp.send_message(email)
            print("Inquiry email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Example usage
    # Replace the following details with actual information
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    recipient_email = "recipient_email@example.com"
    subject = "Inquiry About a Property"
    property_details = "Property ID: 12345, Address: 2ms.pt property listing"
    inquiry_message = "I would like to know more details about the property, including its price and availability."

    # Send the inquiry email
    send_property_inquiry(sender_email, sender_password, recipient_email, subject, property_details, inquiry_message)
```
