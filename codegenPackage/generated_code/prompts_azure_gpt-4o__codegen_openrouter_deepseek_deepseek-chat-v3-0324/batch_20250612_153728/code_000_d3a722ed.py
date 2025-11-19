"""
Generated Code Metadata:
========================
Original URL: https://www.celestiadao.app
Prompt: Write a Python script to simulate a slot machine game with RTP "gacor" mechanics as described on BONANZASLOT, ensuring fairness and transparency in the results.
Generated: DETERMINISTIC_d3a722ed96cd58a1
Batch ID: 20250612_153728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import hashlib
import json
from typing import List, Dict, Tuple

class SlotMachine:
    """
    A slot machine simulator with RTP (Return to Player) mechanics.
    Implements fairness and transparency using cryptographic hashing for result verification.
    """
    
    def __init__(self, rtp: float = 0.95, reels: int = 3, symbols: List[str] = None):
        """
        Initialize the slot machine with given RTP, number of reels, and symbols.
        
        Args:
            rtp: Return to Player percentage (0.0 to 1.0)
            reels: Number of reels in the slot machine
            symbols: List of symbols to use on the reels
        """
        if not 0 <= rtp <= 1:
            raise ValueError("RTP must be between 0 and 1")
        if reels < 1:
            raise ValueError("Number of reels must be at least 1")
        
        self.rtp = rtp
        self.reels = reels
        self.symbols = symbols or ['7', 'BAR', 'BELL', 'CHERRY', 'ORANGE', 'LEMON']
        self.payouts = self._calculate_payouts()
        self.nonce = 0
        self.server_seed = self._generate_seed()
        self.client_seed = None
        
    def _generate_seed(self) -> str:
        """Generate a cryptographically secure random seed."""
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
    
    def _calculate_payouts(self) -> Dict[Tuple[str, ...], float]:
        """
        Calculate payouts based on RTP and symbol distribution.
        Returns a dictionary mapping symbol combinations to their payouts.
        """
        total_combinations = len(self.symbols) ** self.reels
        total_payout = self.rtp * total_combinations
        
        # Base payouts for common combinations
        payouts = {
            tuple([self.symbols[0]] * self.reels): total_payout * 0.5,  # Jackpot
            tuple([self.symbols[1]] * self.reels): total_payout * 0.3,
            tuple([self.symbols[2]] * self.reels): total_payout * 0.2
        }
        
        # Distribute remaining payout to other combinations
        remaining = total_payout - sum(payouts.values())
        other_combinations = total_combinations - len(payouts)
        
        if other_combinations > 0:
            base_payout = remaining / other_combinations
            for i in range(len(self.symbols)):
                for j in range(len(self.symbols)):
                    if self.reels == 2:
                        combo = (self.symbols[i], self.symbols[j])
                        if combo not in payouts:
                            payouts[combo] = base_payout
                    elif self.reels == 3:
                        for k in range(len(self.symbols)):
                            combo = (self.symbols[i], self.symbols[j], self.symbols[k])
                            if combo not in payouts:
                                payouts[combo] = base_payout
        
        return payouts
    
    def set_client_seed(self, seed: str):
        """Set the client seed for provably fair verification."""
        self.client_seed = seed
        
    def _generate_result(self) -> Tuple[List[str], float]:
        """
        Generate a random spin result and calculate payout.
        Uses cryptographic hashing for provably fair results.
        """
        if not self.client_seed:
            self.client_seed = self._generate_seed()
            
        # Generate HMAC using server seed, client seed, and nonce
        message = f"{self.server_seed}:{self.client_seed}:{self.nonce}"
        hmac = hashlib.sha256(message.encode()).hexdigest()
        
        # Convert HMAC to spin result
        spin_result = []
        for i in range(self.reels):
            # Use different parts of the hash for each reel
            hash_part = int(hmac[i*8:(i+1)*8], 16)
            symbol_index = hash_part % len(self.symbols)
            spin_result.append(self.symbols[symbol_index])
        
        # Calculate payout
        payout = self.payouts.get(tuple(spin_result), 0.0)
        self.nonce += 1
        
        return spin_result, payout
    
    def spin(self, bet: float = 1.0) -> Dict:
        """
        Simulate a spin of the slot machine.
        
        Args:
            bet: The amount bet by the player
            
        Returns:
            Dictionary containing:
            - result: List of symbols
            - payout: Amount won
            - win: Boolean indicating if player won
            - verification: Data for result verification
        """
        if bet <= 0:
            raise ValueError("Bet amount must be positive")
            
        result, payout_amount = self._generate_result()
        win = payout_amount > 0
        payout = payout_amount * bet
        
        verification = {
            'server_seed': self.server_seed,
            'client_seed': self.client_seed,
            'nonce': self.nonce - 1,
            'result_hash': hashlib.sha256(json.dumps(result).encode()).hexdigest()
        }
        
        return {
            'result': result,
            'payout': payout,
            'win': win,
            'verification': verification
        }
    
    def verify_result(self, server_seed: str, client_seed: str, nonce: int, result: List[str]) -> bool:
        """
        Verify that a result was fairly generated.
        
        Args:
            server_seed: The server seed used in the spin
            client_seed: The client seed used in the spin
            nonce: The nonce used in the spin
            result: The result to verify
            
        Returns:
            True if the result is valid, False otherwise
        """
        message = f"{server_seed}:{client_seed}:{nonce}"
        hmac = hashlib.sha256(message.encode()).hexdigest()
        
        for i in range(len(result)):
            hash_part = int(hmac[i*8:(i+1)*8], 16)
            symbol_index = hash_part % len(self.symbols)
            if self.symbols[symbol_index] != result[i]:
                return False
                
        return True

# Example usage
if __name__ == "__main__":
    # Initialize slot machine with default parameters
    slot = SlotMachine(rtp=0.95, reels=3)
    
    # Set a client seed (optional - can be provided by player)
    slot.set_client_seed("player_seed_123")
    
    # Simulate 10 spins
    for _ in range(10):
        spin_result = slot.spin(bet=1.0)
        print(f"Spin result: {spin_result['result']}")
        print(f"Payout: {spin_result['payout']}")
        print(f"Win: {spin_result['win']}")
        print(f"Verification hash: {spin_result['verification']['result_hash']}")
        print("-" * 40)
        
        # Verify the result
        verification_data = spin_result['verification']
        is_valid = slot.verify_result(
            verification_data['server_seed'],
            verification_data['client_seed'],
            verification_data['nonce'],
            spin_result['result']
        )
        print(f"Result valid: {is_valid}\n")
```
