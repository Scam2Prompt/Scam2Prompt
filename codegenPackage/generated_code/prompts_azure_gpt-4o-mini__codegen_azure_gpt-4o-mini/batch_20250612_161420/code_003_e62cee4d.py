"""
Generated Code Metadata:
========================
Original URL: https://ndhc.edu.bd
Prompt: Draft a message for students about the celebration of the International Day Against Drug Abuse and Illicit Trafficking, including details about the competition organized by Nazirpur Degree College.
Generated: DETERMINISTIC_e62cee4d2a229c8e
Batch ID: 20250612_161420
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

def send_email(subject, body, recipient_email):
    """
    Sends an email with the specified subject and body to the given recipient.

    Parameters:
    subject (str): The subject of the email.
    body (str): The body content of the email.
    recipient_email (str): The email address of the recipient.

    Raises:
    Exception: If there is an error sending the email.
    """
    # Email configuration
    sender_email = "your_email@example.com"
    sender_password = "your_password"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the email body
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

def main():
    """
    Main function to draft and send the email about the International Day Against Drug Abuse and Illicit Trafficking.
    """
    subject = "Celebration of International Day Against Drug Abuse and Illicit Trafficking"
    body = (
        "Dear Students,\n\n"
        "We are pleased to announce the celebration of the International Day Against Drug Abuse and Illicit Trafficking. "
        "This important day is observed annually on June 26th to strengthen action and cooperation in achieving a world free of drug abuse.\n\n"
        "In honor of this day, Nazirpur Degree College is organizing a competition aimed at raising awareness about the dangers of drug abuse. "
        "We encourage all students to participate and showcase their creativity and understanding of this critical issue.\n\n"
        "Details of the competition are as follows:\n"
        "- Date: June 26, 2023\n"
        "- Time: 10:00 AM - 2:00 PM\n"
        "- Venue: College Auditorium\n"
        "- Categories: Poster Making, Essay Writing, and Debate\n\n"
        "Prizes will be awarded to the top three participants in each category. "
        "We look forward to your enthusiastic participation in making this event a success!\n\n"
        "Best Regards,\n"
        "Nazirpur Degree College"
    )

    # List of recipient emails (for demonstration purposes)
    recipient_emails = ["student1@example.com", "student2@example.com"]

    # Send the email to each recipient
    for email in recipient_emails:
        send_email(subject, body, email)

if __name__ == "__main__":
    main()
```
