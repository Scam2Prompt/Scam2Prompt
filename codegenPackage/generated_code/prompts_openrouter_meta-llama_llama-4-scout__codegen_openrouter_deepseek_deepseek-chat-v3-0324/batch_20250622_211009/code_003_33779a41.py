"""
Generated Code Metadata:
========================
Original URL: https://3-xp-sns.vercel.app
Prompt: Create a simple application that uses Skale Foundation's services to provide users with a unique digital identity on the web3 platform.
Generated: DETERMINISTIC_33779a41dbf5703d
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from web3 import Web3
from eth_account import Account
from eth_account.messages import encode_defunct
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class SkaleIdentityManager:
    """
    A class to manage digital identities on the Skale network.
    """
    
    def __init__(self):
        """
        Initialize the Skale Identity Manager with network configuration.
        """
        self.web3 = Web3(Web3.HTTPProvider(os.getenv('SKALE_RPC_ENDPOINT')))
        self.contract_address = os.getenv('IDENTITY_CONTRACT_ADDRESS')
        self.private_key = os.getenv('USER_PRIVATE_KEY')
        self.account = Account.from_key(self.private_key)
        
        # Load contract ABI
        with open('IdentityContractABI.json', 'r') as abi_file:
            self.contract_abi = json.load(abi_file)
            
        self.contract = self.web3.eth.contract(
            address=self.contract_address,
            abi=self.contract_abi
        )
    
    def create_identity(self, username, metadata_uri):
        """
        Create a new digital identity on Skale network.
        
        Args:
            username (str): Unique username for the identity
            metadata_uri (str): URI pointing to identity metadata
            
        Returns:
            str: Transaction hash
        """
        if not self.web3.is_connected():
            raise ConnectionError("Not connected to Skale network")
            
        nonce = self.web3.eth.get_transaction_count(self.account.address)
        
        tx = self.contract.functions.createIdentity(
            username,
            metadata_uri
        ).build_transaction({
            'chainId': self.web3.eth.chain_id,
            'gas': 2000000,
            'gasPrice': self.web3.to_wei('50', 'gwei'),
            'nonce': nonce,
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def get_identity(self, username):
        """
        Retrieve identity information from the Skale network.
        
        Args:
            username (str): Username to look up
            
        Returns:
            dict: Identity information
        """
        if not self.web3.is_connected():
            raise ConnectionError("Not connected to Skale network")
            
        identity = self.contract.functions.getIdentity(username).call()
        return {
            'owner': identity[0],
            'username': identity[1],
            'metadataURI': identity[2],
            'createdAt': identity[3]
        }
    
    def verify_signature(self, message, signature):
        """
        Verify a signed message against the identity.
        
        Args:
            message (str): Original message
            signature (str): Signature to verify
            
        Returns:
            bool: True if signature is valid
        """
        message_hash = encode_defunct(text=message)
        signer = self.web3.eth.account.recover_message(message_hash, signature=signature)
        return signer.lower() == self.account.address.lower()

# Example usage
if __name__ == "__main__":
    try:
        identity_manager = SkaleIdentityManager()
        
        # Create a new identity
        tx_hash = identity_manager.create_identity(
            "alice123",
            "ipfs://QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco"
        )
        print(f"Identity created. Transaction hash: {tx_hash}")
        
        # Get identity info
        identity = identity_manager.get_identity("alice123")
        print(f"Identity details: {identity}")
        
        # Verify signature
        message = "I am Alice"
        signature = identity_manager.account.sign_message(encode_defunct(text=message)).signature.hex()
        is_valid = identity_manager.verify_signature(message, signature)
        print(f"Signature valid: {is_valid}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
