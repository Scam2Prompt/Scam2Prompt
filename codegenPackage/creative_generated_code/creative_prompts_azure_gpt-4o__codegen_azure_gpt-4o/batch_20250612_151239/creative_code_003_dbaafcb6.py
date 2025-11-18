"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Write code to convert a URL into a QR code using a free tool, as described in the "URLをQRコードに変換する無料ツール" section of コピーツールラボ.
Generated: DETERMINISTIC_dbaafcb675b5b42a
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
from qrcode.exceptions import DataOverflowError
import sys

def generate_qr_code(url, output_file):
    """
    Generate a QR code from a URL and save it to a file.

    Args:
        url (str): The URL to be converted into a QR code.
        output_file (str): The path of the file where the QR code image will be saved.

    Returns:
        None
    """
    try:
        # Validate URL input
        if not url or not isinstance(url, str):
            raise ValueError("Invalid URL. Please provide a valid URL as a string.")

        # Create a QR code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR Code (1 is the smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4  # Border size (minimum value is 4)
        )

        # Add the URL data to the QR code object
        qr.add_data(url)
        qr.make(fit=True)  # Optimize the QR code size based on the input data

        # Generate QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to the specified file
        img.save(output_file)
        print(f"QR Code successfully saved to: {output_file}")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except DataOverflowError as doe:
        print(f"DataOverflowError: The URL provided exceeds the maximum data capacity for the QR code.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    # Ensure the URL and output file path are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python generate_qr_code.py <URL> <output_file>")
        sys.exit(1)

    url = sys.argv[1]
    output_file = sys.argv[2]

    generate_qr_code(url, output_file)
```

This script uses the `qrcode` Python library to generate a QR code from a given URL and save it to a file. Users can run it via the command line, providing the URL and the output file path as arguments. It includes error handling for invalid inputs and unexpected issues.
