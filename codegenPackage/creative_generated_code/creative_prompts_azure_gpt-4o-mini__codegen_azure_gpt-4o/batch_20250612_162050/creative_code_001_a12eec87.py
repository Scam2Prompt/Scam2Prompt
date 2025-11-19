"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vanaclochayasociados.com
Prompt: Write a Python script that sends an email to a law firm, requesting information about their services in family law and administrative issues.
Generated: DETERMINISTIC_a12eec87be522639
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

def send_email(sender_email, sender_password, recipient_email):
    """
    Sends an email to a law firm requesting information about family law
    and administrative services.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.
        recipient_email (str): The recipient's email address (law firm's email).
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = "Request for Information: Family Law & Administrative Services"

        # Email body content
        body = (
            "Dear [Law Firm Name],\n\n"
            "I hope this message finds you well. I am writing to inquire about your services "
            "related to family law and administrative issues. I would greatly appreciate it "
            "if you could provide information regarding your expertise in these areas, as well "
            "as the process for engaging your firm.\n\n"
            "Please let me know if there are any forms, documents, or initial consultations required.\n\n"
            "Thank you for your time and assistance. I look forward to hearing from you.\n\n"
            "Best regards,\n\n"
            "[Your Name]"
        )

        # Attach the email body to the message
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        smtp_server = 'smtp.gmail.com'  # For Gmail; update for other providers
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection

        # Log in to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)
        print("Email sent successfully!")

        # Close the SMTP connection
        server.quit()

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage: Replace with actual sender and recipient details
    sender_email = "your_email@example.com"
    sender_password = "your_password"  # Use environment variables for sensitive data in production
    recipient_email = "law_firm_email@example.com"

    send_email(sender_email, sender_password, recipient_email)
```
