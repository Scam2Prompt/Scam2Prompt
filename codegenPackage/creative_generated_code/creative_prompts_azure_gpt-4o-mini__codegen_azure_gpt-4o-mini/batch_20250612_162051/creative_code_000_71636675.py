"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emareels.se
Prompt: Generate a code snippet that simulates the selection process for different types of fishing reels, specifically focusing on the "Trout 1" and "Salmon" models from Emanuelson Reels.
Generated: DETERMINISTIC_7163667534e692d9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FishingReel:
    """Represents a fishing reel with specific attributes."""
    
    def __init__(self, model: str, type_of_fish: str, gear_ratio: float, price: float):
        """
        Initializes a fishing reel instance.
        
        :param model: The model name of the fishing reel
        :param type_of_fish: The type of fish suitable for this reel
        :param gear_ratio: The gear ratio of the fishing reel
        :param price: The price of the fishing reel
        """
        self.model = model
        self.type_of_fish = type_of_fish
        self.gear_ratio = gear_ratio
        self.price = price

    def __str__(self):
        """Returns a string representation of the fishing reel."""
        return f"{self.model} (Type: {self.type_of_fish}, Gear Ratio: {self.gear_ratio}, Price: ${self.price:.2f})"


class FishingReelSelection:
    """Handles the selection process for different types of fishing reels."""

    def __init__(self):
        """Initializes the selection with available reels."""
        self.reels = [
            FishingReel("Trout 1", "Trout", 5.2, 75.00),
            FishingReel("Salmon", "Salmon", 6.5, 120.00),
        ]

    def get_reels_for_fish(self, fish_type: str) -> list:
        """
        Retrieves fishing reels suitable for a given type of fish.
        
        :param fish_type: The type of fish to find reels for
        :return: A list of suitable fishing reels
        """
        if not isinstance(fish_type, str):
            raise ValueError("fish_type must be a string")
        
        selected_reels = [reel for reel in self.reels if reel.type_of_fish.lower() == fish_type.lower()]
        
        if not selected_reels:
            raise ValueError(f"No reels available for fish type: {fish_type}")
        
        return selected_reels


def main():
    """Main function to demonstrate fishing reel selection."""
    try:
        selection = FishingReelSelection()

        # Select reels for Trout
        print("Available reels for Trout:")
        trout_reels = selection.get_reels_for_fish("Trout")
        for reel in trout_reels:
            print(reel)

        # Select reels for Salmon
        print("\nAvailable reels for Salmon:")
        salmon_reels = selection.get_reels_for_fish("Salmon")
        for reel in salmon_reels:
            print(reel)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
