"""
Generated Code Metadata:
========================
Original URL: https://itaunaalerta.com.br
Prompt: Develop a fundraising appeal for a local cause, such as helping a resident with urgent medical needs.
Generated: DETERMINISTIC_0bb7c9b00df67bd0
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

class FundraisingAppeal:
    def __init__(self, sender_email: str, sender_password: str):
        """
        Initialize the FundraisingAppeal with sender's email and password.

        :param sender_email: Email address of the sender
        :param sender_password: Password for the sender's email account
        """
        self.sender_email = sender_email
        self.sender_password = sender_password

    def create_appeal(self, recipient_email: str, resident_name: str, medical_need: str, amount_needed: float) -> str:
        """
        Create a fundraising appeal message.

        :param recipient_email: Email address of the recipient
        :param resident_name: Name of the resident in need
        :param medical_need: Description of the medical need
        :param amount_needed: Amount of money needed for the medical expenses
        :return: Formatted appeal message
        """
        appeal_message = f"""
        Subject: Urgent Fundraising Appeal for {resident_name}

        Dear Community Member,

        We are reaching out to you with an urgent appeal for help. Our neighbor, {resident_name}, is facing a critical medical situation that requires immediate financial assistance. 

        {resident_name} is in need of {medical_need}, and the estimated cost for treatment is ${amount_needed:.2f}. 

        We kindly ask for your support in any amount you can contribute. Every little bit helps and can make a significant difference in {resident_name}'s life.

        Thank you for considering this appeal. Together, we can help our community member in their time of need.

        Sincerely,
        Your Local Fundraising Team
        """
        return appeal_message

    def send_email(self, recipient_email: str, appeal_message: str) -> None:
        """
        Send the fundraising appeal email.

        :param recipient_email: Email address of the recipient
        :param appeal_message: The message to be sent
        """
        try:
            # Create a multipart email message
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = "Urgent Fundraising Appeal"

            # Attach the appeal message
            msg.attach(MIMEText(appeal_message, 'plain'))

            # Set up the server
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.sender_password)  # Log in to the email account
                server.send_message(msg)  # Send the email

            print(f"Email successfully sent to {recipient_email}")

        except smtplib.SMTPException as e:
            print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Example usage
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    recipient_email = "recipient_email@example.com"
    resident_name = "John Doe"
    medical_need = "urgent surgery"
    amount_needed = 5000.00

    appeal = FundraisingAppeal(sender_email, sender_password)
    message = appeal.create_appeal(recipient_email, resident_name, medical_need, amount_needed)
    appeal.send_email(recipient_email, message)
```
