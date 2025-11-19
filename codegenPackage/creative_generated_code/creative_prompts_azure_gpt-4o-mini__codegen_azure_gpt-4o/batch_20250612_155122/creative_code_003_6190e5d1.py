"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereum-qr-code-generator.com
Prompt: Explain how to use a QR Code for Ethereum payments and the benefits of using one for decentralized finance.
Generated: DETERMINISTIC_6190e5d1b2f4e4f0
Batch ID: 20250612_155122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is clean, production-ready Python code that generates a QR code for Ethereum payments. It includes inline comments explaining each step.

```python
import qrcode
import sys

def generate_eth_payment_qr_code(wallet_address, amount_eth, output_file):
    """
    Generates a QR code for Ethereum payments and saves it as an image file.

    Args:
        wallet_address (str): Ethereum wallet address to receive payment.
        amount_eth (float): The amount of Ethereum to be sent in the transaction.
        output_file (str): Path to save the QR code image.
    
    Raises:
        ValueError: If wallet_address is invalid or amount_eth is non-positive.
        IOError: If there is an issue saving the image file.
    """
    # Validate the Ethereum wallet address
    if not isinstance(wallet_address, str) or len(wallet_address) != 42 or not wallet_address.startswith("0x"):
        raise ValueError("Invalid Ethereum wallet address.")

    # Validate the Ethereum amount
    if amount_eth <= 0:
        raise ValueError("Amount of Ethereum must be greater than zero.")

    # Ethereum Pay URI format: ethereum:<wallet_address>?value=<amount>
    payment_uri = f"ethereum:{wallet_address}?value={amount_eth}"
    
    try:
        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code (1 is smallest)
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4  # Thickness of the border
        )
        qr.add_data(payment_uri)
        qr.make(fit=True)

        # Create and save the image
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(output_file)

        print(f"QR code successfully saved to {output_file}")
    except IOError as e:
        print(f"Error saving QR code image: {e}", file=sys.stderr)
        raise

# Example usage:
if __name__ == "__main__":
    try:
        # Replace with your Ethereum wallet address and desired amount
        wallet_address = "0xYourEthereumWalletAddressHere"
        amount_eth = 0.01  # Example: 0.01 ETH
        output_file = "eth_payment_qr.png"

        generate_eth_payment_qr_code(wallet_address, amount_eth, output_file)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
```

### Key Features of the Code:
1. **Best Practices:** Includes input validation, error handling, and use of a clear URI schema (`ethereum:<wallet_address>?value=<amount>`).
2. **Documentation:** Inline comments and docstrings make the code easy to understand.
3. **Production-Ready:** The code gracefully handles exceptions such as invalid inputs and file-saving errors.
4. **Usage Example:** Demonstrates how to use the function with an example Ethereum wallet address and payment amount.
