"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://8147f917.carbon-app-csq.pages.dev
Prompt: Generate a script to send email login codes for authentication in a Cloudflare Access environment.
Generated: DETERMINISTIC_28801ae21eec267b
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Constants for email settings
SMTP_SERVER = 'smtp.your-email-provider.com'  # Replace with your SMTP server
SMTP_PORT = 587  # Common SMTP port
USERNAME = 'your-email@example.com'  # Your email address
PASSWORD = 'your-email-password'  # Your email password

def generate_login_code(length=6):
    """Generate a random numeric login code of specified length."""
    return ''.join(random.choices(string.digits, k=length))

def send_email(recipient_email, login_code):
    """Send an email containing the login code to the specified recipient."""
    try:
        # Create the email content
        subject = "Your Login Code"
        body = f"Your login code is: {login_code}"

        # Set up the email
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted TLS/SSL connection
            server.login(USERNAME, PASSWORD)
            server.send_message(msg)

        print("Email sent successfully.")
    except smtplib.SMTPException as e:
        # Handle SMTP errors
        print(f"Failed to send email: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {e}")

def main():
    """Main function to execute the email sending process."""
    recipient_email = input("Enter the recipient's email address: ")
    
    # Generate a login code
    login_code = generate_login_code()

    # Send the email with the login code
    send_email(recipient_email, login_code)

if __name__ == "__main__":
    main()
```
