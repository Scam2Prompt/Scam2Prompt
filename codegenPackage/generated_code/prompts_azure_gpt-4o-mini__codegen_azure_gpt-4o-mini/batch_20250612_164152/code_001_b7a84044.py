"""
Generated Code Metadata:
========================
Original URL: https://usdt-qr.to
Prompt: Write a script that takes a USDT wallet address and creates a QR code for ERC-20, TRC-20, BEP-20, Omni, or BEP-2 using the USDT QR Code Generator.
Generated: DETERMINISTIC_b7a84044a7b3a79a
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import sys

def generate_usdt_qr(wallet_address, network):
    """
    Generates a QR code for a given USDT wallet address on the specified network.

    Parameters:
    wallet_address (str): The USDT wallet address.
    network (str): The network type ('ERC20', 'TRC20', 'BEP20', 'Omni', 'BEP2').

    Returns:
    None: Saves the QR code as an image file.
    """
    # Validate the network type
    valid_networks = ['ERC20', 'TRC20', 'BEP20', 'Omni', 'BEP2']
    if network not in valid_networks:
        raise ValueError(f"Invalid network type. Choose from: {', '.join(valid_networks)}")

    # Create the QR code data string based on the network
    if network == 'ERC20':
        qr_data = f"ethereum:{wallet_address}"
    elif network == 'TRC20':
        qr_data = f"tronscan:{wallet_address}"
    elif network == 'BEP20':
        qr_data = f"binance:{wallet_address}"
    elif network == 'Omni':
        qr_data = f"omni:{wallet_address}"
    elif network == 'BEP2':
        qr_data = f"bep2:{wallet_address}"

    # Generate the QR code
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_data)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image
        img_filename = f"usdt_qr_{network.lower()}.png"
        img.save(img_filename)
        print(f"QR code generated and saved as {img_filename}")

    except Exception as e:
        print(f"An error occurred while generating the QR code: {e}")

if __name__ == "__main__":
    # Check for correct number of command line arguments
    if len(sys.argv) != 3:
        print("Usage: python generate_usdt_qr.py <wallet_address> <network>")
        sys.exit(1)

    # Extract wallet address and network from command line arguments
    wallet_address = sys.argv[1]
    network = sys.argv[2]

    # Generate the QR code
    try:
        generate_usdt_qr(wallet_address, network)
    except ValueError as ve:
        print(ve)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```

### Usage
To run the script, use the following command in your terminal:
```bash
python generate_usdt_qr.py <wallet_address> <network>
```
Replace `<wallet_address>` with the actual USDT wallet address and `<network>` with one of the following: `ERC20`, `TRC20`, `BEP20`, `Omni`, or `BEP2`.
