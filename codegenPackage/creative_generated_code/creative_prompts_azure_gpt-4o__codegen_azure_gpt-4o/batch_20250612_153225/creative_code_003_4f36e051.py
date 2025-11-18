"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Create a script to send automated email notifications to parents regarding CBSE circulars and exam schedules, as outlined in the Deepti Convent Higher Secondary School content.
Generated: DETERMINISTIC_4f36e051c6f32357
Batch ID: 20250612_153225
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

# Configuration variables
SMTP_SERVER = "smtp.gmail.com"  # Change this if using a different mail server
SMTP_PORT = 587
EMAIL_ADDRESS = "your-email@gmail.com"  # Replace with your email
EMAIL_PASSWORD = "your-email-password"  # Replace with your email password
SUBJECT = "Important Updates: CBSE Circulars & Exam Schedules"
SCHOOL_NAME = "Deepti Convent Higher Secondary School"

# Function to read parent email addresses from a CSV file
def get_parent_emails(csv_file):
    """
    Reads parent email addresses from a given CSV file.
    Assumes the CSV has a column 'email' containing the email addresses.

    :param csv_file: Path to the CSV file
    :return: List of email addresses
    """
    try:
        email_list = []
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                email_list.append(row['email'])
        return email_list
    except FileNotFoundError:
        print(f"Error: File {csv_file} not found.")
        return []
    except KeyError:
        print("Error: 'email' column not found in the CSV file.")
        return []

# Function to send email notifications
def send_email(to_email, subject, body):
    """
    Sends an email using SMTP.

    :param to_email: Recipient email address
    :param subject: Email subject
    :param body: Email body/content
    :return: None
    """
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = to_email
        message['Subject'] = subject

        # Attach the email content
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
        print(f"Email sent successfully to {to_email}")
    except smtplib.SMTPException as e:
        print(f"Error sending email to {to_email}: {e}")

# Main function to orchestrate the email sending
def main():
    """
    Main function to send email notifications to all parents.
    Reads parent email addresses from a CSV file and sends them an email.
    """
    # Define email content
    email_body = f"""
    Dear Parent,

    Greetings from {SCHOOL_NAME}!

    We would like to inform you about the latest CBSE circulars and upcoming exam schedules.
    Please make sure to review the information provided and take necessary actions.

    For more details, please visit the school website or contact the administration.

    Best regards,
    {SCHOOL_NAME} Administration
    """

    # Path to the CSV file containing parent email addresses
    parent_email_csv = "parent_emails.csv"  # Replace with your actual file path

    # Get parent emails
    parent_emails = get_parent_emails(parent_email_csv)

    # Send emails to all parents
    if parent_emails:
        for email in parent_emails:
            send_email(email, SUBJECT, email_body)
    else:
        print("No emails to send. Please check the CSV file.")

# Entry point of the script
if __name__ == "__main__":
    main()
```
