"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esperai.com
Prompt: Can you provide a sample email template for inquiring about the domain for sale on esperai.com?
Generated: DETERMINISTIC_71094cfc77dbbb91
Batch ID: 20250612_162701
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

def send_domain_inquiry(email_sender, email_receiver, email_subject, domain_name):
    """
    Sends an email inquiry about a domain for sale.

    Args:
        email_sender (str): The sender's email address.
        email_receiver (str): The receiver's email address.
        email_subject (str): The subject line of the email.
        domain_name (str): The domain name inquiring about.

    Returns:
        None
    """
    # Create the email content
    email_body = f"""
    Hello,

    I hope this message finds you well. 

    I am writing to inquire about the availability of the domain "{domain_name}" listed on esperai.com.
    Could you please provide me with more information regarding its sale?

    Thank you for your time. 
    I look forward to your response.

    Best regards,
    [Your Name]
    [Your Contact Information]
    """

    # Create a multipart email message
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = email_subject

    # Attach the email body to the message
    msg.attach(MIMEText(email_body, 'plain'))

    # Send the email using SMTP
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with actual SMTP server
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(email_sender, 'your_password')  # Replace with the sender's email password
            server.send_message(msg)  # Send the email message
            print("Email sent successfully.")
    except smtplib.SMTPException as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == '__main__':
    send_domain_inquiry(
        email_sender='your_email@example.com',  # Replace with the sender's email
        email_receiver='info@esperai.com',      # Replace with the receiver's email
        email_subject='Inquiry about Domain for Sale',
        domain_name='example.com'                # Replace with the desired domain name
    )
```
