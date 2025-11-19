"""
Generated Code Metadata:
========================
Original URL: https://ethereum-qr-code-generator.com
Prompt: Write Python code to generate Ethereum QR codes for decentralized finance (DeFi) applications, referencing the Ethereum QR Code Generator tool's features.
Generated: DETERMINISTIC_5863cfbf6ec93e93
Batch ID: 20250612_150329
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
import os
from typing import Optional, Dict, Union
from eth_utils import to_checksum_address

class EthereumQRGenerator:
    """
    Generate Ethereum QR codes for DeFi applications with various customization options.
    Supports standard Ethereum address QR codes and payment request QR codes.
    """
    
    def __init__(self):
        self.default_options = {
            'version': 1,
            'error_correction': qrcode.constants.ERROR_CORRECT_M,
            'box_size': 10,
            'border': 4,
            'fill_color': 'black',
            'back_color': 'white',
            'style': 'default',
            'gradient_start': '#000000',
            'gradient_end': '#FFFFFF'
        }
    
    def _validate_address(self, address: str) -> str:
        """Validate and convert to checksum address."""
        try:
            return to_checksum_address(address)
        except ValueError as e:
            raise ValueError(f"Invalid Ethereum address: {e}")
    
    def _generate_uri(self, address: str, amount: Optional[float] = None, token: Optional[str] = None) -> str:
        """Generate Ethereum payment URI."""
        address = self._validate_address(address)
        uri = f"ethereum:{address}"
        
        params = []
        if amount is not None:
            params.append(f"value={amount}")
        if token is not None:
            params.append(f"token={token}")
        
        if params:
            uri += "?" + "&".join(params)
        
        return uri
    
    def _get_image_style(self, style: str, options: Dict) -> Union[StyledPilImage, None]:
        """Get the appropriate image style based on configuration."""
        if style == 'rounded':
            return StyledPilImage(module_drawer=RoundedModuleDrawer())
        elif style == 'radial':
            return StyledPilImage(
                color_mask=RadialGradiantColorMask(
                    edge_color=options['gradient_start'],
                    center_color=options['gradient_end']
                )
            )
        return None
    
    def generate_qr_code(
        self,
        address: str,
        output_path: str,
        amount: Optional[float] = None,
        token: Optional[str] = None,
        **kwargs
    ) -> None:
        """
        Generate and save an Ethereum QR code.
        
        Args:
            address: Ethereum address (hex string)
            output_path: Path to save the QR code image
            amount: Optional amount of ETH/tokens to request
            token: Optional token contract address
            **kwargs: Additional QR code options:
                - version: QR code version (1-40)
                - error_correction: ERROR_CORRECT_L, M, Q, H
                - box_size: Pixel size of each QR code box
                - border: Border size in boxes
                - fill_color: Foreground color
                - back_color: Background color
                - style: 'default', 'rounded', or 'radial'
                - gradient_start: Start color for radial gradient
                - gradient_end: End color for radial gradient
        """
        try:
            # Merge default options with user-provided options
            options = {**self.default_options, **kwargs}
            
            # Generate the Ethereum URI
            uri = self._generate_uri(address, amount, token)
            
            # Create QR code instance
            qr = qrcode.QRCode(
                version=options['version'],
                error_correction=options['error_correction'],
                box_size=options['box_size'],
                border=options['border'],
            )
            
            qr.add_data(uri)
            qr.make(fit=True)
            
            # Determine image style
            img_style = self._get_image_style(options['style'], options)
            
            # Generate the image
            if img_style:
                img = qr.make_image(
                    image_factory=img_style,
                    fill_color=options['fill_color'],
                    back_color=options['back_color']
                )
            else:
                img = qr.make_image(
                    fill_color=options['fill_color'],
                    back_color=options['back_color']
                )
            
            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            # Save the image
            img.save(output_path)
            
        except Exception as e:
            raise RuntimeError(f"Failed to generate QR code: {e}")
    
    def generate_qr_code_base64(
        self,
        address: str,
        amount: Optional[float] = None,
        token: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Generate Ethereum QR code and return as base64 encoded string.
        
        Args:
            address: Ethereum address (hex string)
            amount: Optional amount of ETH/tokens to request
            token: Optional token contract address
            **kwargs: Additional QR code options (see generate_qr_code)
            
        Returns:
            Base64 encoded image string
        """
        try:
            import io
            import base64
            
            # Merge default options with user-provided options
            options = {**self.default_options, **kwargs}
            
            # Generate the Ethereum URI
            uri = self._generate_uri(address, amount, token)
            
            # Create QR code instance
            qr = qrcode.QRCode(
                version=options['version'],
                error_correction=options['error_correction'],
                box_size=options['box_size'],
                border=options['border'],
            )
            
            qr.add_data(uri)
            qr.make(fit=True)
            
            # Determine image style
            img_style = self._get_image_style(options['style'], options)
            
            # Generate the image
            if img_style:
                img = qr.make_image(
                    image_factory=img_style,
                    fill_color=options['fill_color'],
                    back_color=options['back_color']
                )
            else:
                img = qr.make_image(
                    fill_color=options['fill_color'],
                    back_color=options['back_color']
                )
            
            # Convert to base64
            buffered = io.BytesIO()
            img.save(buffered, format="PNG")
            return base64.b64encode(buffered.getvalue()).decode('utf-8')
            
        except Exception as e:
            raise RuntimeError(f"Failed to generate QR code: {e}")


# Example usage
if __name__ == "__main__":
    generator = EthereumQRGenerator()
    
    # Simple address QR code
    generator.generate_qr_code(
        address="0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
        output_path="output/eth_address.png"
    )
    
    # Payment request with styling
    generator.generate_qr_code(
        address="0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
        output_path="output/eth_payment.png",
        amount=1.5,
        token="0xdac17f958d2ee523a2206206994597c13d831ec7",  # USDT
        style="rounded",
        fill_color="#4E44CE",
        back_color="#F8F9FA"
    )
    
    # Get as base64
    base64_qr = generator.generate_qr_code_base64(
        address="0x71C7656EC7ab88b098defB751B7401B5f6d8976F",
        style="radial",
        gradient_start="#4E44CE",
        gradient_end="#8B85E9"
    )
    print(f"Base64 QR code: {base64_qr[:50]}...")
```
