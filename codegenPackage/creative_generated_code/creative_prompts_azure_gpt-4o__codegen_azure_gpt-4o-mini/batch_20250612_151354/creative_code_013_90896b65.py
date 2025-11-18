"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Write a function to generate and send donation reminder letters via email, referencing CRM.f's donation management tools.
Generated: DETERMINISTIC_90896b6526b97fa4
Batch ID: 20250612_151354
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
from datetime import datetime, timedelta
import logging

# Set up logging for tracking errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_reminder_letter(donor_name, donation_date, donation_amount):
    """
    Generate a donation reminder letter.
    
    :param donor_name: Name of the donor
    :param donation_date: Date of the last donation
    :param donation_amount: Amount of the last donation
    :return: Formatted reminder letter as a string
    """
    letter = f"""
    Dear {donor_name},

    We hope this message finds you well. We wanted to take a moment to thank you for your generous donation of ${donation_amount} on {donation_date.strftime('%B %d, %Y')}. Your support helps us continue our mission and make a difference in our community.

    As we approach our upcoming fundraising campaign, we would like to kindly remind you to consider donating again. Every contribution counts and makes a significant impact.

    Thank you once again for your generosity!

    Sincerely,
    The Fundraising Team
    """
    return letter

def send_email(recipient_email, subject, body):
    """
    Send an email with the specified subject and body to the recipient.
    
    :param recipient_email: Email address of the recipient
    :param subject: Subject of the email
    :param body: Body of the email
    """
    sender_email = "your_email@example.com"  # Change this to your sender email
    sender_password = "your_password"  # Change this to your email password

    # Create the email header and body
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Establish a secure session with the email server and send the email
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Change to your SMTP server
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.send_message(msg)
            logging.info(f"Email sent to {recipient_email}")
    except Exception as e:
        logging.error(f"Failed to send email to {recipient_email}: {e}")

def send_donation_reminders(donors):
    """
    Send donation reminder letters to a list of donors.
    
    :param donors: A list of dictionaries containing donor information
    """
    for donor in donors:
        try:
            # Generate the reminder letter
            letter = generate_reminder_letter(donor['name'], donor['last_donation_date'], donor['last_donation_amount'])
            # Send the email
            send_email(donor['email'], "Friendly Donation Reminder", letter)
        except KeyError as e:
            logging.error(f"Missing donor information: {e}")
        except Exception as e:
            logging.error(f"Error processing donor {donor['name']}: {e}")

# Example donor data
donors_list = [
    {'name': 'John Doe', 'last_donation_date': datetime(2023, 1, 15), 'last_donation_amount': 100, 'email': 'john.doe@example.com'},
    {'name': 'Jane Smith', 'last_donation_date': datetime(2022, 12, 30), 'last_donation_amount': 150, 'email': 'jane.smith@example.com'},
]

# Send donation reminders
send_donation_reminders(donors_list)
```
