"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Develop a tool that converts URLs into QR codes without displaying the link, similar to the free tool featured on コピーツールラボ.
Generated: DETERMINISTIC_a90c7ab8c43e025a
Batch ID: 20250612_163659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com": {
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
import qrcode
import sys

def generate_qr_code(url, output_file="qrcode.png"):
    """
    Generates a QR code from a given URL and saves it as an image file.

    Parameters:
        url (str): The URL to be converted into a QR code.
        output_file (str): The name of the output image file. Default is 'qrcode.png'.

    Returns:
        None
    """
    try:
        # Validate URL input
        if not url or not isinstance(url, str):
            raise ValueError("Invalid URL provided. Please input a valid string.")

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,  # Controls size of QR code. Higher version = larger code.
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Border size (minimum is 4 per spec)
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to the specified output file
        img.save(output_file)
        print(f"QR code generated and saved to: {output_file}")

    except Exception as e:
        print(f"Error occurred while generating QR code: {e}")
        sys.exit(1)


if __name__ == "__main__":
    import argparse

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Convert URLs into QR codes.")
    parser.add_argument(
        "url", type=str, help="The URL to be converted into a QR code."
    )
    parser.add_argument(
        "-o", "--output", type=str, default="qrcode.png",
        help="The output file name to save the QR code image (default: qrcode.png)."
    )

    args = parser.parse_args()

    # Call the function to generate the QR code
    generate_qr_code(args.url, args.output)
```

### Usage:
1. Save this code to a `.py` file (e.g., `generate_qr_code.py`).
2. Run the script from the command line, passing the URL and optional output file name:
   ```
   python generate_qr_code.py "https://example.com" -o "example_qrcode.png"
   ```
3. The QR code image will be saved to the specified file (default is `qrcode.png` if no output file is provided).
