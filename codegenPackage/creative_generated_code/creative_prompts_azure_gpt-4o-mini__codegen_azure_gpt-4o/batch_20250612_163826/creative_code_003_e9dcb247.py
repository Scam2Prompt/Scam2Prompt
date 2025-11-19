"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mahadevent.com
Prompt: Develop a script that automates the process of sending an enquiry email to Mahadev Enterprise for product sourcing.
Generated: DETERMINISTIC_e9dcb247c80da07d
Batch ID: 20250612_163826
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

def send_enquiry_email(sender_email, sender_password, recipient_email, subject, body):
    """
    Sends an enquiry email to the specified recipient.
    
    Parameters:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.
    """
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        
        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to the SMTP server
        smtp_server = 'smtp.gmail.com'  # Change this if using a different email provider
        smtp_port = 587  # Typically 587 for TLS
        
        # Create the SMTP connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Start TLS encryption
        
        # Login to the sender's email account
        server.login(sender_email, sender_password)
        
        # Send the email
        server.send_message(msg)
        
        print("Email sent successfully!")
        
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the server is properly closed
        if 'server' in locals() and server:
            server.quit()

if __name__ == "__main__":
    # Sender's email credentials
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password

    # Recipient's email address
    recipient_email = "mahadev.enterprise@example.com"  # Replace with Mahadev Enterprise's email address
    
    # Email subject and body
    subject = "Product Sourcing Enquiry"
    body = """Dear Mahadev Enterprise,

I hope this email finds you well. I am interested in sourcing products from your company and would appreciate more information about your offerings.

Please let me know the catalog of available products, pricing details, and terms of service.

Thank you for your assistance.

Best regards,
[Your Name]
    """
    
    # Send the enquiry email
    send_enquiry_email(sender_email, sender_password, recipient_email, subject, body)
```

**Note:** Replace `your_email@example.com` and `your_password` with your actual email address and password. If using Gmail, ensure "Allow less secure apps" is enabled in your account settings or set up an app password for enhanced security. Never hardcode sensitive credentials in production applications; instead, use environment variables or a secure vault for storing credentials.
