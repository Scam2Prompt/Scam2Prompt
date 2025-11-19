"""
Generated Code Metadata:
========================
Original URL: https://coin-qr.to
Prompt: What features does the Bitcoin QR Code Generator offer for creating QR codes for Bitcoin, Ethereum, and other cryptocurrencies?
Generated: DETERMINISTIC_de03b6f889117bac
Batch ID: 20250612_135427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from typing import Optional, Dict, Union
import json

class CryptoQRGenerator:
    """
    A QR code generator for various cryptocurrencies including Bitcoin and Ethereum.
    Supports custom styling, error correction, and various output formats.
    """
    
    def __init__(self):
        self.supported_cryptos = {
            'bitcoin': {
                'prefix': 'bitcoin:',
                'params': ['amount', 'label', 'message']
            },
            'ethereum': {
                'prefix': 'ethereum:',
                'params': ['value', 'gas', 'data']
            },
            # Add more cryptocurrencies as needed
        }
    
    def generate_uri(
        self,
        crypto_type: str,
        address: str,
        params: Optional[Dict[str, str]] = None
    ) -> str:
        """
        Generate a cryptocurrency payment URI.
        
        Args:
            crypto_type: Type of cryptocurrency (e.g., 'bitcoin', 'ethereum')
            address: Wallet address
            params: Additional parameters (amount, label, etc.)
            
        Returns:
            Formatted payment URI string
            
        Raises:
            ValueError: If crypto_type is not supported
        """
        if crypto_type.lower() not in self.supported_cryptos:
            raise ValueError(f"Unsupported cryptocurrency: {crypto_type}")
            
        crypto = self.supported_cryptos[crypto_type.lower()]
        uri = f"{crypto['prefix']}{address}"
        
        if params:
            query = '&'.join(f"{k}={v}" for k, v in params.items() if k in crypto['params'])
            if query:
                uri += f"?{query}"
                
        return uri
    
    def generate_qr_code(
        self,
        crypto_type: str,
        address: str,
        params: Optional[Dict[str, str]] = None,
        output_file: Optional[str] = None,
        size: int = 10,
        border: int = 4,
        error_correction: str = 'M',
        style: Optional[str] = None,
        color: Optional[str] = None,
        background: Optional[str] = None
    ) -> Union[None, bytes]:
        """
        Generate a QR code for cryptocurrency payment.
        
        Args:
            crypto_type: Type of cryptocurrency
            address: Wallet address
            params: Additional parameters
            output_file: Path to save QR code (None returns bytes)
            size: QR code size
            border: Border size
            error_correction: Error correction level (L, M, Q, H)
            style: QR code style ('rounded', None for default)
            color: Primary color (hex)
            background: Background color (hex)
            
        Returns:
            If output_file is None, returns QR code as bytes. Otherwise saves to file.
            
        Raises:
            ValueError: For invalid parameters
        """
        # Generate payment URI
        uri = self.generate_uri(crypto_type, address, params)
        
        # Configure QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=getattr(qrcode.constants, f'ERROR_CORRECT_{error_correction.upper()}'),
            box_size=size,
            border=border,
        )
        qr.add_data(uri)
        qr.make(fit=True)
        
        # Configure styling
        img_kwargs = {}
        
        if style == 'rounded':
            img_kwargs['module_drawer'] = RoundedModuleDrawer()
        
        if color or background:
            if not color:
                color = '#000000'
            if not background:
                background = '#FFFFFF'
            img_kwargs['color_mask'] = RadialGradiantColorMask(
                edge_color=color,
                center_color=color,
                back_color=background
            )
        
        # Generate image
        if img_kwargs:
            img = qr.make_image(image_factory=StyledPilImage, **img_kwargs)
        else:
            img = qr.make_image()
        
        # Output result
        if output_file:
            img.save(output_file)
            return None
        else:
            from io import BytesIO
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            return buffer.getvalue()
    
    def get_supported_cryptos(self) -> Dict:
        """Return a dictionary of supported cryptocurrencies and their parameters."""
        return json.dumps(self.supported_cryptos, indent=2)

# Example usage
if __name__ == "__main__":
    generator = CryptoQRGenerator()
    
    # Generate Bitcoin QR
    bitcoin_uri = generator.generate_uri(
        'bitcoin',
        '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa',
        {'amount': '0.01', 'label': 'Donation'}
    )
    print(f"Bitcoin URI: {bitcoin_uri}")
    
    # Generate Ethereum QR with styling
    generator.generate_qr_code(
        'ethereum',
        '0x71C7656EC7ab88b098defB751B7401B5f6d8976F',
        {'value': '1.5'},
        output_file='ethereum_qr.png',
        style='rounded',
        color='#627EEA',
        background='#F5F5F5'
    )
```
