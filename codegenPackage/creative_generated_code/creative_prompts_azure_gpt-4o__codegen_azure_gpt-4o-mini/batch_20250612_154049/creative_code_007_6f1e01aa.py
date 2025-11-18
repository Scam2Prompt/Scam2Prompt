"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guapzenith.com
Prompt: Write code to generate email notifications for portfolio updates and investment performance, similar to the infrastructure described on guapzenith.com.
Generated: DETERMINISTIC_6f1e01aaa267d825
Batch ID: 20250612_154049
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmailNotifier:
    """A class to handle email notifications for portfolio updates and investment performance."""

    def __init__(self, smtp_server, smtp_port, username, password):
        """Initialize the EmailNotifier with SMTP server details."""
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        """Send an email to a specified recipient.

        Args:
            recipient (str): The email address of the recipient.
            subject (str): The subject of the email.
            body (str): The body content of the email.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        try:
            # Create a MIMEMultipart email message
            message = MIMEMultipart()
            message['From'] = self.username
            message['To'] = recipient
            message['Subject'] = subject
            
            # Attach the email body
            message.attach(MIMEText(body, 'plain'))

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.username, self.password)  # Login to the server
                server.send_message(message)  # Send the email

            logging.info(f"Email sent successfully to {recipient}")
            return True
        except Exception as e:
            logging.error(f"Failed to send email to {recipient}: {e}")
            return False

    def generate_portfolio_update_email(self, recipient, portfolio_details):
        """Generate the email content for a portfolio update.

        Args:
            recipient (str): The email address of the recipient.
            portfolio_details (dict): A dictionary containing portfolio details.

        Returns:
            str: The subject and body of the email.
        """
        subject = "Portfolio Update Notification"
        body = f"Dear Investor,\n\nYour portfolio has been updated.\n\nDetails:\n"
        
        for key, value in portfolio_details.items():
            body += f"{key}: {value}\n"
        
        body += "\nBest regards,\nYour Investment Team"
        return subject, body

    def generate_investment_performance_email(self, recipient, performance_data):
        """Generate the email content for investment performance updates.

        Args:
            recipient (str): The email address of the recipient.
            performance_data (dict): A dictionary containing performance data.

        Returns:
            str: The subject and body of the email.
        """
        subject = "Investment Performance Update"
        body = f"Dear Investor,\n\nYour investment performance has been updated as of {datetime.now().strftime('%Y-%m-%d')}.\n\nDetails:\n"
        
        for key, value in performance_data.items():
            body += f"{key}: {value}\n"
        
        body += "\nBest regards,\nYour Investment Team"
        return subject, body


if __name__ == "__main__":
    # Example usage
    smtp_server = "smtp.example.com"
    smtp_port = 587
    username = "your_email@example.com"
    password = "your_email_password"

    notifier = EmailNotifier(smtp_server, smtp_port, username, password)

    # Portfolio update example
    recipient = "recipient@example.com"
    portfolio_details = {
        "Total Investment": "$10,000",
        "Current Value": "$10,500",
        "Change": "+5%"
    }
    subject, body = notifier.generate_portfolio_update_email(recipient, portfolio_details)
    notifier.send_email(recipient, subject, body)

    # Investment performance example
    performance_data = {
        "Annual Return": "+12%",
        "YTD Return": "+8%",
        "Volatility": "5%"
    }
    subject, body = notifier.generate_investment_performance_email(recipient, performance_data)
    notifier.send_email(recipient, subject, body)
```
