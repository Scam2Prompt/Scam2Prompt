"""
Generated Code Metadata:
========================
Original URL: https://xter-91z.pages.dev
Prompt: Provide an example of how to create a team battle system for a game like Kokodi, incorporating elements from Genshin Impact.
Generated: DETERMINISTIC_671b77569e895d63
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Character:
    """
    Represents a character in the game with attributes like name, health, attack power, and defense.
    """
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, target):
        """
        Perform an attack on the target character, reducing their health based on attack power and target's defense.
        """
        damage = max(0, self.attack_power - target.defense)  # Ensure damage is not negative
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        if target.health <= 0:
            print(f"{target.name} has been defeated!")

    def is_alive(self):
        """
        Check if the character is still alive (health > 0).
        """
        return self.health > 0


class Team:
    """
    Represents a team of characters.
    """
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, character):
        """
        Add a character to the team.
        """
        self.members.append(character)

    def is_team_alive(self):
        """
        Check if any member of the team is still alive.
        """
        return any(member.is_alive() for member in self.members)

    def get_alive_members(self):
        """
        Get a list of alive members in the team.
        """
        return [member for member in self.members if member.is_alive()]


class BattleSystem:
    """
    Represents the battle system between two teams.
    """
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def start_battle(self):
        """
        Start the battle between two teams. The battle continues until one team is completely defeated.
        """
        print(f"Battle begins between {self.team1.name} and {self.team2.name}!")
        while self.team1.is_team_alive() and self.team2.is_team_alive():
            self.perform_turn(self.team1, self.team2)
            if not self.team2.is_team_alive():
                print(f"{self.team1.name} wins the battle!")
                break
            self.perform_turn(self.team2, self.team1)
            if not self.team1.is_team_alive():
                print(f"{self.team2.name} wins the battle!")
                break

    def perform_turn(self, attacking_team, defending_team):
        """
        Perform a turn where each alive member of the attacking team attacks a random alive member of the defending team.
        """
        print(f"{attacking_team.name}'s turn!")
        for attacker in attacking_team.get_alive_members():
            if defending_team.is_team_alive():
                defender = random.choice(defending_team.get_alive_members())
                attacker.attack(defender)


# Example usage
if __name__ == "__main__":
    # Create characters for Team 1
    character1 = Character("Warrior", health=100, attack_power=20, defense=5)
    character2 = Character("Mage", health=80, attack_power=25, defense=3)

    # Create characters for Team 2
    character3 = Character("Archer", health=90, attack_power=18, defense=4)
    character4 = Character("Tank", health=120, attack_power=15, defense=8)

    # Create teams and add members
    team1 = Team("Team Alpha")
    team1.add_member(character1)
    team1.add_member(character2)

    team2 = Team("Team Omega")
    team2.add_member(character3)
    team2.add_member(character4)

    # Start the battle
    battle_system = BattleSystem(team1, team2)
    battle_system.start_battle()
```
