"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploys.work
Prompt: Generate a sample code snippet for sending login codes via email using deploys.work.
Generated: DETERMINISTIC_9dc5d7e0b450be5d
Batch ID: 20250612_161323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
from email.message import EmailMessage
import uuid
import os

# Configuration for Deploys.work API
DEPLOYS_WORK_API_KEY = os.getenv("DEPLOYS_WORK_API_KEY")  # Load API key from environment variables
DEPLOYS_WORK_SENDER_EMAIL = os.getenv("DEPLOYS_WORK_SENDER_EMAIL")  # Email sender address from environment variables
DEPLOYS_WORK_SMTP_SERVER = "smtp.deploys.work"  # Deploys.work SMTP server
DEPLOYS_WORK_SMTP_PORT = 587  # Deploys.work SMTP port

def generate_login_code():
    """
    Generates a unique 6-digit login code.
    """
    return str(uuid.uuid4().int)[:6]  # Extract the first 6 digits from a UUID


def send_login_code_via_email(recipient_email):
    """
    Sends a login code to the provided email address using the Deploys.work service.

    Args:
        recipient_email (str): The recipient's email address.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Generate a login code
        login_code = generate_login_code()

        # Create an email message
        email = EmailMessage()
        email["From"] = DEPLOYS_WORK_SENDER_EMAIL
        email["To"] = recipient_email
        email["Subject"] = "Your Login Code"
        email.set_content(f"Your login code is: {login_code}")

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(DEPLOYS_WORK_SMTP_SERVER, DEPLOYS_WORK_SMTP_PORT) as server:
            server.starttls()  # Start TLS encryption
            server.login(DEPLOYS_WORK_SENDER_EMAIL, DEPLOYS_WORK_API_KEY)  # Log in to Deploys.work SMTP server
            server.send_message(email)  # Send the email

        print(f"Login code sent successfully to {recipient_email}")
        return True

    except Exception as e:
        # Log the error (for production, use proper logging instead of print)
        print(f"Failed to send login code: {e}")
        return False


# Sample usage:
if __name__ == "__main__":
    recipient = input("Enter the recipient's email address: ")
    if send_login_code_via_email(recipient):
        print("Email sent successfully.")
    else:
        print("Failed to send the email.")
```

**Note:** Replace `DEPLOYS_WORK_API_KEY` and `DEPLOYS_WORK_SENDER_EMAIL` with actual environment variable values or secrets for your production environment.
