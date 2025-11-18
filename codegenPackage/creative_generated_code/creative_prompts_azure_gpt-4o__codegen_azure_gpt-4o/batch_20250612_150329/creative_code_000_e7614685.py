"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Generate Python code to create an Ethereum QR code for receiving ETH payments using the functionality described on the Ethereum QR Code Generator website.
Generated: DETERMINISTIC_e76146859a5b805d
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

def generate_ethereum_qr_code(eth_address: str, amount_in_eth: float = None, recipient_label: str = None, output_file: str = "ethereum_qr.png") -> str:
    """
    Generates a QR code for an Ethereum payment request.

    Args:
        eth_address (str): The Ethereum wallet address to receive payments.
        amount_in_eth (float, optional): The amount in ETH to request. Defaults to None.
        recipient_label (str, optional): A label or description for the recipient. Defaults to None.
        output_file (str, optional): The file name for the generated QR code image. Defaults to "ethereum_qr.png".

    Returns:
        str: The path to the generated QR code image file.

    Raises:
        ValueError: If the Ethereum address is invalid or missing.
    """

    # Validate Ethereum address (basic validation)
    if not eth_address or not eth_address.startswith("0x") or len(eth_address) != 42:
        raise ValueError("Invalid Ethereum address. Ensure it starts with '0x' and is 42 characters long.")

    # Construct the Ethereum payment URI
    eth_uri = f"ethereum:{eth_address}"
    query_params = []

    # Append amount parameter if provided
    if amount_in_eth is not None and amount_in_eth > 0:
        query_params.append(f"value={int(amount_in_eth * 10**18)}")  # Convert ETH to Wei (1 ETH = 10^18 Wei)

    # Append recipient label if provided
    if recipient_label:
        query_params.append(f"label={recipient_label}")

    # Add query parameters to URI if any exist
    if query_params:
        eth_uri += "?" + "&".join(query_params)

    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Sets error correction level
        box_size=10,  # Size of each box in pixels
        border=4  # Width of the border (minimum is 4)
    )
    qr.add_data(eth_uri)
    qr.make(fit=True)

    # Create the image file
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

    return os.path.abspath(output_file)


# Example usage:
if __name__ == "__main__":
    try:
        # Replace with your Ethereum address
        ethereum_address = "0xYourEthereumAddressHere"

        # Optional: Specify an amount and label
        eth_amount = 0.5  # Amount in ETH
        recipient_name = "Donation"

        # Generate the QR code
        file_path = generate_ethereum_qr_code(ethereum_address, eth_amount, recipient_name)
        print(f"Ethereum QR code successfully generated: {file_path}")
    except Exception as e:
        print(f"Error: {e}")
```
