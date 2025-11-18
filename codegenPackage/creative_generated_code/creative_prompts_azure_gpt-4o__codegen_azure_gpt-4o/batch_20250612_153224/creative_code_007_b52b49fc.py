"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://schengenapostille.com
Prompt: Write a function to format and send email notifications to users about the status of their Apostille documents, referencing the communication methods used by Schengen Apostille.
Generated: DETERMINISTIC_b52b49fcd2f8f29e
Batch ID: 20250612_153224
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

def send_apostille_notification(email, document_status, user_name):
    """
    Sends an email notification to a user regarding the status of their Apostille documents.
    
    Args:
        email (str): The recipient's email address.
        document_status (str): The status of the Apostille document (e.g., "Processed", "Rejected").
        user_name (str): The name of the recipient.

    Returns:
        None

    Raises:
        Exception: If there is an issue sending the email.
    """
    # Email configuration (replace with actual values in production)
    SMTP_SERVER = "smtp.example.com"  # SMTP server address
    SMTP_PORT = 587                  # SMTP port (use 465 for SSL)
    SENDER_EMAIL = "no-reply@example.com"  # Sender email address
    SENDER_PASSWORD = "your_password"     # Sender email password

    try:
        # Create the email message
        subject = f"Apostille Document Status Update"
        body = f"""
        Dear {user_name},

        We are writing to inform you about the status of your Apostille documents.
        
        Current Status: {document_status}

        If you have any questions, please contact our support team.

        Best regards,
        Schengen Apostille Support Team
        """

        # Construct the email
        message = MIMEMultipart()
        message['From'] = SENDER_EMAIL
        message['To'] = email
        message['Subject'] = subject

        # Attach the body content to the email
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, email, message.as_string())

        print(f"Email successfully sent to {email}")

    except smtplib.SMTPException as e:
        # Handle SMTP errors
        print(f"Failed to send email: {str(e)}")
        raise

    except Exception as e:
        # Handle other unforeseen errors
        print(f"An error occurred: {str(e)}")
        raise

# Example usage
# Replace with actual values for testing
try:
    send_apostille_notification(
        email="user@example.com",
        document_status="Processed",
        user_name="John Doe"
    )
except Exception as e:
    print(f"Notification error: {str(e)}")
```
