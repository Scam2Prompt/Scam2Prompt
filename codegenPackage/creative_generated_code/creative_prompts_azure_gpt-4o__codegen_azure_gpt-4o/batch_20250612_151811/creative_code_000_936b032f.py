"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Write Python code to generate a QR code that includes contact information, such as phone number and email, for use with the QRubi platform.
Generated: DETERMINISTIC_936b032fa31af15d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import qrcode  # Module for generating QR codes
import os      # Module for handling file paths and directories

def generate_contact_qr(output_file, name, phone, email):
    """
    Generate a QR code containing contact information and save it as an image file.
    
    Args:
        output_file (str): The path to save the generated QR code image.
        name (str): Name of the contact.
        phone (str): Phone number of the contact.
        email (str): Email address of the contact.
    
    Raises:
        ValueError: If any of the inputs are invalid.
        FileNotFoundError: If the output directory does not exist.
    """
    # Validate inputs
    if not name or not phone or not email:
        raise ValueError("Name, phone, and email must be provided and non-empty.")
    if not os.path.isdir(os.path.dirname(output_file)):
        raise FileNotFoundError(f"The directory '{os.path.dirname(output_file)}' does not exist.")
    
    # Prepare contact information for QR code
    contact_info = f"Name: {name}\nPhone: {phone}\nEmail: {email}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # Version of the QR Code (1-40, higher = larger capacity)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4     # Border size (minimum is 4)
    )
    qr.add_data(contact_info)  # Add contact information to the QR code
    qr.make(fit=True)          # Finalize QR code creation
    
    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to the specified file
    img.save(output_file)
    print(f"QR code successfully saved to {output_file}")


# Example usage of the function
if __name__ == "__main__":
    try:
        # Replace these values with actual contact details and desired output file
        name = "John Doe"
        phone = "+1234567890"
        email = "john.doe@example.com"
        output_file = "output/contact_qr.png"

        # Generate the contact QR code
        generate_contact_qr(output_file, name, phone, email)
    except Exception as e:
        print(f"Error: {e}")
```
