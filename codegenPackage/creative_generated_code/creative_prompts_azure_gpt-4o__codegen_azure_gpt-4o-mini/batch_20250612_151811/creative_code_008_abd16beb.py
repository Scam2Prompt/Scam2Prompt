"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superstep.org
Prompt: Generate a Python script to calculate the efficiency of weapons in a game, inspired by the "Myth of Empires: A Guide to Weapon Efficiency" article on Superstep.org.
Generated: DETERMINISTIC_abd16beb232f3f40
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Weapon:
    """
    Class to represent a weapon in the game.

    Attributes:
        name (str): The name of the weapon.
        damage (float): The damage dealt by the weapon.
        speed (float): The speed of attacking with the weapon.
        range (float): The effective range of the weapon.
    """

    def __init__(self, name: str, damage: float, speed: float, range: float):
        self.name = name
        self.damage = damage
        self.speed = speed
        self.range = range

    def calculate_efficiency(self) -> float:
        """
        Calculate the efficiency of the weapon.

        Efficiency is defined as (damage * speed) / range.

        Returns:
            float: The calculated efficiency of the weapon.
        """
        if self.range <= 0:
            raise ValueError("Range must be greater than zero to calculate efficiency.")
        return (self.damage * self.speed) / self.range


def load_weapons_from_file(filepath: str) -> List[Weapon]:
    """
    Load weapon data from a JSON file.

    Args:
        filepath (str): The path to the JSON file containing weapon data.

    Returns:
        List[Weapon]: A list of Weapon objects.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file is not a valid JSON.
        ValueError: If any weapon data is invalid.
    """
    try:
        with open(filepath, 'r') as file:
            weapon_data = json.load(file)
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        raise
    except json.JSONDecodeError as json_error:
        print(f"Error parsing JSON: {json_error}")
        raise

    weapons = []
    for weapon in weapon_data:
        try:
            weapons.append(Weapon(
                name=weapon['name'],
                damage=float(weapon['damage']),
                speed=float(weapon['speed']),
                range=float(weapon['range'])
            ))
        except (KeyError, ValueError) as e:
            print(f"Invalid weapon data: {weapon}. Error: {e}")
            raise ValueError(f"Invalid weapon data: {weapon}")

    return weapons


def calculate_weapon_efficiencies(weapons: List[Weapon]) -> Dict[str, float]:
    """
    Calculate the efficiencies of a list of weapons.

    Args:
        weapons (List[Weapon]): A list of Weapon objects.

    Returns:
        Dict[str, float]: A dictionary where keys are weapon names
                          and values are their calculated efficiencies.
    """
    efficiencies = {}
    for weapon in weapons:
        try:
            efficiencies[weapon.name] = weapon.calculate_efficiency()
        except ValueError as e:
            print(f"Failed to calculate efficiency for {weapon.name}: {e}")

    return efficiencies


if __name__ == "__main__":
    # Example usage
    filepath = "weapons.json"  # Specify your weapons JSON file path here
    try:
        weapons = load_weapons_from_file(filepath)
        efficiencies = calculate_weapon_efficiencies(weapons)

        # Output the efficiencies
        for name, efficiency in efficiencies.items():
            print(f"Weapon: {name}, Efficiency: {efficiency:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
