"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Write a Python script to simulate a provably fair game mechanism similar to those described on Betpanda, ensuring outcome verification for fairness.
Generated: DETERMINISTIC_06d374d0a0e0c284
Batch ID: 20250612_152526
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
from typing import Tuple, Optional, Dict, Any

class ProvablyFairGame:
    """
    A provably fair game mechanism that allows verification of game outcomes.
    """
    
    def __init__(self, server_seed: str, client_seed: str, nonce: int):
        """
        Initialize the game with server seed, client seed, and nonce.
        
        Args:
            server_seed: Secret server seed (hex format)
            client_seed: Client-provided seed
            nonce: Incremental nonce value
        """
        self.server_seed = server_seed
        self.client_seed = client_seed
        self.nonce = nonce
    
    @staticmethod
    def generate_server_seed() -> str:
        """
        Generate a cryptographically secure random server seed.
        
        Returns:
            Hex-encoded server seed
        """
        return hashlib.sha256(hashlib.sha256().hexdigest().encode()).hexdigest()
    
    def generate_hmac(self) -> str:
        """
        Generate HMAC using server seed as key and client seed + nonce as message.
        
        Returns:
            Hex-encoded HMAC-SHA256
        """
        message = f"{self.client_seed}:{self.nonce}".encode()
        return hmac.new(
            bytes.fromhex(self.server_seed),
            message,
            hashlib.sha256
        ).hexdigest()
    
    def calculate_result(self, hmac_hash: str) -> float:
        """
        Calculate game result from HMAC hash (0-1 range).
        
        Args:
            hmac_hash: HMAC hash to derive result from
            
        Returns:
            Float between 0 and 1 representing game result
        """
        # Use first 8 characters of HMAC for 32-bit precision
        hex_str = hmac_hash[:8]
        integer = int(hex_str, 16)
        max_32bit = 0xFFFFFFFF
        return integer / max_32bit
    
    def verify_result(self, hmac_hash: str, expected_result: float) -> bool:
        """
        Verify that the result matches the expected value.
        
        Args:
            hmac_hash: HMAC hash to verify
            expected_result: Expected game result
            
        Returns:
            bool: True if verification succeeds
        """
        calculated_result = self.calculate_result(hmac_hash)
        return abs(calculated_result - expected_result) < 1e-10
    
    def generate_game_outcome(self) -> Tuple[float, Dict[str, Any]]:
        """
        Generate a verifiable game outcome.
        
        Returns:
            Tuple of (result, verification_data)
        """
        hmac_hash = self.generate_hmac()
        result = self.calculate_result(hmac_hash)
        
        verification_data = {
            "server_seed": self.server_seed,
            "client_seed": self.client_seed,
            "nonce": self.nonce,
            "hmac": hmac_hash,
            "result": result
        }
        
        return result, verification_data
    
    @staticmethod
    def verify_game_outcome(verification_data: Dict[str, Any]) -> bool:
        """
        Verify a game outcome using stored verification data.
        
        Args:
            verification_data: Dictionary containing verification data
            
        Returns:
            bool: True if verification succeeds
        """
        try:
            game = ProvablyFairGame(
                verification_data["server_seed"],
                verification_data["client_seed"],
                verification_data["nonce"]
            )
            return game.verify_result(
                verification_data["hmac"],
                verification_data["result"]
            )
        except (KeyError, ValueError) as e:
            raise ValueError("Invalid verification data") from e

# Example usage
if __name__ == "__main__":
    # Generate a new game instance
    server_seed = ProvablyFairGame.generate_server_seed()
    client_seed = "player_seed_123"
    nonce = 1
    
    game = ProvablyFairGame(server_seed, client_seed, nonce)
    result, verification_data = game.generate_game_outcome()
    
    print(f"Game result: {result}")
    print("Verification data:")
    print(json.dumps(verification_data, indent=2))
    
    # Verify the result
    is_valid = ProvablyFairGame.verify_game_outcome(verification_data)
    print(f"Verification successful: {is_valid}")
```
