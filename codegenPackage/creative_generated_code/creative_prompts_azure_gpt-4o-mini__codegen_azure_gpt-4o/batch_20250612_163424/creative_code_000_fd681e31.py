"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://salesstudios.com
Prompt: How can I automate my email marketing strategy to increase engagement and open rates, similar to the methods used by Sales Studios?
Generated: DETERMINISTIC_fd681e3104ce0bdd
Batch ID: 20250612_163424
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
import csv
import schedule
import time

class EmailMarketingAutomation:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        """
        Initialize the email marketing automation class.
        :param smtp_server: SMTP server address (e.g., smtp.gmail.com)
        :param smtp_port: SMTP server port (e.g., 587)
        :param sender_email: Sender email address
        :param sender_password: Sender email password
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, recipient_email, subject, body):
        """
        Sends an email to the specified recipient.
        :param recipient_email: The recipient's email address
        :param subject: The subject of the email
        :param body: The body content of the email
        """
        try:
            # Create a MIME text object for the email
            msg = MIMEMultipart()
            msg['From'] = self.sender_email
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))
            
            # Connect to the SMTP server and send the email
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Secure the connection
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipient_email, msg.as_string())
                print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"Error sending email to {recipient_email}: {e}")

    def read_recipients_from_csv(self, csv_file):
        """
        Reads email recipients from a CSV file.
        :param csv_file: Path to the CSV file containing email addresses
        :return: List of email addresses
        """
        recipients = []
        try:
            with open(csv_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    if len(row) > 0:
                        recipients.append(row[0])
            return recipients
        except Exception as e:
            print(f"Error reading CSV file {csv_file}: {e}")
            return []

    def schedule_email_campaign(self, csv_file, subject, body, interval_minutes):
        """
        Schedules an email campaign.
        :param csv_file: Path to the CSV file with recipient email addresses
        :param subject: Email subject
        :param body: Email body
        :param interval_minutes: Time interval between each batch of emails
        """
        recipients = self.read_recipients_from_csv(csv_file)
        if not recipients:
            print("No recipients loaded. Email campaign aborted.")
            return

        def job():
            """
            Job to send emails to recipients.
            """
            for recipient in recipients:
                self.send_email(recipient, subject, body)
        
        # Schedule the email campaign
        schedule.every(interval_minutes).minutes.do(job)
        print(f"Email campaign scheduled every {interval_minutes} minutes.")
        
        # Keep the script running to execute scheduled tasks
        while True:
            schedule.run_pending()
            time.sleep(1)

# Example usage:
if __name__ == "__main__":
    # Replace with real SMTP server details and sender credentials
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    
    email_automation = EmailMarketingAutomation(smtp_server, smtp_port, sender_email, sender_password)
    
    # Replace with your CSV file path
    csv_file = "recipients.csv"
    subject = "Exciting Offer Just for You!"
    body = "Hello, we have an exciting offer just for you. Click here to learn more!"
    interval_minutes = 60  # Send emails every 60 minutes
    
    # Start the email campaign
    email_automation.schedule_email_campaign(csv_file, subject, body, interval_minutes)
```

This Python code automates email marketing by reading recipient email addresses from a CSV file and scheduling email campaigns. Make sure to replace the placeholder values (e.g., `your_email@gmail.com`, `your_password`, `recipients.csv`) with real data before running it in production.
