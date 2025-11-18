"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase-support-number-pro.blogspot.com
Prompt: Write a Python script to send an email to support@coinbase.com with a predefined message template for reporting a hacked account issue.
Generated: DETERMINISTIC_da4b6fa2386a5f05
Batch ID: 20250612_154131
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

def send_hacked_account_email(sender_email, sender_password):
    """
    Sends an email to support@coinbase.com to report a hacked account issue.
    
    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
    """
    # Coinbase support email
    recipient_email = "support@coinbase.com"
    
    # Email subject
    subject = "URGENT: Hacked Account Report Issue"
    
    # Predefined message template
    message_body = """
    Dear Coinbase Support Team,

    This is to report a hacked account issue. My account appears to have been compromised, and I am unable to regain access.
    Please assist me in resolving this issue as soon as possible.

    Relevant details:
    - Name: [Your Name]
    - Registered Email: [Your Registered Email Address]
    - Date of Incident: [Approximate Date]

    Please let me know if you need further information to assist me.

    Regards,
    [Your Name]
    """
    
    try:
        # Create email container
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        
        # Attach the body content to the email
        message.attach(MIMEText(message_body, "plain"))
        
        # Connect to the SMTP server (Example: Gmail SMTP server)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        
        # Establish connection to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        
        # Log in to the SMTP server
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        
        print("Email sent successfully.")

    except smtplib.SMTPException as e:
        # Handle SMTP-related errors
        print(f"Failed to send email: {e}")
    
    except Exception as e:
        # Handle other general errors
        print(f"An error occurred: {e}")
    
    finally:
        # Ensure the server is properly closed
        try:
            server.quit()
        except NameError:
            pass  # The server object may not have been initialized if an error occurred earlier


# Example usage
if __name__ == "__main__":
    # Replace with your email credentials
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"
    
    send_hacked_account_email(sender_email, sender_password)
```

**Note**: Replace `your_email@example.com` and `your_email_password` with your actual email credentials. If using sensitive credentials, consider storing them in environment variables or a secrets management tool for better security practices.
