"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudsverse-opsec.com
Prompt: Write code to flag fraudulent communications claiming to represent M2 Earn Ltd, using their official contact details and fraud prevention guidelines.
Generated: DETERMINISTIC_ca8708e470140825
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for M2 Earn Ltd official contact details
OFFICIAL_EMAIL = "support@m2earn.com"
OFFICIAL_PHONE = "+1234567890"
FRAUD_REPORT_EMAIL = "fraud-report@m2earn.com"

# Define a simple class to handle fraudulent communication detection
class FraudDetection:
    def __init__(self):
        # Compile regex patterns for common fraud indicators
        self.email_pattern = re.compile(r'[\w\.-]+@m2earn\.com')
        self.phone_pattern = re.compile(r'\+?(\d[\d -]{7,12}\d)')  # International format

    def is_fraudulent(self, communication):
        """
        Check if the communication is fraudulent based on predefined criteria.
        
        :param communication: A string representing the communication message
        :return: True if fraudulent, False otherwise
        """
        # Check if the official email or phone number is misused
        if self.email_pattern.search(communication) or self.phone_pattern.search(communication):
            return True
        return False

    def report_fraud(self, communication):
        """
        Send an email to the fraud report address if fraudulent communication is detected.
        
        :param communication: A string representing the fraudulent communication message
        """
        message = MIMEMultipart()
        message['From'] = OFFICIAL_EMAIL
        message['To'] = FRAUD_REPORT_EMAIL
        message['Subject'] = "Fraudulent Communication Detected"

        # Create the body of the email
        body = f"Fraudulent communication detected:\n\n{communication}"
        message.attach(MIMEText(body, 'plain'))

        # Attempt to send the email
        try:
            with smtplib.SMTP('smtp.m2earn.com', 587) as server:
                server.starttls()
                server.login(OFFICIAL_EMAIL, 'your_email_password')  # Replace with actual password
                server.send_message(message)
                print("Fraud report sent successfully.")
        except smtplib.SMTPException as e:
            print(f"Error occurred while sending email: {e}")

# Example usage
if __name__ == "__main__":
    # Sample communication to check
    sample_communication = "Contact us at support@m2earn.com or call +1234567890 for assistance."

    # Create an instance of the FraudDetection class
    fraud_detector = FraudDetection()

    # Check if the communication is fraudulent
    if fraud_detector.is_fraudulent(sample_communication):
        print("Fraudulent communication detected.")
        fraud_detector.report_fraud(sample_communication)
    else:
        print("Communication is legitimate.")
```

**Note**: Replace `'your_email_password'` with the actual password or use an environment variable for better security practices.
