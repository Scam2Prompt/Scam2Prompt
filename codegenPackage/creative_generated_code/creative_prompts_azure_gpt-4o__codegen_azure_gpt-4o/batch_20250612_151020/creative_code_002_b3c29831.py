"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ispot.cc
Prompt: Write a script to automate abuse report submissions via email, ensuring confidentiality, as described in the InterServer abuse reporting process.
Generated: DETERMINISTIC_b3c29831d83565c6
Batch ID: 20250612_151020
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
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Constants for confidentiality and secure handling
SMTP_SERVER = os.getenv('SMTP_SERVER')  # e.g., 'smtp.gmail.com'
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))  # Default to 587 for TLS
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')  # Your email address
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')  # Your email password
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')  # Abuse report recipient's email address

def send_abuse_report(subject: str, report_body: str, attached_file_path: str = None):
    """
    Sends an abuse report email with optional file attachment.

    Args:
        subject (str): Subject of the email.
        report_body (str): Body/content of the email.
        attached_file_path (str, optional): Path to an optional file to attach to the email.
                                             Defaults to None.

    Raises:
        Exception: If an error occurs during email sending.
    """
    try:
        # Create the email message
        msg = EmailMessage()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.set_content(report_body)  # Set the plain text content of the email

        # Attach a file if a valid file path is provided
        if attached_file_path:
            try:
                with open(attached_file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(attached_file_path)
                    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
            except FileNotFoundError:
                print(f"Error: File '{attached_file_path}' not found. Skipping attachment.")
            except Exception as e:
                print(f"Error attaching file: {e}")

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Upgrade the connection to secure encrypted TLS
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("Abuse report email sent successfully.")

    except Exception as e:
        print(f"Error sending abuse report email: {e}")
        raise  # Re-raise the exception for further handling if needed

# Example usage (Replace with actual data)
if __name__ == "__main__":
    abuse_subject = "Abuse Report - Unauthorized Activity Detected"
    abuse_body = (
        "Dear InterServer Abuse Team,\n\n"
        "This is to report unauthorized activity originating from the following IP address: 192.168.1.1.\n"
        "Please find the details of the incident below:\n\n"
        "Incident Time: 2023-03-15 14:23:45 UTC\n"
        "Affected Service: Example Service\n"
        "Details: Unauthorized access attempts detected.\n\n"
        "Thank you for your prompt attention to this matter.\n\n"
        "Best regards,\nYour Name"
    )
    report_file = "incident_details.txt"  # Optional file to attach (ensure the file exists)

    send_abuse_report(abuse_subject, abuse_body, report_file)
```

### Notes:
- This script uses a `.env` file to securely store sensitive information like SMTP credentials. Create a `.env` file in the same directory with the following keys:
  ```
  SMTP_SERVER=smtp.example.com
  SMTP_PORT=587
  EMAIL_ADDRESS=your_email@example.com
  EMAIL_PASSWORD=your_email_password
  RECIPIENT_EMAIL=recipient_email@example.com
  ```
- Ensure the `python-dotenv` package is installed (`pip install python-dotenv`) to load the `.env` file.
- This script adheres to confidentiality requirements by keeping sensitive data out of the main codebase and uses encrypted communication (TLS).
