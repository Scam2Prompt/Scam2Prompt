"""
Generated Code Metadata:
========================
Original URL: https://dogecoinmixer.com
Prompt: Create a function to securely mix Ethereum (ETH) transactions using a mixer API, with fixed service fees of 0.0100 ETH and support for self-custodial transfers.
Generated: DETERMINISTIC_c625baac845a80e1
Batch ID: 20250612_150234
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
from web3 import Web3
from typing import Dict, Optional

class EthereumMixer:
    """
    A class to securely mix Ethereum (ETH) transactions using a mixer API.
    Supports fixed service fees of 0.0100 ETH and self-custodial transfers.
    """
    
    def __init__(self, mixer_api_url: str, web3_provider_url: str):
        """
        Initialize the EthereumMixer with API and Web3 provider URLs.
        
        Args:
            mixer_api_url: URL of the mixer API endpoint
            web3_provider_url: URL of the Web3 provider (e.g., Infura, Alchemy)
        """
        self.mixer_api_url = mixer_api_url
        self.web3 = Web3(Web3.HTTPProvider(web3_provider_url))
        self.fixed_fee = Web3.to_wei(0.01, 'ether')  # 0.0100 ETH in wei
        
    def _validate_address(self, address: str) -> bool:
        """Validate an Ethereum address."""
        return Web3.is_address(address)
    
    def _send_api_request(self, endpoint: str, payload: Dict) -> Dict:
        """
        Send a request to the mixer API.
        
        Args:
            endpoint: API endpoint to call
            payload: Data to send with the request
            
        Returns:
            Response from the API as a dictionary
            
        Raises:
            Exception: If API request fails
        """
        url = f"{self.mixer_api_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")
    
    def create_mix_request(
        self,
        sender_address: str,
        recipient_address: str,
        amount_eth: float,
        private_key: Optional[str] = None
    ) -> Dict:
        """
        Create a mix request for ETH transfer.
        
        Args:
            sender_address: ETH address sending funds
            recipient_address: ETH address receiving mixed funds
            amount_eth: Amount of ETH to mix (before fee)
            private_key: Optional private key for self-custodial transfer
            
        Returns:
            Dictionary containing mix request details
            
        Raises:
            ValueError: If addresses are invalid or amount is insufficient
            Exception: If mix request fails
        """
        if not self._validate_address(sender_address):
            raise ValueError("Invalid sender address")
        if not self._validate_address(recipient_address):
            raise ValueError("Invalid recipient address")
            
        amount_wei = Web3.to_wei(amount_eth, 'ether')
        if amount_wei <= self.fixed_fee:
            raise ValueError("Amount must be greater than the fixed fee (0.01 ETH)")
            
        net_amount = amount_wei - self.fixed_fee
        
        payload = {
            "sender": sender_address,
            "recipient": recipient_address,
            "amount": str(net_amount),
            "fee": str(self.fixed_fee),
            "self_custodial": private_key is not None
        }
        
        if private_key:
            # For self-custodial transfers, sign the transaction locally
            try:
                signed_tx = self._create_signed_tx(
                    sender_address,
                    private_key,
                    net_amount
                )
                payload['signed_tx'] = signed_tx.rawTransaction.hex()
            except Exception as e:
                raise Exception(f"Failed to create signed transaction: {str(e)}")
        
        return self._send_api_request("mix", payload)
    
    def _create_signed_tx(
        self,
        sender_address: str,
        private_key: str,
        amount_wei: int
    ):
        """
        Create a signed transaction for self-custodial transfer.
        
        Args:
            sender_address: ETH address sending funds
            private_key: Private key for signing
            amount_wei: Amount to send in wei
            
        Returns:
            Signed transaction object
            
        Raises:
            Exception: If transaction creation fails
        """
        try:
            nonce = self.web3.eth.get_transaction_count(sender_address)
            tx = {
                'nonce': nonce,
                'to': self.mixer_api_url,  # Mixer's deposit address
                'value': amount_wei,
                'gas': 21000,
                'gasPrice': self.web3.eth.gas_price
            }
            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            return signed_tx
        except Exception as e:
            raise Exception(f"Transaction signing failed: {str(e)}")
    
    def check_mix_status(self, mix_id: str) -> Dict:
        """
        Check the status of a mix request.
        
        Args:
            mix_id: ID of the mix request to check
            
        Returns:
            Dictionary containing mix status information
            
        Raises:
            Exception: If status check fails
        """
        return self._send_api_request(f"status/{mix_id}", {})
```
