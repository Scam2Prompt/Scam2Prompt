"""
Generated Code Metadata:
========================
Original URL: https://fastpaymentve.com
Prompt: Write a Python code snippet to integrate a payment gateway with a dual SIM and QR code reader, similar to FastPayment's T1 WIFI LECTOR CÓDIGO QR.
Generated: DETERMINISTIC_5b7ef56c6302dbd4
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Optional, Dict
import qrcode
from io import BytesIO
import base64

class PaymentGateway:
    """
    Payment Gateway integration with dual SIM and QR code functionality.
    """
    
    def __init__(self, api_key: str, api_url: str, sim_selection: str = "SIM1"):
        """
        Initialize the payment gateway with API credentials and SIM selection.
        
        Args:
            api_key: Payment gateway API key
            api_url: Base URL for the payment gateway API
            sim_selection: Which SIM to use for transactions ("SIM1" or "SIM2")
        """
        self.api_key = api_key
        self.api_url = api_url
        self.sim_selection = sim_selection
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def _make_request(self, endpoint: str, payload: Dict) -> Dict:
        """
        Internal method to make API requests with error handling.
        
        Args:
            endpoint: API endpoint to call
            payload: Dictionary with request data
            
        Returns:
            Dictionary with API response
            
        Raises:
            Exception: If request fails
        """
        try:
            url = f"{self.api_url}/{endpoint}"
            response = requests.post(
                url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def process_payment(self, amount: float, currency: str, description: str) -> Dict:
        """
        Process a payment transaction.
        
        Args:
            amount: Transaction amount
            currency: Currency code (e.g., "USD")
            description: Transaction description
            
        Returns:
            Dictionary with transaction details
        """
        payload = {
            "amount": amount,
            "currency": currency,
            "description": description,
            "sim_selection": self.sim_selection
        }
        return self._make_request("transactions/process", payload)
    
    def generate_qr_code(self, transaction_id: str) -> str:
        """
        Generate a QR code for a transaction.
        
        Args:
            transaction_id: ID of the transaction
            
        Returns:
            Base64 encoded QR code image
        """
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(transaction_id)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color="black", back_color="white")
            buffered = BytesIO()
            img.save(buffered)
            return base64.b64encode(buffered.getvalue()).decode("utf-8")
        except Exception as e:
            raise Exception(f"QR code generation failed: {str(e)}")
    
    def read_qr_code(self, image_data: str) -> Optional[str]:
        """
        Read a QR code from image data.
        
        Args:
            image_data: Base64 encoded image data
            
        Returns:
            Decoded QR content or None if failed
        """
        try:
            # In a real implementation, this would use a QR code reader library
            # This is a placeholder for the actual implementation
            decoded_data = base64.b64decode(image_data)
            # Simulate QR code reading
            return "transaction_12345"  # Placeholder return
        except Exception:
            return None
    
    def switch_sim(self, new_sim: str) -> bool:
        """
        Switch between SIM cards.
        
        Args:
            new_sim: Which SIM to switch to ("SIM1" or "SIM2")
            
        Returns:
            True if successful, False otherwise
        """
        if new_sim in ["SIM1", "SIM2"]:
            self.sim_selection = new_sim
            return True
        return False
```
