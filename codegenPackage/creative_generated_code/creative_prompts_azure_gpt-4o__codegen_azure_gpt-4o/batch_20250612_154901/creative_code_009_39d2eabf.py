"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hurmanblirrikqmph.firebaseapp.com
Prompt: Provide an example of how to enable email access for a user programmatically, following the steps outlined on hurmanblirrikqmph.firebaseapp.com.
Generated: DETERMINISTIC_39d2eabf6351bf17
Batch ID: 20250612_154901
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

def enable_email_access(user_email, smtp_server, smtp_port, login, password):
    """
    Function to enable email access for a user by sending a test email.

    Parameters:
        user_email (str): The email address of the user to enable email access.
        smtp_server (str): SMTP server address for sending emails.
        smtp_port (int): SMTP server port number.
        login (str): Login email for the SMTP server.
        password (str): Password for the SMTP server login.

    Returns:
        bool: True if email successfully sent, False otherwise.
    """
    try:
        # Create the email content
        subject = "Welcome to Email Access"
        body = "Your email access has been successfully enabled."
        
        # Construct the email message
        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = user_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish connection to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(login, password)  # Login to the server
            server.sendmail(login, user_email, msg.as_string())  # Send the email
        
        print(f"Email successfully sent to {user_email}.")
        return True
    
    except smtplib.SMTPException as e:
        # Handle SMTP-related errors
        print(f"Failed to send email due to SMTP error: {e}")
        return False
    
    except Exception as e:
        # Catch-all for any other exceptions
        print(f"An unexpected error occurred: {e}")
        return False


# Example usage:
if __name__ == "__main__":
    # Replace placeholders with actual values
    USER_EMAIL = "user@example.com"
    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587  # Common port for TLS
    LOGIN_EMAIL = "your-email@example.com"
    LOGIN_PASSWORD = "your-email-password"
    
    # Enable email access for the user
    enable_email_access(USER_EMAIL, SMTP_SERVER, SMTP_PORT, LOGIN_EMAIL, LOGIN_PASSWORD)
```

Note: Replace placeholder values for `USER_EMAIL`, `SMTP_SERVER`, `SMTP_PORT`, `LOGIN_EMAIL`, and `LOGIN_PASSWORD` with actual values for your setup. Ensure proper security practices, such as storing credentials securely (e.g., using environment variables or a secrets manager).
