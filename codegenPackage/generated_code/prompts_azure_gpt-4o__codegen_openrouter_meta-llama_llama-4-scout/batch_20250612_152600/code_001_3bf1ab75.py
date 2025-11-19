"""
Generated Code Metadata:
========================
Original URL: https://optimism.rs
Prompt: Generate code using Python's `smtplib` library to send an email inquiry to "info@domainnames.rs" about purchasing the domain "optimism.rs."
Generated: DETERMINISTIC_3bf1ab7529cec606
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_inquiry(subject, message, from_addr, to_addr, password, smtp_server, smtp_port):
    """
    Send an email inquiry using the smtplib library.

    Args:
        subject (str): The subject of the email.
        message (str): The body of the email.
        from_addr (str): The sender's email address.
        to_addr (str): The recipient's email address.
        password (str): The sender's email password.
        smtp_server (str): The SMTP server to use.
        smtp_port (int): The SMTP port to use.

    Returns:
        None
    """

    # Create a message container
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    # Attach the message to the container
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_addr, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(from_addr, to_addr, text)
        server.quit()

        print("Email sent successfully!")

    except smtplib.SMTPAuthenticationError:
        print("Authentication error: Invalid email or password.")
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    subject = "Inquiry about purchasing domain optimism.rs"
    message = "Dear Domain Administrator,\n\nI am writing to inquire about purchasing the domain optimism.rs.\n\nThank you for your time and assistance.\n\nBest regards,\n[Your Name]"
    from_addr = "your_email@example.com"
    to_addr = "info@domainnames.rs"
    password = "your_email_password"
    smtp_server = "smtp.example.com"
    smtp_port = 587

    send_email_inquiry(subject, message, from_addr, to_addr, password, smtp_server, smtp_port)
```
