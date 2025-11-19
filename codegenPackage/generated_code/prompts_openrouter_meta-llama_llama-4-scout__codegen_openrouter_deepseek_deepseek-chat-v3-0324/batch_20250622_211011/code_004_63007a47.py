"""
Generated Code Metadata:
========================
Original URL: https://helio-midasalchemists.web.app
Prompt: Develop a Python library to interact with Helio's Web3 payments API, focusing on SOL payments and QR code functionality.
Generated: DETERMINISTIC_63007a47ad959b8a
Batch ID: 20250622_211011
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api-sandbox.hel.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hel.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Optional, Dict, Any
from base64 import b64encode
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
from urllib.parse import urlencode

class HelioPaymentError(Exception):
    """Base exception for Helio payment API errors"""
    pass

class HelioAPI:
    """
    A Python client for interacting with Helio's Web3 payments API.
    
    Attributes:
        api_key (str): The API key for authentication
        base_url (str): The base URL for the API endpoints
    """
    
    def __init__(self, api_key: str, sandbox: bool = False):
        """
        Initialize the Helio API client.
        
        Args:
            api_key: Your Helio API key
            sandbox: Whether to use the sandbox environment (default: False)
        """
        self.api_key = api_key
        self.base_url = "https://api-sandbox.hel.io" if sandbox else "https://api.hel.io"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Internal method to make HTTP requests to the Helio API.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path
            data: Optional payload to send with the request
            
        Returns:
            The JSON response from the API
            
        Raises:
            HelioPaymentError: If the request fails
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise HelioPaymentError(f"API request failed: {str(e)}")
    
    def create_sol_payment(
        self,
        amount: float,
        reference_id: str,
        metadata: Optional[Dict] = None,
        success_url: Optional[str] = None,
        cancel_url: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Create a new SOL payment request.
        
        Args:
            amount: The amount to charge in SOL
            reference_id: A unique reference ID for the payment
            metadata: Optional metadata to attach to the payment
            success_url: URL to redirect to after successful payment
            cancel_url: URL to redirect to if payment is cancelled
            
        Returns:
            The payment response containing payment details
        """
        payload = {
            "amount": amount,
            "currency": "SOL",
            "referenceId": reference_id,
            "metadata": metadata or {},
            "successUrl": success_url,
            "cancelUrl": cancel_url
        }
        return self._make_request("POST", "/v1/payment", payload)
    
    def get_payment_status(self, payment_id: str) -> Dict[str, Any]:
        """
        Get the status of a payment by its ID.
        
        Args:
            payment_id: The ID of the payment to check
            
        Returns:
            The payment status response
        """
        return self._make_request("GET", f"/v1/payment/{payment_id}")
    
    def generate_payment_qr_code(
        self,
        payment_url: str,
        size: int = 300,
        output_path: Optional[str] = None
    ) -> bytes:
        """
        Generate a QR code for a payment URL.
        
        Args:
            payment_url: The payment URL to encode in the QR code
            size: The size of the QR code in pixels (default: 300)
            output_path: Optional path to save the QR code image
            
        Returns:
            The QR code image as bytes (PNG format)
            
        Raises:
            HelioPaymentError: If QR code generation fails
        """
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(payment_url)
            qr.make(fit=True)
            
            img = qr.make_image(
                image_factory=StyledPilImage,
                module_drawer=RoundedModuleDrawer(),
                color_mask=RadialGradiantColorMask()
            )
            
            img = img.resize((size, size))
            
            if output_path:
                img.save(output_path)
            
            from io import BytesIO
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            return buffer.getvalue()
        except Exception as e:
            raise HelioPaymentError(f"QR code generation failed: {str(e)}")
    
    def create_checkout_url(
        self,
        amount: float,
        reference_id: str,
        metadata: Optional[Dict] = None,
        success_url: Optional[str] = None,
        cancel_url: Optional[str] = None
    ) -> str:
        """
        Create a checkout URL with prefilled parameters.
        
        Args:
            amount: The amount to charge in SOL
            reference_id: A unique reference ID for the payment
            metadata: Optional metadata to attach to the payment
            success_url: URL to redirect to after successful payment
            cancel_url: URL to redirect to if payment is cancelled
            
        Returns:
            The checkout URL
        """
        params = {
            "amount": amount,
            "currency": "SOL",
            "referenceId": reference_id,
            **({"metadata": json.dumps(metadata)} if metadata else {}),
            **({"successUrl": success_url} if success_url else {}),
            **({"cancelUrl": cancel_url} if cancel_url else {})
        }
        
        return f"{self.base_url}/checkout?{urlencode(params)}"
```
