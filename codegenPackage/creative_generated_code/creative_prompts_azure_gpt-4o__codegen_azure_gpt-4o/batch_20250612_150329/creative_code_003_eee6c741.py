"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Create a Python script that generates an Ethereum QR code and saves it as an image file, as described on the Ethereum QR Code Generator site.
Generated: DETERMINISTIC_eee6c74194d6e98f
Batch ID: 20250612_150329
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

def generate_ethereum_qr(
    address, amount=None, gas=None, data=None, output_file="ethereum_qr.png"
):
    """
    Generates an Ethereum QR code from the given parameters and saves it as an image file.

    Args:
        address (str): The Ethereum address to encode in the QR code. Should be a valid Ethereum address.
        amount (str, optional): The amount of Ether to send (in ETH). Defaults to None.
        gas (str, optional): Gas limit for the transaction. Defaults to None.
        data (str, optional): Hexadecimal data payload for the transaction. Defaults to None.
        output_file (str, optional): The name of the output image file. Defaults to "ethereum_qr.png".

    Returns:
        str: The path to the saved QR code image.

    Raises:
        ValueError: If the Ethereum address is missing or invalid.
        IOError: If the image file cannot be saved.
    """
    # Validate Ethereum address (basic validation for length and prefix)
    if not address or not isinstance(address, str) or not address.startswith("0x") or len(address) != 42:
        raise ValueError("Invalid Ethereum address. Ensure it starts with '0x' and is 42 characters long.")

    # Construct the Ethereum URI
    uri = f"ethereum:{address}"
    query_params = []

    if amount:
        query_params.append(f"amount={amount}")
    if gas:
        query_params.append(f"gas={gas}")
    if data:
        query_params.append(f"data={data}")

    if query_params:
        uri += "?" + "&".join(query_params)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code grid
        border=4,  # Border size (minimum is 4)
    )
    qr.add_data(uri)
    qr.make(fit=True)

    # Create the image
    img = qr.make_image(fill_color="black", back_color="white")

    try:
        # Save the image
        img.save(output_file)
        return os.path.abspath(output_file)
    except IOError as e:
        raise IOError(f"Failed to save QR code image: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        ethereum_address = "0x1234567890abcdef1234567890abcdef12345678"
        ether_amount = "0.5"  # Amount in ETH (optional)
        gas_limit = "21000"  # Gas limit (optional)
        hex_data = "0x"  # Transaction data payload (optional)

        output_path = generate_ethereum_qr(
            address=ethereum_address,
            amount=ether_amount,
            gas=gas_limit,
            data=hex_data,
            output_file="eth_qr.png",
        )
        print(f"Ethereum QR code saved to: {output_path}")
    except Exception as e:
        print(f"Error: {e}")
```
