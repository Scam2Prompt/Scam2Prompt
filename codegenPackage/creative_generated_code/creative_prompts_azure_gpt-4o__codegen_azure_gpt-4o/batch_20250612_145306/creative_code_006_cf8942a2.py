"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lcoksrare.com
Prompt: Develop a Python script to resend authentication codes and handle errors for RBC PayEdge login attempts.
Generated: DETERMINISTIC_cf8942a2257b4e41
Batch ID: 20250612_145306
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


class AuthenticationService:
    """
    A service to handle authentication code generation and resending for RBC PayEdge login attempts.
    """

    def __init__(self):
        # Store authentication codes for users in a dictionary
        self.auth_codes = {}

    def generate_auth_code(self) -> str:
        """
        Generates a 6-digit random authentication code.

        Returns:
            str: A 6-digit authentication code as a string.
        """
        return f"{random.randint(100000, 999999)}"

    def send_auth_code(self, email: str) -> bool:
        """
        Sends an authentication code to the user's email.

        Args:
            email (str): The recipient's email address.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        # Generate a new authentication code
        auth_code = self.generate_auth_code()
        self.auth_codes[email] = auth_code

        # Configure email parameters
        sender_email = "no-reply@rbcpayedge.com"
        email_subject = "Your RBC PayEdge Authentication Code"
        email_body = f"Your authentication code is: {auth_code}"

        try:
            # Create the email
            msg = EmailMessage()
            msg['Subject'] = email_subject
            msg['From'] = sender_email
            msg['To'] = email
            msg.set_content(email_body)

            # Send the email using SMTP (this is a placeholder configuration)
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login("smtp_user", "smtp_password")  # Replace with actual credentials
                server.send_message(msg)
            
            print(f"Authentication code sent to {email}")
            return True

        except smtplib.SMTPException as e:
            print(f"Error sending email to {email}: {e}")
            return False

    def resend_auth_code(self, email: str) -> bool:
        """
        Resends the existing authentication code to the user's email.

        Args:
            email (str): The recipient's email address.

        Returns:
            bool: True if the email was sent successfully, False otherwise.
        """
        if email not in self.auth_codes:
            print(f"No authentication code found for {email}. Unable to resend.")
            return False

        # Retrieve the existing authentication code
        auth_code = self.auth_codes[email]

        # Configure email parameters
        sender_email = "no-reply@rbcpayedge.com"
        email_subject = "Your RBC PayEdge Authentication Code (Resent)"
        email_body = f"Your authentication code is: {auth_code}"

        try:
            # Create the email
            msg = EmailMessage()
            msg['Subject'] = email_subject
            msg['From'] = sender_email
            msg['To'] = email
            msg.set_content(email_body)

            # Send the email using SMTP (this is a placeholder configuration)
            with smtplib.SMTP('smtp.example.com', 587) as server:
                server.starttls()
                server.login("smtp_user", "smtp_password")  # Replace with actual credentials
                server.send_message(msg)
            
            print(f"Authentication code resent to {email}")
            return True

        except smtplib.SMTPException as e:
            print(f"Error resending email to {email}: {e}")
            return False


# Example usage
if __name__ == "__main__":
    auth_service = AuthenticationService()

    user_email = "user@example.com"

    # Send a new authentication code
    if auth_service.send_auth_code(user_email):
        print("Code sent successfully!")

    # Attempt to resend the authentication code
    if auth_service.resend_auth_code(user_email):
        print("Code resent successfully!")
    else:
        print("Failed to resend the code.")
```
