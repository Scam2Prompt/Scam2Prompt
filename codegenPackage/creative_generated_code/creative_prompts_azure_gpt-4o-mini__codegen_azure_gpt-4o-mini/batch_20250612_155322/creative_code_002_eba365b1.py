"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Generate a code snippet that sends an email notification to clients when their PPI claim status changes, inspired by the customer service practices of Financial Recovery Solutions Ltd.
Generated: DETERMINISTIC_eba365b105825f19
Batch ID: 20250612_155322
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
from typing import List, Dict, Any

class EmailNotificationService:
    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str) -> None:
        """
        Initialize the EmailNotificationService with SMTP server credentials.
        
        :param smtp_server: SMTP server address
        :param smtp_port: SMTP server port
        :param username: Email account username
        :param password: Email account password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipients: List[str], subject: str, body: str) -> None:
        """
        Send an email to the specified recipients.
        
        :param recipients: List of email addresses to send the notification to
        :param subject: Subject of the email
        :param body: Body content of the email
        """
        # Create a multipart email message
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Establish a secure session with the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.username, self.password)  # Log in to the email account
                server.send_message(msg)  # Send the email
            print("Email sent successfully.")
        except smtplib.SMTPException as e:
            # Handle SMTP exceptions
            print(f"Failed to send email: {e}")

def notify_clients_about_claim_status(claims: List[Dict[str, Any]], email_service: EmailNotificationService) -> None:
    """
    Notify clients about the status change of their PPI claims.
    
    :param claims: List of claims with client email and new status
    :param email_service: Instance of EmailNotificationService to send emails
    """
    for claim in claims:
        client_email = claim.get('email')
        new_status = claim.get('status')
        
        if client_email and new_status:
            subject = "Update on Your PPI Claim Status"
            body = f"Dear Client,\n\nYour PPI claim status has changed to: {new_status}.\n\nBest regards,\nFinancial Recovery Solutions Ltd."
            email_service.send_email([client_email], subject, body)
        else:
            print(f"Missing email or status for claim: {claim}")

# Example usage
if __name__ == "__main__":
    smtp_info = {
        'smtp_server': 'smtp.example.com',
        'smtp_port': 587,
        'username': 'your_email@example.com',
        'password': 'your_password'
    }

    email_service = EmailNotificationService(**smtp_info)

    # Example claims data
    claims_data = [
        {'email': 'client1@example.com', 'status': 'Approved'},
        {'email': 'client2@example.com', 'status': 'Rejected'},
        {'email': 'client3@example.com', 'status': 'In Review'}
    ]

    notify_clients_about_claim_status(claims_data, email_service)
```
