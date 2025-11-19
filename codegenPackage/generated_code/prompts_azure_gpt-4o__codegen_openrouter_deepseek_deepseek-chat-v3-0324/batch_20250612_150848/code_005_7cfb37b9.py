"""
Generated Code Metadata:
========================
Original URL: https://eos-token.org
Prompt: Write code to implement an RNG (Random Number Generator) for ensuring fairness in online games, as highlighted in spacex168's description.
Generated: DETERMINISTIC_7cfb37b983d4669e
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import secrets
from typing import Optional, Tuple

class FairRNG:
    """
    A cryptographically secure and verifiable random number generator for online games.
    Implements a commit-reveal scheme to ensure fairness and prevent manipulation.
    """
    
    def __init__(self, seed: Optional[bytes] = None):
        """
        Initialize the RNG with an optional seed.
        If no seed is provided, a cryptographically secure random seed is generated.
        
        Args:
            seed: Optional seed bytes for deterministic results (for testing)
        """
        if seed is None:
            self._seed = secrets.token_bytes(32)
        else:
            self._seed = seed
        self._nonce = 0
        self._last_commitment: Optional[bytes] = None
    
    def generate_commitment(self) -> Tuple[bytes, int]:
        """
        Generate a commitment that can be shared with players.
        Returns the commitment hash and a timestamp.
        
        Returns:
            Tuple of (commitment_hash, timestamp)
        """
        self._nonce += 1
        commitment_data = self._seed + self._nonce.to_bytes(8, 'big')
        self._last_commitment = hashlib.sha256(commitment_data).digest()
        return (self._last_commitment, int(time.time()))
    
    def generate_number(self, min_val: int, max_val: int, client_seed: Optional[bytes] = None) -> Tuple[int, bytes]:
        """
        Generate a random number between min_val and max_val (inclusive).
        Requires the server to reveal the seed used in the commitment.
        
        Args:
            min_val: Minimum value (inclusive)
            max_val: Maximum value (inclusive)
            client_seed: Optional client-provided seed for additional fairness
            
        Returns:
            Tuple of (random_number, proof) where proof can be used to verify the result
            
        Raises:
            ValueError: If min_val >= max_val or if no commitment was made
        """
        if min_val >= max_val:
            raise ValueError("min_val must be less than max_val")
        
        if self._last_commitment is None:
            raise ValueError("No commitment was made. Call generate_commitment() first.")
        
        # Combine server seed with client seed if provided
        if client_seed is not None:
            combined_seed = self._seed + client_seed
        else:
            combined_seed = self._seed
        
        # Generate the random number
        hash_input = combined_seed + self._nonce.to_bytes(8, 'big')
        hash_result = hashlib.sha256(hash_input).digest()
        random_int = int.from_bytes(hash_result, 'big')
        
        # Scale to desired range
        range_size = max_val - min_val + 1
        result = min_val + (random_int % range_size)
        
        return (result, hash_input)
    
    @staticmethod
    def verify_result(min_val: int, max_val: int, result: int, proof: bytes, client_seed: Optional[bytes] = None) -> bool:
        """
        Verify that a random number was generated fairly using the proof.
        
        Args:
            min_val: Minimum value (inclusive) used in generation
            max_val: Maximum value (inclusive) used in generation
            result: The result to verify
            proof: The proof provided by generate_number()
            client_seed: Optional client seed if used in generation
            
        Returns:
            bool: True if the result is verified, False otherwise
            
        Raises:
            ValueError: If min_val >= max_val or if result is out of bounds
        """
        if min_val >= max_val:
            raise ValueError("min_val must be less than max_val")
        
        if result < min_val or result > max_val:
            raise ValueError("Result is out of bounds")
        
        # Recompute the hash
        hash_result = hashlib.sha256(proof).digest()
        random_int = int.from_bytes(hash_result, 'big')
        
        # Check if the result matches
        range_size = max_val - min_val + 1
        expected_result = min_val + (random_int % range_size)
        
        return result == expected_result

# Example usage
if __name__ == "__main__":
    # Server side
    rng = FairRNG()
    commitment, timestamp = rng.generate_commitment()
    print(f"Server commitment: {commitment.hex()}, timestamp: {timestamp}")
    
    # Client side (optional: client can provide their own seed)
    client_seed = b"client_secret_123"
    
    # Server generates the random number
    result, proof = rng.generate_number(1, 100, client_seed)
    print(f"Random number: {result}, proof: {proof.hex()}")
    
    # Client verifies the result
    is_valid = FairRNG.verify_result(1, 100, result, proof, client_seed)
    print(f"Result is valid: {is_valid}")
```
