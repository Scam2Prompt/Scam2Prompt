"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://springsinternational.org
Prompt: Recommend a library for creating and distributing digital flyers for events like Easter Eve programs, and provide sample code for generating and emailing the flyers.
Generated: DETERMINISTIC_80defce32dee216f
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fpdf import FPDF
from datetime import datetime

# Constants for email configuration
SMTP_SERVER = 'smtp.example.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common port for SMTP
USERNAME = 'your_email@example.com'  # Your email username
PASSWORD = 'your_password'  # Your email password

class FlyerGenerator:
    """Class for generating digital flyers for events."""
    
    def __init__(self, title, date, time, location, description):
        """
        Initializes the FlyerGenerator with event details.
        
        Parameters:
            title (str): The title of the event.
            date (str): The date of the event.
            time (str): The time of the event.
            location (str): The location of the event.
            description (str): A description of the event.
        """
        self.title = title
        self.date = date
        self.time = time
        self.location = location
        self.description = description

    def create_flyer(self, filename='flyer.pdf'):
        """Generates a PDF flyer using the provided event details."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        
        # Title
        pdf.cell(0, 10, self.title, ln=True, align='C')
        
        # Date and Time
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(0, 10, f'Date: {self.date}', ln=True, align='C')
        pdf.cell(0, 10, f'Time: {self.time}', ln=True, align='C')
        
        # Location
        pdf.cell(0, 10, f'Location: {self.location}', ln=True, align='C')
        
        # Description
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, self.description)
        
        # Save the PDF
        pdf.output(filename)
        return os.path.abspath(filename)

class EmailSender:
    """Class for sending emails with attachments."""
    
    def __init__(self, smtp_server, port, username, password):
        """
        Initializes the EmailSender with SMTP configuration.
        
        Parameters:
            smtp_server (str): The SMTP server address.
            port (int): The port to connect to the SMTP server.
            username (str): The email username.
            password (str): The email password.
        """
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password

    def send_email(self, recipient_email, subject, body, attachment_path):
        """Sends an email with an attachment."""
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = self.username
            msg['To'] = recipient_email
            msg['Subject'] = subject
            
            # Attach the body
            msg.attach(MIMEText(body, 'plain'))
            
            # Attach the flyer
            with open(attachment_path, 'rb') as attachment:
                part = MIMEText(attachment.read(), 'base64')
                part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
                msg.attach(part)

            # Send the email
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()  # Enable security
                server.login(self.username, self.password)
                server.send_message(msg)

            print(f'Email sent successfully to {recipient_email}')

        except Exception as e:
            print(f'Failed to send email. Error: {str(e)}')

# Sample usage
if __name__ == '__main__':
    event_title = 'Easter Eve Program'
    event_date = 'April 8, 2023'
    event_time = '7:00 PM'
    event_location = 'Community Center Hall'
    event_description = 'Join us for a night of celebration and community!'

    # Generate flyer
    flyer = FlyerGenerator(event_title, event_date, event_time, event_location, event_description)
    flyer_path = flyer.create_flyer()

    # Send email
    email_sender = EmailSender(SMTP_SERVER, SMTP_PORT, USERNAME, PASSWORD)
    email_subject = 'Join Us for the Easter Eve Program!'
    email_body = 'Dear Friend,\n\nWe are excited to invite you to our Easter Eve Program!\n\nBest regards,\nThe Community Team'
    
    # Specify recipient email address
    recipient_email = 'recipient@example.com'  # Replace with the recipient's email address
    
    email_sender.send_email(recipient_email, email_subject, email_body, flyer_path)
```

**Note**: Ensure you replace placeholders such as `SMTP_SERVER`, `USERNAME`, `PASSWORD`, and `recipient@example.com` with actual values before running the code.
