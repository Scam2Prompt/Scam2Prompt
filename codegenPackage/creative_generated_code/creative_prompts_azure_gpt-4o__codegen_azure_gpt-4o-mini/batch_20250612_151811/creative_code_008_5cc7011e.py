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
import json
import base64
from cryptography.fernet import Fernet
import os

class QRCodeGenerator:
    def __init__(self, key: bytes):
        """
        Initialize the QRCodeGenerator with a symmetric encryption key.
        
        :param key: A bytes object representing the encryption key.
        """
        self.cipher = Fernet(key)

    @staticmethod
    def generate_key() -> bytes:
        """
        Generates a symmetric encryption key using Fernet.
        
        :return: A bytes object representing the generated key.
        """
        return Fernet.generate_key()

    def encrypt_contact_info(self, contact_info: dict) -> str:
        """
        Encrypts contact information using symmetric encryption.
        
        :param contact_info: A dictionary containing contact information.
        :return: A base64 encoded string of the encrypted contact information.
        """
        try:
            data_json = json.dumps(contact_info)
            encrypted_data = self.cipher.encrypt(data_json.encode())
            return base64.urlsafe_b64encode(encrypted_data).decode()
        except Exception as e:
            raise RuntimeError("Failed to encrypt contact information.") from e

    def generate_qr_code(self, data: str, file_path: str) -> None:
        """
        Generates a QR code from the provided data and saves it to a file.
        
        :param data: The data to encode in the QR code.
        :param file_path: The file path where the QR code image will be saved.
        """
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(data)
            qr.make(fit=True)

            img = qr.make_image(fill='black', back_color='white')
            img.save(file_path)
        except Exception as e:
            raise RuntimeError("Failed to generate QR code.") from e


if __name__ == "__main__":
    # Generate a new encryption key (store this securely)
    encryption_key = QRCodeGenerator.generate_key()
    
    # Instantiate the QRCodeGenerator with the generated key
    qr_generator = QRCodeGenerator(encryption_key)

    # Define the contact information
    contact_information = {
        "name": "John Doe",
        "phone": "+1234567890",
        "email": "johndoe@example.com"
    }

    # Encrypt the contact information
    try:
        encrypted_info = qr_generator.encrypt_contact_info(contact_information)
    except RuntimeError as e:
        print(f"Error: {e}")
        exit(1)

    # Generate and save the QR code
    qr_code_file_path = "contact_info_qr.png"
    try:
        qr_generator.generate_qr_code(encrypted_info, qr_code_file_path)
        print(f"QR code saved to {qr_code_file_path}")
    except RuntimeError as e:
        print(f"Error: {e}")
        exit(1)
```
