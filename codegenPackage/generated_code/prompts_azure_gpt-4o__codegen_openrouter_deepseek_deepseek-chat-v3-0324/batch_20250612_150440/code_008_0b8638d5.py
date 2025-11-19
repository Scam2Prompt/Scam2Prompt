"""
Generated Code Metadata:
========================
Original URL: https://btc-qr.to
Prompt: Explain how to use the `qrcode` library in Python to generate QR codes for Bitcoin addresses and include options for adding logos and customizing the appearance, inspired by btc-qr.to.
Generated: DETERMINISTIC_0b8638d59627b035
Batch ID: 20250612_150440
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
from PIL import Image, ImageDraw
import io
import os

def generate_bitcoin_qr(
    bitcoin_address: str,
    output_path: str = None,
    logo_path: str = None,
    size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white",
    rounded_corners: bool = False,
    gradient: bool = False,
    gradient_start: str = "blue",
    gradient_end: str = "cyan"
) -> Image.Image:
    """
    Generate a QR code for a Bitcoin address with optional logo and styling.
    
    Args:
        bitcoin_address: Bitcoin address to encode
        output_path: Path to save the QR code (None returns PIL Image)
        logo_path: Path to logo image to embed in center
        size: QR code size (1-40)
        border: Border size in modules
        fill_color: Main QR code color
        back_color: Background color
        rounded_corners: Use rounded modules
        gradient: Use radial gradient color
        gradient_start: Start color for gradient
        gradient_end: End color for gradient
        
    Returns:
        PIL.Image.Image or None if saved to file
    """
    try:
        # Validate Bitcoin address (basic check)
        if not (bitcoin_address.startswith('1') or 
                bitcoin_address.startswith('3') or 
                bitcoin_address.startswith('bc1')):
            raise ValueError("Invalid Bitcoin address format")
            
        if size < 1 or size > 40:
            raise ValueError("Size must be between 1 and 40")
            
        if border < 0:
            raise ValueError("Border must be positive")

        # Configure QR code
        qr = qrcode.QRCode(
            version=size,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=border,
        )
        qr.add_data(f"bitcoin:{bitcoin_address}")
        qr.make(fit=True)
        
        # Create image with optional styling
        img_kwargs = {
            'fill_color': fill_color,
            'back_color': back_color
        }
        
        if rounded_corners and gradient:
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                color_mask=RadialGradiantColorMask(
                    center_color=gradient_start,
                    edge_color=gradient_end
                )
            )
        elif rounded_corners:
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                **img_kwargs
            )
        elif gradient:
            img = qr.make_image(
                image_factory=StyledPilImage,
                color_mask=RadialGradiantColorMask(
                    center_color=gradient_start,
                    edge_color=gradient_end
                )
            )
        else:
            img = qr.make_image(**img_kwargs)
            
        # Add logo if provided
        if logo_path and os.path.exists(logo_path):
            logo = Image.open(logo_path)
            
            # Calculate logo size (20% of QR code size)
            logo_size = min(
                img.size[0] // 5,
                img.size[1] // 5,
                logo.size[0],
                logo.size[1]
            )
            
            # Resize logo
            logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Create circular mask for logo
            mask = Image.new('L', (logo_size, logo_size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, logo_size, logo_size), fill=255)
            
            # Paste logo in center
            pos = (
                (img.size[0] - logo_size) // 2,
                (img.size[1] - logo_size) // 2
            )
            img.paste(logo, pos, mask)
            
        # Save or return image
        if output_path:
            img.save(output_path)
            return None
        return img
        
    except Exception as e:
        raise Exception(f"Error generating QR code: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Generate basic QR code
        qr_img = generate_bitcoin_qr(
            bitcoin_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
            output_path="basic_qr.png"
        )
        
        # Generate QR with logo and styling
        generate_bitcoin_qr(
            bitcoin_address="3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5",
            output_path="styled_qr.png",
            logo_path="logo.png",  # Replace with actual logo path
            rounded_corners=True,
            gradient=True,
            gradient_start="#0d6efd",
            gradient_end="#0dcaf0"
        )
        
    except Exception as e:
        print(f"Error: {e}")
```
