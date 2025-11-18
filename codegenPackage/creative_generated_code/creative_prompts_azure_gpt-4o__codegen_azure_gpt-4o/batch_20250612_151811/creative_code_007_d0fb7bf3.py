"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lioncash.top
Prompt: Write code to implement a notification system that alerts users about loan status updates and repayment reminders, inspired by Lion Cash's user-friendly app.
Generated: DETERMINISTIC_d0fb7bf351b34c07
Batch ID: 20250612_151811
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
import datetime

class NotificationSystem:
    """
    A notification system to alert users about loan status updates and repayment reminders.
    """

    def __init__(self, smtp_server, smtp_port, email_user, email_password):
        """
        Initialize the notification system.

        Args:
            smtp_server (str): The SMTP server address.
            smtp_port (int): The SMTP server port.
            email_user (str): The sender's email address.
            email_password (str): The sender's email password.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.email_password = email_password

    def send_email(self, recipient_email, subject, message):
        """
        Send an email notification.

        Args:
            recipient_email (str): The recipient's email address.
            subject (str): The subject of the email.
            message (str): The body of the email.
        """
        try:
            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = self.email_user
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.email_user, self.email_password)  # Authenticate
                server.sendmail(self.email_user, recipient_email, msg.as_string())  # Send the email

        except Exception as e:
            print(f"Error sending email to {recipient_email}: {e}")
            return False

        return True

    def send_loan_status_update(self, recipient_email, loan_status):
        """
        Send a loan status update notification.

        Args:
            recipient_email (str): The recipient's email address.
            loan_status (str): The status of the loan.
        """
        subject = "Loan Status Update"
        message = f"Dear user,\n\nYour loan status has been updated to: {loan_status}.\n\nThank you,\nLoan Notification System"
        return self.send_email(recipient_email, subject, message)

    def send_repayment_reminder(self, recipient_email, repayment_date, amount_due):
        """
        Send a repayment reminder notification.

        Args:
            recipient_email (str): The recipient's email address.
            repayment_date (datetime.date): The repayment due date.
            amount_due (float): The amount due for repayment.
        """
        subject = "Repayment Reminder"
        message = (
            f"Dear user,\n\nThis is a reminder that your loan repayment of ${amount_due:.2f} is due on {repayment_date.strftime('%Y-%m-%d')}."
            "\n\nPlease ensure timely repayment to avoid penalties.\n\nThank you,\nLoan Notification System"
        )
        return self.send_email(recipient_email, subject, message)

# Example usage:
if __name__ == "__main__":
    # Configuration for the email server
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    EMAIL_USER = "your_email@example.com"
    EMAIL_PASSWORD = "your_password"

    # Initialize the notification system
    notification_system = NotificationSystem(SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASSWORD)

    # Send example notifications
    recipient = "user_email@example.com"
    loan_status = "Approved"
    repayment_date = datetime.date(2023, 11, 15)
    amount_due = 500.75

    # Loan status update
    if notification_system.send_loan_status_update(recipient, loan_status):
        print("Loan status update sent successfully!")

    # Repayment reminder
    if notification_system.send_repayment_reminder(recipient, repayment_date, amount_due):
        print("Repayment reminder sent successfully!")
```
