"""
Generated Code Metadata:
========================
Original URL: https://usdt-qrcode-generator.com
Prompt: Write a Python script that accepts a Tether address and blockchain type (Ethereum, Tron, Ton, Polygon, or BNB) as input and generates a corresponding USDT QR code.
Generated: DETERMINISTIC_9d4179921d844839
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
import re

def is_valid_address(address: str, blockchain: str) -> bool:
    """
    Validate the Tether address based on the blockchain type.
    
    Args:
        address (str): The Tether address to validate.
        blockchain (str): The blockchain type (Ethereum, Tron, Ton, Polygon, BNB).
    
    Returns:
        bool: True if the address is valid, False otherwise.
    """
    # Define regex patterns for each blockchain type
    patterns = {
        'Ethereum': r'^0x[a-fA-F0-9]{40}$',
        'Tron': r'^T[a-zA-Z0-9]{33}$',
        'Ton': r'^EQ[a-zA-Z0-9]{48}$',
        'Polygon': r'^0x[a-fA-F0-9]{40}$',
        'BNB': r'^0x[a-fA-F0-9]{40}$'
    }
    
    # Check if the blockchain type is valid
    if blockchain not in patterns:
        raise ValueError("Invalid blockchain type. Choose from: Ethereum, Tron, Ton, Polygon, BNB.")
    
    # Validate the address using the corresponding regex pattern
    return re.match(patterns[blockchain], address) is not None

def generate_qr_code(address: str, blockchain: str) -> None:
    """
    Generate a QR code for the given Tether address and save it as an image file.
    
    Args:
        address (str): The Tether address.
        blockchain (str): The blockchain type.
    """
    # Create the QR code data string
    qr_data = f"{blockchain}:{address}"
    
    # Generate the QR code
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
    
    # Save the image to a file
    img_filename = f"{blockchain}_USDT_QR.png"
    img.save(img_filename)
    print(f"QR code generated and saved as {img_filename}")

def main():
    """
    Main function to execute the QR code generation process.
    """
    try:
        # Accept user input for address and blockchain type
        address = input("Enter the Tether address: ").strip()
        blockchain = input("Enter the blockchain type (Ethereum, Tron, Ton, Polygon, BNB): ").strip()
        
        # Validate the address
        if not is_valid_address(address, blockchain):
            print("Invalid Tether address for the specified blockchain type.")
            return
        
        # Generate the QR code
        generate_qr_code(address, blockchain)
        
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
