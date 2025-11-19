"""
Generated Code Metadata:
========================
Original URL: https://immediatepeak.com
Prompt: Generate a sample email template for a user to send to an investment education firm after being matched through Immediate Peak.
Generated: DETERMINISTIC_b86c05cf776b636f
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that generates an email template for the requested scenario:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def generate_investment_email(
    recipient_name: str,
    firm_name: str,
    sender_name: str,
    sender_email: str,
    sender_phone: str
) -> str:
    """
    Generates a professional email template for contacting an investment education firm.
    
    Args:
        recipient_name (str): Name of the recipient at the firm
        firm_name (str): Name of the investment education firm
        sender_name (str): Name of the person sending the email
        sender_email (str): Email of the sender
        sender_phone (str): Phone number of the sender
        
    Returns:
        str: Formatted email body text
    """
    
    email_template = f"""
Dear {recipient_name},

I hope this message finds you well. My name is {sender_name}, and I was recently matched with {firm_name} 
through Immediate Peak as I'm looking to enhance my investment knowledge and skills.

I'm particularly interested in learning more about your educational offerings and how they might 
help me achieve my financial goals. Would it be possible to schedule a call or receive more 
information about your programs?

A little about my background:
- Currently exploring investment opportunities
- Eager to build a solid foundation in financial markets
- Looking for structured education to make informed decisions

Please feel free to contact me at your earliest convenience:
- Email: {sender_email}
- Phone: {sender_phone}

I'm looking forward to hearing from you and potentially beginning this educational journey with {firm_name}.

Best regards,
{sender_name}
"""
    return email_template.strip()


def send_email(
    sender_email: str,
    sender_password: str,
    recipient_email: str,
    subject: str,
    body: str,
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587
) -> None:
    """
    Sends an email using SMTP protocol.
    
    Args:
        sender_email (str): Email address of the sender
        sender_password (str): Password for the sender's email account
        recipient_email (str): Email address of the recipient
        subject (str): Subject line of the email
        body (str): Body content of the email
        smtp_server (str): SMTP server address
        smtp_port (int): SMTP port number
        
    Raises:
        smtplib.SMTPException: If there's an error during email sending
    """
    try:
        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Add body to email
        msg.attach(MIMEText(body, 'plain'))
        
        # Create SMTP session
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            
        print("Email sent successfully!")
    except Exception as e:
        raise smtplib.SMTPException(f"Failed to send email: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Generate email content
    email_body = generate_investment_email(
        recipient_name="John Smith",
        firm_name="Wealth Education Partners",
        sender_name="Jane Doe",
        sender_email="jane.doe@example.com",
        sender_phone="(555) 123-4567"
    )
    
    print("Generated Email Template:")
    print(email_body)
    
    # Uncomment to actually send the email
    # send_email(
    #     sender_email="your_email@gmail.com",
    #     sender_password="your_password",
    #     recipient_email="recipient@example.com",
    #     subject="Investment Education Inquiry - Matched via Immediate Peak",
    #     body=email_body
    # )
```
