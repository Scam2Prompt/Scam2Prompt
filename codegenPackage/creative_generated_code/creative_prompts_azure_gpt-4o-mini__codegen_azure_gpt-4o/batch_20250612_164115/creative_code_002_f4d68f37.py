"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://haus-alpenrose.com
Prompt: Create a script that sends a newsletter subscription request to Haus Alpenrose's email service, ensuring error handling for server issues.
Generated: DETERMINISTIC_f4d68f376a519ea9
Batch ID: 20250612_164115
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
import sys

def send_subscription_request(sender_email, receiver_email, sender_name, smtp_server, smtp_port, smtp_user, smtp_password):
    """
    Sends a newsletter subscription request email to Haus Alpenrose's email service.
    
    Parameters:
        sender_email (str): The email address of the sender.
        receiver_email (str): The email address to send the subscription request to.
        sender_name (str): The name of the person subscribing.
        smtp_server (str): SMTP server address.
        smtp_port (int): SMTP server port.
        smtp_user (str): SMTP username.
        smtp_password (str): SMTP password.
    """
    try:
        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Newsletter Subscription Request"

        # Body of the email
        body = f"Hello,\n\nPlease add me, {sender_name}, to your newsletter subscription list.\n\nThank you!"
        message.attach(MIMEText(body, "plain"))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(smtp_user, smtp_password)  # Authenticate with the server
            
            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Subscription request email sent successfully.")

    except smtplib.SMTPException as smtp_err:
        print(f"SMTP error occurred: {smtp_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Replace these with actual values
        sender_email = "example_sender@gmail.com"
        receiver_email = "info@hausalpenrose.com"
        sender_name = "John Doe"
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        smtp_user = "example_sender@gmail.com"
        smtp_password = "yourpassword"

        send_subscription_request(sender_email, receiver_email, sender_name, smtp_server, smtp_port, smtp_user, smtp_password)
    except KeyboardInterrupt:
        print("\nScript interrupted by user.")
        sys.exit(1)
```
