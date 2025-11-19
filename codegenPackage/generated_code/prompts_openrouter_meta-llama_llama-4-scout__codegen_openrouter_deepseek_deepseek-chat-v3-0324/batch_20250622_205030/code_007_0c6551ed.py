"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Design a Monero QR code with a custom image using a library like Python's Pillow.
Generated: DETERMINISTIC_0c6551ed50d442f5
Batch ID: 20250622_205030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageOps
import qrcode
from io import BytesIO

def create_monero_qr_with_logo(monero_address, logo_path, output_path, qr_size=300, logo_size=100):
    """
    Creates a Monero QR code with a custom logo embedded in the center.
    
    Args:
        monero_address (str): Monero wallet address to encode in QR code.
        logo_path (str): Path to the logo image file.
        output_path (str): Path to save the final QR code image.
        qr_size (int): Size of the QR code in pixels (default: 300).
        logo_size (int): Size of the logo in pixels (default: 100).
    """
    try:
        # Create basic QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(monero_address)
        qr.make(fit=True)
        
        # Generate QR code image
        qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        qr_img = qr_img.resize((qr_size, qr_size))
        
        # Open and resize logo
        logo = Image.open(logo_path).convert("RGBA")
        logo = logo.resize((logo_size, logo_size))
        
        # Create circular mask for logo
        mask = Image.new('L', (logo_size, logo_size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, logo_size, logo_size), fill=255)
        
        # Apply mask to logo
        logo = ImageOps.fit(logo, mask.size, centering=(0.5, 0.5))
        logo.putalpha(mask)
        
        # Calculate position to center logo on QR code
        pos = ((qr_img.size[0] - logo.size[0]) // 2,
               (qr_img.size[1] - logo.size[1]) // 2)
        
        # Paste logo onto QR code
        qr_img.paste(logo, pos, logo)
        
        # Save final image
        qr_img.save(output_path)
        print(f"QR code successfully saved to {output_path}")
        
    except FileNotFoundError:
        print(f"Error: Logo file not found at {logo_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    monero_address = "48jW3d3QYd4D5Qw5q51fX7VZ1c5J1rJ1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J1J
