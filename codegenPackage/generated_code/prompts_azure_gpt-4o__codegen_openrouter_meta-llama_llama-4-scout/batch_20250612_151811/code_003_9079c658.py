"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Develop a Python program to print QR codes for objects using the QRubi Light version, ensuring the QR code contains customizable contact information.
Generated: DETERMINISTIC_9079c6588c666c83
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import GappedSquareModuleDrawer
from PIL import Image
import os

def generate_qr_code(data, filename):
    """
    Generate a QR code with the provided data and save it to a file.

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str): The filename to save the QR code image.

    Returns:
        None
    """
    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        
        # Add data to the QR code instance
        qr.add_data(data)
        qr.make(fit=True)

        # Create an empty image
        img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=GappedSquareModuleDrawer())
        
        # Save the image to a file
        img_1.save(filename)

        print(f"QR code saved to {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")


def create_contact_qr_code(name, phone_number, email, filename):
    """
    Create a QR code containing contact information.

    Args:
        name (str): The name of the contact.
        phone_number (str): The phone number of the contact.
        email (str): The email address of the contact.
        filename (str): The filename to save the QR code image.

    Returns:
        None
    """
    try:
        # Create a string containing the contact information in vCard format
        contact_info = f"BEGIN:VCARD\nVERSION:3.0\nFN:{name}\nTEL:{phone_number}\nEMAIL:{email}\nEND:VCARD"

        # Generate the QR code
        generate_qr_code(contact_info, filename)

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    filename = input("Enter the filename to save the QR code (e.g., contact_qr_code.png): ")

    # Check if the filename has an image extension
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
        filename += '.png'

    create_contact_qr_code(name, phone_number, email, filename)


if __name__ == "__main__":
    main()
```
