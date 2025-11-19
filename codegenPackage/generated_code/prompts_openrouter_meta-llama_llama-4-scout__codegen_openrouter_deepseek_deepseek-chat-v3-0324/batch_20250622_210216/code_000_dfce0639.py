"""
Generated Code Metadata:
========================
Original URL: https://dop-en.web.app
Prompt: Write a Python code snippet using zero-knowledge proofs to selectively disclose token holdings on Ethereum L1, considering ERC20, ERC721, and ERC1155 assets.
Generated: DETERMINISTIC_dfce0639ea0f545d
Batch ID: 20250622_210216
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
from typing import Dict, List, Union
from web3 import Web3
from eth_account import Account
from eth_abi import encode_abi
from zksnark import Groth16
import hashlib

# Initialize Web3 connection to Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Define standard ERC interfaces
ERC20_ABI = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]')
ERC721_ABI = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]')
ERC1155_ABI = json.loads('[{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_id","type":"uint256"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]')

class SelectiveDisclosure:
    """
    Implements zero-knowledge proof for selective disclosure of token holdings.
    Supports ERC20, ERC721, and ERC1155 token standards.
    """
    
    def __init__(self, private_key: str):
        """
        Initialize with user's Ethereum private key.
        
        Args:
            private_key: Hex string of user's private key
        """
        self.account = Account.from_key(private_key)
        self.address = self.account.address
        self.proving_key = None
        self.verification_key = None
        
    def load_proving_system(self, proving_key_path: str, verification_key_path: str):
        """
        Load Groth16 proving system keys.
        
        Args:
            proving_key_path: Path to proving key file
            verification_key_path: Path to verification key file
        """
        with open(proving_key_path, 'r') as f:
            self.proving_key = json.load(f)
        with open(verification_key_path, 'r') as f:
            self.verification_key = json.load(f)
    
    def get_token_balance(self, token_address: str, token_type: str, token_id: int = None) -> int:
        """
        Get balance of specified token for the user.
        
        Args:
            token_address: Contract address of the token
            token_type: 'ERC20', 'ERC721', or 'ERC1155'
            token_id: Required for ERC1155 tokens
            
        Returns:
            Token balance as integer
        """
        token_address = Web3.toChecksumAddress(token_address)
        
        if token_type == 'ERC20':
            contract = w3.eth.contract(address=token_address, abi=ERC20_ABI)
            return contract.functions.balanceOf(self.address).call()
        elif token_type == 'ERC721':
            contract = w3.eth.contract(address=token_address, abi=ERC721_ABI)
            return contract.functions.balanceOf(self.address).call()
        elif token_type == 'ERC1155':
            if token_id is None:
                raise ValueError("token_id required for ERC1155")
            contract = w3.eth.contract(address=token_address, abi=ERC1155_ABI)
            return contract.functions.balanceOf(self.address, token_id).call()
        else:
            raise ValueError("Invalid token type")
    
    def generate_proof(
        self,
        token_address: str,
        token_type: str,
        token_id: int = None,
        threshold: int = None,
        exact_value: int = None
    ) -> Dict:
        """
        Generate ZK proof for token holding.
        
        Args:
            token_address: Contract address of the token
            token_type: 'ERC20', 'ERC721', or 'ERC1155'
            token_id: Required for ERC1155 tokens
            threshold: Minimum balance to prove (optional)
            exact_value: Exact balance to prove (optional)
            
        Returns:
            Dictionary containing proof and public signals
        """
        if self.proving_key is None:
            raise ValueError("Proving system not initialized")
            
        balance = self.get_token_balance(token_address, token_type, token_id)
        
        # Prepare inputs for the proof
        inputs = {
            'address': self.address,
            'token_address': token_address,
            'token_type': token_type,
            'balance': balance,
            'threshold': threshold if threshold is not None else 0,
            'exact_value': exact_value if exact_value is not None else 0
        }
        
        # Hash inputs for privacy
        input_hash = hashlib.sha256(
            encode_abi(
                ['address', 'address', 'string', 'uint256', 'uint256', 'uint256'],
                [
                    Web3.toBytes(hexstr=inputs['address']),
                    Web3.toBytes(hexstr=inputs['token_address']),
                    inputs['token_type'].encode(),
                    inputs['balance'],
                    inputs['threshold'],
                    inputs['exact_value']
                ]
            )
        ).hexdigest()
        
        # Generate proof
        proof = Groth16.prove(
            self.proving_key,
            [int(input_hash, 16)]  # Convert hash to integer
        )
        
        return {
            'proof': proof,
            'public_signals': {
                'token_address': token_address,
                'token_type': token_type,
                'threshold': threshold,
                'exact_value': exact_value
            }
        }
    
    def verify_proof(self, proof: Dict) -> bool:
        """
        Verify a ZK proof of token holdings.
        
        Args:
            proof: Dictionary containing proof and public signals
            
        Returns:
            True if proof is valid, False otherwise
        """
        if self.verification_key is None:
            raise ValueError("Verification system not initialized")
            
        return Groth16.verify(
            self.verification_key,
            proof['proof'],
            [int(hashlib.sha256(
                encode_abi(
                    ['address', 'string', 'uint256', 'uint256'],
                    [
                        Web3.toBytes(hexstr=proof['public_signals']['token_address']),
                        proof['public_signals']['token_type'].encode(),
                        proof['public_signals']['threshold'] if 'threshold' in proof['public_signals'] else 0,
                        proof['public_signals']['exact_value'] if 'exact_value' in proof['public_signals'] else 0
                    ]
                )
            ).hexdigest(), 16)]
        )

# Example usage
if __name__ == "__main__":
    # Initialize with user's private key
    sd = SelectiveDisclosure("0xYOUR_PRIVATE_KEY_HERE")
    
    # Load proving system keys (paths to your generated keys)
    sd.load_proving_system("proving_key.json", "verification_key.json")
    
    # Generate proof for ERC20 token holding > 100 tokens
    proof = sd.generate_proof(
        token_address="0xTOKEN_ADDRESS",
        token_type="ERC20",
        threshold=100
    )
    
    # Verify the proof
    is_valid = sd.verify_proof(proof)
    print(f"Proof is valid: {is_valid}")
```
