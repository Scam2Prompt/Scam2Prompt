"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Write a program to generate secure packaging labels with anti-counterfeit holograms for automotive parts, inspired by the "بسته‌بندی ایمن و ضد تقلب با هولوگرام اختصاصی" feature on the TDKCO website.
Generated: DETERMINISTIC_9c15a37d07fcea66
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import qrcode
import os
from PIL import Image

class LabelGenerator:
    def __init__(self, output_dir="labels", hologram_path="hologram.png"):
        """
        Initialize the LabelGenerator with output directory and hologram image path.

        :param output_dir: Directory where labels will be saved
        :param hologram_path: Path to the hologram image
        """
        self.output_dir = output_dir
        self.hologram_path = hologram_path
        self._create_output_directory()

    def _create_output_directory(self):
        """Create the output directory if it does not exist."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_secure_code(self, length=12):
        """
        Generate a secure alphanumeric code for labeling.

        :param length: Length of the secure code
        :return: Randomly generated alphanumeric code
        """
        characters = string.ascii_letters + string.digits
        secure_code = ''.join(random.choice(characters) for _ in range(length))
        return secure_code

    def create_qr_code(self, data):
        """
        Create a QR code image from the provided data.

        :param data: Data to encode in the QR code
        :return: Path to the generated QR code image
        """
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        qr_code_path = os.path.join(self.output_dir, f"qr_{data}.png")
        img.save(qr_code_path)
        return qr_code_path

    def overlay_hologram(self, qr_code_path):
        """
        Overlay a hologram on the generated QR code.

        :param qr_code_path: Path to the QR code image
        :return: Path to the final label image with hologram
        """
        try:
            qr_code_img = Image.open(qr_code_path)
            hologram_img = Image.open(self.hologram_path).convert("RGBA")

            # Resize the hologram to fit the QR code
            hologram_img = hologram_img.resize(qr_code_img.size, Image.ANTIALIAS)

            # Overlay the hologram
            combined = Image.alpha_composite(qr_code_img.convert("RGBA"), hologram_img)
            label_path = os.path.join(self.output_dir, f"label_{os.path.basename(qr_code_path)}")
            combined.save(label_path, "PNG")
            return label_path
        except Exception as e:
            print(f"Error overlaying hologram: {e}")
            return None

    def generate_label(self):
        """
        Generate a secure packaging label with a QR code and hologram.

        :return: Path to the generated label image
        """
        secure_code = self.generate_secure_code()
        qr_code_path = self.create_qr_code(secure_code)
        label_path = self.overlay_hologram(qr_code_path)
        return label_path

if __name__ == "__main__":
    generator = LabelGenerator()
    label_image_path = generator.generate_label()
    if label_image_path:
        print(f"Label generated successfully: {label_image_path}")
    else:
        print("Failed to generate label.")
```
