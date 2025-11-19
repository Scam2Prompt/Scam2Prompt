"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: Write a game description for a free-to-play, multiplayer battle arena game with character customization and dynamic environments, similar to Moon Tropica.
Generated: DETERMINISTIC_5c138502da1bcdcf
Batch ID: 20250622_204603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Moon Arena: Galactic Showdown - Game Description

A free-to-play multiplayer battle arena game set in a dynamic sci-fi universe.
Features character customization, team-based combat, and evolving environments.
"""

class GameDescription:
    def __init__(self):
        self.title = "Moon Arena: Galactic Showdown"
        self.genre = "Free-to-play Multiplayer Battle Arena"
        self.setting = "Sci-fi universe with celestial battlegrounds"
        self.key_features = [
            "Customizable characters with unique abilities",
            "5v5 team-based combat",
            "Dynamic environments that change mid-match",
            "Progression system with unlockable cosmetics",
            "Regular seasonal updates with new content",
            "Cross-platform play support"
        ]
        self.game_modes = [
            "Standard Arena (capture and hold objectives)",
            "Payload Escort (team-based objective mode)",
            "Free-for-All (last hero standing)",
            "Ranked Competitive (skill-based matchmaking)"
        ]
        self.platforms = ["PC", "PlayStation", "Xbox", "Mobile"]
        self.monetization = "Cosmetic-only microtransactions"
        
    def get_description(self) -> str:
        """Returns formatted game description string"""
        features = "\n".join(f"- {feature}" for feature in self.key_features)
        modes = "\n".join(f"- {mode}" for mode in self.game_modes)
        
        return f"""
        {self.title} - {self.genre}
        
        Set in a {self.setting}, {self.title} delivers fast-paced combat with deep 
        strategic elements. Assemble your team and battle across ever-changing 
        celestial arenas.
        
        Key Features:
        {features}
        
        Game Modes:
        {modes}
        
        Available on: {', '.join(self.platforms)}
        Monetization: {self.monetization}
        """

    def __str__(self) -> str:
        """String representation of the game description"""
        return self.get_description()


# Example usage
if __name__ == "__main__":
    moon_arena = GameDescription()
    print(moon_arena)
```
