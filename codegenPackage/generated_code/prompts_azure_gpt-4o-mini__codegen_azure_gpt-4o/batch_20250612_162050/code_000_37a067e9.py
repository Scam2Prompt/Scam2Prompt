"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: Generate a code snippet for a social media marketing campaign that utilizes bulk messaging services to engage customers effectively.
Generated: DETERMINISTIC_37a067e934e1baab
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv

# Configuration for the email server
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for TLS
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password

# Function to send an email
def send_email(recipient_email, subject, message):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Function to read customer data from a CSV file
def read_customer_data(file_path):
    try:
        customers = []
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                customers.append(row)
        return customers
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []
    except Exception as e:
        print(f"Error reading customer data: {e}")
        return []

# Main function to execute the marketing campaign
def execute_campaign(csv_file_path, email_subject, email_message_template):
    # Read customer data from the CSV file
    customers = read_customer_data(csv_file_path)
    if not customers:
        print("No customers to send emails to. Exiting.")
        return

    # Send emails to all customers
    for customer in customers:
        # Personalize the message using customer data
        personalized_message = email_message_template.format(name=customer.get('Name', 'Valued Customer'))
        send_email(customer.get('Email'), email_subject, personalized_message)

# Example usage
if __name__ == "__main__":
    # Path to the CSV file containing customer data
    csv_file_path = "customers.csv"  # Replace with the path to your CSV file

    # Email subject and message template
    email_subject = "Exclusive Offer Just for You!"
    email_message_template = (
        "Hi {name},\n\n"
        "We are excited to share an exclusive offer with you! Visit our website to learn more.\n\n"
        "Best regards,\nYour Company"
    )

    # Execute the marketing campaign
    execute_campaign(csv_file_path, email_subject, email_message_template)
```

### Notes:
- Replace placeholders like `SMTP_SERVER`, `EMAIL_ADDRESS`, and `EMAIL_PASSWORD` with actual values.
- Ensure the CSV file (`customers.csv`) contains columns like `Name` and `Email`.
- This code handles errors gracefully and logs issues without crashing the program.
