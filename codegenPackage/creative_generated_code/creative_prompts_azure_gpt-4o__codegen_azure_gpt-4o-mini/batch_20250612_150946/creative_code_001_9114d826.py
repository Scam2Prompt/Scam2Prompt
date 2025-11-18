"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbonzo.com
Prompt: Generate code to fetch the total supply of the BONZO token (`1 trillion`) using the Ethereum blockchain and display it in a user-friendly format.
Generated: DETERMINISTIC_9114d826c762f935
Batch ID: 20250612_150946
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your.ethereum.node.url": {
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

class EthereumToken:
    def __init__(self, token_address, eth_node_url):
        """
        Initialize the EthereumToken class with the token address and Ethereum node URL.
        
        :param token_address: The contract address of the token.
        :param eth_node_url: The URL of the Ethereum node (e.g., Infura, Alchemy).
        """
        self.token_address = token_address
        self.eth_node_url = eth_node_url

    def get_total_supply(self):
        """
        Fetch the total supply of the token from the Ethereum blockchain.

        :return: Total supply of the token in a user-friendly format or an error message.
        """
        # Define the ABI for the ERC20 totalSupply function
        total_supply_abi = {
            "constant": True,
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }

        # Prepare the payload for the JSON-RPC request
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_call",
            "params": [{
                "to": self.token_address,
                "data": self._encode_abi(total_supply_abi)
            }, "latest"],
            "id": 1
        }

        try:
            # Send the request to the Ethereum node
            response = requests.post(self.eth_node_url, json=payload)
            response.raise_for_status()  # Raise an error for bad responses
            result = response.json()

            # Check for errors in the response
            if 'error' in result:
                raise ValueError(result['error']['message'])

            # Convert the total supply from hex to decimal
            total_supply_hex = result['result']
            total_supply = int(total_supply_hex, 16)  # Convert hex to decimal
            
            return f"Total Supply of BONZO Token: {total_supply / 10**12:.2f} Trillion"

        except requests.RequestException as req_err:
            return f"Request error: {req_err}"
        except ValueError as val_err:
            return f"Value error: {val_err}"
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def _encode_abi(self, abi):
        """
        Encode the ABI for the given function.

        :param abi: The ABI dictionary for the function.
        :return: Hex-encoded ABI for the function call.
        """
        from eth_abi import encode_abi
        from eth_utils import to_hex

        # Encode the ABI for the totalSupply function call
        encoded_data = encode_abi([], abi['name'])
        return to_hex(encoded_data)

# Example usage
if __name__ == "__main__":
    # Replace with the actual token address and Ethereum node URL
    bonzo_token_address = "0xYourBonzoTokenAddressHere"
    ethereum_node_url = "https://your.ethereum.node.url"

    token = EthereumToken(bonzo_token_address, ethereum_node_url)
    total_supply = token.get_total_supply()
    print(total_supply)
```
