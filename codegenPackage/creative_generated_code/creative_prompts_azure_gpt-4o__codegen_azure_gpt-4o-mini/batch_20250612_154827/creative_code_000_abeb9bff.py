"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Write Python code to automate the process of submitting insurance policy change requests via email, using the format described on the Aibao Insurance website.
Generated: DETERMINISTIC_abeb9bff04835cc1
Batch ID: 20250612_154827
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
from typing import List
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InsurancePolicyChangeRequest:
    """
    A class to represent an insurance policy change request.
    """

    def __init__(self, policy_number: str, customer_name: str, change_details: str, 
                 recipient_email: str, sender_email: str, smtp_server: str, smtp_port: int, email_password: str):
        self.policy_number = policy_number
        self.customer_name = customer_name
        self.change_details = change_details
        self.recipient_email = recipient_email
        self.sender_email = sender_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_password = email_password

    def create_email_message(self) -> MIMEMultipart:
        """
        Creates the email message for the policy change request.
        
        Returns:
            MIMEMultipart: The email message ready to be sent.
        """
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.recipient_email
        message['Subject'] = 'Insurance Policy Change Request'
        
        # Email body
        body = f"""
        Dear Aibao Insurance Team,

        I would like to request a change to my insurance policy.

        Policy Number: {self.policy_number}
        Customer Name: {self.customer_name}
        Change Details: {self.change_details}

        Thank you for your attention to this matter.

        Best regards,
        {self.customer_name}
        """
        message.attach(MIMEText(body, 'plain'))
        return message

    def send_email(self):
        """
        Sends the email containing the policy change request.
        """
        try:
            # Create email message
            message = self.create_email_message()

            # Connect to the SMTP server and send email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade to secure connection
                server.login(self.sender_email, self.email_password)  # Log in to the server
                server.send_message(message)  # Send the email

            logging.info('Email sent successfully to %s', self.recipient_email)

        except smtplib.SMTPException as e:
            logging.error('Failed to send email: %s', e)
        except Exception as e:
            logging.error('An unexpected error occurred: %s', e)

def main():
    """
    Main function to execute the policy change request submission.
    """
    # Example data (replace with actual values)
    POLICY_NUMBER = '123456789'
    CUSTOMER_NAME = 'John Doe'
    CHANGE_DETAILS = 'Change of address to 123 New St, New City, NY'
    RECIPIENT_EMAIL = 'support@aibaoinusurance.com'  # Replace with required recipient
    SENDER_EMAIL = 'your_email@example.com'  # Replace with your email
    SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
    SMTP_PORT = 587  # Common port for SMTP
    EMAIL_PASSWORD = 'your_password'  # Replace with your email password

    # Create an instance of the request
    request = InsurancePolicyChangeRequest(POLICY_NUMBER, CUSTOMER_NAME, CHANGE_DETAILS,
                                           RECIPIENT_EMAIL, SENDER_EMAIL, SMTP_SERVER,
                                           SMTP_PORT, EMAIL_PASSWORD)
    
    # Send the email
    request.send_email()

if __name__ == "__main__":
    main()
```
