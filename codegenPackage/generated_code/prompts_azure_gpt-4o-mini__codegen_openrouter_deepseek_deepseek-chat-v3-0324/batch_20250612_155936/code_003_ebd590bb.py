"""
Generated Code Metadata:
========================
Original URL: https://hemi.host
Prompt: How does the Proof-of-Proof security mechanism in Hemi ensure Bitcoin-powered finality, and how can I implement it in my project?
Generated: DETERMINISTIC_ebd590bb9687896a
Batch ID: 20250612_155936
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://blockstream.info/api/": {
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
import hashlib
import json
import requests
from typing import Dict, Optional, Tuple

class HemiProofOfProof:
    """
    Implementation of Hemi's Proof-of-Proof mechanism for Bitcoin-powered finality.
    This class provides methods to verify Bitcoin block headers and validate PoP proofs.
    """
    
    def __init__(self, bitcoin_node_url: str = "https://blockstream.info/api/"):
        """
        Initialize with a Bitcoin node URL (defaults to Blockstream's API)
        """
        self.bitcoin_node_url = bitcoin_node_url.rstrip('/')
        
    def get_bitcoin_block_header(self, block_height: int) -> Optional[Dict]:
        """
        Fetch Bitcoin block header by height from the configured node.
        
        Args:
            block_height: The height of the Bitcoin block to fetch
            
        Returns:
            Dict containing block header data or None if not found
        """
        try:
            response = requests.get(f"{self.bitcoin_node_url}/block-height/{block_height}")
            if response.status_code != 200:
                return None
                
            block_hash = response.text.strip()
            header_response = requests.get(f"{self.bitcoin_node_url}/block/{block_hash}/header")
            if header_response.status_code != 200:
                return None
                
            return {
                'height': block_height,
                'hash': block_hash,
                'header': header_response.text.strip()
            }
        except requests.RequestException:
            return None
    
    def verify_block_header(self, block_header: str) -> bool:
        """
        Verify a Bitcoin block header by checking its hash meets difficulty target.
        
        Args:
            block_header: Hex-encoded Bitcoin block header (80 bytes)
            
        Returns:
            bool: True if header is valid, False otherwise
        """
        if len(block_header) != 160:  # 80 bytes in hex
            return False
            
        try:
            header_bytes = bytes.fromhex(block_header)
            # Reverse the header for little-endian hash calculation
            reversed_header = header_bytes[::-1]
            # Double SHA-256 hash
            first_hash = hashlib.sha256(reversed_header).digest()
            second_hash = hashlib.sha256(first_hash).digest()
            # Convert back to little-endian hex
            block_hash = second_hash[::-1].hex()
            
            # Check if hash meets difficulty target (simplified check)
            # In production, you would verify against actual difficulty bits
            return block_hash < "0000ffff00000000000000000000000000000000000000000000000000000000"
        except ValueError:
            return False
    
    def generate_pop_proof(self, data: str, bitcoin_block_height: int) -> Optional[Dict]:
        """
        Generate a Proof-of-Proof by anchoring data to a Bitcoin block.
        
        Args:
            data: The data to be anchored
            bitcoin_block_height: The Bitcoin block height to use as anchor
            
        Returns:
            Dict containing the PoP proof or None if generation fails
        """
        block_header = self.get_bitcoin_block_header(bitcoin_block_height)
        if not block_header or not self.verify_block_header(block_header['header']):
            return None
            
        # Create Merkle proof (simplified - in production use a proper Merkle tree)
        data_hash = hashlib.sha256(data.encode()).hexdigest()
        
        return {
            'version': '1.0',
            'bitcoin_block_height': bitcoin_block_height,
            'bitcoin_block_hash': block_header['hash'],
            'bitcoin_block_header': block_header['header'],
            'data': data,
            'data_hash': data_hash,
            'timestamp': int(time.time())
        }
    
    def verify_pop_proof(self, proof: Dict) -> Tuple[bool, str]:
        """
        Verify a Proof-of-Proof by checking Bitcoin block header and data consistency.
        
        Args:
            proof: The PoP proof to verify
            
        Returns:
            Tuple of (bool: verification result, str: error message if any)
        """
        try:
            # Check proof structure
            required_fields = {
                'version', 'bitcoin_block_height', 'bitcoin_block_hash',
                'bitcoin_block_header', 'data', 'data_hash', 'timestamp'
            }
            if not all(field in proof for field in required_fields):
                return False, "Missing required fields in proof"
                
            # Verify Bitcoin block header
            if not self.verify_block_header(proof['bitcoin_block_header']):
                return False, "Invalid Bitcoin block header"
                
            # Verify data hash matches
            data_hash = hashlib.sha256(proof['data'].encode()).hexdigest()
            if data_hash != proof['data_hash']:
                return False, "Data hash mismatch"
                
            # Optional: Verify the block header matches the height/hash
            # This requires additional API calls to confirm
                
            return True, "Proof is valid"
        except Exception as e:
            return False, f"Verification error: {str(e)}"

# Example usage
if __name__ == "__main__":
    import time
    
    pop = HemiProofOfProof()
    
    # Example data to anchor
    data_to_anchor = "Hemi PoP security mechanism example"
    
    # Get current Bitcoin block height (simplified - in production use actual latest block)
    latest_block = pop.get_bitcoin_block_header(800000)  # Example block height
    
    if latest_block:
        print(f"Using Bitcoin block {latest_block['height']} with hash {latest_block['hash']}")
        
        # Generate PoP proof
        proof = pop.generate_pop_proof(data_to_anchor, latest_block['height'])
        if proof:
            print("Generated PoP proof:")
            print(json.dumps(proof, indent=2))
            
            # Verify the proof
            is_valid, message = pop.verify_pop_proof(proof)
            print(f"\nProof verification: {is_valid}, Message: {message}")
        else:
            print("Failed to generate PoP proof")
    else:
        print("Failed to fetch Bitcoin block header")
```
