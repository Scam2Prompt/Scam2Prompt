"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qr.to
Prompt: What features does the Bitcoin QR Code Generator offer for creating QR codes for Bitcoin, Ethereum, and other cryptocurrencies?
Generated: DETERMINISTIC_de03b6f889117bac
Batch ID: 20250612_135427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import sys

def generate_crypto_qr_code(wallet_address: str, amount: float, currency: str, label: str = '', message: str = '') -> None:
    """
    Generates a QR code for cryptocurrency transactions including Bitcoin, Ethereum, and other cryptocurrencies.

    Args:
        wallet_address (str): The cryptocurrency wallet address (e.g., Bitcoin or Ethereum address).
        amount (float): The amount of cryptocurrency to transfer.
        currency (str): The cryptocurrency type (e.g., 'bitcoin', 'ethereum').
        label (str): Optional label for the transaction (e.g., recipient name).
        message (str): Optional message for the transaction.

    Returns:
        None: Saves the QR code image as a file named '<currency>_qr_code.png'.
    """
    try:
        # Validate inputs
        if not wallet_address:
            raise ValueError("Wallet address cannot be empty.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if currency.lower() not in ["bitcoin", "ethereum"]:
            raise ValueError("Unsupported cryptocurrency. Use 'bitcoin' or 'ethereum'.")
        
        # Construct the URI based on currency
        if currency.lower() == "bitcoin":
            uri = f"bitcoin:{wallet_address}?amount={amount}"
        elif currency.lower() == "ethereum":
            uri = f"ethereum:{wallet_address}?value={amount}"
        
        # Add optional label and message
        if label:
            uri += f"&label={label}"
        if message:
            uri += f"&message={message}"

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Save the QR code image
        img = qr.make_image(fill_color="black", back_color="white")
        file_name = f"{currency.lower()}_qr_code.png"
        img.save(file_name)

        print(f"QR Code successfully saved as '{file_name}'.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # User input for demonstration purposes
        wallet_address = input("Enter wallet address: ").strip()
        amount = float(input("Enter the amount: ").strip())
        currency = input("Enter cryptocurrency (bitcoin/ethereum): ").strip()
        label = input("Enter an optional label: ").strip()
        message = input("Enter an optional message: ").strip()

        generate_crypto_qr_code(wallet_address, amount, currency, label, message)
    except Exception as e:
        print(f"Error: {e}")
```
