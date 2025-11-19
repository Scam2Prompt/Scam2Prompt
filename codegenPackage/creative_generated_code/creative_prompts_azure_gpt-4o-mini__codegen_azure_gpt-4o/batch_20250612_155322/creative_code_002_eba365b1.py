"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://financialrecoverysolutions.co.uk
Prompt: Generate a code snippet that sends an email notification to clients when their PPI claim status changes, inspired by the customer service practices of Financial Recovery Solutions Ltd.
Generated: DETERMINISTIC_eba365b105825f19
Batch ID: 20250612_155322
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

# Function to send email notification
def send_email_notification(client_email, client_name, claim_status):
    """
    Sends an email notification to the client when their PPI claim status changes.
    
    :param client_email: str - The email address of the client
    :param client_name: str - The name of the client
    :param claim_status: str - The updated status of the PPI claim
    """
    try:
        # Email server configuration
        smtp_server = "smtp.example.com"  # Replace with your SMTP server
        smtp_port = 587  # Common port for SMTP (TLS)
        sender_email = "your_email@example.com"  # Replace with your sender email
        sender_password = "your_password"  # Replace with your email password
        
        # Email content
        subject = "Update on Your PPI Claim Status"
        body = f"""
        Dear {client_name},

        We wanted to inform you that the status of your PPI claim has been updated to: {claim_status}.

        If you have any questions or need further assistance, please don't hesitate to contact us.

        Best regards,
        Financial Recovery Solutions Ltd
        """

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = client_email
        message["Subject"] = subject

        # Attach the email body
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted one
            server.login(sender_email, sender_password)  # Login to the SMTP server
            server.send_message(message)  # Send the email

        print(f"Email successfully sent to {client_email}")

    except smtplib.SMTPException as e:
        # Handle SMTP-specific errors
        print(f"Failed to send email: {e}")
    except Exception as e:
        # Handle general errors
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual client data
    client_email = "client_email@example.com"
    client_name = "John Doe"
    claim_status = "Approved"

    send_email_notification(client_email, client_name, claim_status)
```
