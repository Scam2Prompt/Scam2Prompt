"""
Generated Code Metadata:
========================
Original URL: https://web3portal.com
Prompt: Design a Web3-based system for user-owned identity management, using blockchain technology for secure data storage.
Generated: DETERMINISTIC_58cc03b8f593ce11
Batch ID: 20250622_212122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# web3_identity_manager.py
import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from eth_account.messages import encode_defunct
from typing import Dict, Optional, Tuple

class Web3IdentityManager:
    """
    A Web3-based identity management system that allows users to own and control their identity data.
    Uses blockchain for secure storage and verification.
    """
    
    def __init__(self, contract_address: str, provider_url: str, contract_abi_path: str):
        """
        Initialize the identity manager with blockchain connection details.
        
        Args:
            contract_address: Address of the deployed identity contract
            provider_url: URL of the Ethereum provider (e.g., Infura)
            contract_abi_path: Path to the contract ABI JSON file
        """
        self.web3 = Web3(Web3.HTTPProvider(provider_url))
        self.web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        
        with open(contract_abi_path) as f:
            contract_abi = json.load(f)
        
        self.contract = self.web3.eth.contract(
            address=contract_address,
            abi=contract_abi
        )
    
    def create_identity(self, private_key: str, identity_data: Dict) -> Tuple[str, str]:
        """
        Create a new identity on the blockchain.
        
        Args:
            private_key: Private key of the user creating the identity
            identity_data: Dictionary containing identity information
            
        Returns:
            Tuple of (transaction_hash, identity_id)
        """
        account = Account.from_key(private_key)
        identity_id = Web3.keccak(text=account.address).hex()
        
        tx = self.contract.functions.createIdentity(
            identity_id,
            json.dumps(identity_data)
        ).build_transaction({
            'from': account.address,
            'nonce': self.web3.eth.get_transaction_count(account.address),
            'gas': 2000000,
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex(), identity_id
    
    def update_identity(self, private_key: str, identity_id: str, identity_data: Dict) -> str:
        """
        Update existing identity data on the blockchain.
        
        Args:
            private_key: Private key of the identity owner
            identity_data: Updated identity information
            
        Returns:
            Transaction hash
        """
        account = Account.from_key(private_key)
        
        tx = self.contract.functions.updateIdentity(
            identity_id,
            json.dumps(identity_data)
        ).build_transaction({
            'from': account.address,
            'nonce': self.web3.eth.get_transaction_count(account.address),
            'gas': 2000000,
            'gasPrice': self.web3.eth.gas_price
        })
        
        signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
        tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        return tx_hash.hex()
    
    def get_identity(self, identity_id: str) -> Optional[Dict]:
        """
        Retrieve identity data from the blockchain.
        
        Args:
            identity_id: The ID of the identity to retrieve
            
        Returns:
            Dictionary containing identity data or None if not found
        """
        try:
            identity_data = self.contract.functions.getIdentity(identity_id).call()
            return json.loads(identity_data) if identity_data else None
        except Exception:
            return None
    
    def verify_identity_ownership(self, identity_id: str, signature: str, message: str) -> bool:
        """
        Verify that a user owns the identity by validating their signature.
        
        Args:
            identity_id: The ID of the identity to verify
            signature: Signature to verify
            message: Original message that was signed
            
        Returns:
            True if signature is valid and matches identity owner, False otherwise
        """
        try:
            identity_data = self.get_identity(identity_id)
            if not identity_data:
                return False
                
            signer = self._recover_signer(message, signature)
            identity_owner = self.contract.functions.getIdentityOwner(identity_id).call()
            
            return signer.lower() == identity_owner.lower()
        except Exception:
            return False
    
    def _recover_signer(self, message: str, signature: str) -> str:
        """
        Recover the signer's address from a message and signature.
        
        Args:
            message: Original message that was signed
            signature: Signature to verify
            
        Returns:
            Signer's address
        """
        message_hash = encode_defunct(text=message)
        return Account.recover_message(message_hash, signature=signature)
```

```solidity
// IdentityManager.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract IdentityManager {
    struct Identity {
        string data;
        address owner;
    }
    
    mapping(bytes32 => Identity) public identities;
    
    event IdentityCreated(bytes32 indexed identityId, address indexed owner);
    event IdentityUpdated(bytes32 indexed identityId, address indexed owner);
    
    modifier onlyOwner(bytes32 identityId) {
        require(msg.sender == identities[identityId].owner, "Not identity owner");
        _;
    }
    
    function createIdentity(bytes32 identityId, string memory identityData) external {
        require(identities[identityId].owner == address(0), "Identity already exists");
        
        identities[identityId] = Identity({
            data: identityData,
            owner: msg.sender
        });
        
        emit IdentityCreated(identityId, msg.sender);
    }
    
    function updateIdentity(bytes32 identityId, string memory identityData) external onlyOwner(identityId) {
        identities[identityId].data = identityData;
        emit IdentityUpdated(identityId, msg.sender);
    }
    
    function getIdentity(bytes32 identityId) external view returns (string memory) {
        return identities[identityId].data;
    }
    
    function getIdentityOwner(bytes32 identityId) external view returns (address) {
        return identities[identityId].owner;
    }
}
```
