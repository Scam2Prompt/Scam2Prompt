"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anonymixer.xyz
Prompt: Write a script to generate a "Letter of Guarantee" in both text and PDF formats, digitally signed using PGP keys, as described on Anonymixer's website.
Generated: DETERMINISTIC_1d26325ef3b6c60e
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import tempfile
from fpdf import FPDF
import gnupg

# Path to the GPG home directory (ensure this directory exists and has the keys)
GPG_HOME = os.path.expanduser('~/.gnupg')
gpg = gnupg.GPG(gnupghome=GPG_HOME)

def generate_letter_of_guarantee(content: str, filename: str):
    """
    Generates a letter of guarantee in text and PDF formats.

    Parameters:
        content (str): The content of the letter.
        filename (str): The base filename for the output files (without extension).
    """
    # Generate text file
    text_file_path = f"{filename}.txt"
    try:
        with open(text_file_path, 'w') as text_file:
            text_file.write(content)
        print(f"Text file generated at: {text_file_path}")
    except IOError as e:
        print(f"Error writing text file: {e}")
        return
    
    # Generate PDF file using FPDF
    pdf_file_path = f"{filename}.pdf"
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, content)
        pdf.output(pdf_file_path)
        print(f"PDF file generated at: {pdf_file_path}")
    except Exception as e:
        print(f"Error generating PDF file: {e}")
        return

    return text_file_path, pdf_file_path

def sign_file(file_path: str, recipient: str) -> str:
    """
    Signs a file using PGP with the specified recipient's key.

    Parameters:
        file_path (str): The path of the file to be signed.
        recipient (str): The recipient's email or key ID used for signing.

    Returns:
        str: The path to the signed file or an error message.
    """
    try:
        with open(file_path, 'rb') as file:
            signed_data = gpg.sign_file(file, keyid=recipient)
        if signed_data:
            signed_file_path = f"{file_path}.sig"
            with open(signed_file_path, 'wb') as signed_file:
                signed_file.write(signed_data.data)
            print(f"File signed successfully: {signed_file_path}")
            return signed_file_path
        else:
            print("Error signing file:", signed_data.stderr)
            return "Error signing file."
    except Exception as e:
        print(f"Error during signing: {e}")
        return "Error during signing."

def main():
    # Example content for the Letter of Guarantee
    letter_content = """\
    Letter of Guarantee

    To Whom It May Concern,

    This letter serves as a guarantee for the transaction as discussed.

    Sincerely,
    [Your Name]
    """
    
    # Generate the letter
    filename = "letter_of_guarantee"
    text_file, pdf_file = generate_letter_of_guarantee(letter_content, filename)
    
    # Sign the text file (replace 'recipient@example.com' with actual recipient's key or ID)
    recipient_key = 'recipient@example.com'
    if text_file:
        signed_file_path = sign_file(text_file, recipient_key)
        if signed_file_path:
            print(f"Signed File Path: {signed_file_path}")

if __name__ == "__main__":
    main()
```

### Note:
- Ensure that `gnupg` and `fpdf` libraries are installed in your Python environment. You can install them using:
  ```bash
  pip install python-gnupg fpdf
  ```
- Update `recipient_key` with the actual recipient's email or key ID for signing.
- Make sure you have valid PGP keys in your GPG home directory (`~/.gnupg`).
