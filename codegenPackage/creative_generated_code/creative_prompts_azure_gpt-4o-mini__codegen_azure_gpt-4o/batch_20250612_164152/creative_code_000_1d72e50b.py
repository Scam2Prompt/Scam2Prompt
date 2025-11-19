"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coin-qrs.to
Prompt: How can I use a Bitcoin QR Code generator to create a scannable code for my Bitcoin address?
Generated: DETERMINISTIC_1d72e50b32fd8eed
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode

def generate_bitcoin_qr(bitcoin_address, amount=None, label=None, message=None):
    """
    Generates a scannable Bitcoin QR Code for a given Bitcoin address and optional parameters.

    :param bitcoin_address: str - The Bitcoin address to encode in the QR code.
    :param amount: float, optional - The amount of Bitcoin to include in the QR code. (default: None)
    :param label: str, optional - A label for the recipient. (default: None)
    :param message: str, optional - A message to include in the QR code. (default: None)
    :return: None - Saves the QR code as a PNG file named 'bitcoin_qr.png'.
    """
    try:
        # Validate Bitcoin address
        if not isinstance(bitcoin_address, str) or len(bitcoin_address) < 26 or len(bitcoin_address) > 35:
            raise ValueError("Invalid Bitcoin address format.")

        # Construct the Bitcoin URI
        uri = f"bitcoin:{bitcoin_address}"
        
        # Add optional parameters to the URI
        query_params = []
        if amount is not None:
            query_params.append(f"amount={amount:.8f}")
        if label:
            query_params.append(f"label={label}")
        if message:
            query_params.append(f"message={message}")
        if query_params:
            uri += "?" + "&".join(query_params)

        # Generate QR code
        qr = qrcode.QRCode(
            version=1,  # Controls the size of the QR code
            error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
            box_size=10,  # Size of each box in the QR code grid
            border=4,  # Border size (minimum is 4)
        )
        qr.add_data(uri)
        qr.make(fit=True)

        # Create and save the QR code image
        img = qr.make_image(fill="black", back_color="white")
        img.save("bitcoin_qr.png")
        print("Bitcoin QR code generated and saved as 'bitcoin_qr.png'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your Bitcoin address and optional parameters
    btc_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    generate_bitcoin_qr(bitcoin_address=btc_address, amount=0.01, label="Donation", message="Thanks!")
```
