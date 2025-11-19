"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write a Python script that automates the process of collecting client testimonials for a digital branding agency.
Generated: DETERMINISTIC_492f8a1d7bede40c
Batch ID: 20250612_162051
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
import os
from datetime import datetime

# Configuration settings
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Replace with your SMTP port
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
TESTIMONIALS_FILE = "client_testimonials.csv"  # File to store testimonials
CLIENTS_FILE = "clients.csv"  # File containing client information

# Email template
EMAIL_SUBJECT = "We'd love your feedback!"
EMAIL_BODY = """
Dear {client_name},

Thank you for working with us at [Your Agency Name]! We value your opinion and would love to hear your feedback.

Please take a moment to share your testimonial by replying to this email. Your feedback helps us improve and showcase our work to future clients.

Thank you for your time!

Best regards,
[Your Name]
[Your Agency Name]
"""

def send_email(client_email, client_name):
    """
    Sends an email to the client requesting a testimonial.

    :param client_email: The email address of the client
    :param client_name: The name of the client
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = client_email
        msg['Subject'] = EMAIL_SUBJECT

        # Personalize the email body
        personalized_body = EMAIL_BODY.format(client_name=client_name)
        msg.attach(MIMEText(personalized_body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print(f"Email sent successfully to {client_email}")
    except Exception as e:
        print(f"Failed to send email to {client_email}: {e}")

def collect_testimonials():
    """
    Automates the process of collecting client testimonials.
    Reads client information from a CSV file and sends testimonial request emails.
    """
    if not os.path.exists(CLIENTS_FILE):
        print(f"Error: {CLIENTS_FILE} not found.")
        return

    try:
        # Read client information from the CSV file
        with open(CLIENTS_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                client_name = row.get('Name')
                client_email = row.get('Email')

                if client_name and client_email:
                    send_email(client_email, client_name)
                else:
                    print(f"Invalid client data: {row}")
    except Exception as e:
        print(f"Error reading {CLIENTS_FILE}: {e}")

def save_testimonial(client_name, testimonial):
    """
    Saves a client testimonial to a CSV file.

    :param client_name: The name of the client
    :param testimonial: The testimonial provided by the client
    """
    try:
        # Check if the testimonials file exists
        file_exists = os.path.exists(TESTIMONIALS_FILE)

        # Open the file in append mode
        with open(TESTIMONIALS_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)

            # Write the header if the file is new
            if not file_exists:
                writer.writerow(['Timestamp', 'Client Name', 'Testimonial'])

            # Write the testimonial data
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            writer.writerow([timestamp, client_name, testimonial])

        print(f"Testimonial saved for {client_name}")
    except Exception as e:
        print(f"Error saving testimonial: {e}")

if __name__ == "__main__":
    print("Starting testimonial collection process...")
    collect_testimonials()
    print("Testimonial collection process completed.")
```
