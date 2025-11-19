"""
Generated Code Metadata:
========================
Original URL: https://data-portability-ui.vercel.vana.com
Prompt: Provide an example of integrating a crypto wallet to secure personal data and enable querying, based on the Vana Network demo.
Generated: DETERMINISTIC_4b11443b1071b615
Batch ID: 20250612_155057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
import json
import hashlib
from typing import Dict, Optional
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from eth_keys import keys
from cryptography.fernet import Fernet

# Configuration
CONFIG = {
    "rpc_url": "https://ropsten.infura.io/v3/YOUR_INFURA_PROJECT_ID",
    "contract_address": "0xYourContractAddress",
    "contract_abi": json.loads('''[
        {
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "internalType": "address",
                    "name": "user",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "internalType": "string",
                    "name": "dataHash",
                    "type": "string"
                }
            ],
            "name": "DataStored",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "dataHash",
                    "type": "string"
                }
            ],
            "name": "storeData",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "user",
                    "type": "address"
                }
            ],
            "name": "getUserDataHash",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ]''')
}

class CryptoWalletManager:
    """Manages crypto wallet operations and data encryption/decryption."""
    
    def __init__(self, private_key: str):
        """
        Initialize the wallet manager with a private key.
        
        Args:
            private_key: The private key for the Ethereum wallet.
        """
        self.web3 = Web3(Web3.HTTPProvider(CONFIG["rpc_url"]))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        self.account = Account.from_key(private_key)
        self.contract = self.web3.eth.contract(
            address=CONFIG["contract_address"],
            abi=CONFIG["contract_abi"]
        )
        
        # Generate encryption key from private key hash
        key_hash = hashlib.sha256(private_key.encode()).digest()
        self.fernet = Fernet(Fernet.generate_key())
    
    def encrypt_data(self, data: str) -> str:
        """
        Encrypt data using Fernet symmetric encryption.
        
        Args:
            data: The data to encrypt.
            
        Returns:
            The encrypted data as a string.
        """
        return self.fernet.encrypt(data.encode()).decode()
    
    def decrypt_data(self, encrypted_data: str) -> str:
        """
        Decrypt data using Fernet symmetric encryption.
        
        Args:
            encrypted_data: The encrypted data to decrypt.
            
        Returns:
            The decrypted data as a string.
        """
        return self.fernet.decrypt(encrypted_data.encode()).decode()
    
    def store_data(self, data: str) -> str:
        """
        Store encrypted data on the blockchain.
        
        Args:
            data: The data to store.
            
        Returns:
            The transaction hash.
            
        Raises:
            Exception: If the transaction fails.
        """
        encrypted_data = self.encrypt_data(data)
        data_hash = hashlib.sha256(encrypted_data.encode()).hexdigest()
        
        try:
            tx = self.contract.functions.storeData(data_hash).build_transaction({
                'chainId': self.web3.eth.chain_id,
                'gas': 200000,
                'gasPrice': self.web3.eth.gas_price,
                'nonce': self.web3.eth.get_transaction_count(self.account.address),
            })
            
            signed_tx = self.web3.eth.account.sign_transaction(tx, self.account.key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            self.web3.eth.wait_for_transaction_receipt(tx_hash)
            
            return tx_hash.hex()
        except Exception as e:
            raise Exception(f"Failed to store data: {str(e)}")
    
    def get_data(self, user_address: Optional[str] = None) -> Dict:
        """
        Retrieve and decrypt data from the blockchain.
        
        Args:
            user_address: The address to query. If None, uses the current wallet.
            
        Returns:
            A dictionary containing the data hash and decrypted data.
            
        Raises:
            Exception: If the data retrieval fails.
        """
        try:
            address = user_address if user_address else self.account.address
            data_hash = self.contract.functions.getUserDataHash(address).call()
            
            if not data_hash:
                return {"data_hash": None, "data": None}
            
            # In a real implementation, you would fetch the encrypted data
            # associated with the hash from your storage solution
            encrypted_data = "..."  # Placeholder - replace with actual encrypted data fetch
            decrypted_data = self.decrypt_data(encrypted_data)
            
            return {
                "data_hash": data_hash,
                "data": decrypted_data
            }
        except Exception as e:
            raise Exception(f"Failed to retrieve data: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with a private key (in production, use secure key management)
        wallet = CryptoWalletManager("YOUR_PRIVATE_KEY")
        
        # Store data
        tx_hash = wallet.store_data("Sensitive personal data")
        print(f"Data stored. Transaction hash: {tx_hash}")
        
        # Retrieve data
        data = wallet.get_data()
        print(f"Retrieved data: {data}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
