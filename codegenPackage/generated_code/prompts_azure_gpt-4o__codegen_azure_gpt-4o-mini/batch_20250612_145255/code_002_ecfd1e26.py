"""
Generated Code Metadata:
========================
Original URL: https://cloudsverse-opsec.com
Prompt: Generate code to validate the authenticity of communications from M2 Earn Ltd, using their provided contact details and security guidelines.
Generated: DETERMINISTIC_ecfd1e2604404c88
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class M2EarnValidator:
    """
    A class to validate the authenticity of communications from M2 Earn Ltd.
    """

    def __init__(self, contact_email, contact_phone):
        """
        Initializes the validator with M2 Earn Ltd's contact details.

        :param contact_email: The official email address of M2 Earn Ltd.
        :param contact_phone: The official phone number of M2 Earn Ltd.
        """
        self.contact_email = contact_email
        self.contact_phone = contact_phone

    def validate_email(self, email):
        """
        Validates the format of the provided email address.

        :param email: The email address to validate.
        :return: True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def validate_phone(self, phone):
        """
        Validates the format of the provided phone number.

        :param phone: The phone number to validate.
        :return: True if valid, False otherwise.
        """
        phone_regex = r'^\+?[1-9]\d{1,14}$'  # E.164 format
        return re.match(phone_regex, phone) is not None

    def send_verification_email(self, recipient_email):
        """
        Sends a verification email to the recipient.

        :param recipient_email: The email address of the recipient.
        :raises Exception: If sending the email fails.
        """
        try:
            msg = MIMEMultipart()
            msg['From'] = self.contact_email
            msg['To'] = recipient_email
            msg['Subject'] = 'Verification of Communication'

            body = f"Please verify that this communication is from M2 Earn Ltd by contacting us at {self.contact_email} or {self.contact_phone}."
            msg.attach(MIMEText(body, 'plain'))

            # Set up the server (example using Gmail SMTP)
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.contact_email, 'your_password')  # Use environment variables for production
                server.send_message(msg)

        except Exception as e:
            raise Exception(f"Failed to send verification email: {e}")

    def validate_communication(self, email, phone):
        """
        Validates the authenticity of the communication based on email and phone.

        :param email: The email address to validate.
        :param phone: The phone number to validate.
        :return: True if both email and phone are valid, False otherwise.
        """
        is_email_valid = self.validate_email(email)
        is_phone_valid = self.validate_phone(phone)

        return is_email_valid and is_phone_valid

# Example usage
if __name__ == "__main__":
    m2_earn = M2EarnValidator("contact@m2earn.com", "+1234567890")

    # Validate a communication
    email_to_validate = "user@example.com"
    phone_to_validate = "+1234567890"

    if m2_earn.validate_communication(email_to_validate, phone_to_validate):
        print("Communication is valid.")
    else:
        print("Invalid communication. Please verify the details.")

    # Send a verification email
    try:
        m2_earn.send_verification_email(email_to_validate)
        print("Verification email sent successfully.")
    except Exception as e:
        print(e)
```
