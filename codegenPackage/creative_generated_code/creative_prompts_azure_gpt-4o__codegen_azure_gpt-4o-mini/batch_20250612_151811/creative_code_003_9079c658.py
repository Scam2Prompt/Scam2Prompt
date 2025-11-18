"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Develop a Python program to print QR codes for objects using the QRubi Light version, ensuring the QR code contains customizable contact information.
Generated: DETERMINISTIC_9079c6588c666c83
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import os

def generate_qr_code(contact_info, file_path):
    """
    Generate a QR code for the given contact information and save it to the specified file path.

    Args:
        contact_info (str): The contact information to encode in the QR code.
        file_path (str): The file path where the QR code image will be saved.

    Raises:
        ValueError: If contact_info is empty or file_path is invalid.
        Exception: For any other issues during QR code generation or saving.
    """
    if not contact_info:
        raise ValueError("Contact information cannot be empty.")
    
    if not isinstance(file_path, str) or not file_path.endswith('.png'):
        raise ValueError("File path must be a valid string ending with '.png'.")

    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=4,  # Thickness of the border
        )

        # Add data to the QR code
        qr.add_data(contact_info)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill='black', back_color='white')

        # Save the QR code image to the specified file path
        img.save(file_path)
        print(f"QR code saved to {file_path}")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {str(e)}")

def main():
    """
    Main function to execute the QR code generation process.
    Prompts the user for contact information and saves the QR code.
    """
    # Prompt user for contact information
    contact_info = input("Enter the contact information (e.g., name, phone, email): ").strip()
    file_path = input("Enter the file path to save the QR code (must end with .png): ").strip()

    # Generate the QR code
    generate_qr_code(contact_info, file_path)

if __name__ == "__main__":
    main()
```

### Requirements
To run this code, you will need to install the `qrcode` library, which can be done using pip:

```bash
pip install qrcode[pil]
```

Ensure to run the program in an environment where you have permission to create files at the specified `file_path`.
