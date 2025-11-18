"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gra-pro-canv.webflow.io
Prompt: Develop a script to maximize engagement for a grants program by automating outreach and tracking grantee experiences, referencing Gitcoin's framework.
Generated: DETERMINISTIC_f3482ec054fea8e1
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import csv
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    filename='grants_program.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Constants for email configuration
SMTP_SERVER = 'smtp.gmail.com'  # Use appropriate SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your app-specific password

# File paths
GRANTEES_FILE = 'grantees.csv'  # CSV file containing grantee information
FEEDBACK_FILE = 'feedback.csv'  # CSV file to collect grantee experiences

# Function to send an email
def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.
    
    :param to_email: Recipient's email address
    :param subject: Subject of the email
    :param body: Body of the email
    """
    try:
        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.set_content(body)

        # Connect to SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        logging.info(f"Email sent successfully to {to_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {to_email}: {e}")

# Function to read grantee information from a CSV file
def read_grantees(file_path):
    """
    Reads grantee information from a CSV file.
    
    :param file_path: Path to the CSV file
    :return: List of dictionaries containing grantee data
    """
    grantees = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            grantees = [row for row in reader]
        logging.info(f"Successfully read grantee data from {file_path}")
    except Exception as e:
        logging.error(f"Error reading grantee data from {file_path}: {e}")
    return grantees

# Function to collect feedback
def collect_feedback(grantee_name, feedback):
    """
    Appends feedback from grantees into a CSV file.
    
    :param grantee_name: Name of the grantee providing feedback
    :param feedback: Feedback text
    """
    try:
        with open(FEEDBACK_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), grantee_name, feedback])
        logging.info(f"Feedback collected from {grantee_name}")
    except Exception as e:
        logging.error(f"Error collecting feedback from {grantee_name}: {e}")

# Main function to execute the outreach and feedback collection process
def main():
    """
    Main function to automate outreach and track grantee experiences.
    """
    # Step 1: Read grantee details from the CSV file
    grantees = read_grantees(GRANTEES_FILE)
    
    # Step 2: Send outreach emails to each grantee
    for grantee in grantees:
        name = grantee.get('Name', 'Grantee')
        email = grantee.get('Email', '')
        if email:
            subject = "We Value Your Feedback - Grants Program Engagement"
            body = (
                f"Dear {name},\n\n"
                "Thank you for participating in our grants program. "
                "We would love to hear your feedback on your experience.\n\n"
                "Please reply to this email or fill out our feedback form.\n\n"
                "Best regards,\nGrants Program Team"
            )
            send_email(email, subject, body)
        else:
            logging.warning(f"Invalid email address for grantee: {name}")

    # Step 3: Prompt to collect feedback (for demonstration)
    print("Feedback collection initiated...")
    while True:
        grantee_name = input("Enter grantee name (or type 'exit' to quit): ")
        if grantee_name.lower() == 'exit':
            break
        feedback = input(f"Enter feedback for {grantee_name}: ")
        collect_feedback(grantee_name, feedback)

# Entry point of the script
if __name__ == "__main__":
    main()
```
