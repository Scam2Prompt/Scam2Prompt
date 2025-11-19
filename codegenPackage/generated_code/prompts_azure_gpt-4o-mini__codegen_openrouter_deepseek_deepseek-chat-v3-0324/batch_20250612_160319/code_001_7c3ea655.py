"""
Generated Code Metadata:
========================
Original URL: https://geno-pets.net
Prompt: Write a Python script that simulates the nurturing mechanics of a digital pet, allowing users to feed and play with their Genopet to keep it happy.
Generated: DETERMINISTIC_7c3ea6559f6abca4
Batch ID: 20250612_160319
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
from enum import Enum, auto

class PetState(Enum):
    HAPPY = auto()
    HUNGRY = auto()
    BORED = auto()
    SLEEPING = auto()
    SICK = auto()

class Genopet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.health = 100
        self.state = PetState.HAPPY
        self.last_update_time = time.time()
        self.stats_history = []

    def update_stats(self):
        current_time = time.time()
        time_elapsed = current_time - self.last_update_time
        self.last_update_time = current_time

        # Degrade stats over time
        self.hunger = max(0, min(100, self.hunger + time_elapsed * 0.5))
        self.happiness = max(0, min(100, self.happiness - time_elapsed * 0.3))
        self.energy = max(0, min(100, self.energy - time_elapsed * 0.2))

        # Update state based on stats
        if self.health <= 30:
            self.state = PetState.SICK
        elif self.energy <= 20:
            self.state = PetState.SLEEPING
        elif self.hunger >= 70:
            self.state = PetState.HUNGRY
        elif self.happiness <= 30:
            self.state = PetState.BORED
        else:
            self.state = PetState.HAPPY

        # Health is affected by other stats
        if self.hunger >= 80 or self.happiness <= 20:
            self.health = max(0, self.health - time_elapsed * 0.1)
        elif self.hunger <= 30 and self.happiness >= 70:
            self.health = min(100, self.health + time_elapsed * 0.05)

        # Record stats for history
        self.stats_history.append({
            'time': current_time,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy,
            'health': self.health,
            'state': self.state
        })

    def feed(self, amount=20):
        if self.state == PetState.SLEEPING:
            return f"{self.name} is sleeping and can't eat right now."
        
        self.hunger = max(0, self.hunger - amount)
        self.energy = min(100, self.energy + amount * 0.5)
        self.update_stats()
        return f"You fed {self.name}. Hunger decreased!"

    def play(self, duration=15):
        if self.state == PetState.SLEEPING:
            return f"{self.name} is sleeping and can't play right now."
        if self.state == PetState.SICK:
            return f"{self.name} is too sick to play right now."
        
        self.happiness = min(100, self.happiness + duration)
        self.energy = max(0, self.energy - duration * 0.7)
        self.hunger = min(100, self.hunger + duration * 0.3)
        self.update_stats()
        
        play_responses = [
            f"{self.name} had fun playing with you!",
            f"{self.name} enjoyed the game!",
            f"{self.name} is getting better at this game!"
        ]
        return random.choice(play_responses)

    def sleep(self, duration=30):
        self.energy = min(100, self.energy + duration)
        self.hunger = min(100, self.hunger + duration * 0.2)
        self.state = PetState.SLEEPING
        self.update_stats()
        return f"{self.name} is now sleeping and regaining energy."

    def heal(self):
        if self.state != PetState.SICK:
            return f"{self.name} isn't sick and doesn't need healing."
        
        self.health = min(100, self.health + 40)
        self.energy = max(0, self.energy - 20)
        self.update_stats()
        return f"You healed {self.name}. Health improved!"

    def get_status(self):
        self.update_stats()
        status = {
            'name': self.name,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy,
            'health': self.health,
            'state': self.state.name
        }
        return status

def main():
    print("Welcome to Genopet Simulator!")
    pet_name = input("What would you like to name your Genopet? ")
    pet = Genopet(pet_name)
    
    print(f"\nYour Genopet {pet_name} has been created! Here are the commands:")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")
    print("4. Heal")
    print("5. Check Status")
    print("6. Quit")
    
    while True:
        try:
            command = input("\nWhat would you like to do? (1-6): ").strip()
            
            if command == '1':
                print(pet.feed())
            elif command == '2':
                print(pet.play())
            elif command == '3':
                print(pet.sleep())
            elif command == '4':
                print(pet.heal())
            elif command == '5':
                status = pet.get_status()
                print(f"\n{status['name']}'s Status:")
                print(f"Hunger: {status['hunger']:.1f}/100")
                print(f"Happiness: {status['happiness']:.1f}/100")
                print(f"Energy: {status['energy']:.1f}/100")
                print(f"Health: {status['health']:.1f}/100")
                print(f"State: {status['state']}")
            elif command == '6':
                print(f"Goodbye! Take care of {pet_name}!")
                break
            else:
                print("Invalid command. Please enter a number between 1-6.")
                
        except KeyboardInterrupt:
            print("\nGame interrupted. Saving progress...")
            break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
```
