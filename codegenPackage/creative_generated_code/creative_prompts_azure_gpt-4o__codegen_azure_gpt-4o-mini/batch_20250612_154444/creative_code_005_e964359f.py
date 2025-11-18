"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Develop a script to automate property management tasks, including tenant communication and financial reporting, using the streamlined and results-driven approach mentioned by Bebold Properties.
Generated: DETERMINISTIC_e964359f07b280f0
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import logging
from datetime import datetime
import pandas as pd

# Configure logging for better debugging and record-keeping
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PropertyManager:
    def __init__(self, email, password):
        """
        Initializes the PropertyManager with email credentials for sending emails.

        :param email: The email address used for sending tenant communications.
        :param password: The password for the email account.
        """
        self.email = email
        self.password = password
        self.tenants = {}
        
    def add_tenant(self, name, email):
        """
        Adds a tenant to the property management system.

        :param name: The name of the tenant.
        :param email: The email address of the tenant.
        """
        self.tenants[name] = email
        logging.info(f'Tenant {name} added with email {email}.')

    def send_email(self, recipient, subject, message):
        """
        Sends an email to a specified recipient.

        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param message: The content of the email.
        """
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email, self.password)
                email_message = f'Subject: {subject}\n\n{message}'
                server.sendmail(self.email, recipient, email_message)
                logging.info(f'Email sent to {recipient} with subject "{subject}".')
        except Exception as e:
            logging.error(f'Failed to send email to {recipient}: {e}')

    def generate_financial_report(self, payments):
        """
        Generates a financial report from a list of payments.

        :param payments: A list of dictionaries containing payment data.
        :return: DataFrame summarizing the financial report.
        """
        try:
            df = pd.DataFrame(payments)
            report = df.groupby('tenant').agg({'amount': 'sum'}).reset_index()
            report['date'] = datetime.now().strftime('%Y-%m-%d')
            logging.info('Financial report generated successfully.')
            return report
        except Exception as e:
            logging.error(f'Error generating financial report: {e}')
            return pd.DataFrame()  # Return an empty DataFrame on error

    def communicate_with_tenants(self, message):
        """
        Sends a message to all tenants.

        :param message: The message to be sent to tenants.
        """
        for tenant, email in self.tenants.items():
            self.send_email(email, "Important Update", message)

# Example usage:
if __name__ == '__main__':
    # Email credentials (replace with your actual credentials)
    EMAIL = 'your_email@gmail.com'
    PASSWORD = 'your_password'

    # Initialize Property Manager
    manager = PropertyManager(EMAIL, PASSWORD)

    # Add tenants
    manager.add_tenant('John Doe', 'johndoe@example.com')
    manager.add_tenant('Jane Smith', 'janesmith@example.com')

    # Communicate with tenants
    manager.communicate_with_tenants("Hi, this is an important update regarding your lease.")

    # Generate financial report
    payments = [
        {'tenant': 'John Doe', 'amount': 1200},
        {'tenant': 'Jane Smith', 'amount': 1300},
        {'tenant': 'John Doe', 'amount': 200},
    ]
    report = manager.generate_financial_report(payments)
    print(report)
```
