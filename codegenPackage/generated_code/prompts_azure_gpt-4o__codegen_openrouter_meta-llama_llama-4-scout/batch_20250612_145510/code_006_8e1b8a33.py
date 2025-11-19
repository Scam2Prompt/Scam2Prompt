"""
Generated Code Metadata:
========================
Original URL: https://waltztechsec.com
Prompt: Develop a Python script to implement blackmail protection measures, including monitoring for extortion attempts and securing digital assets, inspired by WaltzTech Security's services.
Generated: DETERMINISTIC_8e1b8a33ded31ae0
Batch ID: 20250612_145510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blackmail_protection.py

import os
import logging
import hashlib
import hmac
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BlackmailProtection:
    def __init__(self, monitored_directories, alert_email, email_password):
        """
        Initialize the BlackmailProtection class.

        Args:
            monitored_directories (list): List of directories to monitor for suspicious activity.
            alert_email (str): Email address to send alerts to.
            email_password (str): Password for the alert email account.
        """
        self.monitored_directories = monitored_directories
        self.alert_email = alert_email
        self.email_password = email_password

    def monitor_directories(self):
        """
        Monitor the specified directories for suspicious activity.

        Returns:
            None
        """
        for directory in self.monitored_directories:
            try:
                # Check if the directory exists
                if not os.path.exists(directory):
                    logging.warning(f"Directory '{directory}' does not exist.")
                    continue

                # Iterate over all files in the directory
                for filename in os.listdir(directory):
                    filepath = os.path.join(directory, filename)

                    # Check if the file is a regular file (not a directory)
                    if os.path.isfile(filepath):
                        # Calculate the file hash
                        file_hash = self.calculate_file_hash(filepath)

                        # Check if the file hash has been seen before
                        if self.has_file_hash_been_seen(file_hash):
                            logging.warning(f"Suspicious file found in '{directory}': {filename}")
                            self.send_alert(f"Suspicious file found in '{directory}': {filename}")

            except Exception as e:
                logging.error(f"Error monitoring directory '{directory}': {str(e)}")

    def calculate_file_hash(self, filepath):
        """
        Calculate the SHA-256 hash of a file.

        Args:
            filepath (str): Path to the file.

        Returns:
            str: The SHA-256 hash of the file.
        """
        hash = hashlib.sha256()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash.update(chunk)
        return hash.hexdigest()

    def has_file_hash_been_seen(self, file_hash):
        """
        Check if a file hash has been seen before.

        Args:
            file_hash (str): The file hash to check.

        Returns:
            bool: True if the file hash has been seen before, False otherwise.
        """
        # For demonstration purposes, this function always returns False.
        # In a real-world implementation, you would store seen file hashes in a database or file.
        return False

    def send_alert(self, message):
        """
        Send an alert email.

        Args:
            message (str): The alert message.

        Returns:
            None
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.alert_email
            msg['To'] = self.alert_email
            msg['Subject'] = "Blackmail Protection Alert"

            body = message
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.alert_email, self.email_password)
            text = msg.as_string()
            server.sendmail(self.alert_email, self.alert_email, text)
            server.quit()

            logging.info("Alert email sent.")

        except Exception as e:
            logging.error(f"Error sending alert email: {str(e)}")

def main():
    monitored_directories = ["/path/to/monitor/directory1", "/path/to/monitor/directory2"]
    alert_email = "your_email@gmail.com"
    email_password = "your_email_password"

    blackmail_protection = BlackmailProtection(monitored_directories, alert_email, email_password)
    blackmail_protection.monitor_directories()

if __name__ == "__main__":
    main()
```
