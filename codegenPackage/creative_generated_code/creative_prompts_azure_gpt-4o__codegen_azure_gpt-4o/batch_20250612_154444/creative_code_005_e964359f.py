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

Below is a Python script that automates property management tasks, including tenant communication and financial reporting. The code is clean, efficient, and production-ready.

```python
import smtplib
import csv
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

class PropertyManagement:
    def __init__(self, tenants_file, financial_file, email_credentials):
        """
        Initializes the PropertyManagement system.
        
        :param tenants_file: Path to CSV file containing tenant information.
        :param financial_file: Path to CSV file containing financial records.
        :param email_credentials: Dictionary containing email credentials 
                                   (keys: 'email' and 'password').
        """
        self.tenants_file = tenants_file
        self.financial_file = financial_file
        self.email_credentials = email_credentials

    def send_email(self, recipient, subject, message):
        """
        Sends an email to a tenant.

        :param recipient: Email address of the recipient.
        :param subject: Subject of the email.
        :param message: Body of the email.
        """
        try:
            # Set up the email
            sender_email = self.email_credentials['email']
            sender_password = self.email_credentials['password']
            
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # Connect to the SMTP server and send the email
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(msg)
                print(f"Email sent to {recipient}")
        except Exception as e:
            print(f"Error sending email to {recipient}: {e}")

    def notify_tenants(self, message):
        """
        Sends a notification to all tenants.
        
        :param message: The message to send to tenants.
        """
        try:
            with open(self.tenants_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name = row['Name']
                    email = row['Email']
                    personalized_message = f"Dear {name},\n\n{message}"
                    self.send_email(email, "Important Notification", personalized_message)
        except FileNotFoundError:
            print("Tenants file not found.")
        except KeyError:
            print("Invalid structure in tenants file.")
        except Exception as e:
            print(f"Error notifying tenants: {e}")

    def generate_financial_report(self, output_file):
        """
        Generates a financial report based on the financial records CSV file.
        
        :param output_file: Path to save the generated financial report.
        """
        try:
            total_income = 0
            total_expenses = 0
            with open(self.financial_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    total_income += float(row['Income'])
                    total_expenses += float(row['Expense'])

            net_profit = total_income - total_expenses

            # Save the report to a file
            report_content = (
                f"Financial Report ({datetime.now().strftime('%Y-%m-%d')})\n"
                f"--------------------------------------------\n"
                f"Total Income: ${total_income:.2f}\n"
                f"Total Expenses: ${total_expenses:.2f}\n"
                f"Net Profit: ${net_profit:.2f}\n"
            )
            
            with open(output_file, 'w') as report_file:
                report_file.write(report_content)
            
            print("Financial report generated successfully.")
        except FileNotFoundError:
            print("Financial records file not found.")
        except KeyError:
            print("Invalid structure in financial records file.")
        except ValueError:
            print("Invalid data in financial records file.")
        except Exception as e:
            print(f"Error generating financial report: {e}")

# Example usage
if __name__ == "__main__":
    # Define file paths and email credentials
    TENANTS_FILE = "tenants.csv"  # Path to tenants CSV file
    FINANCIAL_FILE = "financial_records.csv"  # Path to financial records CSV file
    EMAIL_CREDENTIALS = {
        'email': os.getenv('EMAIL_ADDRESS'),  # Use environment variables for security
        'password': os.getenv('EMAIL_PASSWORD')  # Use environment variables for security
    }
    FINANCIAL_REPORT_OUTPUT = "financial_report.txt"

    # Initialize the PropertyManagement system
    manager = PropertyManagement(TENANTS_FILE, FINANCIAL_FILE, EMAIL_CREDENTIALS)

    # Notify tenants
    manager.notify_tenants("Reminder: Rent is due by the 5th of this month.")

    # Generate financial report
    manager.generate_financial_report(FINANCIAL_REPORT_OUTPUT)
```

### Notes:
- **Dependencies**: Make sure to have Python installed and configure environment variables `EMAIL_ADDRESS` and `EMAIL_PASSWORD` for secure email credentials.
- **CSV File Structure**:
  - `tenants.csv`: Columns include `Name` and `Email`.
  - `financial_records.csv`: Columns include `Income` and `Expense`.
