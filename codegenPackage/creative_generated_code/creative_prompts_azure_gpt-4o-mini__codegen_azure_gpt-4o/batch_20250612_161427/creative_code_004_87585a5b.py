"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniapt.space
Prompt: How do I contact the server administrator for a 500 Internal Server Error issue, as mentioned for uniapt.space?
Generated: DETERMINISTIC_87585a5bc631e4a2
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to generate a contact message for the server administrator in case of a 500 Internal Server Error.
This script prompts the user for details related to the error and formats an email to the administrator.
"""

import smtplib
from email.message import EmailMessage

# Configuration for sending the email
SMTP_SERVER = "smtp.example.com"  # Replace with your SMTP server
SMTP_PORT = 587  # Common SMTP port
SMTP_USERNAME = "your_email@example.com"  # Replace with your email username
SMTP_PASSWORD = "your_password"  # Replace with your email password
ADMIN_EMAIL = "admin@uniapt.space"  # Replace with the administrator's email

def send_error_email(user_email, error_details):
    """
    Sends an email to the server administrator with details about the error.

    Args:
        user_email (str): The contact email address of the user reporting the error.
        error_details (str): Detailed information about the error encountered.
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg["Subject"] = "500 Internal Server Error Report - uniapt.space"
        msg["From"] = SMTP_USERNAME
        msg["To"] = ADMIN_EMAIL
        msg.set_content(f"""
        Dear Administrator,

        A user has encountered a 500 Internal Server Error on uniapt.space.
        Below are the details provided by the user:

        User Contact Email: {user_email}
        Error Details: {error_details}

        Please look into this issue at the earliest convenience.

        Best Regards,
        Error Reporting System
        """)

        # Establish a connection to the SMTP server
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure encrypted SSL/TLS
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)

        print("Error report email sent successfully.")

    except Exception as e:
        print(f"Failed to send error report email. Error: {e}")

def main():
    """
    Main function to gather user input and send the error report email.
    """
    print("500 Internal Server Error Reporting - uniapt.space")

    # Gather user input
    user_email = input("Please enter your email address: ").strip()
    error_details = input("Please describe the issue you encountered: ").strip()

    # Validate user input
    if not user_email or not error_details:
        print("Both email address and error details are required to send the report.")
        return

    # Send the error email
    send_error_email(user_email, error_details)

if __name__ == "__main__":
    main()
```
