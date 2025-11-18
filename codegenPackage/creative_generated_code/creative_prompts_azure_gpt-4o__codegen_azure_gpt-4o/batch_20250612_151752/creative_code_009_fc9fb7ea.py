"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://luke.jecool.net
Prompt: Provide a step-by-step guide to verify email addresses during the registration of generic domains on Endora.cz, as outlined in their documentation.
Generated: DETERMINISTIC_fc9fb7eaff61b193
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import smtplib
from email.message import EmailMessage

class EmailVerification:
    """
    A class to handle email verification during registration
    for domains on Endora.cz.
    """

    def __init__(self, smtp_server, smtp_port, smtp_user, smtp_password):
        """
        Initialize the EmailVerification instance.
        
        Parameters:
            smtp_server (str): SMTP server address.
            smtp_port (int): SMTP server port.
            smtp_user (str): Username for SMTP authentication.
            smtp_password (str): Password for SMTP authentication.
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_user = smtp_user
        self.smtp_password = smtp_password

    def is_valid_email(self, email):
        """
        Validate the email address format using regex.

        Parameters:
            email (str): The email address to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    def send_verification_email(self, to_email, verification_code):
        """
        Sends a verification email to the user.

        Parameters:
            to_email (str): Recipient's email address.
            verification_code (str): Unique verification code to send.

        Returns:
            bool: True if email was sent successfully, False otherwise.
        """
        try:
            # Create the email message
            msg = EmailMessage()
            msg['Subject'] = 'Verify Your Email Address'
            msg['From'] = self.smtp_user
            msg['To'] = to_email
            msg.set_content(f"Please use the following code to verify your email address: {verification_code}")

            # Connect to the SMTP server
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()  # Upgrade the connection to secure TLS
                server.login(self.smtp_user, self.smtp_password)
                server.send_message(msg)

            return True
        except Exception as e:
            # Handle email sending errors
            print(f"Error sending email: {e}")
            return False

    def verify_email_code(self, input_code, actual_code):
        """
        Verifies the email using the provided code.

        Parameters:
            input_code (str): Code provided by the user.
            actual_code (str): Actual code sent to the user's email.

        Returns:
            bool: True if the codes match, False otherwise.
        """
        return input_code == actual_code


# Example usage
if __name__ == "__main__":
    # Configuration for the SMTP server (replace with actual credentials)
    SMTP_SERVER = 'smtp.example.com'
    SMTP_PORT = 587
    SMTP_USER = 'your-email@example.com'
    SMTP_PASSWORD = 'your-email-password'

    # Initialize the EmailVerification instance
    email_verifier = EmailVerification(SMTP_SERVER, SMTP_PORT, SMTP_USER, SMTP_PASSWORD)

    # Step 1: Collect user email address
    user_email = input("Enter your email address: ")

    # Step 2: Verify email format
    if not email_verifier.is_valid_email(user_email):
        print("Invalid email format. Please try again.")
        exit()

    # Step 3: Generate a unique verification code (e.g., a 6-digit random number)
    import random
    verification_code = str(random.randint(100000, 999999))
    print(f"Verification code generated: {verification_code}")  # For testing purposes only

    # Step 4: Send the verification email
    if email_verifier.send_verification_email(user_email, verification_code):
        print("A verification email has been sent. Please check your inbox.")
    else:
        print("Failed to send the verification email. Please try again later.")
        exit()

    # Step 5: Ask the user to enter the code
    user_input_code = input("Enter the verification code sent to your email: ")

    # Step 6: Verify the code
    if email_verifier.verify_email_code(user_input_code, verification_code):
        print("Email verification successful!")
    else:
        print("Invalid verification code. Please try again.")
```
