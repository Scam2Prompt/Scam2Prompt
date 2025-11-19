"""
Generated Code Metadata:
========================
Original URL: https://monero-qr-code-generator.com
Prompt: Suggest tools or libraries for creating Monero QR codes that support private and anonymous blockchain transactions, referencing the Monero QR Code Generator website.
Generated: DETERMINISTIC_f0e8d039e35d34de
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
import qrcode.image.svg
from io import BytesIO
from monero.wallet import Wallet
from monero.address import Address

class MoneroQRGenerator:
    """
    A class to generate Monero QR codes for private and anonymous transactions.
    Supports generating QR codes for payment addresses and integrated addresses.
    """
    
    def __init__(self):
        """Initialize the QR code generator with default settings."""
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
    
    def generate_payment_qr(self, address: str, amount: float = None, description: str = None) -> BytesIO:
        """
        Generate a QR code for a Monero payment address.
        
        Args:
            address: Monero wallet address (validated)
            amount: Optional amount in XMR
            description: Optional payment description
            
        Returns:
            BytesIO: In-memory file containing the QR code image
            
        Raises:
            ValueError: If address is invalid
        """
        if not Address.is_valid(address):
            raise ValueError("Invalid Monero address")
            
        uri = f"monero:{address}"
        if amount:
            uri += f"?tx_amount={amount}"
        if description:
            uri += f"&tx_description={description}" if '?' in uri else f"?tx_description={description}"
            
        return self._generate_qr(uri)
    
    def generate_integrated_qr(self, payment_id: str, address: str, amount: float = None) -> BytesIO:
        """
        Generate a QR code for a Monero integrated address.
        
        Args:
            payment_id: 64-character hexadecimal payment ID
            address: Monero wallet address
            amount: Optional amount in XMR
            
        Returns:
            BytesIO: In-memory file containing the QR code image
            
        Raises:
            ValueError: If address or payment ID is invalid
        """
        if not Address.is_valid(address):
            raise ValueError("Invalid Monero address")
        if not self._validate_payment_id(payment_id):
            raise ValueError("Invalid payment ID (must be 64-character hex)")
            
        integrated_address = Wallet().integrated_address(address, payment_id)
        uri = f"monero:{integrated_address}"
        if amount:
            uri += f"?tx_amount={amount}"
            
        return self._generate_qr(uri)
    
    def _generate_qr(self, data: str) -> BytesIO:
        """Internal method to generate QR code from data string."""
        self.qr.clear()
        self.qr.add_data(data)
        self.qr.make(fit=True)
        
        img = self.qr.make_image(fill_color="black", back_color="white")
        img_buffer = BytesIO()
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        return img_buffer
    
    def _validate_payment_id(self, payment_id: str) -> bool:
        """Validate that payment ID is 64-character hexadecimal string."""
        if len(payment_id) != 64:
            return False
        try:
            int(payment_id, 16)
            return True
        except ValueError:
            return False

# Example usage
if __name__ == "__main__":
    generator = MoneroQRGenerator()
    
    # Generate payment QR
    try:
        payment_qr = generator.generate_payment_qr(
            address="48jewbtxe4jU3MnzJj46Y7MVsN2jbrJ1vP2kvQN1K1KoJ4oJ3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3",
            amount=1.5,
            description="Donation"
        )
        with open("monero_payment.png", "wb") as f:
            f.write(payment_qr.getbuffer())
    except ValueError as e:
        print(f"Error generating payment QR: {e}")
    
    # Generate integrated QR
    try:
        integrated_qr = generator.generate_integrated_qr(
            payment_id="1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef",
            address="48jewbtxe4jU3MnzJj46Y7MVsN2jbrJ1vP2kvQN1K1KoJ4oJ3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3J3",
            amount=0.5
        )
        with open("monero_integrated.png", "wb") as f:
            f.write(integrated_qr.getbuffer())
    except ValueError as e:
        print(f"Error generating integrated QR: {e}")
```
