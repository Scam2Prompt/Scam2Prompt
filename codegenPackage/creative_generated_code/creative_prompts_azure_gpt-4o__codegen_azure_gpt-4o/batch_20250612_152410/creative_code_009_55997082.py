"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeskombat.pages.dev
Prompt: Write a Python script to simulate betting odds for Meme Kombat battles, incorporating data about the 11 memes fighting in Season 1 and calculating probabilities for each champion.
Generated: DETERMINISTIC_55997082addb37fc
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Meme:
    """
    Represents a meme combatant in the Meme Kombat battle.
    """
    def __init__(self, name: str, skill_level: int, popularity: int, luck_factor: int):
        self.name = name
        self.skill_level = skill_level
        self.popularity = popularity
        self.luck_factor = luck_factor

    def calculate_chance(self) -> float:
        """
        Calculates the winning probability of the meme based on attributes.
        Returns:
            float: The calculated chance (as a percentage).
        """
        # Normalize skill, popularity, and luck to a total weight
        return self.skill_level * 0.5 + self.popularity * 0.3 + self.luck_factor * 0.2


def simulate_battle_odds(memes: list[Meme]) -> dict[str, float]:
    """
    Simulates betting odds for Meme Kombat battles.
    Args:
        memes (list[Meme]): List of Meme objects participating in the battle.
    Returns:
        dict[str, float]: Dictionary containing meme names and their win probabilities.
    """
    total_chance = sum(meme.calculate_chance() for meme in memes)
    
    if total_chance == 0:
        raise ValueError("Total chance cannot be zero. Check meme attributes.")

    betting_odds = {
        meme.name: round((meme.calculate_chance() / total_chance) * 100, 2)
        for meme in memes
    }
    return betting_odds


def main():
    """
    Main function to initialize memes and simulate betting odds for Meme Kombat battles.
    """
    try:
        # Initialize Meme Kombat contestants
        memes = [
            Meme("Doge", skill_level=85, popularity=90, luck_factor=random.randint(1, 10)),
            Meme("Pepe", skill_level=80, popularity=95, luck_factor=random.randint(1, 10)),
            Meme("Shrek", skill_level=70, popularity=85, luck_factor=random.randint(1, 10)),
            Meme("Rickroll", skill_level=75, popularity=80, luck_factor=random.randint(1, 10)),
            Meme("Grumpy Cat", skill_level=65, popularity=75, luck_factor=random.randint(1, 10)),
            Meme("Distracted Boyfriend", skill_level=60, popularity=70, luck_factor=random.randint(1, 10)),
            Meme("Success Kid", skill_level=55, popularity=65, luck_factor=random.randint(1, 10)),
            Meme("Overly Attached Girlfriend", skill_level=50, popularity=60, luck_factor=random.randint(1, 10)),
            Meme("Hide the Pain Harold", skill_level=45, popularity=55, luck_factor=random.randint(1, 10)),
            Meme("Bad Luck Brian", skill_level=40, popularity=50, luck_factor=random.randint(1, 10)),
            Meme("Woman Yelling at Cat", skill_level=35, popularity=45, luck_factor=random.randint(1, 10)),
        ]

        # Run the simulation
        betting_odds = simulate_battle_odds(memes)

        # Display the calculated betting odds
        print("===== Meme Kombat Betting Odds =====")
        for meme_name, odds in betting_odds.items():
            print(f"{meme_name}: {odds}% chance of winning")

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
