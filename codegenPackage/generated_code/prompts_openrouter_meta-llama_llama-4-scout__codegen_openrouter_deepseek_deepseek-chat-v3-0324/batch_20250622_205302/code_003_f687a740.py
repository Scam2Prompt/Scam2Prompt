"""
Generated Code Metadata:
========================
Original URL: https://bitcoinqr.io
Prompt: Explain the role of QR codes in simplifying Bitcoin transactions, including their structure, encoding, and significance in representing Bitcoin addresses.
Generated: DETERMINISTIC_f687a74056a00fbe
Batch ID: 20250622_205302
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
import base58
import hashlib

class BitcoinQRCodeGenerator:
    """
    A class to generate QR codes for Bitcoin addresses and transaction information.
    Handles address validation, QR code generation, and proper URI formatting.
    """
    
    def __init__(self):
        self.bitcoin_prefix = "bitcoin:"
    
    def validate_bitcoin_address(self, address: str) -> bool:
        """
        Validates a Bitcoin address using Base58Check decoding.
        
        Args:
            address: The Bitcoin address to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            decoded = base58.b58decode_check(address)
            return len(decoded) == 21 and decoded[0] in [0x00, 0x05]  # Mainnet addresses
        except (ValueError, IndexError):
            return False
    
    def generate_payment_uri(self, address: str, amount: float = None, label: str = None, message: str = None) -> str:
        """
        Generates a Bitcoin payment URI according to BIP21.
        
        Args:
            address: Valid Bitcoin address
            amount: Optional amount in BTC
            label: Optional label for the payment
            message: Optional message for the payment
            
        Returns:
            str: Formatted Bitcoin payment URI
        """
        if not self.validate_bitcoin_address(address):
            raise ValueError("Invalid Bitcoin address")
        
        uri = f"{self.bitcoin_prefix}{address}"
        params = []
        
        if amount is not None:
            params.append(f"amount={amount}")
        if label is not None:
            params.append(f"label={label}")
        if message is not None:
            params.append(f"message={message}")
        
        if params:
            uri += "?" + "&".join(params)
        
        return uri
    
    def generate_qr_code(self, data: str, output_file: str = None, box_size: int = 10, border: int = 4) -> qrcode.QRCode:
        """
        Generates a QR code from the given data.
        
        Args:
            data: The data to encode in the QR code
            output_file: Optional path to save the QR code image
            box_size: Size of each box in the QR code
            border: Border size around the QR code
            
        Returns:
            qrcode.QRCode: The generated QR code object
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=ERROR_CORRECT_L,
            box_size=box_size,
            border=border,
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        if output_file:
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(output_file)
        
        return qr

# Example usage
if __name__ == "__main__":
    qr_generator = BitcoinQRCodeGenerator()
    
    # Example Bitcoin address (replace with real one)
    test_address = "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"
    
    try:
        # Generate payment URI
        payment_uri = qr_generator.generate_payment_uri(
            address=test_address,
            amount=0.01,
            label="Donation",
            message="Thank you!"
        )
        
        print(f"Bitcoin Payment URI: {payment_uri}")
        
        # Generate and save QR code
        qr_generator.generate_qr_code(
            data=payment_uri,
            output_file="bitcoin_payment.png"
        )
        print("QR code generated successfully as bitcoin_payment.png")
        
    except ValueError as e:
        print(f"Error: {e}")
```
