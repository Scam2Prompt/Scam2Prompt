"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: Write Python code to generate a Bitcoin QR Code using a static Bitcoin address, referencing the functionality described on the "Bitcoin QR Code Generator" website.
Generated: DETERMINISTIC_89fcceb3dea2b494
Batch ID: 20250612_150440
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

def generate_bitcoin_qr_code(bitcoin_address, amount=None, label=None, message=None, output_file="bitcoin_qr.png"):
    """
    Generate a Bitcoin QR Code with optional parameters.

    Args:
        bitcoin_address (str): The Bitcoin address for the QR code.
        amount (float, optional): The amount to be included in the QR code. Defaults to None.
        label (str, optional): A label for the QR code (e.g., recipient's name). Defaults to None.
        message (str, optional): A message to include in the QR code. Defaults to None.
        output_file (str): The file name for the generated QR code image. Defaults to "bitcoin_qr.png".

    Returns:
        str: The file path of the generated QR code image.

    Raises:
        ValueError: If the Bitcoin address is missing or invalid.
    """
    # Validate the Bitcoin address
    if not bitcoin_address or not isinstance(bitcoin_address, str):
        raise ValueError("A valid Bitcoin address must be provided.")

    # Construct the Bitcoin URI
    bitcoin_uri = f"bitcoin:{bitcoin_address}"
    query_params = []

    if amount:
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        query_params.append(f"amount={amount}")

    if label:
        query_params.append(f"label={label}")

    if message:
        query_params.append(f"message={message}")

    if query_params:
        bitcoin_uri += "?" + "&".join(query_params)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # auto-adjusts the size based on data
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(bitcoin_uri)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code to the output file
    output_path = os.path.abspath(output_file)
    img.save(output_path)

    return output_path


# Example usage
if __name__ == "__main__":
    try:
        # Static Bitcoin address (you can replace it with your own)
        bitcoin_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
        
        # Optional parameters
        amount = 0.01  # Amount in BTC
        label = "Test Label"
        message = "Thank you for your support!"

        # Generate the QR code
        output_file = "bitcoin_qr_code.png"
        qr_code_path = generate_bitcoin_qr_code(bitcoin_address, amount, label, message, output_file)
        print(f"Bitcoin QR Code generated and saved to: {qr_code_path}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
