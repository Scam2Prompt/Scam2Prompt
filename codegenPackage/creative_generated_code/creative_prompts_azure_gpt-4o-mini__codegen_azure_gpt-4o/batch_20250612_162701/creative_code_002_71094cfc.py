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
# Python script to generate and send an email inquiry about the domain "esperai.com" being for sale
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email):
    """
    Send an email inquiry about the domain "esperai.com" being for sale.

    Parameters:
    sender_email (str): The email address of the sender.
    sender_password (str): The password for the sender's email account.
    recipient_email (str): The email address of the recipient (domain owner or broker).
    """
    try:
        # Create the email subject and body
        subject = "Inquiry About Domain Sale: esperai.com"
        body = """
        Dear Sir/Madam,

        I am writing to inquire about the availability of the domain "esperai.com" for purchase.
        If the domain is for sale, please provide the asking price and any additional details 
        regarding the transfer process.

        Thank you for your time and assistance. I look forward to your reply.

        Best regards,
        [Your Name]
        [Your Contact Information]
        """

        # Create the email headers
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        # Attach the email body to the message
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Secure the connection using TLS
            server.login(sender_email, sender_password)  # Log in to the email server
            server.sendmail(sender_email, recipient_email, message.as_string())  # Send the email

        print("Email sent successfully.")

    except Exception as e:
        # Handle any errors that occur during the email sending process
        print(f"An error occurred while sending the email: {e}")

# Example usage of the function
if __name__ == "__main__":
    sender_email = "your_email@example.com"  # Replace with your email address
    sender_password = "your_password"  # Replace with your email password
    recipient_email = "domain_owner@example.com"  # Replace with the recipient's email address

    send_email(sender_email, sender_password, recipient_email)
```

Note: Replace `your_email@example.com`, `your_password`, and `domain_owner@example.com` with actual values before running this script. Ensure secure handling of credentials (e.g., use environment variables or a secure credential manager).
