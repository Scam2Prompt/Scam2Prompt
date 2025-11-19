"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://id.stromkonto.net
Prompt: What are the steps to create a QR code for Grünstrom transactions using the features outlined on the Stromkonto site?
Generated: DETERMINISTIC_aa4a5ae9d0c99bc7
Batch ID: 20250612_135121
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

def create_qr_code(data: str, filename: str) -> None:
    """
    Generates a QR code from the given data and saves it to a specified file.

    Args:
        data (str): The data to be encoded in the QR code.
        filename (str): The filename where the QR code will be saved.

    Raises:
        ValueError: If the data is empty or if the filename is invalid.
        Exception: For any unexpected errors during QR code generation or saving.
    """
    # Validate input data
    if not data:
        raise ValueError("Data for QR code cannot be empty.")
    
    if not filename.endswith('.png'):
        raise ValueError("Filename must have a .png extension.")
    
    try:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img.save(filename)
        print(f"QR code saved as {filename}")

    except Exception as e:
        print(f"An error occurred while generating QR code: {e}")

if __name__ == "__main__":
    # Example data for Grünstrom transaction
    gruenstrom_data = "Example Grünstrom transaction data"
    output_filename = "gruenstrom_transaction_qr.png"

    # Create a QR code for the Grünstrom transaction
    create_qr_code(gruenstrom_data, output_filename)
```
