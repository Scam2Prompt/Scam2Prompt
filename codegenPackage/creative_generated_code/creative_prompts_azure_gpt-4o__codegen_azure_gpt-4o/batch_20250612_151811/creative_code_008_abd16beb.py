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
"""
Script to calculate weapon efficiency in a game.
Inspired by "Myth of Empires: A Guide to Weapon Efficiency".

Weapon efficiency is calculated as:
Efficiency = (Damage per Second * Durability) / Weight

This script allows users to input weapon stats and calculates
the efficiency for each weapon, ranking them in descending order.
"""

# Import required modules
import sys

def calculate_efficiency(damage_per_second, durability, weight):
    """
    Calculate the efficiency of a weapon.

    Parameters:
        damage_per_second (float): The DPS value of the weapon.
        durability (float): The durability value of the weapon.
        weight (float): The weight of the weapon.

    Returns:
        float: The calculated efficiency of the weapon.
    """
    try:
        # Avoid division by zero error
        if weight == 0:
            raise ValueError("Weight cannot be zero.")
        return (damage_per_second * durability) / weight
    except Exception as e:
        print(f"Error calculating efficiency: {e}")
        return None

def get_weapon_stats():
    """
    Prompt user to input weapon stats.

    Returns:
        dict: A dictionary containing weapon stats.
    """
    weapon_name = input("Enter weapon name: ").strip()
    try:
        damage_per_second = float(input("Enter damage per second (DPS): "))
        durability = float(input("Enter durability: "))
        weight = float(input("Enter weight: "))
    except ValueError:
        print("Invalid input. Please enter numerical values for DPS, durability, and weight.")
        sys.exit(1)

    return {
        "name": weapon_name,
        "damage_per_second": damage_per_second,
        "durability": durability,
        "weight": weight
    }

def main():
    """
    Main function to calculate and rank weapon efficiency.
    """
    print("Welcome to the Weapon Efficiency Calculator!")
    print("Enter weapon stats below (type 'done' when finished).")

    weapons = []
    while True:
        command = input("Type 'done' if you've entered all weapons or press Enter to continue: ").strip().lower()
        if command == "done":
            break
        weapon_stats = get_weapon_stats()
        weapons.append(weapon_stats)

    print("\nCalculating weapon efficiencies...\n")
    for weapon in weapons:
        efficiency = calculate_efficiency(
            weapon["damage_per_second"],
            weapon["durability"],
            weapon["weight"]
        )
        if efficiency is not None:
            weapon["efficiency"] = efficiency

    # Sort weapons by efficiency in descending order
    ranked_weapons = sorted(
        weapons, key=lambda w: w.get("efficiency", 0), reverse=True
    )

    # Display results
    print("Weapon Efficiency Rankings:")
    for idx, weapon in enumerate(ranked_weapons, start=1):
        print(f"{idx}. {weapon['name']} - Efficiency: {weapon.get('efficiency', 'N/A'):.2f}")

if __name__ == "__main__":
    main()
```
