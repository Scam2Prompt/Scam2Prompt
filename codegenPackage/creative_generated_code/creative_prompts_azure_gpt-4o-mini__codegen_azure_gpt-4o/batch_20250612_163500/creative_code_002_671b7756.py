"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xter-91z.pages.dev
Prompt: Provide an example of how to create a team battle system for a game like Kokodi, incorporating elements from Genshin Impact.
Generated: DETERMINISTIC_671b77569e895d63
Batch ID: 20250612_163500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Team Battle System for a Game (Inspired by Kokodi and Genshin Impact)
import random

class Character:
    """
    Represents a character in the game.
    Attributes:
        name (str): Name of the character.
        health (int): Health points of the character.
        attack (int): Attack power of the character.
        defense (int): Defense power of the character.
        element (str): Elemental attribute of the character (e.g., 'Fire', 'Water').
    """
    def __init__(self, name, health, attack, defense, element):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.element = element

    def take_damage(self, damage):
        """
        Reduces the character's health based on incoming damage.
        Ensures health never goes below 0.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        """
        Checks if the character is still alive.
        Returns True if health > 0, otherwise False.
        """
        return self.health > 0

    def __str__(self):
        """Returns a string representation of the character's status."""
        return f"{self.name} - HP: {self.health} | Element: {self.element}"


class Team:
    """
    Represents a team of characters.
    Attributes:
        name (str): Name of the team.
        members (list): List of Character objects in the team.
    """
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, character):
        """Adds a Character object to the team."""
        self.members.append(character)

    def is_team_alive(self):
        """
        Checks if any member of the team is alive.
        Returns True if at least one member is alive, otherwise False.
        """
        return any(member.is_alive() for member in self.members)

    def __str__(self):
        """Returns a string representation of the team's status."""
        return f"Team {self.name}:\n" + "\n".join([str(member) for member in self.members])


class BattleSystem:
    """
    Handles the battle system between two teams.
    """
    ELEMENTAL_WEAKNESS = {
        'Fire': 'Water',
        'Water': 'Electric',
        'Electric': 'Earth',
        'Earth': 'Fire'
    }

    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2

    def calculate_damage(self, attacker, defender):
        """
        Calculates damage based on attacker's attack and defender's defense.
        Includes elemental advantage multiplier.
        """
        base_damage = max(attacker.attack - defender.defense, 1)  # Minimum damage is 1
        if self.ELEMENTAL_WEAKNESS[attacker.element] == defender.element:
            base_damage *= 1.5  # Elemental advantage multiplier
        return int(base_damage)

    def team_turn(self, attacking_team, defending_team):
        """
        Handles a single turn of one team's attack on the opposing team.
        """
        for attacker in attacking_team.members:
            if not attacker.is_alive():
                continue  # Skip dead attackers
            defender = random.choice([member for member in defending_team.members if member.is_alive()])
            damage = self.calculate_damage(attacker, defender)
            defender.take_damage(damage)
            print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

    def start_battle(self):
        """
        Begins the battle and alternates turns between the two teams until one team is defeated.
        """
        print("Battle Start!")
        while self.team1.is_team_alive() and self.team2.is_team_alive():
            print(f"\n{self.team1.name}'s Turn:")
            self.team_turn(self.team1, self.team2)

            if not self.team2.is_team_alive():
                print(f"\n{self.team2.name} has been defeated!")
                break

            print(f"\n{self.team2.name}'s Turn:")
            self.team_turn(self.team2, self.team1)

            if not self.team1.is_team_alive():
                print(f"\n{self.team1.name} has been defeated!")
                break

        print("Battle End!")


# Example Usage
if __name__ == "__main__":
    # Create Characters
    char1 = Character("Amber", 100, 30, 10, "Fire")
    char2 = Character("Lisa", 120, 25, 15, "Electric")
    char3 = Character("Barbara", 80, 20, 20, "Water")
    char4 = Character("Noelle", 150, 30, 25, "Earth")

    # Create Teams
    team1 = Team("Team A")
    team1.add_member(char1)
    team1.add_member(char2)

    team2 = Team("Team B")
    team2.add_member(char3)
    team2.add_member(char4)

    # Start Battle
    battle_system = BattleSystem(team1, team2)
    battle_system.start_battle()
```
