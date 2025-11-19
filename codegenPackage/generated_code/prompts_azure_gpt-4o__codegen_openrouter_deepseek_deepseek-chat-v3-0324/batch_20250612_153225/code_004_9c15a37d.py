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
import os
import hashlib
import qrcode
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import secrets
import string

class SecureLabelGenerator:
    """
    A class to generate secure packaging labels with anti-counterfeit holograms for automotive parts.
    """
    
    def __init__(self, output_dir="labels"):
        """
        Initialize the label generator with output directory.
        
        Args:
            output_dir (str): Directory to save generated labels. Defaults to "labels".
        """
        self.output_dir = output_dir
        self._create_output_dir()
        
    def _create_output_dir(self):
        """Create output directory if it doesn't exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def _generate_serial_number(self, length=16):
        """
        Generate a secure random serial number.
        
        Args:
            length (int): Length of the serial number. Defaults to 16.
            
        Returns:
            str: Generated serial number.
        """
        chars = string.ascii_uppercase + string.digits
        return ''.join(secrets.choice(chars) for _ in range(length))
    
    def _generate_hash(self, data):
        """
        Generate SHA-256 hash of the input data.
        
        Args:
            data (str): Data to hash.
            
        Returns:
            str: SHA-256 hash of the data.
        """
        return hashlib.sha256(data.encode()).hexdigest()
    
    def _generate_qr_code(self, data, filename):
        """
        Generate a QR code from the input data.
        
        Args:
            data (str): Data to encode in QR code.
            filename (str): Path to save the QR code image.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
    
    def _generate_hologram_overlay(self, width, height):
        """
        Generate a simple hologram effect overlay.
        
        Args:
            width (int): Width of the hologram.
            height (int): Height of the hologram.
            
        Returns:
            Image: Generated hologram overlay.
        """
        # Create a transparent image
        hologram = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(hologram)
        
        # Draw rainbow gradient circles to simulate hologram effect
        colors = [
            (255, 0, 0, 50),    # Red
            (255, 165, 0, 50),  # Orange
            (255, 255, 0, 50),  # Yellow
            (0, 255, 0, 50),    # Green
            (0, 0, 255, 50),    # Blue
            (75, 0, 130, 50),   # Indigo
            (238, 130, 238, 50) # Violet
        ]
        
        for i, color in enumerate(colors):
            radius = (i + 1) * 20
            draw.ellipse(
                [(width//2 - radius, height//2 - radius), 
                 (width//2 + radius, height//2 + radius)],
                outline=color,
                width=2
            )
        
        return hologram
    
    def generate_label(self, part_number, part_name, manufacturer, batch_number=None):
        """
        Generate a secure packaging label with anti-counterfeit features.
        
        Args:
            part_number (str): Part number/identifier.
            part_name (str): Name/description of the part.
            manufacturer (str): Manufacturer name.
            batch_number (str, optional): Batch/lot number. If None, will be generated.
            
        Returns:
            str: Path to the generated label image.
        """
        try:
            # Generate unique identifiers
            serial_number = self._generate_serial_number()
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            batch_number = batch_number or self._generate_serial_number(8)
            
            # Create verification data
            verification_data = f"{part_number}|{serial_number}|{batch_number}|{timestamp}"
            verification_hash = self._generate_hash(verification_data)
            
            # Create base label image
            label_width, label_height = 800, 500
            label = Image.new('RGB', (label_width, label_height), 'white')
            draw = ImageDraw.Draw(label)
            
            # Add border
            draw.rectangle([(10, 10), (label_width-10, label_height-10)], outline="black", width=2)
            
            # Add title
            font_large = ImageFont.truetype("arial.ttf", 24)
            font_medium = ImageFont.truetype("arial.ttf", 18)
            font_small = ImageFont.truetype("arial.ttf", 14)
            
            draw.text((label_width//2, 30), "SECURE AUTOMOTIVE PART", fill="black", font=font_large, anchor="mt")
            
            # Add part information
            y_offset = 80
            draw.text((50, y_offset), f"Part Number: {part_number}", fill="black", font=font_medium)
            draw.text((50, y_offset+30), f"Part Name: {part_name}", fill="black", font=font_medium)
            draw.text((50, y_offset+60), f"Manufacturer: {manufacturer}", fill="black", font=font_medium)
            draw.text((50, y_offset+90), f"Batch/Lot: {batch_number}", fill="black", font=font_medium)
            draw.text((50, y_offset+120), f"Serial: {serial_number}", fill="black", font=font_medium)
            
            # Generate and add QR code
            qr_filename = os.path.join(self.output_dir, f"qr_{serial_number}.png")
            self._generate_qr_code(verification_data, qr_filename)
            qr_img = Image.open(qr_filename)
            label.paste(qr_img, (label_width-200, y_offset))
            
            # Add verification hash
            draw.text((50, y_offset+150), f"Verification Hash:", fill="black", font=font_medium)
            draw.text((50, y_offset+180), verification_hash[:32], fill="black", font=font_small)
            draw.text((50, y_offset+200), verification_hash[32:], fill="black", font=font_small)
            
            # Add hologram overlay
            hologram = self._generate_hologram_overlay(label_width, label_height)
            label = Image.alpha_composite(label.convert('RGBA'), hologram).convert('RGB')
            
            # Add security notice
            draw.text((label_width//2, label_height-50), 
                     "This label contains security features to prevent counterfeiting",
                     fill="red", font=font_medium, anchor="mt")
            
            # Save the label
            output_path = os.path.join(self.output_dir, f"label_{part_number}_{serial_number}.png")
            label.save(output_path)
            
            return output_path
            
        except Exception as e:
            raise Exception(f"Error generating label: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        generator = SecureLabelGenerator()
        label_path = generator.generate_label(
            part_number="TDK-2023-001",
            part_name="Turbocharger Bearing",
            manufacturer="TDK Automotive"
        )
        print(f"Label generated successfully at: {label_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
