"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlwallcone.blogspot.com
Prompt: Create a code snippet that sends an email notification to customers about new products at Alyne Distribuidora using their contact information.
Generated: DETERMINISTIC_f080c529cbcbda5d
Batch ID: 20250612_164058
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

def send_email_notification(to_email, subject, body):
    """
    Sends an email notification.

    Parameters:
    to_email (str): Recipient's email address.
    subject (str): Subject of the email.
    body (str): Body content of the email.

    Returns:
    None
    """
    # SMTP server configuration
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password (consider using environment variables instead)

    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Establish connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Enable TLS encryption
            server.login(sender_email, sender_password)  # Login to the sender's email account
            server.send_message(msg)  # Send the email
            print(f"Email successfully sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

# Example usage
if __name__ == "__main__":
    # Customer email and message details
    customer_email = "customer_email@example.com"
    email_subject = "New Products at Alyne Distribuidora"
    email_body = (
        "Hello,\n\n"
        "We are excited to announce that new products have arrived at Alyne Distribuidora! "
        "Check them out on our website.\n\n"
        "Best regards,\n"
        "Alyne Distribuidora Team"
    )
    
    # Send email notification
    send_email_notification(customer_email, email_subject, email_body)
```

**Note:**  
- Replace `your_email@example.com` and `your_password` with your actual email credentials.  
- For production use, consider using environment variables or secure methods to store sensitive information like email credentials.
