"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conferencesglobal.org
Prompt: Create a Python script to send an email request for an invitation letter to the conference secretary, including all necessary travel visa details as outlined on the Conferences Global website.
Generated: DETERMINISTIC_8aaf4c0f1b9ef86d
Batch ID: 20250612_154452
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

def send_email_request(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an email request for an invitation letter to the conference secretary
    including necessary travel visa details.

    :param sender_email: str, email address of the sender
    :param sender_password: str, sender's email password
    :param recipient_email: str, recipient's email address
    :param subject: str, subject of the email
    :param body: str, body of the email
    :return: None
    """
    try:
        # Set up the MIME message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        # Attach the body of the email
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade connection to secure encryption
            server.login(sender_email, sender_password)  # Log in to the server
            server.send_message(msg)  # Send the email
            print("Email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

# Example usage
if __name__ == "__main__":
    # Replace these with actual values
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    recipient_email = "conference_secretary@example.com"
    subject = "Request for Invitation Letter for Conference"
    
    # Customize the email body as per visa details required
    body = """
    Dear Conference Secretary,

    I am writing to formally request an invitation letter for the upcoming conference 
    hosted by Conferences Global. I require this letter to apply for a travel visa. 
    Below are my details to include in the invitation letter:

    Full Name: [Your Full Name]
    Passport Number: [Your Passport Number]
    Nationality: [Your Nationality]
    Conference Name: [Conference Name]
    Conference Dates: [Start Date - End Date]
    Purpose of Visit: [Brief Purpose]

    Please let me know if you require any additional information from my side.

    Thank you for your assistance.

    Best regards,
    [Your Name]
    """

    # Send the email
    send_email_request(sender_email, sender_password, recipient_email, subject, body)
```
