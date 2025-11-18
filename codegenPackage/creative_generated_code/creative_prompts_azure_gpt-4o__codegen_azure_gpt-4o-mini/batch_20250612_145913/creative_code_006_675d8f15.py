"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tc-harsewinkel.de
Prompt: Demonstrate how to use a QR code generator library in Python to create QR codes for logging into a member management system like "easyVerein."
Generated: DETERMINISTIC_675d8f15a7ee2506
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://easyverein.com/login?user=member123": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import qrcode  # Import the qrcode library for generating QR codes
import os      # Import os for file handling
import sys     # Import sys for error handling

def generate_qr_code(data: str, file_name: str) -> None:
    """
    Generates a QR code for the given data and saves it as an image file.

    :param data: The data to encode in the QR code (e.g., URL for login).
    :param file_name: The name of the file to save the QR code image.
    :raises ValueError: If the data is empty or file_name is not a valid string.
    """
    # Validate input data
    if not data:
        raise ValueError("Data for the QR code cannot be empty.")
    if not isinstance(file_name, str) or not file_name:
        raise ValueError("File name must be a non-empty string.")

    try:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code
            border=4,  # Thickness of the border (minimum is 4)
        )

        # Add data to the QR code
        qr.add_data(data)
        qr.make(fit=True)  # Adjust QR code size to the data

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a file
        img.save(file_name)
        print(f"QR code generated and saved as '{file_name}'.")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Example usage
    try:
        # Data for the QR code (a login URL for easyVerein)
        login_url = "https://easyverein.com/login?user=member123"
        file_name = "easyverein_login_qr.png"

        # Generate the QR code
        generate_qr_code(login_url, file_name)

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)
```
