"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogs.pages.dev
Prompt: Generate code for a simple game on the Bitcoin blockchain, incorporating elements of the Bitcoin Dogs game, such as feeding and dueling dogs.
Generated: DETERMINISTIC_96d861a858117ef2
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# Bitcoin Dogs Game - A simple blockchain-based game for feeding and dueling dogs

import hashlib
import json
import time
from typing import Dict, List, Optional, Tuple

class Dog:
    """Represents a dog in the game with attributes and stats."""
    
    def __init__(self, name: str, breed: str, owner: str):
        self.name = name
        self.breed = breed
        self.owner = owner
        self.hunger = 50
        self.strength = 50
        self.happiness = 50
        self.last_fed = int(time.time())
        self.last_trained = int(time.time())
        self.id = self._generate_id()
    
    def _generate_id(self) -> str:
        """Generate a unique ID for the dog based on its attributes."""
        data = f"{self.name}{self.breed}{self.owner}{time.time()}"
        return hashlib.sha256(data.encode()).hexdigest()[:16]
    
    def feed(self) -> None:
        """Feed the dog, reducing hunger and increasing happiness."""
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - 10)
            self.happiness = min(100, self.happiness + 5)
            self.last_fed = int(time.time())
    
    def train(self) -> None:
        """Train the dog, increasing strength."""
        self.strength = min(100, self.strength + 5)
        self.last_trained = int(time.time())
    
    def to_dict(self) -> Dict:
        """Convert dog object to dictionary for serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'breed': self.breed,
            'owner': self.owner,
            'hunger': self.hunger,
            'strength': self.strength,
            'happiness': self.happiness,
            'last_fed': self.last_fed,
            'last_trained': self.last_trained
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Dog':
        """Create a Dog instance from dictionary data."""
        dog = cls(data['name'], data['breed'], data['owner'])
        dog.id = data['id']
        dog.hunger = data['hunger']
        dog.strength = data['strength']
        dog.happiness = data['happiness']
        dog.last_fed = data['last_fed']
        dog.last_trained = data['last_trained']
        return dog

class BitcoinDogsGame:
    """Main game class handling dog management and blockchain integration."""
    
    def __init__(self):
        self.dogs: Dict[str, Dog] = {}
        self.transactions: List[Dict] = []
        self.blockchain: List[Dict] = []
        self._initialize_blockchain()
    
    def _initialize_blockchain(self) -> None:
        """Initialize the blockchain with genesis block if empty."""
        if not self.blockchain:
            genesis_block = self._create_block(previous_hash='0')
            self._add_block(genesis_block)
    
    def _create_block(self, previous_hash: str) -> Dict:
        """Create a new block with pending transactions."""
        block = {
            'index': len(self.blockchain) + 1,
            'timestamp': int(time.time()),
            'transactions': self.transactions.copy(),
            'previous_hash': previous_hash,
            'nonce': 0
        }
        
        # Reset current list of transactions
        self.transactions = []
        
        # Proof of work
        block['hash'] = self._proof_of_work(block)
        return block
    
    def _proof_of_work(self, block: Dict) -> str:
        """Simple proof of work algorithm."""
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    def _add_block(self, block: Dict) -> None:
        """Add a new block to the blockchain."""
        self.blockchain.append(block)
    
    def create_dog(self, name: str, breed: str, owner: str) -> Dog:
        """Create a new dog and add to the game."""
        if not name or not breed or not owner:
            raise ValueError("Name, breed, and owner are required")
        
        dog = Dog(name, breed, owner)
        self.dogs[dog.id] = dog
        
        # Add transaction to blockchain
        transaction = {
            'type': 'create_dog',
            'dog_id': dog.id,
            'name': name,
            'breed': breed,
            'owner': owner,
            'timestamp': int(time.time())
        }
        self.transactions.append(transaction)
        
        # Mine new block if enough transactions
        if len(self.transactions) >= 3:
            last_block = self.blockchain[-1]
            new_block = self._create_block(last_block['hash'])
            self._add_block(new_block)
        
        return dog
    
    def feed_dog(self, dog_id: str) -> Optional[Dog]:
        """Feed a dog by its ID."""
        dog = self.dogs.get(dog_id)
        if not dog:
            return None
        
        dog.feed()
        
        transaction = {
            'type': 'feed_dog',
            'dog_id': dog_id,
            'timestamp': int(time.time())
        }
        self.transactions.append(transaction)
        
        return dog
    
    def train_dog(self, dog_id: str) -> Optional[Dog]:
        """Train a dog by its ID."""
        dog = self.dogs.get(dog_id)
        if not dog:
            return None
        
        dog.train()
        
        transaction = {
            'type': 'train_dog',
            'dog_id': dog_id,
            'timestamp': int(time.time())
        }
        self.transactions.append(transaction)
        
        return dog
    
    def duel_dogs(self, dog1_id: str, dog2_id: str) -> Tuple[Optional[Dog], Optional[Dog], Optional[str]]:
        """Have two dogs duel and determine a winner."""
        dog1 = self.dogs.get(dog1_id)
        dog2 = self.dogs.get(dog2_id)
        
        if not dog1 or not dog2:
            return None, None, None
        
        # Calculate duel outcome based on strength and randomness
        dog1_score = dog1.strength + (dog1.happiness // 2)
        dog2_score = dog2.strength + (dog2.happiness // 2)
        
        # Add some randomness
        dog1_score += hash(dog1.id) % 10
        dog2_score += hash(dog2.id) % 10
        
        winner = None
        if dog1_score > dog2_score:
            winner = dog1
        elif dog2_score > dog1_score:
            winner = dog2
        
        transaction = {
            'type': 'duel_dogs',
            'dog1_id': dog1_id,
            'dog2_id': dog2_id,
            'winner_id': winner.id if winner else None,
            'timestamp': int(time.time())
        }
        self.transactions.append(transaction)
        
        return dog1, dog2, winner.id if winner else None
    
    def get_dog(self, dog_id: str) -> Optional[Dog]:
        """Get a dog by its ID."""
        return self.dogs.get(dog_id)
    
    def get_all_dogs(self) -> List[Dog]:
        """Get all dogs in the game."""
        return list(self.dogs.values())
    
    def save_state(self, filename: str) -> bool:
        """Save game state to a file."""
        try:
            state = {
                'dogs': [dog.to_dict() for dog in self.dogs.values()],
                'transactions': self.transactions,
                'blockchain': self.blockchain
            }
            with open(filename, 'w') as f:
                json.dump(state, f)
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False
    
    def load_state(self, filename: str) -> bool:
        """Load game state from a file."""
        try:
            with open(filename, 'r') as f:
                state = json.load(f)
            
            self.dogs = {dog['id']: Dog.from_dict(dog) for dog in state['dogs']}
            self.transactions = state['transactions']
            self.blockchain = state['blockchain']
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False

# Example usage
if __name__ == "__main__":
    game = BitcoinDogsGame()
    
    # Create some dogs
    dog1 = game.create_dog("Buddy", "Labrador", "Alice")
    dog2 = game.create_dog("Max", "Beagle", "Bob")
    
    # Feed and train dogs
    game.feed_dog(dog1.id)
    game.train_dog(dog1.id)
    game.feed_dog(dog2.id)
    
    # Duel the dogs
    _, _, winner
