"""
Generated Code Metadata:
========================
Original URL: https://sale-azuki.com
Prompt: Create a script that sends a promotional email for the CHIKARA cooling shirt, highlighting its features and the limited-time offer.
Generated: DETERMINISTIC_b16f83c1a8f89501
Batch ID: 20250612_155200
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

def send_promotional_email(
    sender_email: str, 
    sender_password: str, 
    recipient_email: str, 
    subject: str = "Limited Time Offer: CHIKARA Cooling Shirt"
):
    """
    Sends a promotional email for the CHIKARA cooling shirt.

    Args:
    - sender_email (str): The email address of the sender.
    - sender_password (str): The password of the sender's email account.
    - recipient_email (str): The email address of the recipient.
    - subject (str): The subject of the email. Defaults to "Limited Time Offer: CHIKARA Cooling Shirt".
    """

    # Define the email content
    email_content = """
    Dear Valued Customer,

    We are excited to introduce the CHIKARA cooling shirt, designed to keep you cool and comfortable all day long.

    Features:
    - Moisture-wicking fabric for dry comfort
    - Breathable mesh panels for enhanced ventilation
    - UPF 30+ protection against the sun's UV rays
    - Limited-time offer: 20% off your first purchase

    Don't miss out on this amazing opportunity to upgrade your wardrobe. Order now and stay cool in style!

    Best regards,
    [Your Name]
    """

    try:
        # Create a message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the email content
        message.attach(MIMEText(email_content, 'plain'))

        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication error. Check your email and password.")
    except smtplib.SMTPException as e:
        print(f"Error sending email: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    sender_email = "your-email@gmail.com"
    sender_password = "your-email-password"
    recipient_email = "recipient-email@example.com"

    send_promotional_email(sender_email, sender_password, recipient_email)
```
