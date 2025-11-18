"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instantconnect.info
Prompt: Create a Python script to automate client onboarding for AI education services, reflecting Instant Connect AI's focus on support and results-driven processes.
Generated: DETERMINISTIC_931024a40852f724
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Constants
CLIENT_DATA_FILE = "clients.csv"  # CSV file to store client information
WELCOME_EMAIL_SUBJECT = "Welcome to Instant Connect AI Education Services"
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Standard SMTP port
EMAIL_SENDER = "your_email@example.com"  # Replace with sender's email
EMAIL_PASSWORD = "your_email_password"  # Replace with sender's email password

# Function to ensure the client data file exists
def initialize_client_data_file():
    if not os.path.exists(CLIENT_DATA_FILE):
        with open(CLIENT_DATA_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write the header row
            writer.writerow(["Name", "Email", "Date Onboarded"])
        print(f"{CLIENT_DATA_FILE} created successfully.")

# Function to onboard a client
def onboard_client(name, email):
    try:
        # Write client details to the CSV file
        with open(CLIENT_DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            date_onboarded = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([name, email, date_onboarded])
        print(f"Successfully added client: {name} ({email})")

        # Send welcome email
        send_welcome_email(name, email)
    except Exception as e:
        print(f"Error onboarding client: {e}")

# Function to send a welcome email
def send_welcome_email(name, email):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = email
        msg['Subject'] = WELCOME_EMAIL_SUBJECT

        # Email body
        body = f"""
        Hi {name},

        Welcome to Instant Connect AI Education Services!
        We're thrilled to have you onboard. Our team is here to support you every step of the way.

        If you have any questions or need assistance, feel free to reach out.

        Best regards,
        The Instant Connect AI Team
        """
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Upgrade the connection to secure
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Welcome email sent to {email}")
    except Exception as e:
        print(f"Error sending welcome email: {e}")

# Main function
def main():
    # Initialize data file
    initialize_client_data_file()

    # Sample client onboarding process
    print("Automating client onboarding...")
    onboard_client("John Doe", "john.doe@example.com")
    onboard_client("Jane Smith", "jane.smith@example.com")

if __name__ == "__main__":
    main()
```
