"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monero-qr-code-generator.com
Prompt: Provide code to generate a Monero QR code and save it as an image file, with the option to customize the design for use on social media or websites, as described on https://monero-qr-code-generator.com.
Generated: DETERMINISTIC_d51eae646e6a0149
Batch ID: 20250612_150040
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
from PIL import Image, ImageDraw, ImageFont

def generate_monero_qr(address, amount=None, label=None, message=None, customization=None, filename='monero_qr.png'):
    """
    Generates a Monero QR code for a given address and optional parameters.
    
    Parameters:
    - address (str): The Monero wallet address to encode.
    - amount (str, optional): The amount of Monero to include in the QR code.
    - label (str, optional): A label or description for the transaction.
    - message (str, optional): A message to include with the transaction.
    - customization (dict, optional): Customization options for the QR code design.
    - filename (str): The name of the file to save the QR code image.

    Returns:
    - None
    """
    try:
        # Basic validation of the address
        if not isinstance(address, str) or len(address) != 95:
            raise ValueError("Invalid Monero address. It must be 95 characters long.")
        
        # Constructing the Monero payment URI
        uri_parts = [f'monero:{address}']
        if amount:
            uri_parts.append(f'?amount={amount}')
        if label:
            uri_parts.append(f'&label={label}')
        if message:
            uri_parts.append(f'&message={message}')
        
        monero_uri = ''.join(uri_parts)
        
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(monero_uri)
        qr.make(fit=True)

        # Create the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Apply customization if provided
        if customization:
            img = customize_qr_code(img, customization)
        
        # Save the image
        img.save(filename)
        print(f"QR code saved as '{filename}'")

    except Exception as e:
        print(f"Error generating QR code: {e}")

def customize_qr_code(qr_image, customization):
    """
    Customizes the QR code image based on the provided options.
    
    Parameters:
    - qr_image (PIL.Image): The original QR code image.
    - customization (dict): Customization options for the QR code design.

    Returns:
    - PIL.Image: The customized QR code image.
    """
    # Create a drawing context
    draw = ImageDraw.Draw(qr_image)

    # Apply customizations
    if 'logo' in customization:
        logo_path = customization['logo']
        try:
            logo = Image.open(logo_path)
            logo_size = int(qr_image.size[0] / 4)  # Size of the logo
            logo = logo.resize((logo_size, logo_size), Image.ANTIALIAS)
            qr_image.paste(logo, ((qr_image.size[0] - logo_size) // 2, (qr_image.size[1] - logo_size) // 2), logo)
        except Exception as e:
            print(f"Error adding logo: {e}")

    if 'frame_color' in customization:
        draw.rectangle([(0, 0), qr_image.size], outline=customization['frame_color'], width=5)

    return qr_image

# Example usage
if __name__ == "__main__":
    # Example customization
    custom_options = {
        'logo': 'path/to/logo.png',  # Path to your logo image
        'frame_color': 'blue'         # Frame color
    }

    generate_monero_qr(
        address='44AFFH993rsVh3UeFj4qHh9nYkD3h6d6zY7gD2D4dZV4h8g1FyYX8D2p8t5A3yFQzXrG3k1e2yXU3yX5N7k6R9gQhP1C9dT',
        amount='0.5',
        label='My Monero Payment',
        message='Thank you for your support!',
        customization=custom_options,
        filename='monero_qr_custom.png'
    )
```
