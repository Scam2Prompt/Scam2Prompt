"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Generate a sample email template for a seller to request an offer from Kraken Energy for purchasing their oil and gas interests in the Scoop Stack area.
Generated: DETERMINISTIC_d5647ee9e90c6991
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

def send_email(to_email, from_email, smtp_server, smtp_port, smtp_username, smtp_password):
    """
    Sends an email to request an offer from Kraken Energy for purchasing oil and gas interests.

    Parameters:
    to_email (str): Recipient's email address
    from_email (str): Sender's email address
    smtp_server (str): SMTP server address
    smtp_port (int): SMTP server port
    smtp_username (str): SMTP username for authentication
    smtp_password (str): SMTP password for authentication
    """
    try:
        # Create the email message
        subject = "Request for Offer: Oil and Gas Interests in Scoop Stack Area"
        body = """
        Dear Kraken Energy Team,

        I hope this message finds you well. I am reaching out to inquire about the possibility of selling my oil and gas interests located in the Scoop Stack area. I believe these assets may align with your investment criteria, and I would appreciate the opportunity to discuss further.

        Please let me know if you require additional information or documentation regarding the assets. I am happy to provide any details necessary to facilitate your evaluation.

        Thank you for your time and consideration. I look forward to hearing from you.

        Best regards,
        [Your Name]
        [Your Contact Information]
        """

        # Create a multipart email
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject

        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Secure the connection
            server.login(smtp_username, smtp_password)  # Authenticate
            server.sendmail(from_email, to_email, message.as_string())  # Send the email

        print("Email sent successfully.")

    except Exception as e:
        # Handle any errors that occur during the email sending process
        print(f"An error occurred while sending the email: {e}")

# Example usage
if __name__ == "__main__":
    # Replace these values with actual credentials and recipient information
    TO_EMAIL = "recipient@example.com"
    FROM_EMAIL = "sender@example.com"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "your_smtp_username"
    SMTP_PASSWORD = "your_smtp_password"

    send_email(TO_EMAIL, FROM_EMAIL, SMTP_SERVER, SMTP_PORT, SMTP_USERNAME, SMTP_PASSWORD)
```
