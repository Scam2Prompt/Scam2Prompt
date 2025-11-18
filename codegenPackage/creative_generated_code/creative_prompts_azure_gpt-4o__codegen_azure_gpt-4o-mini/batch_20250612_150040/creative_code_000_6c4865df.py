"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qr.to
Prompt: Write a Python script to generate a QR code for a USDT wallet address using libraries like `qrcode`. Ensure the script supports multiple blockchain formats (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
Generated: DETERMINISTIC_6c4865df51ead9a3
Batch ID: 20250612_150040
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

def generate_qr_code(wallet_address, blockchain_type):
    """
    Generates a QR code for a given wallet address and blockchain type.

    Parameters:
        wallet_address (str): The wallet address to encode in the QR code.
        blockchain_type (str): The blockchain type (ERC-20, TRC-20, BEP-20, Omni, BEP-2).
    
    Returns:
        None: Saves the QR code as an image file.
    
    Raises:
        ValueError: If the wallet address or blockchain type is invalid.
    """
    # Define valid blockchain formats
    valid_blockchains = ['ERC-20', 'TRC-20', 'BEP-20', 'Omni', 'BEP-2']
    
    # Validate inputs
    if blockchain_type not in valid_blockchains:
        raise ValueError(f"Invalid blockchain type. Supported types: {', '.join(valid_blockchains)}")
    
    if not wallet_address:
        raise ValueError("Wallet address cannot be empty.")
    
    # Prepare QR code data format
    blockchain_prefixes = {
        'ERC-20': f"ethereum:{wallet_address}",
        'TRC-20': f"tronscan:{wallet_address}",
        'BEP-20': f"binance:{wallet_address}",
        'Omni': f"omni:{wallet_address}",
        'BEP-2': f"binance-chain:{wallet_address}"
    }
    
    # Create the QR code
    qr_data = blockchain_prefixes[blockchain_type]
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img_filename = f"{blockchain_type}_wallet_qr.png"
    img.save(img_filename)
    print(f"QR code generated and saved as '{img_filename}'")

if __name__ == "__main__":
    # User input for wallet address and blockchain type
    try:
        wallet_address = input("Enter the wallet address: ").strip()
        blockchain_type = input("Enter the blockchain type (ERC-20, TRC-20, BEP-20, Omni, BEP-2): ").strip()
        
        # Generate the QR code
        generate_qr_code(wallet_address, blockchain_type)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Make sure to install the required `qrcode` library before running this script:

```bash
pip install qrcode[pil]
```
