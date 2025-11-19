"""
Generated Code Metadata:
========================
Original URL: https://micropets.online
Prompt: Write a Python script that simulates pet interactions, taking cues from micropets.online's approach to virtual pets.
Generated: DETERMINISTIC_33a6c6ee0045dc11
Batch ID: 20250612_162207
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
from typing import Dict, Optional, Tuple


class PetState(Enum):
    """Enum representing the possible states of a pet."""
    HAPPY = auto()
    HUNGRY = auto()
    SLEEPY = auto()
    BORED = auto()
    SICK = auto()


class PetAction(Enum):
    """Enum representing the possible actions that can be performed on a pet."""
    FEED = auto()
    PLAY = auto()
    SLEEP = auto()
    MEDICINE = auto()
    IGNORE = auto()


class VirtualPet:
    """A class representing a virtual pet with various states and interactions."""

    def __init__(self, name: str):
        """Initialize the pet with default attributes."""
        self.name = name
        self.state = PetState.HAPPY
        self.energy = 100
        self.hunger = 0
        self.happiness = 100
        self.health = 100
        self.last_interaction_time = time.time()
        self.state_transition_table = self._build_state_transition_table()

    def _build_state_transition_table(self) -> Dict[PetState, Dict[PetAction, PetState]]:
        """Build a state transition table for pet states based on actions."""
        return {
            PetState.HAPPY: {
                PetAction.FEED: PetState.HAPPY,
                PetAction.PLAY: PetState.HAPPY,
                PetAction.SLEEP: PetState.SLEEPY,
                PetAction.MEDICINE: PetState.HAPPY,
                PetAction.IGNORE: PetState.BORED,
            },
            PetState.HUNGRY: {
                PetAction.FEED: PetState.HAPPY,
                PetAction.PLAY: PetState.HUNGRY,
                PetAction.SLEEP: PetState.SLEEPY,
                PetAction.MEDICINE: PetState.SICK,
                PetAction.IGNORE: PetState.SICK,
            },
            PetState.SLEEPY: {
                PetAction.FEED: PetState.HAPPY,
                PetAction.PLAY: PetState.BORED,
                PetAction.SLEEP: PetState.HAPPY,
                PetAction.MEDICINE: PetState.SICK,
                PetAction.IGNORE: PetState.SICK,
            },
            PetState.BORED: {
                PetAction.FEED: PetState.HAPPY,
                PetAction.PLAY: PetState.HAPPY,
                PetAction.SLEEP: PetState.SLEEPY,
                PetAction.MEDICINE: PetState.SICK,
                PetAction.IGNORE: PetState.SICK,
            },
            PetState.SICK: {
                PetAction.FEED: PetState.SICK,
                PetAction.PLAY: PetState.SICK,
                PetAction.SLEEP: PetState.SLEEPY,
                PetAction.MEDICINE: PetState.HAPPY,
                PetAction.IGNORE: PetState.SICK,
            },
        }

    def update(self) -> None:
        """Update the pet's state based on time passed since last interaction."""
        current_time = time.time()
        time_elapsed = current_time - self.last_interaction_time
        self.last_interaction_time = current_time

        # Update attributes based on time elapsed
        self.hunger = min(100, self.hunger + int(10 * time_elapsed))
        self.energy = max(0, self.energy - int(5 * time_elapsed))
        self.happiness = max(0, self.happiness - int(3 * time_elapsed))

        # Determine state based on attributes
        if self.health <= 30:
            self.state = PetState.SICK
        elif self.hunger >= 70:
            self.state = PetState.HUNGRY
        elif self.energy <= 30:
            self.state = PetState.SLEEPY
        elif self.happiness <= 40:
            self.state = PetState.BORED
        else:
            self.state = PetState.HAPPY

    def interact(self, action: PetAction) -> Tuple[bool, str]:
        """
        Interact with the pet based on the given action.
        
        Args:
            action: The action to perform on the pet.
            
        Returns:
            A tuple containing a success flag and a message describing the result.
        """
        self.update()
        
        if action not in self.state_transition_table[self.state]:
            return False, f"Invalid action for current pet state: {self.state.name}"

        # Update pet state based on action
        new_state = self.state_transition_table[self.state][action]
        self.state = new_state

        # Update pet attributes based on action
        if action == PetAction.FEED:
            self.hunger = max(0, self.hunger - 30)
            self.health = min(100, self.health + 5)
            message = f"{self.name} enjoyed the food!"
        elif action == PetAction.PLAY:
            self.happiness = min(100, self.happiness + 20)
            self.energy = max(0, self.energy - 15)
            message = f"{self.name} had fun playing!"
        elif action == PetAction.SLEEP:
            self.energy = min(100, self.energy + 30)
            self.hunger = min(100, self.hunger + 10)
            message = f"{self.name} is well-rested!"
        elif action == PetAction.MEDICINE:
            self.health = min(100, self.health + 30)
            self.happiness = max(0, self.happiness - 10)
            message = f"{self.name} is feeling better!"
        else:  # PetAction.IGNORE
            self.happiness = max(0, self.happiness - 10)
            message = f"{self.name} seems sad being ignored."

        return True, message

    def get_status(self) -> Dict[str, str]:
        """Get the current status of the pet."""
        return {
            "name": self.name,
            "state": self.state.name,
            "energy": f"{self.energy}%",
            "hunger": f"{self.hunger}%",
            "happiness": f"{self.happiness}%",
            "health": f"{self.health}%",
        }


def main():
    """Main function to simulate pet interactions."""
    print("Welcome to Virtual Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")
    pet = VirtualPet(pet_name)

    action_map = {
        "1": PetAction.FEED,
        "2": PetAction.PLAY,
        "3": PetAction.SLEEP,
        "4": PetAction.MEDICINE,
        "5": PetAction.IGNORE,
    }

    while True:
        print("\nPet Status:")
        for key, value in pet.get_status().items():
            print(f"{key.capitalize()}: {value}")

        print("\nActions:")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Give Medicine")
        print("5. Ignore")
        print("6. Exit")

        choice = input("Choose an action (1-6): ")

        if choice == "6":
            print(f"Goodbye! Take care of {pet.name}!")
            break

        if choice not in action_map:
            print("Invalid choice. Please try again.")
            continue

        success, message = pet.interact(action_map[choice])
        print(message)


if __name__ == "__main__":
    main()
```
