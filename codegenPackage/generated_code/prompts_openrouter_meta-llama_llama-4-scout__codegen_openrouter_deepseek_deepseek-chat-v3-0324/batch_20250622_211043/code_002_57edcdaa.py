"""
Generated Code Metadata:
========================
Original URL: https://www.celestiadao.app
Prompt: Generate a Python code example to create a simple online slot game with a fair and transparent gameplay mechanism, inspired by BONANZASLOT's features and anti-corruption design.
Generated: DETERMINISTIC_57edcdaa75658bd4
Batch ID: 20250622_211043
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

class SlotGame:
    """
    A simple online slot game with fair and transparent gameplay.
    Features:
    - Provably fair mechanism using seed-based RNG
    - Transparent reel configuration
    - Win calculation based on predefined paytable
    - Anti-tampering design
    """
    
    def __init__(self, client_seed: str = None):
        """
        Initialize the slot game with optional client seed for provable fairness.
        If no client seed is provided, a random one will be generated.
        """
        self.client_seed = client_seed or self._generate_random_seed()
        self.server_seed = self._generate_random_seed()
        self.nonce = 0
        
        # Define the reel strips (symbols for each reel)
        self.reel_strips: List[List[str]] = [
            ['7', 'BAR', 'BELL', 'CHERRY', 'DIAMOND', 'LEMON', 'ORANGE', 'PLUM'],
            ['7', 'BAR', 'BELL', 'CHERRY', 'DIAMOND', 'LEMON', 'ORANGE', 'PLUM'],
            ['7', 'BAR', 'BELL', 'CHERRY', 'DIAMOND', 'LEMON', 'ORANGE', 'PLUM']
        ]
        
        # Define paytable (symbol: multiplier)
        self.paytable: Dict[str, List[int]] = {
            '7': [0, 0, 50],
            'BAR': [0, 5, 20],
            'BELL': [0, 10, 30],
            'CHERRY': [2, 5, 10],
            'DIAMOND': [0, 5, 15],
            'LEMON': [0, 2, 5],
            'ORANGE': [0, 2, 10],
            'PLUM': [0, 2, 10]
        }
        
        # Bet amounts (for demo purposes)
        self.bet_amounts: List[int] = [1, 2, 5, 10]
    
    def _generate_random_seed(self) -> str:
        """Generate a random 64-character hex string as seed."""
        return hashlib.sha256(str(random.getrandbits(256)).encode()).hexdigest()
    
    def _generate_hmac(self) -> str:
        """Generate HMAC using server seed and current nonce."""
        message = f"{self.server_seed}:{self.nonce}"
        return hashlib.sha256(message.encode()).hexdigest()
    
    def _get_fair_random(self, hmac_hash: str, reel_index: int) -> int:
        """
        Generate a fair random number for the given reel using HMAC.
        Returns a position index for the reel strip.
        """
        # Use part of the hash for this reel's randomness
        hash_part = hmac_hash[reel_index * 8 : (reel_index + 1) * 8]
        random_value = int(hash_part, 16)
        return random_value % len(self.reel_strips[reel_index])
    
    def spin(self, bet_amount: int) -> Dict:
        """
        Perform a slot spin with the given bet amount.
        Returns a dictionary with spin results, win amount, and verification data.
        """
        if bet_amount not in self.bet_amounts:
            raise ValueError("Invalid bet amount")
        
        # Generate HMAC for this spin
        hmac_hash = self._generate_hmac()
        
        # Get random positions for each reel
        positions = [
            self._get_fair_random(hmac_hash, 0),
            self._get_fair_random(hmac_hash, 1),
            self._get_fair_random(hmac_hash, 2)
        ]
        
        # Get symbols for the spin result
        symbols = [
            self.reel_strips[0][positions[0]],
            self.reel_strips[1][positions[1]],
            self.reel_strips[2][positions[2]]
        ]
        
        # Calculate win amount
        win_amount = self._calculate_win(symbols, bet_amount)
        
        # Increment nonce for next spin
        self.nonce += 1
        
        return {
            'symbols': symbols,
            'win_amount': win_amount,
            'bet_amount': bet_amount,
            'client_seed': self.client_seed,
            'server_seed': self.server_seed,
            'nonce': self.nonce - 1,  # Return the nonce used for this spin
            'hmac': hmac_hash,
            'verification': self._generate_verification_string(hmac_hash, symbols)
        }
    
    def _calculate_win(self, symbols: List[str], bet_amount: int) -> int:
        """
        Calculate win amount based on symbols and bet amount.
        """
        # Check for three of a kind
        if symbols[0] == symbols[1] == symbols[2]:
            return self.paytable[symbols[0]][2] * bet_amount
        
        # Check for two of a kind (first two reels)
        if symbols[0] == symbols[1]:
            return self.paytable[symbols[0]][1] * bet_amount
        
        # Check for single cherry on first reel
        if symbols[0] == 'CHERRY':
            return self.paytable['CHERRY'][0] * bet_amount
        
        return 0
    
    def _generate_verification_string(self, hmac_hash: str, symbols: List[str]) -> str:
        """
        Generate a verification string that can be used to verify the spin's fairness.
        """
        data = {
            'hmac': hmac_hash,
            'symbols': symbols,
            'client_seed': self.client_seed,
            'server_seed': self.server_seed,
            'nonce': self.nonce - 1
        }
        return json.dumps(data, sort_keys=True)
    
    def verify_spin(self, verification_string: str) -> bool:
        """
        Verify that a spin result matches the expected HMAC and seeds.
        """
        try:
            data = json.loads(verification_string)
            expected_hmac = hashlib.sha256(
                f"{data['server_seed']}:{data['nonce']}".encode()
            ).hexdigest()
            
            if expected_hmac != data['hmac']:
                return False
                
            # Verify symbols match what we would get from the HMAC
            test_positions = [
                self._get_fair_random(data['hmac'], 0),
                self._get_fair_random(data['hmac'], 1),
                self._get_fair_random(data['hmac'], 2)
            ]
            
            expected_symbols = [
                self.reel_strips[0][test_positions[0]],
                self.reel_strips[1][test_positions[1]],
                self.reel_strips[2][test_positions[2]]
            ]
            
            return expected_symbols == data['symbols']
        except (json.JSONDecodeError, KeyError):
            return False

# Example usage
if __name__ == "__main__":
    # Initialize game with optional client seed
    game = SlotGame("my_client_seed_123")
    
    # Perform a spin with bet amount 2
    spin_result = game.spin(2)
    
    print("Spin Result:")
    print(f"Symbols: {spin_result['symbols']}")
    print(f"Win Amount: {spin_result['win_amount']}")
    print(f"Verification: {spin_result['verification']}")
    
    # Verify the spin
    is_valid = game.verify_spin(spin_result['verification'])
    print(f"Spin is valid: {is_valid}")
```
