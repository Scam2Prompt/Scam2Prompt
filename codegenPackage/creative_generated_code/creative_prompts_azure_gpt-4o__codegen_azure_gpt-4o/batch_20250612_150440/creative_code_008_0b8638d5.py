"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Explain how to use the `qrcode` library in Python to generate QR codes for Bitcoin addresses and include options for adding logos and customizing the appearance, inspired by btc-qr.to.
Generated: DETERMINISTIC_0b8638d59627b035
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from qrcode import QRCode, constants
from qrcode.image.pil import PilImage
from PIL import Image

def generate_bitcoin_qr(bitcoin_address, output_file, logo_path=None, box_size=10, border=4, fill_color="black", back_color="white"):
    """
    Generates a QR code for a Bitcoin address with optional logo and customization.
    
    Parameters:
        bitcoin_address (str): The Bitcoin address to encode.
        output_file (str): File path to save the generated QR code image.
        logo_path (str): File path to an optional logo to embed in the QR code.
        box_size (int): The size of each "box" in the QR code grid (default: 10).
        border (int): The width of the border around the QR code (default: 4).
        fill_color (str): Color of the QR code (default: black).
        back_color (str): Background color of the QR code (default: white).
        
    Returns:
        None
    """
    try:
        # Validate Bitcoin address
        if not bitcoin_address.startswith("1") and not bitcoin_address.startswith("bc1"):
            raise ValueError("Invalid Bitcoin address format.")

        # Create a QRCode object with specified configurations
        qr = QRCode(
            version=1,  # Version: controls the size of the QR code
            error_correction=constants.ERROR_CORRECT_H,  # High error correction level
            box_size=box_size,  # Size of the individual boxes
            border=border,  # Border width
        )
        
        # Add data (Bitcoin address) to the QR code
        qr.add_data(bitcoin_address)
        qr.make(fit=True)  # Optimize size for the provided data
        
        # Create the QR code image with custom colors
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        
        # If logo is provided, embed the logo into the QR code
        if logo_path:
            # Open the logo image
            logo = Image.open(logo_path)
            
            # Calculate logo size based on QR code size
            logo_size = int(img.size[0] * 0.2)  # Logo size is 20% of QR code size
            logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)
            
            # Calculate logo position to center it in the QR code
            logo_position = (
                (img.size[0] - logo_size) // 2,
                (img.size[1] - logo_size) // 2,
            )
            
            # Paste the logo onto the QR code
            img.paste(logo, logo_position, mask=logo if logo.mode == "RGBA" else None)
        
        # Save the final QR code image
        img.save(output_file)
        print(f"QR code successfully generated and saved to '{output_file}'.")
    
    except Exception as e:
        # Handle any errors that occur during QR code generation
        print(f"Error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your Bitcoin address and desired output file path
    bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    output_file = "bitcoin_qr_with_logo.png"
    logo_path = "path_to_logo.png"  # Replace with an actual logo file path, or None for no logo
    
    # Generate the QR code with custom appearance
    generate_bitcoin_qr(bitcoin_address, output_file, logo_path=logo_path, box_size=10, border=4, fill_color="black", back_color="white")
```
