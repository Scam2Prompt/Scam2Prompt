"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pshp.com.pk
Prompt: Write a script to send automated newsletters to PSHP members using the contact details provided on the website, ensuring compliance with email marketing best practices.
Generated: DETERMINISTIC_09e1e921d837390a
Batch ID: 20250612_153246
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
import os
from dotenv import load_dotenv

# Load environment variables for email credentials
load_dotenv()

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")  # Your email address
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  # Your email password
SUBJECT = "Your Monthly PSHP Newsletter"
NEWSLETTER_CONTENT = """
Dear Member,

We hope this newsletter finds you well. Here are the highlights for this month from PSHP:

1. Upcoming Events
2. Latest News
3. Member Spotlights

Visit our website for more details!

Warm regards,
PSHP Team
"""

# File containing member details in CSV format
MEMBER_FILE = "pshp_members.csv"  # Ensure this file exists and contains [Name, Email]

def send_newsletter():
    """
    Sends an automated newsletter to PSHP members using the contact details provided in the CSV file.
    """
    try:
        # Establish a connection to the SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Start TLS encryption
        server.login(SENDER_EMAIL, SENDER_PASSWORD)  # Log in to the sender's email account

        # Read the member details from the CSV file
        with open(MEMBER_FILE, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if it exists

            for row in reader:
                if len(row) < 2:  # Ensure record has both Name and Email
                    continue

                name, recipient_email = row[0], row[1]

                # Create the email content
                message = MIMEMultipart()
                message["From"] = SENDER_EMAIL
                message["To"] = recipient_email
                message["Subject"] = SUBJECT

                # Personalize the email content
                personalized_content = f"Hi {name},\n\n" + NEWSLETTER_CONTENT
                message.attach(MIMEText(personalized_content, "plain"))

                # Send the email
                server.sendmail(SENDER_EMAIL, recipient_email, message.as_string())
                print(f"Newsletter sent to {name} at {recipient_email}")

        # Close the SMTP server connection
        server.quit()

    except FileNotFoundError:
        print(f"Error: Member file '{MEMBER_FILE}' not found.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Execute the newsletter sending function
    send_newsletter()
```

**Note**: 
- Ensure you have a `.env` file containing `SENDER_EMAIL` and `SENDER_PASSWORD`.
- Replace `pshp_members.csv` with the actual CSV file containing the member details.
- Use a secure sender email account and abide by email marketing regulations like GDPR and CAN-SPAM Act.
