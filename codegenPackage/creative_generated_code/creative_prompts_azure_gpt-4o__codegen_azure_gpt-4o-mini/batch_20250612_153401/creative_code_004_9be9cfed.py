"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cctpbridge.vercel.app
Prompt: Create a step-by-step guide for integrating the CCTP Bridge API into a Web3 application, ensuring trustless asset transfers.
Generated: DETERMINISTIC_9be9cfed7668a4f1
Batch ID: 20250612_153401
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.cctpbridge.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class CCTPBridgeAPI:
    def __init__(self, api_key: str, base_url: str = "https://api.cctpbridge.com"):
        """
        Initializes the CCTP Bridge API client.
        
        :param api_key: Your API key for authenticating with the CCTP Bridge API.
        :param base_url: Base URL for the CCTP Bridge API. Default is the public endpoint.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint: str, method: str = "GET", data: dict = None):
        """
        Makes an HTTP request to the CCTP Bridge API.
        
        :param endpoint: API endpoint to call.
        :param method: HTTP method to use (GET or POST).
        :param data: Data to send with the request (for POST requests).
        :return: Response data from the API as JSON.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        
        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError("Invalid HTTP method.")

            # Raise an exception for bad responses
            response.raise_for_status()
            return response.json()
        
        except requests.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def initiate_transfer(self, from_address: str, to_address: str, amount: float, asset: str):
        """
        Initiates a trustless transfer of assets through the CCTP Bridge.
        
        :param from_address: Address of the asset sender.
        :param to_address: Address of the asset receiver.
        :param amount: Amount of the asset to transfer.
        :param asset: Type of asset to transfer (e.g., 'ETH', 'USDC').
        :return: Response from the API regarding the transfer initiation.
        """
        endpoint = "transfers/initiate"
        data = {
            "from": from_address,
            "to": to_address,
            "amount": amount,
            "asset": asset
        }
        return self._make_request(endpoint, method="POST", data=data)

    def check_transfer_status(self, transfer_id: str):
        """
        Checks the status of a previously initiated transfer.
        
        :param transfer_id: ID of the transfer to check.
        :return: Status of the transfer from the API.
        """
        endpoint = f"transfers/{transfer_id}/status"
        return self._make_request(endpoint)

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with your actual CCTP Bridge API key
    cctp_bridge = CCTPBridgeAPI(api_key="your_api_key")
    
    # Initiate a transfer
    transfer_response = cctp_bridge.initiate_transfer(
        from_address="0xYourFromAddress",
        to_address="0xYourToAddress",
        amount=1.0,
        asset="ETH"
    )

    if transfer_response:
        print("Transfer initiated:", transfer_response)

        # Optionally check the status of the transfer
        transfer_id = transfer_response.get('id')
        status_response = cctp_bridge.check_transfer_status(transfer_id)
        print("Transfer status:", status_response)
```

This code provides a Python class for interacting with the CCTP Bridge API, including methods for initiating asset transfers and checking their status. It includes error handling and comments to explain each part of the code.
