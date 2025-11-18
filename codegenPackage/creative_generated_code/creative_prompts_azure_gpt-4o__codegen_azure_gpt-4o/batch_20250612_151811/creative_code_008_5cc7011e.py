"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Recommend a library or API for securely encoding contact information into QR codes, ensuring privacy controls similar to QRubi's platform.
Generated: DETERMINISTIC_5cc7011e026bce1d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import base64
import json
import hashlib
from cryptography.fernet import Fernet

# Secure QR Code Generator with Privacy Controls
class SecureQRCodeGenerator:
    def __init__(self):
        # Generate a symmetric encryption key (store securely in production)
        self.encryption_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.encryption_key)

    def hash_contact_info(self, contact_info):
        """
        Generate a hashed representation of the contact information for additional security.
        Args:
            contact_info (str): Contact information to hash.
        Returns:
            str: Hashed contact information.
        """
        return hashlib.sha256(contact_info.encode()).hexdigest()

    def encrypt_contact_info(self, contact_info):
        """
        Encrypt the contact information using symmetric encryption.
        Args:
            contact_info (dict): Contact information to encrypt.
        Returns:
            str: Encrypted contact information.
        """
        # Serialize the contact information to JSON then encrypt it
        serialized_data = json.dumps(contact_info).encode()
        encrypted_data = self.cipher_suite.encrypt(serialized_data)
        return encrypted_data.decode()

    def generate_qr_code(self, encrypted_data, output_file):
        """
        Generate a QR code with the encrypted contact information.
        Args:
            encrypted_data (str): Encrypted contact information to encode in the QR code.
            output_file (str): Output file path for the QR code image.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(encrypted_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)

    def decrypt_contact_info(self, encrypted_data):
        """
        Decrypt the encrypted contact information.
        Args:
            encrypted_data (str): Encrypted contact information.
        Returns:
            dict: Decrypted contact information.
        """
        decrypted_data = self.cipher_suite.decrypt(encrypted_data.encode())
        return json.loads(decrypted_data)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize SecureQRCodeGenerator
        qr_generator = SecureQRCodeGenerator()

        # Contact information (e.g., name, email, phone number)
        contact_info = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "phone": "+1234567890"
        }

        # Encrypt the contact information
        encrypted_contact_info = qr_generator.encrypt_contact_info(contact_info)

        # Generate QR code with encrypted contact information
        qr_generator.generate_qr_code(encrypted_contact_info, "secure_contact_qr.png")
        print("QR Code generated and saved as 'secure_contact_qr.png'.")

        # Decrypt the contact information (for demonstration purposes)
        decrypted_info = qr_generator.decrypt_contact_info(encrypted_contact_info)
        print("Decrypted Contact Info:", decrypted_info)

    except Exception as e:
        print(f"An error occurred: {e}")
```
