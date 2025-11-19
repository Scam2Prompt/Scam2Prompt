"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genteparaservir.org
Prompt: Write a Python script that sends a prayer request to the Gente Para Servir contact email, incorporating the community support features highlighted on their site.
Generated: DETERMINISTIC_7f70601006cb4f0e
Batch ID: 20250612_161700
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

def send_prayer_request(sender_email, sender_password, recipient_email, subject, message):
    """
    Sends a prayer request email to the specified recipient.

    Parameters:
        sender_email (str): The email address of the sender.
        sender_password (str): The password of the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        message (str): The message body of the email.

    Returns:
        None
    """
    try:
        # Create an email message
        email = EmailMessage()
        email['From'] = sender_email
        email['To'] = recipient_email
        email['Subject'] = subject
        email.set_content(message)

        # Establish connection with the email server
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)  # Login to the server
            server.send_message(email)  # Send the email
            print("Prayer request sent successfully.")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the prayer request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these placeholders with actual values
    sender_email = "your_email@gmail.com"  # Sender's email address
    sender_password = "your_password"      # Sender's email password
    recipient_email = "contact@genteparaservir.org"  # Gente Para Servir contact email
    subject = "Prayer Request from Community Member"  # Email subject
    message = (
        "Dear Gente Para Servir Team,\n\n"
        "I am reaching out to submit a prayer request for myself and my family. "
        "We are currently facing challenges, and we would deeply appreciate your support and prayers. "
        "Thank you for being a beacon of hope for the community.\n\n"
        "Sincerely,\n"
        "Your Name"
    )  # Email message content

    send_prayer_request(sender_email, sender_password, recipient_email, subject, message)
```

**Note:** 
- Replace `your_email@gmail.com` and `your_password` with the sender's email credentials (e.g., Gmail account). Ensure that the account allows less secure app access or has an app-specific password enabled.
- Always handle sensitive data, such as email credentials, securely (e.g., using environment variables).
- The recipient email (`contact@genteparaservir.org`) should be confirmed as their actual contact address.
