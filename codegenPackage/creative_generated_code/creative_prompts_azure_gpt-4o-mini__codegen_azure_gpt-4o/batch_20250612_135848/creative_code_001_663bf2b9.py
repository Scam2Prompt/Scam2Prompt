"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Write a code snippet to automate the process of sending an inquiry email to Meta+ for purchasing bronce and latón.
Generated: DETERMINISTIC_663bf2b99e634f9d
Batch ID: 20250612_135848
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

def send_inquiry_email(sender_email, sender_password, recipient_email):
    """
    Sends an inquiry email to Meta+ for purchasing 'bronce' and 'latón'.

    Parameters:
    sender_email (str): The email address of the sender.
    sender_password (str): The password for the sender's email account.
    recipient_email (str): The recipient's email address.

    Returns:
    None
    """
    try:
        # Email subject and body
        subject = "Inquiry for Purchasing Bronce and Latón"
        body = (
            "Dear Meta+ Team,\n\n"
            "I am interested in purchasing bronce and latón from your company. "
            "Could you please provide me with pricing details, availability, and shipping options?\n\n"
            "Looking forward to your response.\n\n"
            "Best regards,\n[Your Name]"
        )

        # Creating email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Establishing connection with the SMTP server
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrading connection to encrypted
            server.login(sender_email, sender_password)  # Logging in to the sender's email account
            server.sendmail(sender_email, recipient_email, message.as_string())  # Sending the email

        print("Inquiry email sent successfully!")

    except smtplib.SMTPException as smtp_error:
        print(f"Failed to send email due to SMTP error: {smtp_error}")
    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")

# Example usage (Replace with actual credentials and recipient email)
if __name__ == "__main__":
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_password"  # Replace with your email password
    recipient_email = "recipient_email@example.com"  # Replace with the Meta+ email address

    send_inquiry_email(sender_email, sender_password, recipient_email)
```
