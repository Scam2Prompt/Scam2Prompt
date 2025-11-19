"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://datmaui.liveblog365.com
Prompt: Create a tutorial on how to manage multiple email accounts using iFastNet's hosting services.
Generated: DETERMINISTIC_0edee7da80969946
Batch ID: 20250612_161044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Managing multiple email accounts using iFastNet hosting services typically involves configurations via their cPanel interface. Below is a Python script using IMAP and SMTP protocols to access and manage multiple email accounts programmatically. Note that this script assumes you have already configured the email accounts in your iFastNet hosting cPanel.

```python
import imaplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration for email accounts
EMAIL_ACCOUNTS = [
    {
        "email": "your-email1@example.com",
        "password": "your-password1",
        "imap_server": "mail.example.com",
        "smtp_server": "mail.example.com",
        "smtp_port": 587,
    },
    {
        "email": "your-email2@example.com",
        "password": "your-password2",
        "imap_server": "mail.example.com",
        "smtp_server": "mail.example.com",
        "smtp_port": 587,
    },
]

def check_inbox(email, password, imap_server):
    """
    Connects to the IMAP server and retrieves the list of emails in the inbox.
    """
    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email, password)
        mail.select("inbox")  # Select the inbox

        # Search for all emails
        result, data = mail.search(None, "ALL")
        if result != "OK":
            print(f"Failed to retrieve emails for {email}")
            return

        email_ids = data[0].split()
        print(f"{email}: {len(email_ids)} emails found.")

        # Fetch the subject of the latest email
        for email_id in email_ids[-5:]:  # Fetch the last 5 emails
            result, msg_data = mail.fetch(email_id, "(RFC822)")
            if result != "OK":
                print(f"Failed to fetch email ID {email_id}")
                continue

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    print(f"Email content: {response_part[1].decode('utf-8')}")

        # Logout
        mail.logout()
    except Exception as e:
        print(f"Error while accessing inbox for {email}: {str(e)}")


def send_email(email, password, smtp_server, smtp_port, recipient, subject, body):
    """
    Sends an email using the SMTP server.
    """
    try:
        # Create SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email, password)

        # Create the email
        msg = MIMEMultipart()
        msg["From"] = email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Send the email
        server.sendmail(email, recipient, msg.as_string())
        print(f"Email sent successfully from {email} to {recipient}")

        # Close the connection
        server.quit()
    except Exception as e:
        print(f"Error while sending email from {email}: {str(e)}")


def manage_emails():
    """
    Manages multiple email accounts by checking inbox and sending emails.
    """
    for account in EMAIL_ACCOUNTS:
        print(f"Managing account: {account['email']}")
        
        # Check inbox
        check_inbox(
            email=account["email"],
            password=account["password"],
            imap_server=account["imap_server"]
        )
        
        # Send a test email (optional)
        recipient = "recipient@example.com"
        subject = "Test Email"
        body = f"Hello, this is a test email from {account['email']}"
        
        send_email(
            email=account["email"],
            password=account["password"],
            smtp_server=account["smtp_server"],
            smtp_port=account["smtp_port"],
            recipient=recipient,
            subject=subject,
            body=body
        )


if __name__ == "__main__":
    # Run the email management script
    manage_emails()
```

### Prerequisites:
1. Replace placeholder values like `your-email1@example.com`, `your-password1`, and `mail.example.com` with your actual credentials and email servers provided by iFastNet.
2. Ensure your email accounts are configured with IMAP and SMTP access enabled.
3. Install Python dependencies if necessary (`pip install secure-smtplib`).

### Disclaimer:
Keep sensitive credentials like email passwords secure and avoid hardcoding them. Use environment variables or secret management tools for production scenarios.
