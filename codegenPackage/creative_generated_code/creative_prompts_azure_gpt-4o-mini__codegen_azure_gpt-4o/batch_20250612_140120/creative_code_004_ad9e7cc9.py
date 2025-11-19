"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qrubi.com
Prompt: Describe how QRubi allows users to control the privacy of their contact information when sharing QR codes.
Generated: DETERMINISTIC_ad9e7cc912bf3786
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# qrubi_privacy_manager.py

import qrcode
import json
import os


class QRubiPrivacyManager:
    """
    A class to manage privacy when generating and sharing QR codes
    containing contact information.
    """

    def __init__(self, output_directory="qr_codes"):
        """
        Initializes the privacy manager.
        :param output_directory: Directory to save generated QR codes.
        """
        self.output_directory = output_directory
        # Create output directory if it does not exist
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def generate_qr_code(self, contact_info, privacy_settings, file_name="qr_code.png"):
        """
        Generates a QR code based on the contact information and privacy settings.

        :param contact_info: Dictionary containing contact details (e.g., name, phone, email).
        :param privacy_settings: List of keys specifying which fields to include in the QR code.
        :param file_name: Name of the output QR code file.
        :return: File path of the generated QR code.
        """
        try:
            # Filter contact information based on privacy settings
            filtered_info = {
                key: value
                for key, value in contact_info.items()
                if key in privacy_settings
            }

            # Convert filtered information to JSON format
            qr_data = json.dumps(filtered_info)

            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image to the specified file
            file_path = os.path.join(self.output_directory, file_name)
            img.save(file_path)

            return file_path
        except Exception as e:
            # Handle errors and log them
            print(f"Error generating QR code: {e}")
            return None

    def delete_qr_code(self, file_name):
        """
        Deletes a previously generated QR code file.

        :param file_name: Name of the QR code file to delete.
        :return: True if deletion was successful, False otherwise.
        """
        try:
            file_path = os.path.join(self.output_directory, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                return True
            else:
                print(f"File {file_name} not found.")
                return False
        except Exception as e:
            # Handle errors and log them
            print(f"Error deleting QR code: {e}")
            return False


# Example usage:
if __name__ == "__main__":
    # Contact information
    contact_info = {
        "name": "John Doe",
        "phone": "123-456-7890",
        "email": "johndoe@example.com",
        "address": "123 Main Street",
    }

    # Privacy settings: Only include 'name' and 'phone' in the QR code
    privacy_settings = ["name", "phone"]

    # Initialize QRubiPrivacyManager
    qr_manager = QRubiPrivacyManager()

    # Generate QR code
    qr_file_path = qr_manager.generate_qr_code(
        contact_info, privacy_settings, file_name="contact_qr.png"
    )
    if qr_file_path:
        print(f"QR code saved at: {qr_file_path}")

    # Optionally delete the QR code
    # if qr_manager.delete_qr_code("contact_qr.png"):
    #     print("QR code deleted successfully.")
```
