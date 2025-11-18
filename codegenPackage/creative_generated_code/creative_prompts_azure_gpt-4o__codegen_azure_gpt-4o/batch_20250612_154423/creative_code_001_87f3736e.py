"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.igeog.uerj.br
Prompt: Generate a script to automate email notifications for candidates based on the results from the IGEOG selection processes, using the data from the "Edital" and "Relação de candidatos aptos" sections.
Generated: DETERMINISTIC_87f3736e9034f871
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Configure logging
logging.basicConfig(
    filename='email_notifications.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password

# Load candidate data
EDITAL_FILE = 'edital.xlsx'  # Replace with the path to your file
CANDIDATES_SHEET = 'Relação de candidatos aptos'

try:
    # Read the Excel file
    data = pd.read_excel(EDITAL_FILE, sheet_name=CANDIDATES_SHEET)
    
    # Ensure required columns exist
    if not {'Candidate Name', 'Email', 'Status', 'Comments'}.issubset(data.columns):
        raise ValueError(
            "Required columns ('Candidate Name', 'Email', 'Status', 'Comments') are missing in the data file."
        )
except Exception as e:
    logging.error(f"Error reading the Excel file: {e}")
    raise

# Prepare and send email notifications
def send_email(to_address, subject, body):
    """
    Sends an email using the provided SMTP configuration.

    :param to_address: Recipient email address
    :param subject: Email subject
    :param body: Email body
    """
    try:
        # Create the email
        message = MIMEMultipart()
        message['From'] = EMAIL_ADDRESS
        message['To'] = to_address
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade to secure connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
            logging.info(f"Email sent successfully to {to_address}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_address}: {e}")


# Generate email content based on candidate data
for _, row in data.iterrows():
    name = row['Candidate Name']
    email = row['Email']
    status = row['Status']
    comments = row['Comments']

    # Customize the email subject and body
    email_subject = f"Notification of Selection Results for {name}"
    email_body = (
        f"Dear {name},\n\n"
        f"Your application has been reviewed and the result is as follows:\n"
        f"Status: {status}\n\n"
        f"Comments: {comments}\n\n"
        "Thank you for your interest.\n\n"
        "Best regards,\n"
        "IGEOG Team"
    )

    # Send the email
    send_email(email, email_subject, email_body)
```
