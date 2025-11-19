"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Develop a code snippet that automates the process of sending inquiries to Trendsetterzs, highlighting their commitment to ethical and sustainable sourcing in the fashion industry.
Generated: DETERMINISTIC_f27eace4f278a2f9
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the requested code snippet:

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_inquiry(sender_email, sender_password, recipient_email, subject, message_body):
    """
    Automates sending an inquiry email to Trendsetterzs regarding their commitment 
    to ethical and sustainable sourcing in the fashion industry.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The email address of the recipient (Trendsetterzs).
        subject (str): The subject of the email.
        message_body (str): The body content of the email.

    Returns:
        None
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(message_body, "plain"))
        
        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the sender's email account
            
            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
        
        print("Inquiry email successfully sent.")

    except smtplib.SMTPAuthenticationError:
        print("Error: Failed to authenticate with the SMTP server. Please check your email credentials.")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"        # Replace with your email password
    recipient_email = "contact@trendsetterzs.com"  # Replace with Trendsetterzs contact email
    subject = "Inquiry About Ethical and Sustainable Sourcing"
    message_body = (
        "Dear Trendsetterzs Team,\n\n"
        "I hope this message finds you well. I am reaching out to inquire about your commitment to ethical "
        "and sustainable sourcing in the fashion industry. Could you provide more details about the practices "
        "and measures you have in place to ensure this?\n\n"
        "Looking forward to your response.\n\n"
        "Best regards,\n"
        "[Your Name]"
    )

    send_inquiry(sender_email, sender_password, recipient_email, subject, message_body)
```

This code snippet automates sending an inquiry email using Python's `smtplib` library. Replace the placeholder values (`your_email@example.com`, `your_password`, etc.) with actual values to execute the program.
