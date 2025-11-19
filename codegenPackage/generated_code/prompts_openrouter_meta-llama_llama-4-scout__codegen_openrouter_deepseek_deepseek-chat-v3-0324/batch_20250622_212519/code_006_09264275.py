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
import hashlib
import datetime
from fpdf import FPDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class LetterOfGuaranteeGenerator:
    """
    A class to generate digitally signed Letters of Guarantee in text and PDF formats.
    """
    
    def __init__(self, issuer_name, issuer_details, private_key_path=None):
        """
        Initialize the generator with issuer information.
        
        Args:
            issuer_name (str): Name of the issuer
            issuer_details (dict): Dictionary containing issuer details
            private_key_path (str, optional): Path to existing private key. Defaults to None.
        """
        self.issuer_name = issuer_name
        self.issuer_details = issuer_details
        self.private_key = self._load_or_generate_private_key(private_key_path)
        self.public_key = self.private_key.public_key()
        
    def _load_or_generate_private_key(self, private_key_path):
        """
        Load existing private key or generate a new one.
        
        Args:
            private_key_path (str): Path to private key file
            
        Returns:
            RSAPrivateKey: The private key object
        """
        if private_key_path and os.path.exists(private_key_path):
            with open(private_key_path, "rb") as key_file:
                private_key = serialization.load_pem_private_key(
                    key_file.read(),
                    password=None,
                    backend=default_backend()
                )
        else:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            
            if private_key_path:
                self._save_private_key(private_key, private_key_path)
                
        return private_key
    
    def _save_private_key(self, private_key, path):
        """
        Save private key to file.
        
        Args:
            private_key (RSAPrivateKey): The private key to save
            path (str): Path to save the key
        """
        pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        with open(path, "wb") as f:
            f.write(pem)
    
    def generate_letter(self, recipient_name, guarantee_details, output_dir="output"):
        """
        Generate a letter of guarantee with digital signature.
        
        Args:
            recipient_name (str): Name of the recipient
            guarantee_details (dict): Details of the guarantee
            output_dir (str): Output directory for files
            
        Returns:
            dict: Dictionary containing paths to generated files
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"letter_of_guarantee_{timestamp}"
        
        # Generate text content
        text_content = self._generate_text_content(recipient_name, guarantee_details)
        text_path = os.path.join(output_dir, f"{base_filename}.txt")
        
        # Generate signature
        signature = self._sign_content(text_content)
        signature_hex = signature.hex()
        
        # Save text file with signature
        with open(text_path, "w") as f:
            f.write(text_content)
            f.write(f"\n\n--- DIGITAL SIGNATURE ---\n{signature_hex}")
        
        # Generate PDF
        pdf_path = os.path.join(output_dir, f"{base_filename}.pdf")
        self._generate_pdf(text_content, signature_hex, pdf_path)
        
        return {
            "text_file": text_path,
            "pdf_file": pdf_path,
            "signature": signature_hex
        }
    
    def _generate_text_content(self, recipient_name, guarantee_details):
        """
        Generate the text content of the letter.
        
        Args:
            recipient_name (str): Name of the recipient
            guarantee_details (dict): Details of the guarantee
            
        Returns:
            str: Formatted letter content
        """
        date = datetime.datetime.now().strftime("%B %d, %Y")
        
        content = f"""
LETTER OF GUARANTEE

Date: {date}

From: {self.issuer_name}
To: {recipient_name}

This letter serves as a guarantee that:

{guarantee_details.get('description', '')}

Terms and Conditions:
{guarantee_details.get('terms', '')}

Issuer Details:
{json.dumps(self.issuer_details, indent=2)}

This guarantee is valid until: {guarantee_details.get('valid_until', 'N/A')}
"""
        return content.strip()
    
    def _sign_content(self, content):
        """
        Sign the content with the private key.
        
        Args:
            content (str): Content to sign
            
        Returns:
            bytes: Digital signature
        """
        signature = self.private_key.sign(
            content.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
    
    def _generate_pdf(self, content, signature, output_path):
        """
        Generate PDF version of the letter.
        
        Args:
            content (str): Letter content
            signature (str): Hex representation of signature
            output_path (str): Path to save PDF
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        
        # Split content into lines and add to PDF
        for line in content.split('\n'):
            pdf.cell(200, 10, txt=line, ln=1)
        
        # Add signature section
        pdf.ln(10)
        pdf.set_font("Arial", 'B', size=12)
        pdf.cell(200, 10, txt="DIGITAL SIGNATURE", ln=1)
        pdf.set_font("Courier", size=10)
        
        # Split signature into chunks for better display
        signature_chunks = [signature[i:i+64] for i in range(0, len(signature), 64)]
        for chunk in signature_chunks:
            pdf.cell(200, 5, txt=chunk, ln=1)
        
        pdf.output(output_path)
    
    def verify_signature(self, content, signature_hex):
        """
        Verify the signature of a letter.
        
        Args:
            content (str): Original content
            signature_hex (str): Hex representation of signature
            
        Returns:
            bool: True if signature is valid, False otherwise
        """
        try:
            signature = bytes.fromhex(signature_hex)
            self.public_key.verify(
                signature,
                content.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False

def example_usage():
    # Example issuer details
    issuer_details = {
        "company": "Example Corp",
        "address": "123 Business St, City, Country",
        "registration_number": "COMP123456",
        "contact_email": "legal@example.com"
    }
    
    # Example guarantee details
    guarantee_details = {
        "description": "We guarantee the payment of all invoices issued by our client up to the amount of $10,000 USD.",
        "terms": "1. This guarantee is valid for 12 months from date of issue.\n2. Claims must be submitted in writing.",
        "valid_until": "December 31, 2023"
    }
    
    # Initialize generator
    generator = LetterOfGuaranteeGenerator(
        issuer_name="Example Corp Legal Department",
        issuer_details=issuer_details,
        private_key_path="private_key.pem"
    )
    
    # Generate letter
    result = generator.generate_letter(
        recipient_name="Acme Inc",
        guarantee_details=guarantee_details
    )
    
    print(f"Generated files:")
    print(f"Text: {result['text_file']}")
    print(f"PDF: {result['pdf_file']}")
    print(f"Signature: {result['signature']}")
    
    # Verify signature
    with open(result['text_file'], 'r') as f:
        content = f.read().split('--- DIGITAL SIGNATURE ---')[0].strip()
    
    is_valid = generator.verify_signature(content, result['signature'])
    print(f"Signature verification: {'VALID' if is_valid else 'INVALID'}")

if __name__ == "__main__":
    example_usage()
```
