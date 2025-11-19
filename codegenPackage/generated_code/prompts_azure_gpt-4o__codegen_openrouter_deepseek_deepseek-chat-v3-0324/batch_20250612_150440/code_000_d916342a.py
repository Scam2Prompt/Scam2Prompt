"""
Generated Code Metadata:
========================
Original URL: https://btc-qr.to
Prompt: Write a Python script to generate a QR code for a Bitcoin address using a library like `qrcode`. Include options to customize the color, size, and add a logo, similar to the features described on btc-qr.to.
Generated: DETERMINISTIC_d916342aa9a22703
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
import argparse
import os
from PIL import Image, ImageDraw, ImageFont
import sys


def validate_bitcoin_address(address):
    """Basic validation for Bitcoin address format."""
    if not address:
        raise ValueError("Bitcoin address cannot be empty")
    if not isinstance(address, str):
        raise ValueError("Bitcoin address must be a string")
    if len(address) < 26 or len(address) > 35:
        raise ValueError("Invalid Bitcoin address length")
    return True


def generate_qr_code(
    bitcoin_address,
    output_file="bitcoin_qr.png",
    size=10,
    border=4,
    fill_color="black",
    back_color="white",
    rounded=False,
    gradient=False,
    logo_path=None,
    text=None,
    text_color="black",
):
    """
    Generate a QR code for a Bitcoin address with customization options.
    
    Args:
        bitcoin_address (str): Bitcoin address to encode
        output_file (str): Output file path
        size (int): QR code size (1-40)
        border (int): Border size in modules
        fill_color (str): Main QR code color
        back_color (str): Background color
        rounded (bool): Use rounded modules
        gradient (bool): Use radial gradient color
        logo_path (str): Path to logo image to embed
        text (str): Text to add below QR code
        text_color (str): Color of the text
    """
    try:
        validate_bitcoin_address(bitcoin_address)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=size,
            border=border,
        )
        qr.add_data(f"bitcoin:{bitcoin_address}")
        qr.make(fit=True)
        
        img_kwargs = {
            "fill_color": fill_color,
            "back_color": back_color,
        }
        
        if rounded or gradient:
            img_kwargs["image_factory"] = StyledPilImage
            if rounded:
                img_kwargs["module_drawer"] = RoundedModuleDrawer()
            if gradient:
                img_kwargs["color_mask"] = RadialGradiantColorMask(
                    center_color=fill_color,
                    edge_color=back_color
                )
        
        img = qr.make_image(**img_kwargs)
        
        # Add logo if provided
        if logo_path:
            try:
                logo = Image.open(logo_path)
                base_width = min(img.size[0] // 4, logo.size[0])
                wpercent = (base_width / float(logo.size[0]))
                hsize = int((float(logo.size[1]) * float(wpercent)))
                logo = logo.resize((base_width, hsize), Image.Resampling.LANCZOS)
                
                pos = (
                    (img.size[0] - logo.size[0]) // 2,
                    (img.size[1] - logo.size[1]) // 2
                )
                img.paste(logo, pos)
            except Exception as e:
                print(f"Error adding logo: {e}", file=sys.stderr)
        
        # Add text if provided
        if text:
            try:
                draw = ImageDraw.Draw(img)
                font = ImageFont.load_default()
                text_width = draw.textlength(text, font=font)
                text_position = (
                    (img.size[0] - text_width) // 2,
                    img.size[1] - 20
                )
                draw.text(text_position, text, fill=text_color, font=font)
            except Exception as e:
                print(f"Error adding text: {e}", file=sys.stderr)
        
        img.save(output_file)
        print(f"QR code successfully generated and saved to {output_file}")
        
    except Exception as e:
        print(f"Error generating QR code: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate a Bitcoin QR code")
    parser.add_argument("address", help="Bitcoin address to encode")
    parser.add_argument("-o", "--output", default="bitcoin_qr.png", help="Output file path")
    parser.add_argument("-s", "--size", type=int, default=10, help="QR code size (1-40)")
    parser.add_argument("-b", "--border", type=int, default=4, help="Border size in modules")
    parser.add_argument("-f", "--fill-color", default="black", help="Main QR code color")
    parser.add_argument("-c", "--back-color", default="white", help="Background color")
    parser.add_argument("-r", "--rounded", action="store_true", help="Use rounded modules")
    parser.add_argument("-g", "--gradient", action="store_true", help="Use radial gradient color")
    parser.add_argument("-l", "--logo", help="Path to logo image to embed")
    parser.add_argument("-t", "--text", help="Text to add below QR code")
    parser.add_argument("--text-color", default="black", help="Color of the text")
    
    args = parser.parse_args()
    
    generate_qr_code(
        bitcoin_address=args.address,
        output_file=args.output,
        size=args.size,
        border=args.border,
        fill_color=args.fill_color,
        back_color=args.back_color,
        rounded=args.rounded,
        gradient=args.gradient,
        logo_path=args.logo,
        text=args.text,
        text_color=args.text_color,
    )


if __name__ == "__main__":
    main()
```
