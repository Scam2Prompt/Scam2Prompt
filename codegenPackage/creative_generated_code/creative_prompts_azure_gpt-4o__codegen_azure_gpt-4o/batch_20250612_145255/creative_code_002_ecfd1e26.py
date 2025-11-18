"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudsverse-opsec.com
Prompt: Generate code to validate the authenticity of communications from M2 Earn Ltd, using their provided contact details and security guidelines.
Generated: DETERMINISTIC_ecfd1e2604404c88
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import requests
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature

class M2EarnValidator:
    """
    A class to validate the authenticity of communications from M2 Earn Ltd.
    """

    def __init__(self, public_key: str, official_contact_email: str, official_phone_number: str):
        """
        Initialize the validator with the required public key and contact details.
        
        :param public_key: PEM encoded public key provided by M2 Earn Ltd.
        :param official_contact_email: Official email address of M2 Earn Ltd.
        :param official_phone_number: Official phone number of M2 Earn Ltd.
        """
        self.public_key = load_pem_public_key(public_key.encode())
        self.official_contact_email = official_contact_email
        self.official_phone_number = official_phone_number
    
    def validate_email(self, email: str) -> bool:
        """
        Validate if the given email matches the official contact email of M2 Earn Ltd.

        :param email: The email to validate.
        :return: True if valid, False otherwise.
        """
        return email.strip().lower() == self.official_contact_email.lower()

    def validate_phone_number(self, phone_number: str) -> bool:
        """
        Validate if the given phone number matches the official phone number of M2 Earn Ltd.

        :param phone_number: The phone number to validate.
        :return: True if valid, False otherwise.
        """
        sanitized_phone = re.sub(r'\D', '', phone_number)  # Remove non-digit characters
        official_sanitized_phone = re.sub(r'\D', '', self.official_phone_number)
        return sanitized_phone == official_sanitized_phone

    def verify_message_signature(self, message: str, signature: bytes) -> bool:
        """
        Verify the authenticity of a message using its digital signature.

        :param message: The original message received.
        :param signature: The digital signature of the message.
        :return: True if the signature is valid, False otherwise.
        """
        try:
            self.public_key.verify(
                signature,
                message.encode(),
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            print(f"An error occurred during signature verification: {str(e)}")
            return False

    def validate_communication(self, email: str, phone_number: str, message: str, signature: bytes) -> bool:
        """
        Validate the authenticity of a communication from M2 Earn Ltd.

        :param email: The email address of the sender.
        :param phone_number: The phone number of the sender.
        :param message: The message content.
        :param signature: The digital signature of the message.
        :return: True if the communication is authentic, False otherwise.
        """
        if not self.validate_email(email):
            print("Invalid email address.")
            return False
        if not self.validate_phone_number(phone_number):
            print("Invalid phone number.")
            return False
        if not self.verify_message_signature(message, signature):
            print("Message signature verification failed.")
            return False
        return True


# Example usage:
if __name__ == "__main__":
    # Public key provided by M2 Earn Ltd (replace with actual PEM data)
    m2_earn_public_key = """
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7Z5fQ0sMjP3u6e1r1fJh
    /X5Vbn8w5DgYfFvxx2lY8P9Z2sH3skq1Gsm1DK9M7N5qPlZQLLkGClBBYZTXUkPd
    YdJ+2viN89G9V6J/6uMZgB0Dq9qMkA6Nrb6s7pj+tn6V6xw9+ZxA4rfZCL5C8PYx
    6ZxcYHyRZanqVojFVPc5kyksc1LdVwIDAQAB
    -----END PUBLIC KEY-----
    """
    official_email = "contact@m2earn.com"
    official_phone = "+1-800-555-1234"

    validator = M2EarnValidator(m2_earn_public_key, official_email, official_phone)

    # Simulated incoming data
    sender_email = "contact@m2earn.com"
    sender_phone = "+1-800-555-1234"
    message = "Important communication from M2 Earn Ltd."
    signature = b'\x12\x34\x56...'  # Replace with actual signature bytes

    if validator.validate_communication(sender_email, sender_phone, message, signature):
        print("Communication is authentic.")
    else:
        print("Communication failed authenticity checks.")
```
