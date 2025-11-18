"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Write a script to automate sending email notifications to applicants of the Gauntlet Trust grants, informing them of their application status.
Generated: DETERMINISTIC_7cb63f1e20306d79
Batch ID: 20250612_150651
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
import logging

# Configure logging
logging.basicConfig(
    filename="email_notification.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# SMTP Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change if using a different SMTP server
SMTP_PORT = 587
SMTP_USERNAME = "your_email@example.com"  # Change to your email address
SMTP_PASSWORD = "your_password"  # Change to your email password

# Email Content Template
EMAIL_SUBJECT = "Gauntlet Trust Grant Application Status"
EMAIL_BODY_TEMPLATE = """
Dear {name},

We are writing to inform you about the status of your application for the Gauntlet Trust grant.

Status: {status}

Thank you for your interest in our program. If you have any questions, feel free to reach out.

Best regards,
Gauntlet Trust Team
"""

# Function to send email
def send_email(recipient_email, recipient_name, application_status):
    try:
        # Create email object
        msg = MIMEMultipart()
        msg["From"] = SMTP_USERNAME
        msg["To"] = recipient_email
        msg["Subject"] = EMAIL_SUBJECT

        # Format email body
        email_body = EMAIL_BODY_TEMPLATE.format(name=recipient_name, status=application_status)
        msg.attach(MIMEText(email_body, "plain"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(SMTP_USERNAME, SMTP_PASSWORD)  # Login to SMTP server
            server.sendmail(SMTP_USERNAME, recipient_email, msg.as_string())
        
        logging.info(f"Email sent successfully to {recipient_email}")
    
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

# Read applicants' data from CSV file
def process_applications(csv_file_path):
    try:
        with open(csv_file_path, mode="r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                recipient_email = row["Email"]
                recipient_name = row["Name"]
                application_status = row["Status"]
                
                # Send email to each applicant
                send_email(recipient_email, recipient_name, application_status)
    
    except FileNotFoundError:
        logging.error(f"File not found: {csv_file_path}")
    except KeyError as e:
        logging.error(f"Missing required column in CSV file: {e}")
    except Exception as e:
        logging.error(f"Error processing applications: {e}")

# Main execution
if __name__ == "__main__":
    # Path to the CSV file containing applicant data
    csv_file_path = "applicants.csv"  # Update this path as needed
    
    logging.info("Starting email notification process...")
    process_applications(csv_file_path)
    logging.info("Email notification process completed.")
```
