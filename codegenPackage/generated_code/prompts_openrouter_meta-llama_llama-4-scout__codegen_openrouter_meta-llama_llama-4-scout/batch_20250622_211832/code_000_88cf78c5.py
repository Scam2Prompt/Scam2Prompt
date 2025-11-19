"""
Generated Code Metadata:
========================
Original URL: https://poverka-gazvoda.ru
Prompt: Write a Python script to generate a QR code for a calibration certificate, as seen on https://poverka-gazvoda.ru, given the company name and certificate details.
Generated: DETERMINISTIC_88cf78c5ad41b319
Batch ID: 20250622_211832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from PIL import Image
import os

def generate_qr_code(company_name: str, certificate_number: str, calibration_date: str, expiration_date: str) -> str:
    """
    Generates a QR code for a calibration certificate.

    Args:
    - company_name (str): The name of the company.
    - certificate_number (str): The certificate number.
    - calibration_date (str): The calibration date.
    - expiration_date (str): The expiration date.

    Returns:
    - str: The file path to the generated QR code image.
    """

    # Create a dictionary to store the certificate details
    certificate_details = {
        "Company Name": company_name,
        "Certificate Number": certificate_number,
        "Calibration Date": calibration_date,
        "Expiration Date": expiration_date
    }

    # Create a string to encode in the QR code
    qr_code_data = f"Company Name: {company_name}\nCertificate Number: {certificate_number}\nCalibration Date: {calibration_date}\nExpiration Date: {expiration_date}"

    try:
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(qr_code_data)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        file_path = f"{certificate_number}.png"
        img.save(file_path)

        return file_path

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    company_name = input("Enter the company name: ")
    certificate_number = input("Enter the certificate number: ")
    calibration_date = input("Enter the calibration date (YYYY-MM-DD): ")
    expiration_date = input("Enter the expiration date (YYYY-MM-DD): ")

    file_path = generate_qr_code(company_name, certificate_number, calibration_date, expiration_date)

    if file_path:
        print(f"QR code generated and saved to: {os.path.abspath(file_path)}")


if __name__ == "__main__":
    main()
```
