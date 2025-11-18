"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cometrecords.co.uk
Prompt: Create a script to automate the submission of demo tracks to Comet Records via their email (demo@cometrecord.co.uk), ensuring proper formatting and metadata inclusion.
Generated: DETERMINISTIC_8d910bb38e9cee05
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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

# Configuration
SMTP_SERVER = "smtp.gmail.com"  # Replace with the appropriate SMTP server
SMTP_PORT = 587                 # SMTP port (587 for TLS)
EMAIL_ADDRESS = "your_email@gmail.com"  # Replace with your email address
EMAIL_PASSWORD = "your_email_password"  # Replace with your email password
RECEIVER_EMAIL = "demo@cometrecord.co.uk"  # Comet Records' email
SUBJECT = "Demo Track Submission"
TRACK_FILE_PATH = "path/to/your/demo_track.mp3"
ARTIST_NAME = "Your Artist Name"
TRACK_TITLE = "Your Track Title"
GENRE = "Your Genre"

def send_demo_email():
    try:
        # Check if the track file exists
        if not os.path.exists(TRACK_FILE_PATH):
            raise FileNotFoundError(f"Demo track file not found: {TRACK_FILE_PATH}")
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = SUBJECT
        
        # Email body with metadata
        body = f"""
        Hi Comet Records Team,

        Please find attached my demo track submission.

        Artist Name: {ARTIST_NAME}
        Track Title: {TRACK_TITLE}
        Genre: {GENRE}

        I look forward to hearing back from you.

        Best regards,
        {ARTIST_NAME}
        """
        msg.attach(MIMEText(body, 'plain'))

        # Attach the demo track file
        with open(TRACK_FILE_PATH, "rb") as track_file:
            track_attachment = MIMEBase('application', 'octet-stream')
            track_attachment.set_payload(track_file.read())
            encoders.encode_base64(track_attachment)
            track_attachment.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(TRACK_FILE_PATH)}"')
            msg.attach(track_attachment)

        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable TLS encryption
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the SMTP server
        server.send_message(msg)  # Send the email
        server.quit()  # Close the connection

        print("Demo track successfully submitted to Comet Records.")
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except smtplib.SMTPException as e:
        print(f"SMTP Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    send_demo_email()
```

This script handles authentication, email formatting, metadata inclusion, and attaches the demo track file. Remember to replace placeholders (`your_email@gmail.com`, `your_email_password`, and `path/to/your/demo_track.mp3`) with your actual data.
