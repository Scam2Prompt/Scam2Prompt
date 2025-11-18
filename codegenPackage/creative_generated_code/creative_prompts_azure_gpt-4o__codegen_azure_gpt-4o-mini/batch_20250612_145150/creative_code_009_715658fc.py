"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Write a detailed explanation of how to implement OTP-based PIN change functionality in a mobile app, using the process described on the Heritage Bank "Change My PIN" page as a reference.
Generated: DETERMINISTIC_715658fc3bf1c2af
Batch ID: 20250612_145150
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import smtplib
from email.message import EmailMessage

class OTPService:
    """
    A service to generate and send OTPs for PIN change verification.
    """

    def __init__(self, email_service, otp_length=6):
        self.otp_length = otp_length
        self.email_service = email_service

    def generate_otp(self):
        """
        Generate a random OTP of specified length.
        """
        return ''.join(random.choices('0123456789', k=self.otp_length))

    def send_otp(self, email, otp):
        """
        Send the generated OTP to the user's email.
        
        Args:
            email (str): User's email address.
            otp (str): The OTP to be sent.
        """
        msg = EmailMessage()
        msg.set_content(f'Your OTP for PIN change is: {otp}')
        msg['Subject'] = 'Your OTP for PIN Change'
        msg['From'] = self.email_service.sender_email
        msg['To'] = email

        try:
            self.email_service.send_email(msg)
            print("OTP sent successfully.")
        except Exception as e:
            print(f"Failed to send OTP: {e}")

class EmailService:
    """
    A service to handle sending emails.
    """

    def __init__(self, smtp_server, smtp_port, sender_email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password

    def send_email(self, msg):
        """
        Connect to SMTP server and send an email message.
        
        Args:
            msg (EmailMessage): The message to send.
        """
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(self.sender_email, self.password)
                server.send_message(msg)
        except smtplib.SMTPException as e:
            raise RuntimeError(f"Error sending email: {e}")

class PINChangeService:
    """
    Service to handle the PIN change process with OTP verification.
    """

    def __init__(self, otp_service):
        self.otp_service = otp_service
        self.user_otp = None

    def request_pin_change(self, email):
        """
        Request a PIN change by generating and sending an OTP to the user.
        
        Args:
            email (str): User's email address.
        """
        self.user_otp = self.otp_service.generate_otp()
        self.otp_service.send_otp(email, self.user_otp)

    def verify_otp(self, entered_otp):
        """
        Verify the OTP entered by the user.
        
        Args:
            entered_otp (str): The OTP entered by the user.
        
        Returns:
            bool: True if the OTP is valid, False otherwise.
        """
        return self.user_otp == entered_otp

    def change_pin(self, new_pin):
        """
        Change the user's PIN after successful OTP verification.
        
        Args:
            new_pin (str): The new PIN to set.
        
        Returns:
            str: Confirmation message.
        """
        # Here you would normally update the user's PIN in the database.
        return "PIN changed successfully."

# Example usage
if __name__ == "__main__":
    # Configuration for email service
    smtp_server = 'smtp.example.com'
    smtp_port = 587
    sender_email = 'no-reply@example.com'
    password = 'yourpassword'

    # Initialize services
    email_service = EmailService(smtp_server, smtp_port, sender_email, password)
    otp_service = OTPService(email_service)
    pin_change_service = PINChangeService(otp_service)

    # Request a PIN change
    user_email = 'user@example.com'
    pin_change_service.request_pin_change(user_email)

    # Simulate user entering the OTP
    user_entered_otp = input("Enter the OTP sent to your email: ")
    
    if pin_change_service.verify_otp(user_entered_otp):
        new_pin = input("Enter your new PIN: ")
        confirmation_message = pin_change_service.change_pin(new_pin)
        print(confirmation_message)
    else:
        print("Invalid OTP. Please try again.")
```

**Note**: Ensure to replace the email service configuration values with actual credentials before running the code. Proper security practices should be followed for handling passwords and sensitive information.
