"""
Generated Code Metadata:
========================
Original URL: https://usdt-qr.to
Prompt: Provide an example of how to use the `qrcode` Python library to generate a QR code for a Tether (USDT) wallet address and explain how to ensure the QR code works across blockchain formats like ERC-20, TRC-20, BEP-20, Omni, and BEP-2.
Generated: DETERMINISTIC_6619341d74e603f8
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L

def generate_usdt_qr_code(wallet_address: str, network: str = "ERC-20", amount: float = None, filename: str = "usdt_qr.png"):
    """
    Generates a QR code for a USDT wallet address with optional network and amount.
    
    Args:
        wallet_address (str): The USDT wallet address.
        network (str): The blockchain network (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
        amount (float, optional): The amount of USDT to transfer. Defaults to None.
        filename (str, optional): Output filename for the QR code. Defaults to "usdt_qr.png".
    
    Raises:
        ValueError: If wallet_address is empty or network is invalid.
    """
    if not wallet_address:
        raise ValueError("Wallet address cannot be empty.")
    
    valid_networks = ["ERC-20", "TRC-20", "BEP-20", "Omni", "BEP-2"]
    if network not in valid_networks:
        raise ValueError(f"Invalid network. Must be one of: {', '.join(valid_networks)}")
    
    # Construct URI based on network
    if network == "ERC-20":
        uri = f"ethereum:{wallet_address}"
    elif network == "TRC-20":
        uri = f"tron:{wallet_address}"
    elif network == "BEP-20":
        uri = f"binance:{wallet_address}"
    elif network == "Omni":
        uri = f"bitcoin:{wallet_address}"
    elif network == "BEP-2":
        uri = f"bnb:{wallet_address}"
    
    # Add amount if specified
    if amount is not None:
        uri += f"?amount={amount}"
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(uri)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
if __name__ == "__main__":
    try:
        generate_usdt_qr_code(
            wallet_address="0x742d35Cc6634C0532925a3b844Bc454e4438f44e",
            network="ERC-20",
            amount=100.0,
            filename="usdt_erc20_qr.png"
        )
    except ValueError as e:
        print(f"Error generating QR code: {e}")
```
