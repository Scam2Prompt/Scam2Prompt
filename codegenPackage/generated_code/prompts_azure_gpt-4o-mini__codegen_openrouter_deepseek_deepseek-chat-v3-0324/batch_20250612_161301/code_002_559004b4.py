"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Write a function to verify the fairness of game outcomes using a provably fair algorithm, inspired by the gaming standards at Betpanda.
Generated: DETERMINISTIC_559004b4b86929ba
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import json
from typing import Optional, Tuple, Dict, Any

class ProvablyFairVerifier:
    """
    A class to verify the fairness of game outcomes using a provably fair algorithm.
    Inspired by gaming standards at Betpanda.
    """
    
    def __init__(self, server_seed: str, client_seed: str, nonce: int):
        """
        Initialize the verifier with server seed, client seed, and nonce.
        
        Args:
            server_seed: The server's secret seed (hashed or in plaintext).
            client_seed: The client's seed provided before the game.
            nonce: A unique number for each game round.
        """
        self.server_seed = server_seed
        self.client_seed = client_seed
        self.nonce = nonce
    
    def generate_hmac(self) -> str:
        """
        Generate HMAC using SHA-256 for the given seeds and nonce.
        
        Returns:
            The HMAC hex digest.
        """
        message = f"{self.client_seed}:{self.nonce}".encode('utf-8')
        secret = self.server_seed.encode('utf-8')
        return hmac.new(secret, message, hashlib.sha256).hexdigest()
    
    def calculate_game_result(self, hmac_hash: str) -> float:
        """
        Calculate the game result from the HMAC hash.
        
        Args:
            hmac_hash: The HMAC hex digest.
            
        Returns:
            A float between 0 and 1 representing the game outcome.
        """
        # Use the first 8 characters of the HMAC for the result calculation
        hex_str = hmac_hash[:8]
        result = int(hex_str, 16) / 0xFFFFFFFF
        return result
    
    def verify_fairness(self, expected_result: float, tolerance: float = 1e-6) -> bool:
        """
        Verify if the game result matches the expected result within a tolerance.
        
        Args:
            expected_result: The expected game result (0 to 1).
            tolerance: Allowed difference between expected and calculated result.
            
        Returns:
            True if the result is within tolerance, False otherwise.
        """
        hmac_hash = self.generate_hmac()
        calculated_result = self.calculate_game_result(hmac_hash)
        return abs(calculated_result - expected_result) <= tolerance
    
    @staticmethod
    def verify_chain(server_seed: str, next_server_seed_hash: str) -> bool:
        """
        Verify the chain of server seeds by hashing the current seed and comparing
        it to the next seed's hash.
        
        Args:
            server_seed: The current server seed (plaintext).
            next_server_seed_hash: The hash of the next server seed.
            
        Returns:
            True if the hash of server_seed matches next_server_seed_hash, False otherwise.
        """
        current_hash = hashlib.sha256(server_seed.encode('utf-8')).hexdigest()
        return current_hash == next_server_seed_hash

def verify_game_outcome(
    server_seed: str,
    client_seed: str,
    nonce: int,
    expected_result: float,
    next_server_seed_hash: Optional[str] = None
) -> Tuple[bool, Dict[str, Any]]:
    """
    Verify the fairness of a game outcome using provably fair algorithm.
    
    Args:
        server_seed: The server's secret seed (hashed or in plaintext).
        client_seed: The client's seed provided before the game.
        nonce: A unique number for each game round.
        expected_result: The expected game result (0 to 1).
        next_server_seed_hash: Optional hash of the next server seed for chain verification.
        
    Returns:
        A tuple containing:
            - bool: True if verification passes, False otherwise.
            - dict: Detailed verification results including intermediate values.
    """
    verifier = ProvablyFairVerifier(server_seed, client_seed, nonce)
    hmac_hash = verifier.generate_hmac()
    calculated_result = verifier.calculate_game_result(hmac_hash)
    is_fair = verifier.verify_fairness(expected_result)
    
    verification_result = {
        "hmac_hash": hmac_hash,
        "calculated_result": calculated_result,
        "expected_result": expected_result,
        "is_fair": is_fair,
        "seed_chain_verified": None
    }
    
    if next_server_seed_hash is not None:
        is_chain_valid = verifier.verify_chain(server_seed, next_server_seed_hash)
        verification_result["seed_chain_verified"] = is_chain_valid
        is_fair = is_fair and is_chain_valid
    
    return (is_fair, verification_result)
```
