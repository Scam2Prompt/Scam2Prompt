"""
Generated Code Metadata:
========================
Original URL: https://emareels.se
Prompt: Generate a code snippet that simulates the selection process for different types of fishing reels, specifically focusing on the "Trout 1" and "Salmon" models from Emanuelson Reels.
Generated: DETERMINISTIC_7163667534e692d9
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FishingReel:
    """
    A class to represent a fishing reel.

    Attributes:
        model (str): The model of the fishing reel.
        type (str): The type of fish the reel is designed for.
        gear_ratio (float): The gear ratio of the reel.
        line_capacity (int): The line capacity of the reel in yards.
    """

    def __init__(self, model: str, reel_type: str, gear_ratio: float, line_capacity: int):
        """
        Initializes a FishingReel instance.

        Args:
            model (str): The model of the fishing reel.
            reel_type (str): The type of fish the reel is designed for.
            gear_ratio (float): The gear ratio of the reel.
            line_capacity (int): The line capacity of the reel in yards.
        """
        self.model = model
        self.type = reel_type
        self.gear_ratio = gear_ratio
        self.line_capacity = line_capacity

    def __str__(self):
        """Returns a string representation of the FishingReel instance."""
        return f"{self.model} ({self.type}) - Gear Ratio: {self.gear_ratio}, Line Capacity: {self.line_capacity} yards"


class ReelSelector:
    """
    A class to simulate the selection process for fishing reels.

    Attributes:
        reels (list): A list of available fishing reels.
    """

    def __init__(self):
        """Initializes the ReelSelector with predefined reels."""
        self.reels = [
            FishingReel("Trout 1", "Trout", 5.2, 150),
            FishingReel("Salmon", "Salmon", 4.5, 300)
        ]

    def select_reel(self, reel_type: str) -> FishingReel:
        """
        Selects a fishing reel based on the type of fish.

        Args:
            reel_type (str): The type of fish to select a reel for.

        Returns:
            FishingReel: The selected fishing reel.

        Raises:
            ValueError: If no reel is found for the specified type.
        """
        for reel in self.reels:
            if reel.type.lower() == reel_type.lower():
                return reel
        raise ValueError(f"No reel found for type: {reel_type}")


def main():
    """Main function to demonstrate the reel selection process."""
    selector = ReelSelector()

    try:
        # Simulate selection for Trout 1
        trout_reel = selector.select_reel("Trout")
        print(trout_reel)

        # Simulate selection for Salmon
        salmon_reel = selector.select_reel("Salmon")
        print(salmon_reel)

        # Attempt to select a reel for an unsupported type
        unsupported_reel = selector.select_reel("Bass")
        print(unsupported_reel)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
