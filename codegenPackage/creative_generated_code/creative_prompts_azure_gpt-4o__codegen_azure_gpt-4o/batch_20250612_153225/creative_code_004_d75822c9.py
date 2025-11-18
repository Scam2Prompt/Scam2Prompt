"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testul-poligraf.ro
Prompt: Write a script to automate sending email reminders for polygraph test appointments, using the contact details format provided on the Euro Poligraf Center website.
Generated: DETERMINISTIC_d75822c9808c7f27
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import csv
from datetime import datetime, timedelta

# SMTP Configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'

# Email Sender Details
SENDER_EMAIL = 'your_email@example.com'
SENDER_NAME = 'Euro Poligraf Center'

# Email Reminder Content
EMAIL_SUBJECT = "Reminder: Upcoming Polygraph Test Appointment"
EMAIL_BODY_TEMPLATE = """\
Dear {name},

This is a friendly reminder for your upcoming polygraph test appointment.

Date: {appointment_date}
Time: {appointment_time}
Location: Euro Poligraf Center

Please let us know if you have any questions or concerns. We look forward to seeing you!

Best regards,
Euro Poligraf Center
"""

# Function to send an email
def send_email(recipient_email, recipient_name, appointment_date, appointment_time):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
        msg['To'] = recipient_email
        msg['Subject'] = EMAIL_SUBJECT

        # Format the email body
        formatted_body = EMAIL_BODY_TEMPLATE.format(
            name=recipient_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        )
        msg.attach(MIMEText(formatted_body, 'plain'))

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the connection
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()

        print(f"Email sent successfully to {recipient_name} ({recipient_email}).")
    except Exception as e:
        print(f"Error sending email to {recipient_name} ({recipient_email}): {e}")

# Function to parse contact details from CSV file
def parse_contacts(file_path):
    contacts = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Extract fields from CSV
                name = row['Name']
                email = row['Email']
                appointment_date = row['Appointment_Date']
                appointment_time = row['Appointment_Time']

                # Convert appointment_date to datetime and check if reminder is needed
                appointment_datetime = datetime.strptime(appointment_date, "%Y-%m-%d")
                if appointment_datetime - datetime.now() <= timedelta(days=1):  # Reminder for tomorrow
                    contacts.append({
                        'name': name,
                        'email': email,
                        'appointment_date': appointment_date,
                        'appointment_time': appointment_time
                    })
    except FileNotFoundError:
        print("Error: Contact details file not found.")
    except KeyError:
        print("Error: Missing required columns in the CSV file.")
    except Exception as e:
        print(f"Error reading contacts file: {e}")
    return contacts

# Main function to send reminders
def main():
    CONTACTS_FILE_PATH = 'contacts.csv'  # Path to the CSV file with contact details

    # Parse contacts from the file
    contacts = parse_contacts(CONTACTS_FILE_PATH)

    # Send reminders to each contact
    for contact in contacts:
        send_email(
            recipient_email=contact['email'],
            recipient_name=contact['name'],
            appointment_date=contact['appointment_date'],
            appointment_time=contact['appointment_time']
        )

if __name__ == "__main__":
    main()
```

### Notes:
- Replace placeholder SMTP settings (`SMTP_SERVER`, `SMTP_USERNAME`, etc.) with real credentials.
- Ensure the CSV file (`contacts.csv`) contains columns: `Name`, `Email`, `Appointment_Date`, `Appointment_Time`.
- Install any required dependencies (e.g., `pip install secure-smtplib` if needed for your environment).
