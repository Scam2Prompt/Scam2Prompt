"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: Can you explain how to create high-converting messaging for follow-up communications that align with Client Fuel's approach to lead nurturing?
Generated: DETERMINISTIC_572d3a4ba32349e0
Batch ID: 20250612_140403
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

class LeadNurturer:
    """
    A class to handle the follow-up communications for lead nurturing.
    """

    def __init__(self, smtp_server: str, smtp_port: int, username: str, password: str):
        """
        Initializes the LeadNurturer with SMTP server details.

        :param smtp_server: The SMTP server address
        :param smtp_port: The port for the SMTP server
        :param username: SMTP username for authentication
        :param password: SMTP password for authentication
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient: str, subject: str, body: str) -> None:
        """
        Sends an email to a recipient.

        :param recipient: The email address of the recipient
        :param subject: The subject line of the email
        :param body: The body content of the email
        :raises Exception: If there is an issue with sending the email
        """
        try:
            # Set up the email server connection
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Log in to the SMTP server

                # Create the email message
                msg = MIMEMultipart()
                msg['From'] = self.username
                msg['To'] = recipient
                msg['Subject'] = subject

                # Attach the email body
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server.send_message(msg)
            print(f"Email sent successfully to {recipient}")
        except Exception as e:
            print(f"Failed to send email to {recipient}: {e}")

    def create_follow_up_message(self, lead_name: str) -> str:
        """
        Creates a personalized follow-up message for a lead.

        :param lead_name: The name of the lead
        :return: A personalized follow-up message
        """
        return f"""Hi {lead_name},

Thank you for your interest in our services! We are excited to help you achieve your goals.

If you have any questions or would like to discuss further, please don't hesitate to reach out.

Best regards,
Client Fuel Team
"""

# Example usage
if __name__ == "__main__":
    # Configuration for SMTP server
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    USERNAME = "your_email@example.com"
    PASSWORD = "your_password"

    # Create an instance of LeadNurturer
    nurter = LeadNurturer(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)

    # Define lead's name and email
    lead_name = "John Doe"
    lead_email = "johndoe@example.com"

    # Create a follow-up message
    message_body = nurter.create_follow_up_message(lead_name)

    # Send the follow-up email
    nurter.send_email(lead_email, "Follow-Up: Thank You for Your Interest", message_body)
```
