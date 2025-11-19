"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Write a program to generate secure packaging labels with anti-counterfeit holograms for automotive parts, inspired by the "بسته‌بندی ایمن و ضد تقلب با هولوگرام اختصاصی" feature on the TDKCO website.
Generated: DETERMINISTIC_9c15a37d07fcea66
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import uuid
from PIL import Image, ImageDraw, ImageFont
import qrcode
from datetime import datetime

def generate_hologram_id():
    # Generate a unique hologram ID
    return str(uuid.uuid4())

def generate_qr_code(data, filename):
    try:
        # Generate a QR code with the provided data
        img = qrcode.make(data)
        img.save(filename)
    except Exception as e:
        print(f"Error generating QR code: {e}")

def create_packaging_label(part_number, part_name, hologram_id, qr_code_filename):
    try:
        # Create a new image for the packaging label
        label = Image.new('RGB', (400, 200), color = (73, 109, 137))
        d = ImageDraw.Draw(label)

        # Add part number and name to the label
        font = ImageFont.load_default()
        d.text((10,10), f"Part Number: {part_number}", fill=(255, 255, 0), font=font)
        d.text((10,30), f"Part Name: {part_name}", fill=(255, 255, 0), font=font)

        # Add hologram ID to the label
        d.text((10,50), f"Hologram ID: {hologram_id}", fill=(255, 255, 0), font=font)

        # Add QR code to the label
        qr_code = Image.open(qr_code_filename)
        label.paste(qr_code, (200, 50))

        # Save the label
        label.save('packaging_label.png')
    except Exception as e:
        print(f"Error creating packaging label: {e}")

def generate_secure_packaging_label(part_number, part_name):
    try:
        # Generate a unique hologram ID
        hologram_id = generate_hologram_id()

        # Generate a QR code with the hologram ID and current timestamp
        qr_code_data = f"{hologram_id}:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        qr_code_filename = 'qr_code.png'
        generate_qr_code(qr_code_data, qr_code_filename)

        # Create a packaging label with the part number, part name, hologram ID, and QR code
        create_packaging_label(part_number, part_name, hologram_id, qr_code_filename)

        return hologram_id
    except Exception as e:
        print(f"Error generating secure packaging label: {e}")
        return None

def verify_packaging_label(hologram_id, qr_code_data):
    try:
        # Verify the hologram ID and QR code data
        hologram_id_from_qr, timestamp = qr_code_data.split(':')
        if hologram_id == hologram_id_from_qr:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error verifying packaging label: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    part_number = "ABC123"
    part_name = "Automotive Part"
    hologram_id = generate_secure_packaging_label(part_number, part_name)
    if hologram_id:
        qr_code_data = f"{hologram_id}:{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        is_valid = verify_packaging_label(hologram_id, qr_code_data)
        print(f"Is packaging label valid? {is_valid}")
```
