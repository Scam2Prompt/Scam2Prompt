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
import json
import logging
from fpdf import FPDF
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization

# Configure logging
logging.basicConfig(level=logging.INFO)

class LetterOfGuarantee:
    def __init__(self, signer_private_key_path: str):
        """
        Initialize the LetterOfGuarantee generator with a private key for signing.

        :param signer_private_key_path: Path to the private key file.
        """
        self.signer_private_key = self.load_private_key(signer_private_key_path)

    def load_private_key(self, private_key_path: str):
        """
        Load the private key from a file.

        :param private_key_path: Path to the private key file.
        :return: Private key object.
        """
        try:
            with open(private_key_path, "rb") as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
            return private_key
        except Exception as e:
            logging.error(f"Failed to load private key: {e}")
            raise

    def generate_letter(self, recipient: str, amount: float, date: str) -> str:
        """
        Generate a letter of guarantee text.

        :param recipient: Name of the recipient.
        :param amount: Amount guaranteed.
        :param date: Date of the guarantee.
        :return: The generated letter text.
        """
        letter_text = f"""
        Letter of Guarantee

        Date: {date}

        To: {recipient}

        This letter serves as a guarantee for the amount of ${amount:.2f}.

        Sincerely,
        [Your Name]
        """
        return letter_text.strip()

    def sign_letter(self, letter_text: str) -> bytes:
        """
        Sign the letter text using the private key.

        :param letter_text: The text of the letter to sign.
        :return: The signature as bytes.
        """
        try:
            signature = self.signer_private_key.sign(
                letter_text.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return signature
        except Exception as e:
            logging.error(f"Failed to sign letter: {e}")
            raise

    def create_pdf(self, letter_text: str, output_path: str):
        """
        Create a PDF file from the letter text.

        :param letter_text: The text of the letter.
        :param output_path: Path to save the PDF file.
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in letter_text.splitlines():
            pdf.cell(200, 10, txt=line, ln=True)
        pdf.output(output_path)
        logging.info(f"PDF created at: {output_path}")

    def generate_letter_of_guarantee(self, recipient: str, amount: float, date: str, output_pdf_path: str) -> dict:
        """
        Generate a letter of guarantee, sign it, and create a PDF.

        :param recipient: Name of the recipient.
        :param amount: Amount guaranteed.
        :param date: Date of the guarantee.
        :param output_pdf_path: Path to save the PDF file.
        :return: A dictionary containing the letter text and signature.
        """
        letter_text = self.generate_letter(recipient, amount, date)
        signature = self.sign_letter(letter_text)
        self.create_pdf(letter_text, output_pdf_path)

        return {
            "letter_text": letter_text,
            "signature": signature.hex()  # Convert signature to hex for easier storage
        }

if __name__ == "__main__":
    # Example usage
    try:
        generator = LetterOfGuarantee("path/to/private_key.pem")
        result = generator.generate_letter_of_guarantee(
            recipient="John Doe",
            amount=1000.00,
            date="2023-10-01",
            output_pdf_path="letter_of_guarantee.pdf"
        )
        print(json.dumps(result, indent=4))
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

Make sure to replace `"path/to/private_key.pem"` with the actual path to your PEM formatted private key file before running the code.
