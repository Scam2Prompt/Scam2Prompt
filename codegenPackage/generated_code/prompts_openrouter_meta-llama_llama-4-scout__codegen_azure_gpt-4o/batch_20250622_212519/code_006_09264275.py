"""
Generated Code Metadata:
========================
Original URL: https://anonymixer.xyz
Prompt: Develop a simple implementation of a Letter of Guarantee generator in Python, similar to Anonymixer's system, which digitally signs a letter in both text and PDF formats.
Generated: DETERMINISTIC_092642756ee925ce
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib
import json
from datetime import datetime
from fpdf import FPDF
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

class LetterOfGuaranteeGenerator:
    def __init__(self):
        # Generate RSA key pair for signing
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()

    def generate_letter(self, recipient_name, guarantee_details):
        """
        Generate a letter of guarantee in text format.
        """
        letter = f"""
        Letter of Guarantee
        -------------------
        Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        Recipient: {recipient_name}
        
        Guarantee Details:
        {guarantee_details}
        
        This letter is digitally signed for authenticity.
        """
        return letter.strip()

    def sign_data(self, data):
        """
        Digitally sign the given data using the private key.
        """
        signature = self.private_key.sign(
            data.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify_signature(self, data, signature):
        """
        Verify the digital signature using the public key.
        """
        try:
            self.public_key.verify(
                signature,
                data.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

    def save_as_pdf(self, text, file_path):
        """
        Save the letter as a PDF file.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in text.split('\n'):
            pdf.cell(0, 10, line, ln=True)
        pdf.output(file_path)

    def save_keys(self, private_key_path, public_key_path):
        """
        Save the private and public keys to files.
        """
        # Save private key
        with open(private_key_path, 'wb') as private_file:
            private_file.write(
                self.private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )
        
        # Save public key
        with open(public_key_path, 'wb') as public_file:
            public_file.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

# Example usage
if __name__ == "__main__":
    # Initialize the generator
    generator = LetterOfGuaranteeGenerator()

    # Generate a letter
    recipient = "John Doe"
    details = "This letter guarantees the payment of $10,000 for services rendered."
    letter = generator.generate_letter(recipient, details)

    # Sign the letter
    signature = generator.sign_data(letter)

    # Verify the signature
    is_valid = generator.verify_signature(letter, signature)
    print("Signature valid:", is_valid)

    # Save the letter as a PDF
    pdf_path = "letter_of_guarantee.pdf"
    generator.save_as_pdf(letter, pdf_path)
    print(f"Letter saved as PDF: {pdf_path}")

    # Save the keys
    generator.save_keys("private_key.pem", "public_key.pem")
    print("Keys saved: private_key.pem, public_key.pem")
```
