"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardedcoin.com
Prompt: Create a script to automate the process of sending transaction screenshots and payment details via email for Guarded Ethereum ©️ cash-out services.
Generated: DETERMINISTIC_a8fc2866ff05a0fd
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Configuration
SMTP_SERVER = "smtp.gmail.com"  # Change to your SMTP server
SMTP_PORT = 587  # Common port for SMTP servers
EMAIL_ADDRESS = "your_email@example.com"  # Sender's email address
EMAIL_PASSWORD = "your_password"  # Sender's email password
RECIPIENT_EMAIL = "recipient_email@example.com"  # Recipient's email address
TRANSACTION_SCREENSHOT_PATH = "path/to/screenshot.png"  # Path to transaction screenshot
PAYMENT_DETAILS = {
    "Transaction_ID": "123456789",
    "Amount": "0.5 ETH",
    "Recipient_Address": "0xRecipientEthereumAddress",
}  # Update with real payment details

def send_email():
    try:
        # Initialize the SMTP server connection
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure the SMTP connection
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Login to the sender's email account

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = "Guarded Ethereum Cash-Out Transaction Details"

        # Create the body of the email
        email_body = f"""\
        Hello,

        Please find the transaction details below:
        Transaction ID: {PAYMENT_DETAILS['Transaction_ID']}
        Amount: {PAYMENT_DETAILS['Amount']}
        Recipient Address: {PAYMENT_DETAILS['Recipient_Address']}

        Attached is the screenshot of the transaction for your reference.

        Regards,
        Guarded Ethereum Cash-Out Service
        """
        msg.attach(MIMEText(email_body, 'plain'))

        # Attach the transaction screenshot
        if os.path.exists(TRANSACTION_SCREENSHOT_PATH):
            with open(TRANSACTION_SCREENSHOT_PATH, "rb") as attachment:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(TRANSACTION_SCREENSHOT_PATH)}"
                )
                msg.attach(part)
        else:
            print(f"Error: Screenshot file not found at {TRANSACTION_SCREENSHOT_PATH}")
            return

        # Send the email
        server.send_message(msg)
        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always close the server connection
        server.quit()

if __name__ == "__main__":
    send_email()
```

**Note:** Replace placeholders like `your_email@example.com`, `your_password`, and file paths with actual values. Use environment variables or a secure vault for credentials.
