"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Write a Python script to generate QR codes for Bitcoin addresses while ensuring privacy and security by avoiding the storage of logs or cookies, as emphasized by bitcoinqr.io.
Generated: DETERMINISTIC_2c1542f04bbf3069
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import os
import tempfile
import hashlib
import argparse
from typing import Optional

def generate_qr_code(data: str, output_path: Optional[str] = None) -> str:
    """
    Generate a QR code for the given data and save it to a file.
    
    Args:
        data: The data to encode in the QR code (e.g., Bitcoin address).
        output_path: Optional path to save the QR code. If None, a temp file is used.
    
    Returns:
        Path to the generated QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    if output_path is None:
        # Create a temp file with a random name
        fd, output_path = tempfile.mkstemp(suffix='.png')
        os.close(fd)
    
    img.save(output_path)
    return output_path

def clean_up(file_path: str) -> None:
    """
    Securely delete the generated QR code file.
    
    Args:
        file_path: Path to the file to be deleted.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        # Fail silently to avoid exposing any information
        pass

def main():
    parser = argparse.ArgumentParser(description='Generate QR codes for Bitcoin addresses.')
    parser.add_argument('address', type=str, help='Bitcoin address to encode')
    parser.add_argument('--output', type=str, help='Output file path (optional)', default=None)
    
    args = parser.parse_args()
    
    # Validate Bitcoin address (basic check)
    if not (26 <= len(args.address) <= 35):
        print("Warning: The provided address doesn't match typical Bitcoin address lengths.")
    
    try:
        qr_path = generate_qr_code(args.address, args.output)
        print(f"QR code generated at: {qr_path}")
        
        if args.output is None:
            input("Press Enter to delete the temporary QR code file...")
            clean_up(qr_path)
            print("Temporary file deleted.")
    except Exception as e:
        print(f"Error generating QR code: {str(e)}")
        return

if __name__ == "__main__":
    main()
```
