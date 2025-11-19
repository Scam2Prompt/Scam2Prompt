"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tpcontact.co.za
Prompt: Write a code snippet that sends an email to Move Up for UK visa inquiries, using the contact information provided on the TelePerformance website.
Generated: DETERMINISTIC_079819d17e047faf
Batch ID: 20250612_155137
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

def send_email(to_email, subject, body, smtp_server, smtp_port, sender_email, sender_password):
    """
    Sends an email using the specified SMTP server.

    Parameters:
    to_email (str): The recipient's email address.
    subject (str): The subject of the email.
    body (str): The body of the email.
    smtp_server (str): The SMTP server address.
    smtp_port (int): The SMTP server port number.
    sender_email (str): The sender's email address.
    sender_password (str): The sender's email password.

    Returns:
    None
    """
    try:
        # Create a MIME Multipart message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = to_email
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.send_message(message)  # Send the email
            
        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")

# Example usage:
if __name__ == "__main__":
    # Replace these values with actual data
    to_email = "ukvisa.moveup@teleperformance.com"  # Example contact email from TelePerformance
    subject = "Inquiry Regarding UK Visa"
    body = "Dear Move Up Team,\n\nI would like to inquire about the UK visa application process.\n\nBest regards,\nYour Name"
    smtp_server = "smtp.gmail.com"  # Example SMTP server
    smtp_port = 587  # Typical SMTP port for TLS
    sender_email = "your_email@gmail.com"  # Replace with your email address
    sender_password = "your_email_password"  # Replace with your email password

    send_email(to_email, subject, body, smtp_server, smtp_port, sender_email, sender_password)
```

**Note:** Ensure that you replace placeholders such as `your_email@gmail.com` and `your_email_password` with actual credentials. Use environment variables or secure methods to store sensitive information like passwords instead of hardcoding them directly in production code.
