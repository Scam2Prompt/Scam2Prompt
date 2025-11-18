"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockbook.btc-2.zelcore.io
Prompt: Create a script to send a Bitcoin transaction using the Blockbook API, ensuring compatibility with the `/Satoshi:29.0.0/` subversion protocol.
Generated: DETERMINISTIC_1009dbe052f6b089
Batch ID: 20250612_151445
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://blockbook.example.com`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://blockbook.example.com": {
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
import json

class BitcoinTransactionError(Exception):
    """Custom exception for Bitcoin transaction errors."""
    pass

class BitcoinTransaction:
    """A class to handle Bitcoin transactions via Blockbook API."""
    
    def __init__(self, base_url, version="Satoshi:29.0.0"):
        """
        Initializes the BitcoinTransaction instance.

        :param base_url: The base URL for the Blockbook API.
        :param version: The subversion of the Bitcoin protocol.
        """
        self.base_url = base_url
        self.version = version

    def send_transaction(self, hex_transaction):
        """
        Sends a raw Bitcoin transaction to the Blockbook API.

        :param hex_transaction: The raw hex-encoded transaction to be sent.
        :return: The result of the transaction.
        :raises BitcoinTransactionError: If the transaction fails.
        """
        url = f"{self.base_url}/api/v2/sendtx/{self.version}"
        headers = {'Content-Type': 'application/json'}
        payload = json.dumps({"tx": hex_transaction})
        
        try:
            response = requests.post(url, headers=headers, data=payload)

            # Check for HTTP errors
            response.raise_for_status()
            
            result = response.json()
            if 'error' in result and result['error']:
                raise BitcoinTransactionError(result['error'])

            return result
            
        except requests.exceptions.HTTPError as http_err:
            raise BitcoinTransactionError(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise BitcoinTransactionError(f"Error during request: {req_err}")
        except json.JSONDecodeError as json_err:
            raise BitcoinTransactionError(f"Error decoding JSON response: {json_err}")

def main():
    """
    Main function to execute the Bitcoin transaction.
    """
    # Initialize the Blockbook API with its base URL
    blockbook_api_url = "https://blockbook.example.com"  # Replace with actual Blockbook API URL
    transaction_hex = "YOUR_HEX_TRANSACTION_HERE"  # Replace with your actual transaction hex

    # Create an instance of the BitcoinTransaction class
    btc_transaction = BitcoinTransaction(base_url=blockbook_api_url)

    try:
        # Send the transaction and print the result
        result = btc_transaction.send_transaction(transaction_hex)
        print("Transaction sent successfully:", result)
    except BitcoinTransactionError as e:
        print(f"Transaction failed: {e}")

if __name__ == "__main__":
    main()
```

Make sure to replace `https://blockbook.example.com` and `YOUR_HEX_TRANSACTION_HERE` with the actual Blockbook API URL and your transaction hex, respectively.
