"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seandahealthcare.co.za
Prompt: Generate a Python script to automate the registration process for healthcare professionals at a placement agency like Seanda Healthcare.
Generated: DETERMINISTIC_8f020a22c4a177c6
Batch ID: 20250612_155732
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

# Import necessary modules for email notification
import smtplib
from email.message import EmailMessage

# Define the script configuration
CONFIG = {
    "data_file": "registrations.json",
    "admin_email": "admin@seandahealthcare.com",
    "smtp_server": "smtp.example.com",  # Replace with actual SMTP server
    "smtp_port": 587,                  # Replace with actual port
    "smtp_user": "your-email@example.com",  # Replace with actual email
    "smtp_password": "your-email-password"  # Replace with actual password
}

def load_registrations(file_path):
    """
    Load existing registrations from the JSON file.
    Creates the file if it does not exist.
    """
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Failed to decode registration file. Starting fresh.")
        return {}

def save_registrations(file_path, data):
    """
    Save registrations to the JSON file.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error: Failed to save registrations. {e}")

def send_email_notification(to_email, subject, body):
    """
    Send an email notification.
    """
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = CONFIG['smtp_user']
        msg['To'] = to_email
        msg.set_content(body)

        with smtplib.SMTP(CONFIG['smtp_server'], CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(CONFIG['smtp_user'], CONFIG['smtp_password'])
            server.send_message(msg)
        print(f"Notification sent to {to_email}.")
    except Exception as e:
        print(f"Error: Failed to send email. {e}")

def register_professional():
    """
    Prompt user for professional registration details and save them.
    """
    print("Welcome to Seanda Healthcare's Registration Portal!")

    # Gather user input
    name = input("Enter your full name: ").strip()
    email = input("Enter your email address: ").strip()
    profession = input("Enter your profession (e.g., Nurse, Doctor): ").strip()
    phone_number = input("Enter your phone number: ").strip()

    # Validate input
    if not name or not email or not profession or not phone_number:
        print("Error: All fields are mandatory. Please try again.")
        return

    # Load existing registrations
    registrations = load_registrations(CONFIG['data_file'])

    # Check if email is already registered
    if email in registrations:
        print("Error: This email is already registered.")
        return

    # Add the new registration
    registrations[email] = {
        "name": name,
        "profession": profession,
        "phone_number": phone_number
    }

    # Save registration
    save_registrations(CONFIG['data_file'], registrations)

    print("Registration successful!")

    # Notify admin
    email_body = (
        f"New healthcare professional registered:\n\n"
        f"Name: {name}\n"
        f"Profession: {profession}\n"
        f"Email: {email}\n"
        f"Phone: {phone_number}"
    )
    send_email_notification(CONFIG['admin_email'], "New Registration Notification", email_body)

def main():
    """
    Main function to start the registration process.
    """
    try:
        register_professional()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
