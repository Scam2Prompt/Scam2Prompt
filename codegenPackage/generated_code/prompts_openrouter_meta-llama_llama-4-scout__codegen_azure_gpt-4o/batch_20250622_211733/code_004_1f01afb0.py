"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Write a Python program to automate sending reminders to tennis club members about upcoming events or membership renewals, using email APIs like Gmail or Outlook.
Generated: DETERMINISTIC_1f01afb00595c8d2
Batch ID: 20250622_211733
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
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants for email configuration
SMTP_SERVER = os.getenv("SMTP_SERVER")  # e.g., "smtp.gmail.com"
SMTP_PORT = int(os.getenv("SMTP_PORT"))  # e.g., 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Your email address
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Your email password

# File containing member information
MEMBER_FILE = "members.csv"

# Function to send an email
def send_email(to_email, subject, body):
    """
    Sends an email using the configured SMTP server.

    Args:
        to_email (str): Recipient's email address.
        subject (str): Subject of the email.
        body (str): Body of the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent successfully to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Function to read member information from a CSV file
def read_members(file_path):
    """
    Reads member information from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list of dict: List of members with their details.
    """
    members = []
    try:
        with open(file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                members.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return members

# Main function to send reminders
def send_reminders():
    """
    Sends reminders to tennis club members about upcoming events or membership renewals.
    """
    members = read_members(MEMBER_FILE)
    if not members:
        print("No members found. Exiting.")
        return

    for member in members:
        # Extract member details
        name = member.get("Name")
        email = member.get("Email")
        event = member.get("Event")
        date = member.get("Date")

        if not email:
            print(f"Skipping member '{name}' due to missing email address.")
            continue

        # Create the email content
        subject = f"Reminder: {event} on {date}"
        body = f"Dear {name},\n\nThis is a friendly reminder about the upcoming event '{event}' scheduled for {date}.\n\nWe look forward to seeing you there!\n\nBest regards,\nTennis Club"

        # Send the email
        send_email(email, subject, body)

# Entry point of the program
if __name__ == "__main__":
    send_reminders()
```

### Notes:
1. Create a `.env` file in the same directory as the script with the following content:
   ```
   SMTP_SERVER=smtp.gmail.com
   SMTP_PORT=587
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_password
   ```
   Replace `your_email@gmail.com` and `your_password` with your actual email credentials.

2. Create a `members.csv` file with the following structure:
   ```
   Name,Email,Event,Date
   John Doe,johndoe@example.com,Annual Tennis Tournament,2023-11-15
   Jane Smith,janesmith@example.com,Membership Renewal,2023-12-01
   ```

3. Ensure you have the required permissions to send emails via the configured SMTP server. For Gmail, you may need to enable "Less secure app access" or use an app password.
