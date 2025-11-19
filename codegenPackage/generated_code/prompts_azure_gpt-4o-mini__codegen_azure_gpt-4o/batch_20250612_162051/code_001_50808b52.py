"""
Generated Code Metadata:
========================
Original URL: https://isbgames.isbeventteam.com
Prompt: Write a promotional email highlighting the unique features of the ISB Games 2024, focusing on the introduction of Bowling and the spirit of sportsmanship among ISB-ers.
Generated: DETERMINISTIC_50808b52901b4863
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_promotional_email(sender_email, sender_password, recipient_email):
    """
    Sends a promotional email highlighting the unique features of ISB Games 2024.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.

    Returns:
        None
    """
    try:
        # Email subject and sender/recipient details
        subject = "🎳 ISB Games 2024: Bowling, Sportsmanship, and More! 🏆"
        
        # Create the email content
        email_body = """
        <html>
        <body>
            <h1 style="color: #2E86C1;">ISB Games 2024: A Celebration of Sportsmanship and New Beginnings!</h1>
            <p>Dear ISB Community,</p>
            <p>We are thrilled to announce the much-awaited <strong>ISB Games 2024</strong>, where the spirit of sportsmanship and camaraderie takes center stage. This year, we are excited to introduce a brand-new event: <strong>Bowling</strong>! 🎳</p>
            <p>Here’s what makes ISB Games 2024 truly special:</p>
            <ul>
                <li><strong>Bowling Debut:</strong> For the first time ever, showcase your precision and strategy in our exciting new Bowling competition.</li>
                <li><strong>Unmatched Sportsmanship:</strong> Experience the true spirit of ISB-ers as we come together to celebrate teamwork, resilience, and fair play.</li>
                <li><strong>Diverse Events:</strong> From classic favorites to new challenges, there’s something for everyone to enjoy and excel in.</li>
            </ul>
            <p>Mark your calendars and get ready to be part of an unforgettable journey of athleticism, friendship, and fun!</p>
            <p><strong>Event Details:</strong></p>
            <ul>
                <li><strong>Date:</strong> March 15-17, 2024</li>
                <li><strong>Location:</strong> ISB Sports Complex</li>
            </ul>
            <p>Don’t miss out on the action! Register now and be a part of the legacy.</p>
            <p>Warm regards,</p>
            <p><strong>The ISB Games 2024 Team</strong></p>
        </body>
        </html>
        """

        # Create a MIMEText object to represent the email
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = recipient_email

        # Attach the email body to the message
        message.attach(MIMEText(email_body, "html"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the SMTP server
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email

        print("Promotional email sent successfully!")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# Replace with actual sender email, password, and recipient email
# send_promotional_email("your_email@gmail.com", "your_password", "recipient_email@gmail.com")
```
