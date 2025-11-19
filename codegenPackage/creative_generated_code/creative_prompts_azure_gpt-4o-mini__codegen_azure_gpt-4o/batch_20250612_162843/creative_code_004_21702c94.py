"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin.forum
Prompt: Implement a contact form submission in Python to inquire about purchasing a single Toncoin domain, using the provided email address.
Generated: DETERMINISTIC_21702c943a2f50e9
Batch ID: 20250612_162843
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

def send_contact_form(domain_name, email_address, inquiry_message):
    """
    Sends a contact form submission via email.
    
    Parameters:
        domain_name (str): The Toncoin domain being inquired about.
        email_address (str): The email address of the person submitting the inquiry.
        inquiry_message (str): The message or details provided by the user.
    
    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    
    # Email server settings
    smtp_server = "smtp.example.com"  # Replace with your SMTP server
    smtp_port = 587                  # Commonly used port for TLS
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"        # Replace with your email password
    
    try:
        # Create the email content
        subject = f"Inquiry about Toncoin Domain: {domain_name}"
        body = f"""
        You have received a new inquiry about purchasing a single Toncoin domain.

        Domain Name: {domain_name}
        Email Address: {email_address}
        
        Inquiry Message:
        {inquiry_message}
        """
        
        # Create a MIME email object
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = sender_email  # Sending to yourself for contact form submissions
        message["Subject"] = subject
        
        # Attach the email body
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)  # Authenticate with the SMTP server
            server.sendmail(sender_email, sender_email, message.as_string())  # Send the email
        
        print("Contact form submitted successfully.")
        return True
    
    except smtplib.SMTPException as e:
        print(f"Failed to send contact form email: {e}")
        return False

# Example usage
if __name__ == "__main__":
    domain_name = "example.ton"
    email_address = "user_email@example.com"
    inquiry_message = "I am interested in purchasing this domain. Please provide more details."
    
    success = send_contact_form(domain_name, email_address, inquiry_message)
    if success:
        print("Email sent successfully.")
    else:
        print("Failed to send email.")
```
