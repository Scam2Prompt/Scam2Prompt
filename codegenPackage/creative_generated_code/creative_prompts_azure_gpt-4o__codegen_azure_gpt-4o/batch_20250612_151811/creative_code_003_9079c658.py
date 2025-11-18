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
"""
Program to generate QR codes for objects containing customizable contact information 
using the QRubi Light version (qrcode library in Python).
"""

import qrcode
import os

def generate_qr_code(data: dict, output_dir: str = "qr_codes", filename: str = "object_qr.png"):
    """
    Function to generate a QR code with customizable contact information.
    
    Args:
        data (dict): A dictionary containing contact information (e.g., name, email, phone, etc.).
        output_dir (str): Directory where the QR code image will be saved. Defaults to 'qr_codes'.
        filename (str): Name of the QR code image file. Defaults to 'object_qr.png'.
        
    Raises:
        ValueError: If the data dictionary is empty.
        IOError: If there is an issue saving the QR code image.
    """
    if not data:
        raise ValueError("Data dictionary is empty. Please provide contact information.")
    
    # Convert the dictionary data into a formatted string for QR code content
    qr_content = "\n".join([f"{key}: {value}" for key, value in data.items()])
    
    # Create a new QR code object
    qr = qrcode.QRCode(
        version=1,  # QR code version (size). '1' is smallest size.
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level: Low (L).
        box_size=10,  # Size of each box in the QR code.
        border=4,  # Border thickness (default is 4).
    )
    qr.add_data(qr_content)  # Add the contact information to the QR code
    qr.make(fit=True)  # Optimize size automatically
    
    # Generate the QR code image
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Define full path for the output file
    output_file = os.path.join(output_dir, filename)
    
    try:
        # Save the QR code image file
        qr_image.save(output_file)
        print(f"QR code successfully generated and saved at: {output_file}")
    except IOError as e:
        raise IOError(f"Unable to save QR code image: {e}")

# Example usage
if __name__ == "__main__":
    # Customizable contact information
    contact_info = {
        "Name": "John Doe",
        "Email": "john.doe@example.com",
        "Phone": "+123456789",
        "Company": "Doe Industries"
    }
    
    try:
        generate_qr_code(contact_info, filename="john_doe_qr.png")
    except Exception as e:
        print(f"An error occurred: {e}")
```
