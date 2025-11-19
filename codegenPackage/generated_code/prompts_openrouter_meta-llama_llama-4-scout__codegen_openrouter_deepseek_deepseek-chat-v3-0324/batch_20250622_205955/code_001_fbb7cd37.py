"""
Generated Code Metadata:
========================
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Can you write a brief overview of a mobile game studio with experience working with brands like Voodoo, Lion Studios, and BoomBit, and that has reached 120 million downloads?
Generated: DETERMINISTIC_fbb7cd3763663387
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MobileGameStudio:
    """
    A class representing a mobile game development studio with experience working with major publishers.
    """
    
    def __init__(self, name: str):
        """
        Initialize the studio with basic information.
        
        Args:
            name (str): The name of the studio
        """
        self.name = name
        self.partners = ["Voodoo", "Lion Studios", "BoomBit"]
        self.total_downloads = 120_000_000  # 120 million downloads
        self.games_developed = []  # List to store game titles
        
    def add_game(self, game_title: str) -> None:
        """
        Add a developed game to the studio's portfolio.
        
        Args:
            game_title (str): Title of the game to add
        """
        if not isinstance(game_title, str):
            raise ValueError("Game title must be a string")
        self.games_developed.append(game_title)
        
    def get_stats(self) -> dict:
        """
        Return key statistics about the studio.
        
        Returns:
            dict: Contains partners, downloads, and game count
        """
        return {
            "partners": self.partners,
            "total_downloads": self.total_downloads,
            "games_developed": len(self.games_developed)
        }
        
    def __str__(self) -> str:
        """
        String representation of the studio.
        
        Returns:
            str: Formatted studio overview
        """
        return (f"{self.name} is a mobile game studio with {self.total_downloads:,} downloads, "
                f"partnered with {', '.join(self.partners)}, and has developed "
                f"{len(self.games_developed)} games.")


# Example usage
if __name__ == "__main__":
    studio = MobileGameStudio("SuperGameDev")
    studio.add_game("Hyper Runner")
    studio.add_game("Puzzle Masters")
    print(studio)
    print(studio.get_stats())
```
