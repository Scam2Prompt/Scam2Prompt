"""
Generated Code Metadata:
========================
Original URL: https://appdevistorias.com.br
Prompt: How can I implement a digital signature feature in a property inspection app similar to BeSoft's application?
Generated: DETERMINISTIC_caecdf8978b14477
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Digital Signature Implementation in Python**
=====================================================

### Requirements

* Python 3.8+
* `cryptography` library for digital signatures
* `PIL` library for image processing

### Installation

```bash
pip install cryptography pillow
```

### Code

```python
import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

class DigitalSignature:
    def __init__(self, private_key_path, public_key_path):
        """
        Initialize digital signature object.

        :param private_key_path: Path to private key file
        :param public_key_path: Path to public key file
        """
        self.private_key_path = private_key_path
        self.public_key_path = public_key_path
        self.private_key = self.load_private_key()
        self.public_key = self.load_public_key()

    def load_private_key(self):
        """
        Load private key from file.

        :return: Private key object
        """
        try:
            with open(self.private_key_path, "rb") as key_file:
                return serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                )
        except FileNotFoundError:
            # Generate new private key if not found
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
            )
            with open(self.private_key_path, "wb") as key_file:
                key_file.write(private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))
            return private_key

    def load_public_key(self):
        """
        Load public key from file.

        :return: Public key object
        """
        try:
            with open(self.public_key_path, "rb") as key_file:
                return serialization.load_pem_public_key(
                    key_file.read()
                )
        except FileNotFoundError:
            # Generate new public key if not found
            public_key = self.private_key.public_key()
            with open(self.public_key_path, "wb") as key_file:
                key_file.write(public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
            return public_key

    def sign(self, message):
        """
        Sign a message with private key.

        :param message: Message to sign
        :return: Signature bytes
        """
        return self.private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

    def verify(self, message, signature):
        """
        Verify a signature with public key.

        :param message: Original message
        :param signature: Signature bytes
        :return: True if valid, False otherwise
        """
        try:
            self.public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except InvalidSignature:
            return False

    def generate_signature_image(self, signature, message):
        """
        Generate an image with signature and message.

        :param signature: Signature bytes
        :param message: Original message
        :return: Image object
        """
        image = Image.new("RGB", (400, 200), color = (73, 109, 137))
        d = ImageDraw.Draw(image)
        fnt = ImageFont.load_default()
        d.text((10, 10), message, font=fnt, fill=(255, 255, 0))
        d.text((10, 30), f"Signature: {signature.hex()}", font=fnt, fill=(255, 255, 0))
        d.text((10, 50), f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", font=fnt, fill=(255, 255, 0))
        return image

def main():
    private_key_path = "private_key.pem"
    public_key_path = "public_key.pem"

    digital_signature = DigitalSignature(private_key_path, public_key_path)

    message = "Inspection completed successfully."
    signature = digital_signature.sign(message)

    print(f"Message: {message}")
    print(f"Signature: {signature.hex()}")

    is_valid = digital_signature.verify(message, signature)
    print(f"Is valid: {is_valid}")

    signature_image = digital_signature.generate_signature_image(signature, message)
    signature_image.save("signature.png")

if __name__ == "__main__":
    main()
```
