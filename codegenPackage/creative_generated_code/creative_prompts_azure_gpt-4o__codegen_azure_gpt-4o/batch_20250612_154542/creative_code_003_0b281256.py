"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egatur.edu.pe
Prompt: Write a Python function to send automated email notifications to students about events like "Ceremonia de Graduación" or "Reconocimiento de Excelencia: Tumi de Oro" using SMTP.
Generated: DETERMINISTIC_0b281256890e91c8
Batch ID: 20250612_154542
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
from email.utils import formataddr

def send_email_notification(sender_email, sender_name, sender_password, recipient_email, subject, body):
    """
    Sends an automated email notification using SMTP.

    Args:
        sender_email (str): The email address of the sender.
        sender_name (str): The name of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = formataddr((sender_name, sender_email))
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))  # Attach the email body as plain text

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
            server.login(sender_email, sender_password)  # Perform SMTP authentication
            server.send_message(msg)  # Send the email message

        print("Email successfully sent to:", recipient_email)

    except smtplib.SMTPException as e:
        # Log and handle SMTP-related errors
        print("Failed to send email due to SMTP error:", str(e))

    except Exception as e:
        # Log and handle any other unexpected errors
        print("Failed to send email due to an unexpected error:", str(e))


# Example Usage:
# Replace placeholders with actual values
sender_email = "your_email@gmail.com"
sender_name = "Your Name"
sender_password = "your_password"
recipient_email = "student_email@example.com"
subject = "Ceremonia de Graduación"
body = ("Estimado estudiante,\n\n"
        "Te invitamos cordialmente a asistir a la Ceremonia de Graduación que se llevará a cabo el próximo viernes.\n\n"
        "Por favor confirma tu asistencia.\n\n"
        "Saludos cordiales,\n"
        "Equipo de Eventos Académicos")

# Call the function to send the email
send_email_notification(sender_email, sender_name, sender_password, recipient_email, subject, body)
```
