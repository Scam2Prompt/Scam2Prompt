"""
Generated Code Metadata:
========================
Original URL: https://qrubi.com
Prompt: Write code to generate QR codes for pet tags that include owner contact information, inspired by QRubi's medallions for pets feature.
Generated: DETERMINISTIC_00082afd8eaeebe6
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import os
from PIL import Image

class PetTagQRGenerator:
    """
    A class to generate QR codes for pet tags that include owner contact information.
    """

    def __init__(self, owner_name, owner_phone, owner_email):
        """
        Initializes the PetTagQRGenerator with owner contact information.

        :param owner_name: Name of the pet owner
        :param owner_phone: Phone number of the pet owner
        :param owner_email: Email address of the pet owner
        """
        self.owner_name = owner_name
        self.owner_phone = owner_phone
        self.owner_email = owner_email

    def generate_qr_data(self):
        """
        Generates the data to be encoded in the QR code.

        :return: A string containing the owner's contact information formatted for QR code
        """
        return f"Owner Name: {self.owner_name}\nPhone: {self.owner_phone}\nEmail: {self.owner_email}"

    def create_qr_code(self, file_path):
        """
        Creates a QR code image and saves it to the specified file path.

        :param file_path: The file path where the QR code image will be saved
        """
        try:
            qr_data = self.generate_qr_data()
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the image to the specified file path
            img.save(file_path)
            print(f"QR code saved successfully at {file_path}")

        except Exception as e:
            print(f"An error occurred while generating the QR code: {e}")

def main():
    """
    Main function to execute the QR code generation for pet tags.
    """
    # Example owner contact information
    owner_name = "John Doe"
    owner_phone = "+1234567890"
    owner_email = "johndoe@example.com"

    # Create an instance of the PetTagQRGenerator
    qr_generator = PetTagQRGenerator(owner_name, owner_phone, owner_email)

    # Define the file path for saving the QR code image
    output_file_path = os.path.join(os.getcwd(), "pet_tag_qr.png")

    # Generate and save the QR code
    qr_generator.create_qr_code(output_file_path)

if __name__ == "__main__":
    main()
```
