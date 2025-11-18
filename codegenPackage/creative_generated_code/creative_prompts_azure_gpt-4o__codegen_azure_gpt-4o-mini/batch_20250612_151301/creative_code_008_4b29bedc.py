"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write code to send automated email confirmations for pre-scheduled gastroenterology exams like pHmetria esofágica and teste de intolerância à frutose, using the clinic's contact details.
Generated: DETERMINISTIC_4b29bedce028795d
Batch ID: 20250612_151301
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
from typing import List, Dict


class EmailSender:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initialize the EmailSender with SMTP server details.

        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email username for authentication
        :param password: Email password for authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Send an email to the specified recipient.

        :param recipient: Email address of the recipient
        :param subject: Subject line of the email
        :param body: Body content of the email
        :raises Exception: If sending the email fails
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient
            msg['Subject'] = subject

            # Attach the email body
            msg.attach(MIMEText(body, 'plain'))

            # Establish connection to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Login to the SMTP server
                server.send_message(msg)  # Send the email

        except Exception as e:
            raise Exception(f"Failed to send email to {recipient}: {str(e)}")


def prepare_email_body(exam_details: Dict[str, str], clinic_info: Dict[str, str]) -> str:
    """
    Prepare the email body for the confirmation.

    :param exam_details: Details of the scheduled exam
    :param clinic_info: Contact details of the clinic
    :return: Formatted email body as a string
    """
    return (f"Dear Patient,\n\n"
            f"This is a confirmation for your scheduled gastroenterology examination:\n\n"
            f"Exam Type: {exam_details['exam_name']}\n"
            f"Date: {exam_details['date']}\n"
            f"Time: {exam_details['time']}\n\n"
            f"Please find our contact details below:\n"
            f"Clinic Name: {clinic_info['name']}\n"
            f"Phone: {clinic_info['phone']}\n"
            f"Email: {clinic_info['email']}\n\n"
            f"Thank you,\n"
            f"{clinic_info['name']}")


def main():
    # SMTP server configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    username = 'your_email@example.com'
    password = 'your_email_password'

    # EmailSender instance
    email_sender = EmailSender(smtp_server, smtp_port, username, password)

    # Exam and clinic details
    exam_details = {
        'exam_name': 'pHmetria esofágica',
        'date': '2023-10-15',
        'time': '10:00 AM'
    }
    
    clinic_info = {
        'name': 'Gastro Clinic',
        'phone': '(11) 1234-5678',
        'email': 'clinic_contact@example.com'
    }

    # Recipient email address
    recipient_email = 'patient_email@example.com'

    # Prepare email body
    email_body = prepare_email_body(exam_details, clinic_info)

    # Send the confirmation email
    try:
        email_sender.send_email(recipient_email, 'Appointment Confirmation', email_body)
        print("Confirmation email sent successfully.")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
```
