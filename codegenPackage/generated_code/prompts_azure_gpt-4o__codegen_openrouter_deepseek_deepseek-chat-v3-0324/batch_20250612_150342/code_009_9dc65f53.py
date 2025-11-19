"""
Generated Code Metadata:
========================
Original URL: https://starkware.eu
Prompt: Provide an example of using StarkWare's cryptographic primitives to secure user data in a decentralized application.
Generated: DETERMINISTIC_9dc65f53dc34efb5
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from starkware.crypto.signature.signature import (
    private_to_stark_key, sign, verify
)
from starkware.starknet.public.abi import get_selector_from_name
from starkware.starknet.core.os.contract_address.contract_address import (
    calculate_contract_address_from_hash
)
from starkware.starknet.definitions.general_config import StarknetChainId
from starkware.starknet.business_logic.state.state import CachedState
from starkware.starknet.business_logic.execution.objects import CallInfo
from starkware.starknet.services.api.contract_class import ContractClass
from starkware.starknet.services.api.gateway.transaction import InvokeFunction
from starkware.starknet.compiler.compile import compile_starknet_files
from starkware.starkware_utils.error_handling import StarkException
import hashlib
import json

class StarkNetDataProtector:
    """
    A class to demonstrate securing user data using StarkWare's cryptographic primitives.
    """
    
    def __init__(self, private_key: int):
        """
        Initialize with user's private key.
        """
        self.private_key = private_key
        self.public_key = private_to_stark_key(private_key)
    
    def generate_signature(self, message_hash: int) -> tuple:
        """
        Sign a message hash with the user's private key.
        Returns (r, s) signature components.
        """
        try:
            return sign(msg_hash=message_hash, priv_key=self.private_key)
        except StarkException as e:
            raise ValueError(f"Signing failed: {e}")
    
    def verify_signature(self, message_hash: int, signature: tuple) -> bool:
        """
        Verify a signature against the user's public key.
        """
        try:
            return verify(
                msg_hash=message_hash,
                r=signature[0],
                s=signature[1],
                public_key=self.public_key
            )
        except StarkException as e:
            raise ValueError(f"Verification failed: {e}")
    
    def hash_data(self, data: dict) -> int:
        """
        Hash structured data to a field element.
        """
        try:
            serialized = json.dumps(data, sort_keys=True).encode()
            return int.from_bytes(hashlib.sha256(serialized).digest(), 'big') % 2**251
        except Exception as e:
            raise ValueError(f"Hashing failed: {e}")
    
    def compute_contract_address(
        self,
        contract_class: ContractClass,
        constructor_calldata: list,
        salt: int
    ) -> int:
        """
        Compute the contract address for deployment.
        """
        try:
            return calculate_contract_address_from_hash(
                salt=salt,
                contract_class=contract_class,
                constructor_calldata=constructor_calldata,
                deployer_address=0
            )
        except StarkException as e:
            raise ValueError(f"Address computation failed: {e}")
    
    def prepare_invoke_transaction(
        self,
        contract_address: int,
        function_name: str,
        calldata: list,
        chain_id: StarknetChainId = StarknetChainId.TESTNET
    ) -> InvokeFunction:
        """
        Prepare an invoke transaction for StarkNet.
        """
        try:
            selector = get_selector_from_name(function_name)
            return InvokeFunction(
                contract_address=contract_address,
                entry_point_selector=selector,
                calldata=calldata,
                max_fee=0,
                version=1,
                signature=[],
                nonce=None,
            )
        except StarkException as e:
            raise ValueError(f"Transaction preparation failed: {e}")
    
    def compile_contract(self, source_path: str) -> ContractClass:
        """
        Compile a StarkNet contract from source.
        """
        try:
            return compile_starknet_files(
                files=[source_path],
                debug_info=True
            )
        except StarkException as e:
            raise ValueError(f"Compilation failed: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with a private key (in practice, this would be securely stored)
        protector = StarkNetDataProtector(private_key=123456789)
        
        # Example data to protect
        user_data = {
            "user_id": "user123",
            "balance": 1000,
            "permissions": ["read", "write"]
        }
        
        # Hash and sign the data
        data_hash = protector.hash_data(user_data)
        signature = protector.generate_signature(data_hash)
        
        # Verify the signature
        is_valid = protector.verify_signature(data_hash, signature)
        print(f"Signature valid: {is_valid}")
        
    except Exception as e:
        print(f"Error: {e}")
```
