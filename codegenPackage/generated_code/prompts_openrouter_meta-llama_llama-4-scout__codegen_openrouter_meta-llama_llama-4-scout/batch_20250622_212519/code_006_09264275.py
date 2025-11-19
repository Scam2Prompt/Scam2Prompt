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
import hashlib
import json
from datetime import datetime
from fpdf import FPDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

class LetterOfGuarantee:
    def __init__(self, issuer_name, issuer_title, recipient_name, recipient_title, amount, description):
        self.issuer_name = issuer_name
        self.issuer_title = issuer_title
        self.recipient_name = recipient_name
        self.recipient_title = recipient_title
        self.amount = amount
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d")

    def generate_text(self):
        text = f"""
        LETTER OF GUARANTEE

        This Letter of Guarantee is issued on {self.date} by {self.issuer_name}, {self.issuer_title},
        in favor of {self.recipient_name}, {self.recipient_title}.

        We hereby guarantee to pay an amount not exceeding {self.amount} for the {self.description}.

        By: {self.issuer_name}
        Title: {self.issuer_title}
        Date: {self.date}
        """
        return text

    def generate_pdf(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=15)
        pdf.cell(200, 10, txt="LETTER OF GUARANTEE", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 5, txt=f"This Letter of Guarantee is issued on {self.date} by {self.issuer_name}, {self.issuer_title},\nin favor of {self.recipient_name}, {self.recipient_title}.")
        pdf.multi_cell(0, 5, txt=f"We hereby guarantee to pay an amount not exceeding {self.amount} for the {self.description}.")
        pdf.ln(10)
        pdf.multi_cell(0, 5, txt=f"By: {self.issuer_name}\nTitle: {self.issuer_title}\nDate: {self.date}")
        return pdf

class DigitalSigner:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

    def get_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.OpenSSH,
            format=serialization.PublicFormat.OpenSSH
        ).decode()

    def sign(self, data):
        signature = self.private_key.sign(
            data.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify(self, data, signature, public_key):
        try:
            public_key = serialization.load_ssh_public_key(public_key.encode())
            public_key.verify(
                signature,
                data.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False

def main():
    # Generate a letter of guarantee
    letter = LetterOfGuarantee(
        issuer_name="John Doe",
        issuer_title="CEO",
        recipient_name="Jane Doe",
        recipient_title="Manager",
        amount="$1000",
        description="services rendered"
    )

    # Generate text and PDF
    text = letter.generate_text()
    pdf = letter.generate_pdf()
    pdf.output("letter_of_guarantee.pdf")

    # Digital signing
    signer = DigitalSigner()
    public_key = signer.get_public_key()
    signature = signer.sign(text)

    # Verification
    is_valid = signer.verify(text, signature, public_key)
    print(f"Is signature valid? {is_valid}")

    # Save data and signature to JSON
    data = {
        "text": text,
        "signature": signature.hex(),
        "public_key": public_key
    }
    with open("letter_of_guarantee.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()
```
