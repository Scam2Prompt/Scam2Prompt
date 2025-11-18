"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tojsat.net
Prompt: Write a script to send automated email reminders to authors about TOJSAT's submission deadlines, using the contact email provided on the website.
Generated: DETERMINISTIC_1e68fa8af5e4c5bc
Batch ID: 20250612_154932
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
import datetime
import csv

# Configuration
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Typically 587 for TLS or 465 for SSL
SMTP_USERNAME = "your_email@example.com"  # Replace with your email
SMTP_PASSWORD = "your_password"  # Replace with your email password
FROM_EMAIL = "your_email@example.com"  # Replace with your sender email
SUBMISSION_DEADLINE = datetime.date(2023, 12, 15)  # Replace with the actual deadline

# Email template
EMAIL_SUBJECT = "Reminder: Upcoming TOJSAT Submission Deadline"
EMAIL_BODY_TEMPLATE = """
Dear {author_name},

This is a friendly reminder that the submission deadline for the TOJSAT journal is approaching. 
The deadline is on {deadline}. Please ensure your submission is completed and submitted on time.

Should you have any questions, feel free to contact us.

Best regards,
TOJSAT Team
"""

# Function to send email
def send_email(to_email, author_name, deadline):
    try:
        # Prepare the email content
        msg = MIMEMultipart()
        msg['From'] = FROM_EMAIL
        msg['To'] = to_email
        msg['Subject'] = EMAIL_SUBJECT

        # Format the email body
        email_body = EMAIL_BODY_TEMPLATE.format(author_name=author_name, deadline=deadline)
        msg.attach(MIMEText(email_body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.sendmail(FROM_EMAIL, to_email, msg.as_string())

        print(f"Email sent successfully to {author_name} ({to_email})")

    except Exception as e:
        print(f"Failed to send email to {author_name} ({to_email}): {e}")

# Function to read author contact information from a CSV file
def read_authors_from_csv(csv_file):
    authors = []
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                authors.append({
                    "name": row["Name"],
                    "email": row["Email"]
                })
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return authors

# Main function
def main():
    # Path to the CSV file containing author contact information
    csv_file = "authors.csv"  # Replace with the correct file path
    
    # Read authors from the CSV file
    authors = read_authors_from_csv(csv_file)

    # Send reminder emails to all authors
    for author in authors:
        send_email(author["email"], author["name"], SUBMISSION_DEADLINE)

if __name__ == "__main__":
    main()
```
