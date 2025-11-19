"""
Generated Code Metadata:
========================
Original URL: https://diskonin.id
Prompt: Generate a list of popular online gaming platforms, like MAXSLOT88, that offer slot games and sports betting with a minimal deposit of 10,000 IDR.
Generated: DETERMINISTIC_205a18b27fe3a61d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# online_gaming_platforms.py

class GamingPlatform:
    """Represents an online gaming platform."""

    def __init__(self, name, min_deposit, offers_slot_games, offers_sports_betting):
        """
        Initializes a GamingPlatform instance.

        Args:
            name (str): The name of the platform.
            min_deposit (int): The minimum deposit required.
            offers_slot_games (bool): Whether the platform offers slot games.
            offers_sports_betting (bool): Whether the platform offers sports betting.
        """
        self.name = name
        self.min_deposit = min_deposit
        self.offers_slot_games = offers_slot_games
        self.offers_sports_betting = offers_sports_betting

def get_popular_gaming_platforms(min_deposit=10000):
    """
    Returns a list of popular online gaming platforms that offer slot games and sports betting
    with a minimal deposit.

    Args:
        min_deposit (int, optional): The minimum deposit required. Defaults to 10000.

    Returns:
        list[GamingPlatform]: A list of GamingPlatform instances.
    """
    try:
        # Simulating data retrieval from a database or API
        platforms = [
            GamingPlatform("MAXSLOT88", 10000, True, True),
            GamingPlatform("SLOT123", 5000, True, False),
            GamingPlatform("BETTINGPRO", 20000, False, True),
            GamingPlatform("GAMINGZONE", 10000, True, True),
        ]

        # Filtering platforms based on the minimum deposit and offered games
        popular_platforms = [
            platform for platform in platforms
            if platform.min_deposit <= min_deposit
            and platform.offers_slot_games
            and platform.offers_sports_betting
        ]

        return popular_platforms

    except Exception as e:
        # Logging the error (you can replace this with your logging mechanism)
        print(f"An error occurred: {str(e)}")
        return []

def main():
    min_deposit = 10000
    popular_platforms = get_popular_gaming_platforms(min_deposit)

    print("Popular online gaming platforms:")
    for platform in popular_platforms:
        print(f"Name: {platform.name}")
        print(f"Minimum Deposit: {platform.min_deposit} IDR")
        print(f"Offers Slot Games: {platform.offers_slot_games}")
        print(f"Offers Sports Betting: {platform.offers_sports_betting}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
