"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Create a script that simulates the process of scanning a QR code on a lost object and sending a notification to the owner, following QRubi's workflow.
Generated: DETERMINISTIC_ff3414d37a588984
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QRCodeScanner:
    def __init__(self, owner_email):
        self.owner_email = owner_email

    def simulate_qr_scan(self, qr_data):
        """
        Simulates the action of scanning a QR code.
        :param qr_data: Data retrieved from the scanned QR code.
        """
        logging.info("QR code scanned with data: %s", qr_data)
        self.send_notification(qr_data)

    def send_notification(self, qr_data):
        """
        Sends a notification email to the owner of the lost object.
        :param qr_data: Data retrieved from the scanned QR code.
        """
        subject = "Lost Object Notification"
        body = f"A QR code associated with your lost object has been scanned.\n\nData: {qr_data}"

        try:
            # Setup the email server and send the email
            sender_email = "your_email@example.com"
            receiver_email = self.owner_email
            password = "your_email_password"  # Use environment variables for production

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Create a secure SSL context
            with smtplib.SMTP_SSL('smtp.example.com', 465) as server:  # Update SMTP server details
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            
            logging.info("Notification sent successfully to %s", self.owner_email)
        except Exception as e:
            logging.error("Failed to send notification: %s", e)

if __name__ == "__main__":
    # Example QR code data and owner's email
    qr_data_example = "Lost Object ID: 123456"
    owner_email_example = "owner@example.com"

    # Instantiate the QR code scanner and simulate the scan
    scanner = QRCodeScanner(owner_email_example)
    scanner.simulate_qr_scan(qr_data_example)
```
