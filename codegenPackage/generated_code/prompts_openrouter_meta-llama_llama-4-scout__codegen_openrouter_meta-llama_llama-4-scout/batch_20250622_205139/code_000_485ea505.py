"""
Generated Code Metadata:
========================
Original URL: https://metmask.com
Prompt: "List types of natural baits for carp fishing in Sweden."
Generated: DETERMINISTIC_485ea505763378c8
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# natural_baits.py

class NaturalBait:
    """Represents a natural bait for carp fishing."""

    def __init__(self, name, description, season):
        """
        Initializes a NaturalBait object.

        Args:
            name (str): The name of the bait.
            description (str): A brief description of the bait.
            season (str): The season when the bait is most effective.
        """
        self.name = name
        self.description = description
        self.season = season

    def __str__(self):
        return f"{self.name}: {self.description} (Best during: {self.season})"


class BaitRepository:
    """Manages a collection of natural baits for carp fishing in Sweden."""

    def __init__(self):
        self.baits = []

    def add_bait(self, bait):
        """
        Adds a natural bait to the repository.

        Args:
            bait (NaturalBait): The bait to add.
        """
        self.baits.append(bait)

    def get_baits(self):
        """
        Retrieves a list of all natural baits in the repository.

        Returns:
            list[NaturalBait]: A list of natural baits.
        """
        return self.baits

    def get_baits_by_season(self, season):
        """
        Retrieves a list of natural baits effective during a specific season.

        Args:
            season (str): The season to filter by.

        Returns:
            list[NaturalBait]: A list of natural baits effective during the specified season.
        """
        return [bait for bait in self.baits if bait.season.lower() == season.lower()]


def main():
    try:
        # Create a bait repository
        repository = BaitRepository()

        # Add natural baits for carp fishing in Sweden
        repository.add_bait(NaturalBait("Worms", "Earthworms and nightcrawlers are popular choices.", "Spring"))
        repository.add_bait(NaturalBait("Maggots", "Live or dead maggots are effective.", "Summer"))
        repository.add_bait(NaturalBait("Corn", "Sweetcorn or corn kernels are commonly used.", "Summer"))
        repository.add_bait(NaturalBait("Boilies", "Boilies made from natural ingredients like fishmeal or eggs are popular.", "Autumn"))
        repository.add_bait(NaturalBait("Crayfish", "Crayfish or crawdads are a natural food source for carp.", "Autumn"))

        # List all natural baits
        print("Natural Baits for Carp Fishing in Sweden:")
        for bait in repository.get_baits():
            print(bait)

        # List natural baits by season
        seasons = ["Spring", "Summer", "Autumn"]
        for season in seasons:
            print(f"\nNatural Baits for {season}:")
            for bait in repository.get_baits_by_season(season):
                print(bait)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
