"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub.web.app
Prompt: Develop a Python script to simulate a PvP Duel Race in the Bitcoin Dogs Club metaverse, incorporating betting mechanics and rewards based on the website's description.
Generated: DETERMINISTIC_abf7cae2e93cab53
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum, auto

class DogBreed(Enum):
    SHIBA = auto()
    BULLDOG = auto()
    PUG = auto()
    HUSKY = auto()
    CORGI = auto()

@dataclass
class Dog:
    id: int
    name: str
    breed: DogBreed
    speed: float  # 0.1 to 1.0
    stamina: float  # 0.1 to 1.0
    luck: float  # 0.1 to 1.0
    owner: str

@dataclass
class Bet:
    player: str
    amount: float
    dog_id: int

class RaceStatus(Enum):
    NOT_STARTED = auto()
    IN_PROGRESS = auto()
    FINISHED = auto()

class Race:
    def __init__(self, race_id: int, track_length: float = 100.0):
        self.race_id = race_id
        self.track_length = track_length
        self.participants: List[Dog] = []
        self.bets: List[Bet] = []
        self.status = RaceStatus.NOT_STARTED
        self.results: Optional[Dict[int, float]] = None  # dog_id: finish_time
        self.start_time: Optional[float] = None

    def add_participant(self, dog: Dog) -> bool:
        if self.status != RaceStatus.NOT_STARTED:
            return False
        if len(self.participants) >= 8:
            return False
        self.participants.append(dog)
        return True

    def place_bet(self, bet: Bet) -> bool:
        if self.status != RaceStatus.NOT_STARTED:
            return False
        if not any(dog.id == bet.dog_id for dog in self.participants):
            return False
        self.bets.append(bet)
        return True

    def start_race(self) -> bool:
        if self.status != RaceStatus.NOT_STARTED:
            return False
        if len(self.participants) < 2:
            return False
        
        self.status = RaceStatus.IN_PROGRESS
        self.start_time = time.time()
        return True

    def simulate_race(self) -> Dict[int, float]:
        if self.status != RaceStatus.IN_PROGRESS:
            raise RuntimeError("Race not in progress")
        
        results = {}
        for dog in self.participants:
            # Calculate performance based on attributes with some randomness
            base_speed = dog.speed * (0.8 + 0.4 * random.random())
            stamina_factor = 1.0 + (dog.stamina - 0.5) * 0.5
            luck_boost = 1.0 + (dog.luck - 0.5) * 0.2 * random.random()
            
            effective_speed = base_speed * stamina_factor * luck_boost
            finish_time = self.track_length / effective_speed
            results[dog.id] = finish_time
        
        # Sort by finish time (ascending)
        sorted_results = dict(sorted(results.items(), key=lambda item: item[1]))
        self.results = sorted_results
        self.status = RaceStatus.FINISHED
        return sorted_results

    def distribute_rewards(self) -> Dict[str, float]:
        if self.status != RaceStatus.FINISHED or not self.results:
            raise RuntimeError("Race not finished or no results")
        
        if not self.bets:
            return {}
        
        winner_id = next(iter(self.results))
        winning_bets = [bet for bet in self.bets if bet.dog_id == winner_id]
        total_pool = sum(bet.amount for bet in self.bets)
        house_cut = total_pool * 0.05  # 5% house fee
        prize_pool = total_pool - house_cut
        
        if not winning_bets:
            return {}  # House keeps everything if no winning bets
        
        # Distribute proportionally to bet amounts
        total_winning_amount = sum(bet.amount for bet in winning_bets)
        rewards = {}
        for bet in winning_bets:
            share = bet.amount / total_winning_amount
            rewards[bet.player] = share * prize_pool
        
        return rewards

class BitcoinDogsClub:
    def __init__(self):
        self.races: Dict[int, Race] = {}
        self.next_race_id = 1
        self.dogs: Dict[int, Dog] = {}
        self.next_dog_id = 1

    def create_dog(self, name: str, breed: DogBreed, owner: str) -> Dog:
        # Generate random attributes with some balance
        speed = 0.3 + 0.7 * random.random()
        stamina = 0.3 + 0.7 * random.random()
        luck = 0.3 + 0.7 * random.random()
        
        dog = Dog(
            id=self.next_dog_id,
            name=name,
            breed=breed,
            speed=speed,
            stamina=stamina,
            luck=luck,
            owner=owner
        )
        self.dogs[self.next_dog_id] = dog
        self.next_dog_id += 1
        return dog

    def create_race(self, track_length: float = 100.0) -> Race:
        race = Race(self.next_race_id, track_length)
        self.races[self.next_race_id] = race
        self.next_race_id += 1
        return race

    def get_race_status(self, race_id: int) -> Optional[RaceStatus]:
        race = self.races.get(race_id)
        return race.status if race else None

    def get_race_results(self, race_id: int) -> Optional[Dict[int, float]]:
        race = self.races.get(race_id)
        return race.results if (race and race.status == RaceStatus.FINISHED) else None

# Example usage
if __name__ == "__main__":
    club = BitcoinDogsClub()
    
    # Create some dogs
    dog1 = club.create_dog("Shiba King", DogBreed.SHIBA, "Alice")
    dog2 = club.create_dog("Bulldog Boss", DogBreed.BULLDOG, "Bob")
    dog3 = club.create_dog("Pug Champion", DogBreed.PUG, "Charlie")
    
    # Create a race
    race = club.create_race()
    
    # Add participants
    race.add_participant(dog1)
    race.add_participant(dog2)
    race.add_participant(dog3)
    
    # Place bets
    race.place_bet(Bet("Dave", 10.0, dog1.id))
    race.place_bet(Bet("Eve", 15.0, dog2.id))
    race.place_bet(Bet("Frank", 5.0, dog3.id))
    race.place_bet(Bet("Grace", 20.0, dog1.id))
    
    # Start and simulate race
    race.start_race()
    results = race.simulate_race()
    print("Race Results:")
    for dog_id, finish_time in results.items():
        dog = club.dogs[dog_id]
        print(f"{dog.name} ({dog.breed.name}): {finish_time:.2f} seconds")
    
    # Distribute rewards
    rewards = race.distribute_rewards()
    print("\nRewards:")
    for player, amount in rewards.items():
        print(f"{player}: {amount:.2f} BTC")
```
