"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Write code to generate QR codes for pet tags that include owner contact information, inspired by QRubi's medallions for pets feature.
Generated: DETERMINISTIC_00082afd8eaeebe6
Batch ID: 20250612_151811
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

class PetTagQRGenerator:
    """
    A class to generate QR codes for pet tags containing owner contact information.
    """

    def __init__(self, owner_name: str, owner_phone: str, owner_email: str):
        """
        Initializes the QR code generator with owner contact information.

        :param owner_name: Owner's name
        :param owner_phone: Owner's phone number
        :param owner_email: Owner's email address
        """
        self.owner_name = owner_name
        self.owner_phone = owner_phone
        self.owner_email = owner_email
        self.qr_data = self._generate_qr_data()

    def _generate_qr_data(self) -> str:
        """
        Generates the QR code data string based on owner's contact information.

        :return: A formatted string containing the owner's contact information.
        """
        return f"Name: {self.owner_name}\nPhone: {self.owner_phone}\nEmail: {self.owner_email}"

    def create_qr_code(self, file_path: str) -> None:
        """
        Creates a QR code and saves it to the specified file path.

        :param file_path: The file path where the QR code image will be saved
        :raises ValueError: If the file path is invalid or if the created QR code is not saved correctly
        """
        try:
            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(self.qr_data)
            qr.make(fit=True)

            # Create an image from the QR Code instance
            img = qr.make_image(fill_color="black", back_color="white")

            # Check if the directory exists, if not raise an error
            directory = os.path.dirname(file_path)
            if directory and not os.path.exists(directory):
                raise ValueError(f"The directory {directory} does not exist.")

            # Save the QR code image
            img.save(file_path)
        except Exception as e:
            raise ValueError(f"An error occurred while creating the QR code: {e}")

def main():
    # Example usage
    owner_name = "John Doe"
    owner_phone = "+1-234-567-8901"
    owner_email = "johndoe@example.com"

    # Create an instance of the QR code generator
    qr_generator = PetTagQRGenerator(owner_name, owner_phone, owner_email)

    # Define the filepath for saving the QR code
    file_path = "pet_tag_qr.png"

    # Generate and save the QR code
    try:
        qr_generator.create_qr_code(file_path)
        print(f"QR Code successfully created and saved to {file_path}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
