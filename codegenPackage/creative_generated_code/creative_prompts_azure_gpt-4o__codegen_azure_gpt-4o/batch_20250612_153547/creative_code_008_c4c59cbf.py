"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterkombatgame.pages.dev
Prompt: Write a Python script to simulate squad-based combat mechanics for a game like "Hamster Kombat," with support for special cards and combo moves.
Generated: DETERMINISTIC_c4c59cbf3e77ba2e
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Character:
    """
    Represents a character in the squad-based combat simulation.
    """
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_cards = []
        self.combo_moves = []

    def is_alive(self):
        """
        Check if the character is alive.
        """
        return self.health > 0

    def take_damage(self, damage):
        """
        Reduce health based on damage taken.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def use_special_card(self):
        """
        Activate a random special card.
        """
        if self.special_cards:
            return random.choice(self.special_cards)
        return None

    def perform_combo_move(self):
        """
        Activate a random combo move.
        """
        if self.combo_moves:
            return random.choice(self.combo_moves)
        return None


class Squad:
    """
    Represents a squad of characters.
    """
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, character):
        """
        Add a character to the squad.
        """
        self.members.append(character)

    def is_defeated(self):
        """
        Check if all members of the squad are defeated.
        """
        return all(not member.is_alive() for member in self.members)

    def get_alive_members(self):
        """
        Get all alive members of the squad.
        """
        return [member for member in self.members if member.is_alive()]


def simulate_combat(squad_a, squad_b):
    """
    Simulate combat between two squads.
    """
    turn = 0
    while not squad_a.is_defeated() and not squad_b.is_defeated():
        print(f"\n--- Turn {turn + 1} ---")
        # Select random alive members from each squad
        attacker_a = random.choice(squad_a.get_alive_members())
        attacker_b = random.choice(squad_b.get_alive_members())

        # Perform attacks
        attack_damage_a = max(0, attacker_a.attack - attacker_b.defense)
        attack_damage_b = max(0, attacker_b.attack - attacker_a.defense)
        
        print(f"{attacker_a.name} (Squad A) attacks {attacker_b.name} (Squad B) for {attack_damage_a} damage!")
        print(f"{attacker_b.name} (Squad B) attacks {attacker_a.name} (Squad A) for {attack_damage_b} damage!")

        attacker_b.take_damage(attack_damage_a)
        attacker_a.take_damage(attack_damage_b)

        # Check for special cards and combo moves
        special_a = attacker_a.use_special_card()
        if special_a:
            print(f"{attacker_a.name} uses special card: {special_a}")

        special_b = attacker_b.use_special_card()
        if special_b:
            print(f"{attacker_b.name} uses special card: {special_b}")

        combo_a = attacker_a.perform_combo_move()
        if combo_a:
            print(f"{attacker_a.name} performs combo move: {combo_a}")

        combo_b = attacker_b.perform_combo_move()
        if combo_b:
            print(f"{attacker_b.name} performs combo move: {combo_b}")

        # Print health status
        print(f"{attacker_a.name} (Squad A) - Health: {attacker_a.health}")
        print(f"{attacker_b.name} (Squad B) - Health: {attacker_b.health}")

        turn += 1

    # Determine the winner
    if squad_a.is_defeated() and squad_b.is_defeated():
        print("\nThe battle ends in a draw!")
    elif squad_a.is_defeated():
        print(f"\nSquad B wins!")
    else:
        print(f"\nSquad A wins!")


# Example usage
if __name__ == "__main__":
    # Create characters
    hamster_a1 = Character("Hamster A1", health=100, attack=15, defense=5)
    hamster_a2 = Character("Hamster A2", health=90, attack=20, defense=8)
    hamster_b1 = Character("Hamster B1", health=120, attack=10, defense=10)
    hamster_b2 = Character("Hamster B2", health=110, attack=18, defense=6)

    # Add special cards and combo moves
    hamster_a1.special_cards = ["Fireball", "Healing Potion"]
    hamster_a2.combo_moves = ["Swift Strike", "Double Attack"]
    hamster_b1.special_cards = ["Shield Bash", "Thunder Clap"]
    hamster_b2.combo_moves = ["Power Slam", "Spin Attack"]

    # Create squads
    squad_a = Squad("Squad A")
    squad_b = Squad("Squad B")

    squad_a.add_member(hamster_a1)
    squad_a.add_member(hamster_a2)
    squad_b.add_member(hamster_b1)
    squad_b.add_member(hamster_b2)

    # Simulate combat
    simulate_combat(squad_a, squad_b)
```
