"""
Generated Code Metadata:
========================
Original URL: https://ouyicn.party
Prompt: Explain how to use OKX's Nitro Spreads feature to manage futures spreads with deep liquidity, and write a sample implementation.
Generated: DETERMINISTIC_c39256c287234a38
Batch ID: 20250612_153745
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com/docs/en/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.okx.com": {
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
import time
import hashlib
import hmac
import json
from typing import Dict, Optional

class OKXNitroSpreads:
    """
    A class to interact with OKX's Nitro Spreads API for managing futures spreads.
    Documentation: https://www.okx.com/docs/en/
    """

    def __init__(self, api_key: str, secret_key: str, passphrase: str, base_url: str = "https://www.okx.com"):
        """
        Initialize the OKX API client with authentication credentials.
        
        Args:
            api_key (str): Your OKX API key
            secret_key (str): Your OKX API secret key
            passphrase (str): Your OKX API passphrase
            base_url (str, optional): OKX API base URL. Defaults to production.
        """
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.base_url = base_url

    def _generate_signature(self, timestamp: str, method: str, request_path: str, body: str = "") -> str:
        """
        Generate OKX-compatible signature for authenticated requests.
        
        Args:
            timestamp (str): Current timestamp in ISO format
            method (str): HTTP method (GET, POST, etc.)
            request_path (str): API endpoint path
            body (str, optional): Request body as string. Defaults to empty.
            
        Returns:
            str: Base64-encoded signature
        """
        message = timestamp + method.upper() + request_path + body
        signature = hmac.new(
            bytes(self.secret_key, 'utf-8'),
            bytes(message, 'utf-8'),
            hashlib.sha256
        ).digest()
        return base64.b64encode(signature).decode('utf-8')

    def _send_request(self, method: str, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Send authenticated request to OKX API.
        
        Args:
            method (str): HTTP method
            endpoint (str): API endpoint
            params (Dict, optional): Request parameters. Defaults to None.
            
        Returns:
            Dict: API response
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.base_url}{endpoint}"
        timestamp = time.strftime('%Y-%m-%dT%H:%M:%S.000Z', time.gmtime())
        body = json.dumps(params) if params else ""
        
        headers = {
            "OK-ACCESS-KEY": self.api_key,
            "OK-ACCESS-SIGN": self._generate_signature(timestamp, method, endpoint, body),
            "OK-ACCESS-TIMESTAMP": timestamp,
            "OK-ACCESS-PASSPHRASE": self.passphrase,
            "Content-Type": "application/json"
        }
        
        try:
            if method.upper() == "GET":
                response = requests.get(url, headers=headers, params=params)
            elif method.upper() == "POST":
                response = requests.post(url, headers=headers, json=params)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
                
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def get_nitro_spreads(self, inst_type: str = "FUTURES") -> Dict:
        """
        Get available Nitro Spreads instruments.
        
        Args:
            inst_type (str, optional): Instrument type. Defaults to "FUTURES".
            
        Returns:
            Dict: Available spreads data
        """
        endpoint = "/api/v5/public/instruments"
        params = {"instType": inst_type, "uly": "BTC-USD"}  # Example for BTC futures
        return self._send_request("GET", endpoint, params)

    def create_spread_order(
        self,
        spread_inst_id: str,
        side: str,
        size: float,
        price: Optional[float] = None,
        order_type: str = "limit"
    ) -> Dict:
        """
        Create a Nitro Spread order.
        
        Args:
            spread_inst_id (str): Spread instrument ID
            side (str): "buy" or "sell"
            size (float): Order size
            price (float, optional): Order price. Required for limit orders.
            order_type (str, optional): "limit" or "market". Defaults to "limit".
            
        Returns:
            Dict: Order creation response
        """
        endpoint = "/api/v5/trade/order"
        params = {
            "instId": spread_inst_id,
            "tdMode": "cross",
            "side": side,
            "ordType": order_type,
            "sz": str(size),
        }
        
        if order_type == "limit":
            if price is None:
                raise ValueError("Price is required for limit orders")
            params["px"] = str(price)
            
        return self._send_request("POST", endpoint, params)

    def close_spread_position(self, spread_inst_id: str) -> Dict:
        """
        Close an existing Nitro Spread position.
        
        Args:
            spread_inst_id (str): Spread instrument ID
            
        Returns:
            Dict: Position closing response
        """
        endpoint = "/api/v5/trade/close-position"
        params = {
            "instId": spread_inst_id,
            "mgnMode": "cross"
        }
        return self._send_request("POST", endpoint, params)

# Example usage
if __name__ == "__main__":
    # Initialize client (replace with your actual credentials)
    client = OKXNitroSpreads(
        api_key="your_api_key",
        secret_key="your_secret_key",
        passphrase="your_passphrase"
    )
    
    try:
        # Get available spreads
        spreads = client.get_nitro_spreads()
        print("Available spreads:", spreads)
        
        # Example: Create a limit order for BTC-USD spread
        spread_inst_id = "BTC-USD-SPREAD"  # Replace with actual instrument ID
        order_response = client.create_spread_order(
            spread_inst_id=spread_inst_id,
            side="buy",
            size=1,
            price=100.50
        )
        print("Order created:", order_response)
        
        # Example: Close position
        close_response = client.close_spread_position(spread_inst_id)
        print("Position closed:", close_response)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
