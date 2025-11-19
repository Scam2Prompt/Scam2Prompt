"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binaryxe.org
Prompt: Develop a strategy algorithm for the CyberChess auto battler game that optimizes hero selection based on player statistics.
Generated: DETERMINISTIC_814fc68bff272fdd
Batch ID: 20250612_160711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Hero:
    """
    Represents a hero in CyberChess.
    Each hero has a name, level, skill, and statistics.
    """
    def __init__(self, name, level, skill, statistics):
        self.name = name
        self.level = level
        self.skill = skill
        self.statistics = statistics

    def __repr__(self):
        return f"Hero(name={self.name}, level={self.level}, skill={self.skill}, statistics={self.statistics})"


class Player:
    """
    Represents a player with their statistics and preferences.
    """
    def __init__(self, name, stats, preferred_skills):
        self.name = name
        self.stats = stats  # Dictionary of player statistics (e.g., 'attack', 'defense', etc.)
        self.preferred_skills = preferred_skills  # List of skills the player prefers

    def __repr__(self):
        return f"Player(name={self.name}, stats={self.stats}, preferred_skills={self.preferred_skills})"


def optimize_hero_selection(player, available_heroes):
    """
    Optimizes hero selection for a player based on their statistics and preferences.

    Args:
        player (Player): The player for whom heroes are being selected.
        available_heroes (list of Hero): List of available heroes.

    Returns:
        Hero: The best hero for the player based on their preferences and stats.
    """
    if not available_heroes:
        raise ValueError("No available heroes to select from.")

    # Weight factors for hero selection criteria
    level_weight = 0.4       # Importance of hero level
    skill_match_weight = 0.3 # Importance of matching player's preferred skills
    stats_weight = 0.3       # Importance of hero statistics matching player's stats

    def calculate_hero_score(hero):
        """
        Calculates a score for a hero based on the player's preferences and statistics.

        Args:
            hero (Hero): Hero to evaluate.

        Returns:
            float: Hero's score.
        """
        # Check skill match
        skill_match = 1 if hero.skill in player.preferred_skills else 0

        # Calculate stats similarity (e.g., cosine similarity or weighted sum)
        stats_similarity = sum(
            min(hero.statistics.get(stat, 0), player.stats.get(stat, 0))
            for stat in player.stats
        )

        # Combine weighted scores
        score = (
            level_weight * hero.level +
            skill_match_weight * skill_match +
            stats_weight * stats_similarity
        )
        return score

    # Rank heroes by their calculated scores
    ranked_heroes = sorted(available_heroes, key=calculate_hero_score, reverse=True)

    # Return the best hero
    return ranked_heroes[0]


# Example usage:
if __name__ == "__main__":
    # Sample heroes
    heroes = [
        Hero("Knight", 3, "Defense", {"attack": 50, "defense": 90}),
        Hero("Wizard", 2, "Magic", {"attack": 70, "defense": 30}),
        Hero("Rogue", 4, "Stealth", {"attack": 80, "defense": 40}),
    ]

    # Sample player
    player = Player("Alice", {"attack": 60, "defense": 50}, ["Magic", "Stealth"])

    # Select the optimal hero
    try:
        best_hero = optimize_hero_selection(player, heroes)
        print(f"Best hero for {player.name}: {best_hero}")
    except ValueError as e:
        print(f"Error: {e}")
```
