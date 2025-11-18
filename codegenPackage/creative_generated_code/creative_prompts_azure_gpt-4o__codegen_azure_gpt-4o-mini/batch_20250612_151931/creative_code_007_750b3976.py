"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beldex-claim.pages.dev
Prompt: Provide an example of integrating zk-SNARKS into a decentralized identity system on the Beldex sidechain.
Generated: DETERMINISTIC_750b397694d2e856
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from typing import Dict, Any, Tuple

# zk-SNARKS Library Imports (assuming a hypothetical library)
from zk_snarks import create_proof, verify_proof, generate_keypair

class DecentralizedIdentitySystem:
    def __init__(self):
        # Generate keypair for zk-SNARKS
        self.pk, self.sk = generate_keypair()
    
    def hash_data(self, data: Dict[str, Any]) -> str:
        """
        Hashes the input data using SHA-256.
        
        :param data: A dictionary containing identity information
        :return: A hexadecimal string of the hashed data
        """
        data_string = json.dumps(data, sort_keys=True).encode('utf-8')
        return hashlib.sha256(data_string).hexdigest()
    
    def create_identity_proof(self, identity_data: Dict[str, Any]) -> Tuple[str, str]:
        """
        Creates a zk-SNARK proof for the provided identity data.
        
        :param identity_data: A dictionary containing identity information
        :return: A tuple of the proof and the public key
        """
        try:
            # Hash the identity data
            hashed_data = self.hash_data(identity_data)
            
            # Create a zk-SNARK proof
            proof = create_proof(hashed_data, self.sk)
            return proof, self.pk
        except Exception as e:
            raise RuntimeError(f"Error creating identity proof: {e}")

    def verify_identity_proof(self, proof: str, public_key: str, identity_data: Dict[str, Any]) -> bool:
        """
        Verifies the zk-SNARK proof for the provided identity data.
        
        :param proof: The zk-SNARK proof to verify
        :param public_key: The public key associated with the identity
        :param identity_data: A dictionary containing identity information
        :return: True if the proof is valid, False otherwise
        """
        try:
            # Hash the identity data for verification
            hashed_data = self.hash_data(identity_data)
            
            # Verify the zk-SNARK proof
            is_valid = verify_proof(hashed_data, proof, public_key)
            return is_valid
        except Exception as e:
            raise RuntimeError(f"Error verifying identity proof: {e}")

# Example usage
if __name__ == "__main__":
    # Instantiate the identity system
    identity_system = DecentralizedIdentitySystem()
    
    # Example identity data
    identity_data = {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 30
    }
    
    # Create proof for identity
    proof, public_key = identity_system.create_identity_proof(identity_data)
    print(f"Created proof: {proof} with public key: {public_key}")

    # Verify the identity proof
    is_valid = identity_system.verify_identity_proof(proof, public_key, identity_data)
    print(f"Is the identity proof valid? {is_valid}")
```
