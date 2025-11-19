"""
Generated Code Metadata:
========================
Original URL: https://usdt-qrcode-generator.com
Prompt: Describe how to use the USDT QR Code Generator for creating QR codes that support multiple blockchains like Ton and Ethereum.
Generated: DETERMINISTIC_d4ac4390848316f6
Batch ID: 20250612_164210
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for a USDT QR Code Generator that supports multiple blockchains:

```python
import qrcode
from qrcode.constants import ERROR_CORRECT_L
from typing import Optional, Dict

class USDTQRGenerator:
    """
    Generates USDT payment QR codes for multiple blockchains.
    Supported blockchains: TON, Ethereum, TRON, etc.
    """
    
    # Supported blockchain URI schemes
    BLOCKCHAIN_URI_SCHEMES = {
        'ethereum': 'ethereum:{address}?amount={amount}',
        'ton': 'ton://transfer/{address}?amount={amount}',
        'tron': 'tron:{address}?amount={amount}',
    }
    
    def __init__(self, blockchain: str = 'ethereum'):
        """
        Initialize QR generator for a specific blockchain.
        
        Args:
            blockchain: The target blockchain (ethereum, ton, tron)
        """
        if blockchain.lower() not in self.BLOCKCHAIN_URI_SCHEMES:
            raise ValueError(f"Unsupported blockchain. Choose from: {list(self.BLOCKCHAIN_URI_SCHEMES.keys())}")
        self.blockchain = blockchain.lower()
    
    def generate_uri(self, address: str, amount: float) -> str:
        """
        Generate payment URI for the specified blockchain.
        
        Args:
            address: Recipient wallet address
            amount: USDT amount to transfer
            
        Returns:
            Formatted payment URI
        """
        if not address:
            raise ValueError("Wallet address cannot be empty")
        if amount <= 0:
            raise ValueError("Amount must be positive")
            
        uri_template = self.BLOCKCHAIN_URI_SCHEMES[self.blockchain]
        return uri_template.format(address=address, amount=amount)
    
    def generate_qr_code(
        self,
        address: str,
        amount: float,
        output_file: Optional[str] = None,
        qr_options: Optional[Dict] = None
    ) -> qrcode.QRCode:
        """
        Generate QR code for USDT payment.
        
        Args:
            address: Recipient wallet address
            amount: USDT amount to transfer
            output_file: Optional path to save QR code image
            qr_options: Custom QR code options (version, box_size, border, etc.)
            
        Returns:
            Generated QR code object
        """
        # Generate payment URI
        payment_uri = self.generate_uri(address, amount)
        
        # Set default QR options if not provided
        if qr_options is None:
            qr_options = {
                'version': 1,
                'error_correction': ERROR_CORRECT_L,
                'box_size': 10,
                'border': 4,
            }
        
        # Generate QR code
        qr = qrcode.QRCode(**qr_options)
        qr.add_data(payment_uri)
        qr.make(fit=True)
        
        # Save to file if output path provided
        if output_file:
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(output_file)
        
        return qr


# Example usage
if __name__ == "__main__":
    try:
        # Generate Ethereum USDT QR
        eth_generator = USDTQRGenerator('ethereum')
        eth_qr = eth_generator.generate_qr_code(
            address="0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
            amount=100.5,
            output_file="eth_usdt_qr.png"
        )
        
        # Generate TON USDT QR
        ton_generator = USDTQRGenerator('ton')
        ton_qr = ton_generator.generate_qr_code(
            address="EQCD39VS5jcptHL8vMjEXrzGaRcCVYto7HUn4bpAOg8xqB2N",
            amount=50.25,
            output_file="ton_usdt_qr.png"
        )
        
    except ValueError as e:
        print(f"Error generating QR code: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
