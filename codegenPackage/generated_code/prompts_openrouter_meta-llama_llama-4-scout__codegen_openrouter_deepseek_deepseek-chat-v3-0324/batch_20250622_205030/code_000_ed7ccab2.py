"""
Generated Code Metadata:
========================
Original URL: https://usdt-qr.to
Prompt: Generate a Python code snippet to create a QR code for a USDT (ERC-20) address using a library like `qrcode`.
Generated: DETERMINISTIC_ed7ccab2f415f7d5
Batch ID: 20250622_205030
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
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

def generate_usdt_qr_code(address, output_file='usdt_qrcode.png'):
    """
    Generates a styled QR code for a USDT (ERC-20) address.
    
    Args:
        address (str): The USDT ERC-20 wallet address
        output_file (str): Output filename for the QR code image
        
    Returns:
        str: Path to the generated QR code image
    """
    try:
        # Validate the address (basic check)
        if not address or not isinstance(address, str) or len(address) != 42:
            raise ValueError("Invalid USDT ERC-20 address")
        
        # Construct the USDT payment URI
        usdt_uri = f"ethereum:{address}?token=USDT"
        
        # Configure QR code with styling
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        qr.add_data(usdt_uri)
        qr.make(fit=True)
        
        # Create styled image
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=RoundedModuleDrawer(),
            color_mask=RadialGradiantColorMask()
        )
        
        # Save the QR code
        img.save(output_file)
        return output_file
    
    except Exception as e:
        raise Exception(f"Error generating QR code: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        usdt_address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"  # Example address
        qr_file = generate_usdt_qr_code(usdt_address)
        print(f"QR code generated successfully: {qr_file}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
