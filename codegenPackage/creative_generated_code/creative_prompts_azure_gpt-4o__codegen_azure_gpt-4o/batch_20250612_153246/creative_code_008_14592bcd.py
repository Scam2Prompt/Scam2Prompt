"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nzothofetcollege.co.za
Prompt: Create a Python script to send automated email reminders to Nzotho FET College students about upcoming semester start dates and deadlines.
Generated: DETERMINISTIC_14592bcd580786c0
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
from datetime import datetime
import csv

# Configuration
SMTP_SERVER = 'smtp.gmail.com'  # Replace with your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@example.com'  # Replace with your email address
EMAIL_PASSWORD = 'your_password'  # Replace with your email password
SUBJECT = 'Reminder: Upcoming Semester Start Dates and Deadlines'
CSV_FILE = 'students.csv'  # CSV file containing student data

# Function to load student data from a CSV file
def load_students(csv_file):
    """
    Load student data from a CSV file.
    The CSV file should have columns: name, email, semester_start_date, deadline_date.
    """
    students = []
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append({
                    'name': row['name'],
                    'email': row['email'],
                    'semester_start_date': row['semester_start_date'],
                    'deadline_date': row['deadline_date']
                })
    except FileNotFoundError:
        print(f'Error: File {csv_file} not found.')
    except KeyError as e:
        print(f'Error: Missing expected column in CSV file: {e}')
    except Exception as e:
        print(f'Error reading CSV file: {e}')
    return students

# Function to send an email
def send_email(to_email, subject, body):
    """
    Send an email to the specified recipient.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Encrypt the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print(f'Email sent successfully to {to_email}')
    except smtplib.SMTPException as e:
        print(f'Error sending email to {to_email}: {e}')

# Function to generate email body
def generate_email_body(student):
    """
    Generate the email body for a student.
    """
    return (f"Dear {student['name']},\n\n"
            f"This is a reminder about the upcoming semester at Nzotho FET College.\n\n"
            f"Semester Start Date: {student['semester_start_date']}\n"
            f"Deadline Date: {student['deadline_date']}\n\n"
            f"Please ensure all required forms and payments are submitted before the deadlines.\n\n"
            f"Best regards,\nNzotho FET College Administration")

# Main function
def main():
    """
    Main function to send email reminders to students.
    """
    print("Loading student data...")
    students = load_students(CSV_FILE)
    if not students:
        print("No student data available. Exiting...")
        return

    print("Sending email reminders...")
    for student in students:
        email_body = generate_email_body(student)
        send_email(student['email'], SUBJECT, email_body)
    print("All emails sent successfully.")

# Entry point
if __name__ == '__main__':
    main()
```
