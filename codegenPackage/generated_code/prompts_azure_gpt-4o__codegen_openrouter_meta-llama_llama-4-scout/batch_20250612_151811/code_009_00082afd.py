"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Write code to generate QR codes for pet tags that include owner contact information, inspired by QRubi's medallions for pets feature.
Generated: DETERMINISTIC_00082afd8eaeebe6
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**QR Code Generator for Pet Tags**
=====================================

### Requirements

* Python 3.8+
* `qrcode` library (`pip install qrcode`)
* `Pillow` library (`pip install pillow`)

### Code
```python
import qrcode
from PIL import Image
import os

def generate_qr_code(data, filename):
    """
    Generate a QR code with the provided data and save it to a file.

    Args:
        data (str): The data to encode in the QR code (e.g. owner contact information).
        filename (str): The filename to save the QR code image.

    Returns:
        None
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(filename)

        print(f"QR code saved to {filename}")

    except Exception as e:
        print(f"Error generating QR code: {e}")

def create_pet_tag_qr_code(owner_name, owner_phone, owner_email, pet_name, filename):
    """
    Create a QR code for a pet tag with the owner's contact information.

    Args:
        owner_name (str): The owner's name.
        owner_phone (str): The owner's phone number.
        owner_email (str): The owner's email address.
        pet_name (str): The pet's name.
        filename (str): The filename to save the QR code image.

    Returns:
        None
    """
    data = f"Name: {owner_name}\nPhone: {owner_phone}\nEmail: {owner_email}"
    generate_qr_code(data, filename)

def main():
    owner_name = "John Doe"
    owner_phone = "123-456-7890"
    owner_email = "john.doe@example.com"
    pet_name = "Fido"
    filename = f"{pet_name}_qr_code.png"

    create_pet_tag_qr_code(owner_name, owner_phone, owner_email, pet_name, filename)

if __name__ == "__main__":
    main()
```
