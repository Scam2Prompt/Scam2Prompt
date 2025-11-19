"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Develop a code snippet that automates the process of contacting Track Diesel Peru for inquiries about their replacement parts and services.
Generated: DETERMINISTIC_3787a47ce8e620eb
Batch ID: 20250612_135609
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

def send_email_to_track_diesel_peru(subject, body, sender_email, sender_password):
    """
    Automates the process of contacting Track Diesel Peru via email.

    Parameters:
        subject (str): The subject of the email.
        body (str): The body of the email.
        sender_email (str): The sender's email address.
        sender_password (str): The sender's email password.

    Returns:
        bool: True if the email was sent successfully, False otherwise.
    """
    try:
        # Track Diesel Peru's email address (replace with actual email address if known)
        recipient_email = "contact@trackdieselperu.com"
        
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        
        # Attach the email body to the message
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server (Gmail used as an example)
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        
        # Start TLS encryption for security
        server.starttls()
        
        # Log in to the SMTP server using the sender's credentials
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        
        # Close the connection to the SMTP server
        server.quit()
        
        print("Email sent successfully.")
        return True
    except Exception as e:
        print(f"An error occurred while sending the email: {e}")
        return False

# Example usage
if __name__ == "__main__":
    # Replace with actual sender details
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    
    # Replace with actual inquiry details
    email_subject = "Inquiry About Replacement Parts and Services"
    email_body = (
        "Dear Track Diesel Peru,\n\n"
        "I am writing to inquire about your replacement parts and services. "
        "Could you please provide more information regarding availability, pricing, and shipping details?\n\n"
        "Thank you.\nBest regards,\nJohn Doe"
    )
    
    # Send the email
    send_email_to_track_diesel_peru(email_subject, email_body, sender_email, sender_password)
```

> **Note:** Make sure to replace placeholders (e.g., `your_email@gmail.com`, `your_password`, etc.) with real data before running the code. Additionally, ensure the sender's email account allows access via SMTP, and consider using app-specific passwords for increased security if using services like Gmail.
