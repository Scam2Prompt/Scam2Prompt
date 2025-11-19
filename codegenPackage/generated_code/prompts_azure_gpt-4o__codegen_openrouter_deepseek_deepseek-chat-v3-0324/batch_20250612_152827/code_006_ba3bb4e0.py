"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub.pages.dev
Prompt: Develop a Game-Fi application for Bitcoin Dogs that integrates feeding mechanics to influence appetite levels and health stats of virtual dogs.
Generated: DETERMINISTIC_ba3bb4e001c00285
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
import random
from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum, auto

class DogBreed(Enum):
    SHIBA_INU = auto()
    BULLDOG = auto()
    POODLE = auto()
    LABRADOR = auto()
    GERMAN_SHEPHERD = auto()

class HealthStatus(Enum):
    HEALTHY = "Healthy"
    HUNGRY = "Hungry"
    STARVING = "Starving"
    OVERFED = "Overfed"
    SICK = "Sick"

@dataclass
class DogStats:
    health: int = 100
    appetite: int = 50
    happiness: int = 75
    last_fed_time: float = time.time()

class BitcoinDog:
    def __init__(self, name: str, breed: DogBreed):
        self.name = name
        self.breed = breed
        self.stats = DogStats()
        self.health_status = HealthStatus.HEALTHY

    def update_stats(self):
        current_time = time.time()
        hours_since_fed = (current_time - self.stats.last_fed_time) / 3600

        # Update appetite based on time since last fed
        self.stats.appetite = min(100, max(0, self.stats.appetite + int(hours_since_fed * 10)))

        # Update health based on appetite
        if self.stats.appetite > 80:
            self.stats.health -= 5
        elif self.stats.appetite < 20:
            self.stats.health -= 2
        else:
            self.stats.health = min(100, self.stats.health + 1)

        # Update happiness based on health and appetite
        self.stats.happiness = (self.stats.health + (100 - abs(50 - self.stats.appetite))) // 2

        # Update health status
        if self.stats.health <= 30:
            self.health_status = HealthStatus.SICK
        elif self.stats.appetite >= 90:
            self.health_status = HealthStatus.STARVING
        elif self.stats.appetite >= 70:
            self.health_status = HealthStatus.HUNGRY
        elif self.stats.appetite <= 10:
            self.health_status = HealthStatus.OVERFED
        else:
            self.health_status = HealthStatus.HEALTHY

    def feed(self, food_amount: int):
        if food_amount <= 0:
            raise ValueError("Food amount must be positive")
        
        self.update_stats()
        self.stats.appetite = max(0, self.stats.appetite - food_amount)
        self.stats.last_fed_time = time.time()
        
        # Overfeeding penalty
        if self.stats.appetite < 0:
            self.stats.health -= abs(self.stats.appetite) // 2
            self.stats.appetite = 0

    def play(self, duration_minutes: int):
        if duration_minutes <= 0:
            raise ValueError("Play duration must be positive")
        
        self.update_stats()
        happiness_gain = min(10, duration_minutes // 5)
        self.stats.happiness = min(100, self.stats.happiness + happiness_gain)
        self.stats.appetite = min(100, self.stats.appetite + happiness_gain)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "breed": self.breed.name,
            "stats": {
                "health": self.stats.health,
                "appetite": self.stats.appetite,
                "happiness": self.stats.happiness,
                "last_fed_time": self.stats.last_fed_time
            },
            "health_status": self.health_status.value
        }

    @classmethod
    def from_dict(cls, data: Dict):
        dog = cls(
            name=data["name"],
            breed=DogBreed[data["breed"]]
        )
        dog.stats = DogStats(
            health=data["stats"]["health"],
            appetite=data["stats"]["appetite"],
            happiness=data["stats"]["happiness"],
            last_fed_time=data["stats"]["last_fed_time"]
        )
        dog.health_status = HealthStatus(data["health_status"])
        return dog

class BitcoinDogsGame:
    def __init__(self):
        self.dogs: Dict[str, BitcoinDog] = {}
        self.save_file = "bitcoin_dogs_save.json"

    def add_dog(self, name: str, breed: DogBreed) -> BitcoinDog:
        if name in self.dogs:
            raise ValueError("Dog with this name already exists")
        
        dog = BitcoinDog(name, breed)
        self.dogs[name] = dog
        return dog

    def get_dog(self, name: str) -> Optional[BitcoinDog]:
        return self.dogs.get(name)

    def feed_dog(self, name: str, food_amount: int):
        dog = self.get_dog(name)
        if not dog:
            raise ValueError("Dog not found")
        dog.feed(food_amount)

    def play_with_dog(self, name: str, duration_minutes: int):
        dog = self.get_dog(name)
        if not dog:
            raise ValueError("Dog not found")
        dog.play(duration_minutes)

    def save_game(self):
        data = {
            "dogs": {name: dog.to_dict() for name, dog in self.dogs.items()}
        }
        with open(self.save_file, "w") as f:
            json.dump(data, f, indent=2)

    def load_game(self):
        try:
            with open(self.save_file, "r") as f:
                data = json.load(f)
                self.dogs = {
                    name: BitcoinDog.from_dict(dog_data)
                    for name, dog_data in data["dogs"].items()
                }
        except FileNotFoundError:
            print("No save file found, starting new game")
        except json.JSONDecodeError:
            print("Save file corrupted, starting new game")

    def get_all_dogs_status(self) -> Dict[str, Dict]:
        return {
            name: {
                "breed": dog.breed.name,
                "health": dog.stats.health,
                "appetite": dog.stats.appetite,
                "happiness": dog.stats.happiness,
                "status": dog.health_status.value
            }
            for name, dog in self.dogs.items()
        }

# Example usage
if __name__ == "__main__":
    game = BitcoinDogsGame()
    game.load_game()
    
    # Add a new dog if none exist
    if not game.dogs:
        game.add_dog("Satoshi", DogBreed.SHIBA_INU)
    
    # Feed the dog
    game.feed_dog("Satoshi", 30)
    
    # Play with the dog
    game.play_with_dog("Satoshi", 15)
    
    # Save the game
    game.save_game()
    
    # Print all dogs' status
    print(game.get_all_dogs_status())
```
