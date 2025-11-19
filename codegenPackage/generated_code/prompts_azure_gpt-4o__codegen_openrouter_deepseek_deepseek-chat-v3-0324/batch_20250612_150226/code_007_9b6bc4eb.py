"""
Generated Code Metadata:
========================
Original URL: https://website2-70z.pages.dev
Prompt: Write code to integrate a decentralized identity system into a crypto network, focusing on redefining ownership as described by Innodapter ApS.
Generated: DETERMINISTIC_9b6bc4ebdd0c2d33
Batch ID: 20250612_150226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
from typing import Dict, Optional, List
from dataclasses import dataclass, asdict
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidSignature
from web3 import Web3
from web3.contract import Contract
from eth_account.messages import encode_defunct

# Configuration
CONTRACT_ADDRESS = "0xYourContractAddressHere"
PROVIDER_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
CHAIN_ID = 1  # Mainnet

@dataclass
class DecentralizedIdentity:
    """Represents a decentralized identity with cryptographic proofs."""
    did: str
    public_key: str
    metadata: Dict
    signature: Optional[str] = None

    def to_dict(self) -> Dict:
        """Serialize the identity to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'DecentralizedIdentity':
        """Deserialize from a dictionary."""
        return cls(**data)

class IdentityManager:
    """Manages decentralized identities on the blockchain."""
    
    def __init__(self):
        self.web3 = Web3(Web3.HTTPProvider(PROVIDER_URL))
        self.contract = self._load_contract()
        self.private_key = None  # Should be securely stored in production
        
    def _load_contract(self) -> Contract:
        """Load the smart contract ABI and address."""
        with open('IdentityContractABI.json') as f:
            abi = json.load(f)
        return self.web3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)
    
    def generate_key_pair(self) -> tuple:
        """Generate a new ECDSA key pair."""
        private_key = ec.generate_private_key(ec.SECP256K1(), default_backend())
        public_key = private_key.public_key()
        
        priv_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        pub_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        return priv_pem.decode(), pub_pem.decode()
    
    def create_did(self, metadata: Dict) -> DecentralizedIdentity:
        """Create a new decentralized identity."""
        priv_key, pub_key = self.generate_key_pair()
        self.private_key = priv_key  # In production, use secure storage
        
        did = f"did:innodapter:{hashlib.sha256(pub_key.encode()).hexdigest()}"
        identity = DecentralizedIdentity(did, pub_key, metadata)
        
        # Sign the identity
        message = encode_defunct(text=json.dumps(identity.to_dict()))
        signed_message = self.web3.eth.account.sign_message(message, private_key=self.private_key)
        identity.signature = signed_message.signature.hex()
        
        return identity
    
    def register_identity(self, identity: DecentralizedIdentity) -> str:
        """Register identity on the blockchain."""
        if not identity.signature:
            raise ValueError("Identity must be signed before registration")
            
        tx = self.contract.functions.registerIdentity(
            identity.did,
            identity.public_key,
            json.dumps(identity.metadata),
            identity.signature
        ).build_transaction({
            'chainId': CHAIN_ID,
            'gas': 200000,
            'gasPrice': self.web3.to_wei('50', 'gwei'),
            'nonce': self.web3.eth.get_transaction_count(self.web3.eth.default_account),
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, self.private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def verify_identity(self, did: str) -> bool:
        """Verify if an identity exists and is valid."""
        return self.contract.functions.verifyIdentity(did).call()
    
    def get_identity(self, did: str) -> Optional[DecentralizedIdentity]:
        """Retrieve an identity from the blockchain."""
        result = self.contract.functions.getIdentity(did).call()
        if not result or not result[0]:  # Check if DID exists
            return None
            
        return DecentralizedIdentity(
            did=result[0],
            public_key=result[1],
            metadata=json.loads(result[2]),
            signature=result[3]
        )

class OwnershipManager:
    """Manages ownership of assets using decentralized identities."""
    
    def __init__(self, identity_manager: IdentityManager):
        self.identity_manager = identity_manager
        
    def claim_ownership(self, asset_id: str, owner_did: str) -> str:
        """Claim ownership of an asset."""
        if not self.identity_manager.verify_identity(owner_did):
            raise ValueError("Invalid owner identity")
            
        tx = self.identity_manager.contract.functions.claimOwnership(
            asset_id,
            owner_did
        ).build_transaction({
            'chainId': CHAIN_ID,
            'gas': 200000,
            'gasPrice': self.identity_manager.web3.to_wei('50', 'gwei'),
            'nonce': self.identity_manager.web3.eth.get_transaction_count(
                self.identity_manager.web3.eth.default_account
            ),
        })
        
        signed_tx = self.identity_manager.web3.eth.account.sign_transaction(
            tx, self.identity_manager.private_key
        )
        tx_hash = self.identity_manager.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def transfer_ownership(self, asset_id: str, from_did: str, to_did: str) -> str:
        """Transfer ownership of an asset between identities."""
        if not (self.identity_manager.verify_identity(from_did) and 
                self.identity_manager.verify_identity(to_did)):
            raise ValueError("Invalid identity in transfer")
            
        tx = self.identity_manager.contract.functions.transferOwnership(
            asset_id,
            from_did,
            to_did
        ).build_transaction({
            'chainId': CHAIN_ID,
            'gas': 200000,
            'gasPrice': self.identity_manager.web3.to_wei('50', 'gwei'),
            'nonce': self.identity_manager.web3.eth.get_transaction_count(
                self.identity_manager.web3.eth.default_account
            ),
        })
        
        signed_tx = self.identity_manager.web3.eth.account.sign_transaction(
            tx, self.identity_manager.private_key
        )
        tx_hash = self.identity_manager.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        return tx_hash.hex()
    
    def get_owner(self, asset_id: str) -> Optional[str]:
        """Get the current owner of an asset."""
        return self.identity_manager.contract.functions.getOwner(asset_id).call()

# Example usage
if __name__ == "__main__":
    # Initialize managers
    identity_manager = IdentityManager()
    ownership_manager = OwnershipManager(identity_manager)
    
    # Create and register identity
    metadata = {"name": "Alice", "role": "developer"}
    identity = identity_manager.create_did(metadata)
    tx_hash = identity_manager.register_identity(identity)
    print(f"Identity registered with tx: {tx_hash}")
    
    # Claim ownership of an asset
    asset_id = "unique-asset-123"
    tx_hash = ownership_manager.claim_ownership(asset_id, identity.did)
    print(f"Ownership claimed with tx: {tx_hash}")
    
    # Verify ownership
    owner = ownership_manager.get_owner(asset_id)
    print(f"Current owner of {asset_id}: {owner}")
```
