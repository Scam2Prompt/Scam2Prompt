"""
Generated Code Metadata:
========================
Original URL: https://anonymixer.xyz
Prompt: Write a script to generate a "Letter of Guarantee" in both text and PDF formats, digitally signed using PGP keys, as described on Anonymixer's website.
Generated: DETERMINISTIC_1d26325ef3b6c60e
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Python, as it's a popular language for such tasks. I'll use the `fpdf` library to generate PDFs, `gnupg` for PGP operations, and `datetime` for date handling.

```python
import datetime
from fpdf import FPDF
import gnupg
import os

def generate_letter_of_guarantee(name, guarantee_text, recipient_name, recipient_email):
    """
    Generate a Letter of Guarantee in text and PDF formats, 
    and digitally sign it using PGP keys.

    Args:
        name (str): The name of the guarantor.
        guarantee_text (str): The text of the guarantee.
        recipient_name (str): The name of the recipient.
        recipient_email (str): The email of the recipient.

    Returns:
        None
    """

    # Generate text version of the letter
    text_letter = generate_text_letter(name, guarantee_text, recipient_name)

    # Generate PDF version of the letter
    pdf_letter = generate_pdf_letter(name, guarantee_text, recipient_name)

    # Digitally sign the letter using PGP keys
    pgp_keyring = gnupg.GPG()
    pgp_keyring = gnupg.GPG(gpgbinary='gpg2')
    signed_text_letter = sign_text(pgp_keyring, text_letter)
    signed_pdf_letter = sign_pdf(pgp_keyring, pdf_letter)

    # Save the signed letters to files
    save_signed_letters(signed_text_letter, signed_pdf_letter, recipient_email)

def generate_text_letter(name, guarantee_text, recipient_name):
    """
    Generate the text version of the Letter of Guarantee.

    Args:
        name (str): The name of the guarantor.
        guarantee_text (str): The text of the guarantee.
        recipient_name (str): The name of the recipient.

    Returns:
        str: The text version of the Letter of Guarantee.
    """
    text_letter = f"""
TO: {recipient_name}

This Letter of Guarantee is issued on {datetime.date.today()} by {name}.

{guarantee_text}

Sincerely,
{name}
"""
    return text_letter

def generate_pdf_letter(name, guarantee_text, recipient_name):
    """
    Generate the PDF version of the Letter of Guarantee.

    Args:
        name (str): The name of the guarantor.
        guarantee_text (str): The text of the guarantee.
        recipient_name (str): The name of the recipient.

    Returns:
        bytes: The PDF version of the Letter of Guarantee.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Letter of Guarantee", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=f"TO: {recipient_name}\n\nThis Letter of Guarantee is issued on {datetime.date.today()} by {name}.\n\n{guarantee_text}\n\nSincerely,\n{name}")
    pdf.output()
    with open("letter.pdf", "rb") as f:
        pdf_bytes = f.read()
    return pdf_bytes

def sign_text(pgp_keyring, text):
    """
    Digitally sign the text using PGP keys.

    Args:
        pgp_keyring (gnupg.GPG): The PGP keyring.
        text (str): The text to be signed.

    Returns:
        str: The digitally signed text.
    """
    try:
        # Load the private key
        with open('private_key.asc', 'r') as f:
            private_key = f.read()
        pgp_keyring.import_key(private_key)

        # Sign the text
        signed_text = pgp_keyring.encrypt(text, 
                                          passphrase='passphrase', 
                                          recipients=None, 
                                          sign=True, 
                                          digest_algorithm='SHA256')
        return signed_text
    except Exception as e:
        print(f"Error signing text: {str(e)}")
        return None

def sign_pdf(pgp_keyring, pdf_bytes):
    """
    Digitally sign the PDF using PGP keys.

    Args:
        pgp_keyring (gnupg.GPG): The PGP keyring.
        pdf_bytes (bytes): The PDF bytes to be signed.

    Returns:
        bytes: The digitally signed PDF bytes.
    """
    try:
        # Load the private key
        with open('private_key.asc', 'r') as f:
            private_key = f.read()
        pgp_keyring.import_key(private_key)

        # Sign the PDF
        signed_pdf = pgp_keyring.encrypt(pdf_bytes, 
                                         passphrase='passphrase', 
                                         recipients=None, 
                                         sign=True, 
                                         digest_algorithm='SHA256')
        return signed_pdf
    except Exception as e:
        print(f"Error signing PDF: {str(e)}")
        return None

def save_signed_letters(signed_text_letter, signed_pdf_letter, recipient_email):
    """
    Save the signed letters to files.

    Args:
        signed_text_letter (str): The digitally signed text letter.
        signed_pdf_letter (bytes): The digitally signed PDF letter.
        recipient_email (str): The email of the recipient.

    Returns:
        None
    """
    try:
        with open(f"signed_letter_{recipient_email}.txt", "w") as f:
            f.write(str(signed_text_letter))

        with open(f"signed_letter_{recipient_email}.pdf", "wb") as f:
            f.write(signed_pdf_letter)
    except Exception as e:
        print(f"Error saving signed letters: {str(e)}")

if __name__ == "__main__":
    generate_letter_of_guarantee("John Doe", "This is a sample guarantee text.", "Jane Doe", "jane@example.com")
```
