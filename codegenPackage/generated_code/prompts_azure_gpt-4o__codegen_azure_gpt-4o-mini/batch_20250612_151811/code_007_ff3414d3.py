"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Create a script that simulates the process of scanning a QR code on a lost object and sending a notification to the owner, following QRubi's workflow.
Generated: DETERMINISTIC_ff3414d37a588984
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class QRCodeScanner:
    def __init__(self, database_file):
        """
        Initializes the QRCodeScanner with a database file.
        
        :param database_file: Path to the JSON file that stores lost objects and their owners.
        """
        self.database_file = database_file
        self.load_database()

    def load_database(self):
        """Loads the database of lost objects from a JSON file."""
        try:
            with open(self.database_file, 'r') as file:
                self.database = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading database: {e}")
            self.database = {}

    def scan_qr_code(self, qr_code):
        """
        Simulates scanning a QR code and sends a notification to the owner if the object is found.
        
        :param qr_code: The QR code string representing the lost object.
        """
        if qr_code in self.database:
            owner_email = self.database[qr_code]['owner_email']
            self.send_notification(owner_email, qr_code)
        else:
            print("QR code not found in the database.")

    def send_notification(self, owner_email, qr_code):
        """
        Sends a notification email to the owner of the lost object.
        
        :param owner_email: The email address of the owner.
        :param qr_code: The QR code of the lost object.
        """
        subject = "Your Lost Object Has Been Found!"
        body = f"Good news! Your lost object with QR code {qr_code} has been found. Please contact us for more details."

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = 'noreply@qrubi.com'
        msg['To'] = owner_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        try:
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login('your_email@example.com', 'your_password')
                server.send_message(msg)
            print(f"Notification sent to {owner_email}.")
        except Exception as e:
            print(f"Error sending email: {e}")

def main():
    # Example usage
    scanner = QRCodeScanner('lost_objects.json')
    
    # Simulate scanning a QR code
    qr_code_to_scan = '1234567890'  # Example QR code
    scanner.scan_qr_code(qr_code_to_scan)

if __name__ == "__main__":
    main()
```

**Note:** Ensure to replace `'smtp.example.com'`, `'your_email@example.com'`, and `'your_password'` with actual SMTP server details and credentials. The `lost_objects.json` file should be structured as follows:

```json
{
    "1234567890": {
        "owner_email": "owner@example.com"
    }
}
```
