"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-qr.to
Prompt: Write a Python script to generate a QR code for a Bitcoin address using a library like `qrcode`. Include options to customize the color, size, and add a logo, similar to the features described on btc-qr.to.
Generated: DETERMINISTIC_d916342aa9a22703
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from PIL import Image

def generate_bitcoin_qr(
    bitcoin_address: str,
    output_file: str,
    fill_color: str = "black",
    back_color: str = "white",
    box_size: int = 10,
    border: int = 4,
    logo_path: str = None
):
    """
    Generates a QR code for a given Bitcoin address with customizable options.

    Args:
        bitcoin_address (str): The Bitcoin address to encode in the QR code.
        output_file (str): The file path where the QR code image will be saved.
        fill_color (str, optional): The color of the QR code blocks. Defaults to "black".
        back_color (str, optional): The background color of the QR code. Defaults to "white".
        box_size (int, optional): The size of each box in the QR code grid. Defaults to 10.
        border (int, optional): The width of the border (minimum 4). Defaults to 4.
        logo_path (str, optional): Path to a logo image to embed in the center of the QR code.
                                   Defaults to None (no logo).
    """
    try:
        # Validate Bitcoin address
        if not bitcoin_address:
            raise ValueError("Bitcoin address cannot be empty.")
        
        # Create QR code object with specified parameters
        qr = qrcode.QRCode(
            version=None,  # Automatically adjust version depending on data size
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for logo embedding
            box_size=box_size,
            border=border
        )
        
        # Add Bitcoin address data to the QR code
        qr.add_data(f"bitcoin:{bitcoin_address}")
        qr.make(fit=True)

        # Create the QR code image with specified colors
        img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

        # If a logo is provided, embed it in the QR code
        if logo_path:
            try:
                logo = Image.open(logo_path)
                
                # Resize the logo to fit in the center of the QR code
                logo_size = min(img.size) // 4  # Logo size is 1/4th of the QR code's size
                logo = logo.resize((logo_size, logo_size), Image.LANCZOS)
                
                # Calculate position to place the logo (centered)
                x_pos = (img.size[0] - logo_size) // 2
                y_pos = (img.size[1] - logo_size) // 2
                
                # Paste the logo on the QR code
                img.paste(logo, (x_pos, y_pos), mask=logo if logo.mode == "RGBA" else None)
            except Exception as e:
                raise ValueError(f"Error embedding logo: {e}")

        # Save the QR code image to the specified file
        img.save(output_file)
        print(f"QR code successfully saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    # Replace "your_bitcoin_address_here" with a valid Bitcoin address
    bitcoin_address = "your_bitcoin_address_here"
    output_file = "bitcoin_qr.png"
    logo_file = "logo.png"  # Set to None if no logo is required

    # Generate QR code with custom options
    generate_bitcoin_qr(
        bitcoin_address=bitcoin_address,
        output_file=output_file,
        fill_color="black",
        back_color="white",
        box_size=10,
        border=4,
        logo_path=logo_file
    )
```
