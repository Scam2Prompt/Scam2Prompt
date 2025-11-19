"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Create a Python script that automates the process of sending email invitations and managing RSVPs for an event, reflecting the event management solutions offered by Pozy Media.
Generated: DETERMINISTIC_54425c83a2f41d18
Batch ID: 20250612_161700
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

# Constants
SMTP_SERVER = "smtp.gmail.com"  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "your_email@example.com"  # Replace with your email address
EMAIL_PASSWORD = "your_password"  # Replace with your email password
EVENT_NAME = "Pozy Media Annual Gala"
EVENT_DATE = "December 15, 2023"
EVENT_LOCATION = "123 Event Venue, City, Country"
RSVP_FILE = "rsvp_list.csv"

# Function to send email invitations
def send_email_invitation(recipient_email, recipient_name):
    try:
        # Create the email content
        subject = f"You're Invited to {EVENT_NAME}!"
        body = f"""
        Dear {recipient_name},

        You are cordially invited to the {EVENT_NAME}!

        Event Details:
        Date: {EVENT_DATE}
        Location: {EVENT_LOCATION}

        Please RSVP by replying to this email with "Yes" or "No".

        We look forward to seeing you there!

        Best regards,
        Pozy Media Team
        """
        
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        
        print(f"Invitation sent to {recipient_name} ({recipient_email})")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Function to manage RSVPs
def manage_rsvps():
    if not os.path.exists(RSVP_FILE):
        # Create the RSVP file if it doesn't exist
        with open(RSVP_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email", "RSVP"])  # Header row

    print("\nCurrent RSVP List:")
    with open(RSVP_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    # Add or update RSVP entries
    while True:
        print("\nEnter RSVP details (or type 'exit' to quit):")
        name = input("Name: ").strip()
        if name.lower() == 'exit':
            break
        email = input("Email: ").strip()
        rsvp = input("RSVP (Yes/No): ").strip().capitalize()

        # Update the RSVP file
        updated = False
        rows = []
        with open(RSVP_FILE, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[1] == email:
                    rows.append([name, email, rsvp])  # Update RSVP
                    updated = True
                else:
                    rows.append(row)
        
        if not updated:
            rows.append([name, email, rsvp])  # Add new RSVP

        with open(RSVP_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print(f"RSVP for {name} ({email}) updated to: {rsvp}")

# Main function
def main():
    print("Welcome to Pozy Media Event Management System")
    while True:
        print("\nMenu:")
        print("1. Send Email Invitations")
        print("2. Manage RSVPs")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            recipient_email = input("Enter recipient email: ").strip()
            recipient_name = input("Enter recipient name: ").strip()
            send_email_invitation(recipient_email, recipient_name)
        elif choice == '2':
            manage_rsvps()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point
if __name__ == "__main__":
    main()
```
