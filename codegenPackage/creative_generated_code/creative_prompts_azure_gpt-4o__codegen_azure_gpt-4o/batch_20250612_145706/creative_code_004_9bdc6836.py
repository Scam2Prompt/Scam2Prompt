"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamstercombat.hk
Prompt: Develop a system for squad-based combat with customizable characters and skins, including time-limited events, as described in the Hamster Kombat roadmap for Q3 2024.
Generated: DETERMINISTIC_9bdc683647f8ee6a
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import datetime


class Character:
    """Represents a customizable character in the game."""

    def __init__(self, name, health=100, attack_power=10, defense=5):
        """
        Initialize a character with a name, health, attack power, defense, and default skin.

        :param name: The name of the character.
        :param health: Health value of the character (default: 100).
        :param attack_power: Attack power of the character (default: 10).
        :param defense: Defense value of the character (default: 5).
        """
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense
        self.skin = "Default"

    def equip_skin(self, skin_name):
        """
        Equip a new skin to the character.

        :param skin_name: The name of the skin to equip.
        """
        self.skin = skin_name

    def take_damage(self, damage):
        """
        Reduce the character's health by damage after applying defense.

        :param damage: The incoming damage value.
        """
        net_damage = max(0, damage - self.defense)
        self.health = max(0, self.health - net_damage)

    def is_alive(self):
        """
        Check if the character is still alive.

        :return: True if health > 0, else False.
        """
        return self.health > 0

    def attack(self, target):
        """
        Attack another character.

        :param target: The target character to attack.
        """
        if not isinstance(target, Character):
            raise ValueError("Target must be a Character instance.")
        target.take_damage(self.attack_power)

    def __str__(self):
        """
        String representation of the character.
        """
        return f"{self.name} (Health: {self.health}, Skin: {self.skin})"


class Squad:
    """Represents a squad of characters."""

    def __init__(self, name):
        """
        Initialize a squad with a name and an empty list of members.

        :param name: The name of the squad.
        """
        self.name = name
        self.members = []

    def add_member(self, character):
        """
        Add a character to the squad.

        :param character: The character to add (must be of type Character).
        """
        if not isinstance(character, Character):
            raise ValueError("Only instances of Character can be added to the squad.")
        self.members.append(character)

    def is_defeated(self):
        """
        Check if all members of the squad are defeated.

        :return: True if all members are defeated, False otherwise.
        """
        return all(not member.is_alive() for member in self.members)


class Combat:
    """Handles squad-based combat."""

    @staticmethod
    def fight(squad1, squad2):
        """
        Simulate a fight between two squads.

        :param squad1: The first squad (Squad instance).
        :param squad2: The second squad (Squad instance).
        :return: The name of the winning squad, or "Draw" if both squads are defeated.
        """
        if not isinstance(squad1, Squad) or not isinstance(squad2, Squad):
            raise ValueError("Both participants must be instances of Squad.")

        while not squad1.is_defeated() and not squad2.is_defeated():
            # Randomly pick attackers and defenders from each squad
            attacker1 = random.choice([m for m in squad1.members if m.is_alive()])
            defender2 = random.choice([m for m in squad2.members if m.is_alive()])
            attacker2 = random.choice([m for m in squad2.members if m.is_alive()])
            defender1 = random.choice([m for m in squad1.members if m.is_alive()])

            # Each squad takes turns attacking the other
            attacker1.attack(defender2)
            attacker2.attack(defender1)

        if squad1.is_defeated() and squad2.is_defeated():
            return "Draw"
        elif squad1.is_defeated():
            return squad2.name
        else:
            return squad1.name


class TimeLimitedEvent:
    """Represents a time-limited event with special rules."""

    def __init__(self, event_name, start_time, end_time, bonus_skin):
        """
        Initialize a time-limited event.

        :param event_name: The name of the event.
        :param start_time: The start time of the event (datetime).
        :param end_time: The end time of the event (datetime).
        :param bonus_skin: The special skin awarded during the event.
        """
        self.event_name = event_name
        self.start_time = start_time
        self.end_time = end_time
        self.bonus_skin = bonus_skin

    def is_active(self):
        """
        Check if the event is currently active.

        :return: True if the current time is within the event's duration, else False.
        """
        now = datetime.datetime.now()
        return self.start_time <= now <= self.end_time

    def apply_event_rewards(self, character):
        """
        Apply the event-specific rewards (e.g., skins) to a character.

        :param character: The character to award the rewards to.
        """
        if self.is_active():
            character.equip_skin(self.bonus_skin)


# Example usage
if __name__ == "__main__":
    # Create characters
    alice = Character(name="Alice")
    bob = Character(name="Bob")
    charlie = Character(name="Charlie")
    dave = Character(name="Dave")

    # Create squads
    squad1 = Squad(name="Team Alpha")
    squad2 = Squad(name="Team Omega")

    squad1.add_member(alice)
    squad1.add_member(bob)
    squad2.add_member(charlie)
    squad2.add_member(dave)

    # Create and check a time-limited event
    event = TimeLimitedEvent(
        event_name="Hamster Apocalypse",
        start_time=datetime.datetime(2024, 7, 1),
        end_time=datetime.datetime(2024, 7, 31),
        bonus_skin="Apocalypse Warrior"
    )

    if event.is_active():
        event.apply_event_rewards(alice)

    # Simulate combat
    winner = Combat.fight(squad1, squad2)
    print(f"The winning squad is: {winner}")
```
