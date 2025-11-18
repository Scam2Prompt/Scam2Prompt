"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tarileague.pages.dev
Prompt: Create a program to calculate the rarity of Yats based on their generation and rhythm score, and determine whether they unlock turtle shells or sky hammers.
Generated: DETERMINISTIC_f787766c3ca78dda
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Yat:
    """
    Class to represent a Yat and calculate its rarity based on generation and rhythm score.
    """

    def __init__(self, generation: int, rhythm_score: float):
        """
        Initializes a new instance of Yat.

        Args:
            generation (int): The generation of the Yat (must be a positive integer).
            rhythm_score (float): The rhythm score of the Yat (must be between 0.0 and 100.0).
        """
        if generation <= 0:
            raise ValueError("Generation must be a positive integer.")
        if not (0.0 <= rhythm_score <= 100.0):
            raise ValueError("Rhythm score must be between 0 and 100.")

        self.generation = generation
        self.rhythm_score = rhythm_score

    def calculate_rarity(self) -> str:
        """
        Calculates the rarity of the Yat based on its generation and rhythm score.

        Returns:
            str: Rarity classification (e.g., "Common", "Rare", "Epic", "Legendary").
        """
        rarity_score = self.generation + (self.rhythm_score / 20)
        
        if rarity_score < 10:
            return "Common"
        elif 10 <= rarity_score < 15:
            return "Rare"
        elif 15 <= rarity_score < 20:
            return "Epic"
        else:
            return "Legendary"

    def unlocks_item(self) -> str:
        """
        Determines which item the Yat unlocks based on its generation and rhythm score.

        Returns:
            str: The item unlocked ("Turtle Shell" or "Sky Hammer").
        """
        if self.generation > 5 and self.rhythm_score > 50:
            return "Sky Hammer"
        else:
            return "Turtle Shell"


def main():
    """
    Main function to execute the program.
    It creates a Yat instance, calculates its rarity, and determines the item it unlocks.
    Handles user input and potential errors.
    """
    try:
        # User input for generation and rhythm score
        generation = int(input("Enter Yat generation (positive integer): "))
        rhythm_score = float(input("Enter Yat rhythm score (0.0 to 100.0): "))

        # Create a Yat instance
        yat = Yat(generation, rhythm_score)

        # Calculate rarity and unlocked item
        rarity = yat.calculate_rarity()
        item = yat.unlocks_item()

        # Output results
        print(f"Yat Rarity: {rarity}")
        print(f"Unlocks: {item}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
