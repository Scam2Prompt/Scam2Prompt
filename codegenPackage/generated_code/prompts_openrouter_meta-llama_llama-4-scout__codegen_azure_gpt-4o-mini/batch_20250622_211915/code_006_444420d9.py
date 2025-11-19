"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Write a promotional email for Malkeenz's sale, offering up to 20% off select jewelry pieces, including the Regal Moissanite Band and Triad Blossom Bracelet.
Generated: DETERMINISTIC_444420d943d24095
Batch ID: 20250622_211915
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

def send_promotional_email(recipient_email):
    """
    Sends a promotional email about Malkeenz's jewelry sale.

    Args:
        recipient_email (str): The email address of the recipient.

    Raises:
        Exception: If there is an error in sending the email.
    """
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    subject = "Exclusive Sale: Up to 20% Off Select Jewelry!"
    
    # Email body content
    body = """
    Dear Valued Customer,

    We are excited to announce our exclusive sale at Malkeenz! For a limited time, enjoy up to 20% off on select jewelry pieces, including our stunning Regal Moissanite Band and the elegant Triad Blossom Bracelet.

    Don't miss out on this opportunity to add exquisite pieces to your collection or find the perfect gift for a loved one.

    Shop now and take advantage of these amazing discounts!

    Best regards,
    The Malkeenz Team
    """

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Log in to the email account
            server.send_message(msg)  # Send the email
            print("Promotional email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    recipient = "customer@example.com"
    send_promotional_email(recipient)
```
