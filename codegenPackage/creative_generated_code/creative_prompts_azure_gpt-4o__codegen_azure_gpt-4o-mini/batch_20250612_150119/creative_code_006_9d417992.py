"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdt-qrcode-generator.com
Prompt: Write a Python script that accepts a Tether address and blockchain type (Ethereum, Tron, Ton, Polygon, or BNB) as input and generates a corresponding USDT QR code.
Generated: DETERMINISTIC_9d4179921d844839
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import qrcode
import re

def is_valid_address(address: str, blockchain: str) -> bool:
    """
    Validate the provided Tether address based on the blockchain type.
    
    Parameters:
        address (str): The Tether address to validate.
        blockchain (str): The blockchain type (Ethereum, Tron, Ton, Polygon, BNB).
    
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Regular expressions for address validation
    address_patterns = {
        'Ethereum': r'^0x[a-fA-F0-9]{40}$',
        'Tron': r'^T[a-zA-Z0-9]{33}$',
        'Ton': r'^EQ[a-zA-Z0-9]{48}$',
        'Polygon': r'^0x[a-fA-F0-9]{40}$',  # Same as Ethereum
        'BNB': r'^0x[a-fA-F0-9]{40}$'       # Same as Ethereum
    }

    pattern = address_patterns.get(blockchain)
    if pattern:
        return re.match(pattern, address) is not None
    return False

def generate_usdt_qr_code(address: str, blockchain: str) -> None:
    """
    Generate a QR code for the given USDT address and blockchain type.
    
    Parameters:
        address (str): The Tether address to encode.
        blockchain (str): The blockchain type (Ethereum, Tron, Ton, Polygon, BNB).
    
    Raises:
        ValueError: If the blockchain type is invalid or the address is not valid.
    """
    # Validate blockchain type
    valid_blockchains = ['Ethereum', 'Tron', 'Ton', 'Polygon', 'BNB']
    if blockchain not in valid_blockchains:
        raise ValueError(f"Invalid blockchain type. Expected one of {valid_blockchains}")

    # Validate the address
    if not is_valid_address(address, blockchain):
        raise ValueError(f"Invalid address for blockchain {blockchain}: {address}")

    # Create the QR code
    qr_data = f"ethereum:{address}" if blockchain in ['Ethereum', 'Polygon', 'BNB'] else f"{blockchain.lower()}:{address}"
    qr = qrcode.make(qr_data)

    # Save the QR code as an image file
    qr_filename = f'usdt_qr_code_{blockchain.lower()}.png'
    qr.save(qr_filename)
    print(f"QR code generated and saved as {qr_filename}")

if __name__ == "__main__":
    try:
        # User input
        tether_address = input("Enter the Tether address: ").strip()
        blockchain_type = input("Enter the blockchain type (Ethereum, Tron, Ton, Polygon, BNB): ").strip()

        # Generate the QR code
        generate_usdt_qr_code(tether_address, blockchain_type)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
