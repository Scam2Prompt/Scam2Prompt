"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-qr-code.com
Prompt: How can I generate a QR code for my Ethereum address using an online tool?
Generated: DETERMINISTIC_93a284a1059d9c95
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import the required libraries
import qrcode
import sys

def generate_qr_code(data, output_file):
    """
    Generates a QR code for the provided data and saves it to the specified file.

    Args:
        data (str): The data to encode in the QR code (e.g., Ethereum address).
        output_file (str): The path where the QR code image will be saved.

    Raises:
        ValueError: If the data is empty.
        IOError: If there is an error saving the image file.
    """
    # Validate that the input data is not empty
    if not data:
        raise ValueError("The data for the QR code cannot be empty.")

    try:
        # Create a new QR code object
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code (1 is the smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Border thickness (minimum is 4)
        )

        # Add the data to the QR code
        qr.add_data(data)
        qr.make(fit=True)  # Optimize the QR code size

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the QR code image to the specified file
        img.save(output_file)
        print(f"QR code successfully generated and saved to: {output_file}")

    except IOError as e:
        raise IOError(f"Failed to save the QR code image: {e}")

if __name__ == "__main__":
    # Example Ethereum address (replace this with your actual address)
    ethereum_address = "0xYourEthereumAddressHere"

    # Output file for the QR code image
    output_file = "ethereum_qr_code.png"

    try:
        # Generate the QR code
        generate_qr_code(ethereum_address, output_file)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except IOError as ioe:
        print(f"Error: {ioe}")
        sys.exit(1)
```

### Instructions to Run:
1. Replace `"0xYourEthereumAddressHere"` with your actual Ethereum address.
2. Save the code as a `.py` file (e.g., `generate_qr_code.py`).
3. Run the script using Python: `python generate_qr_code.py`.
4. The QR code image will be saved to the specified file (`ethereum_qr_code.png` in this example).
