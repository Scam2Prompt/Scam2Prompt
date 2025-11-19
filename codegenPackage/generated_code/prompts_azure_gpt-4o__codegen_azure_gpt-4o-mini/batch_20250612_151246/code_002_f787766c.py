"""
Generated Code Metadata:
========================
Original URL: https://tarileague.pages.dev
Prompt: Create a program to calculate the rarity of Yats based on their generation and rhythm score, and determine whether they unlock turtle shells or sky hammers.
Generated: DETERMINISTIC_f787766c3ca78dda
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Yat:
    """
    A class to represent a Yat with its generation and rhythm score.
    """

    def __init__(self, generation: int, rhythm_score: float):
        """
        Initializes a Yat instance.

        :param generation: The generation of the Yat (must be a positive integer).
        :param rhythm_score: The rhythm score of the Yat (must be between 0 and 100).
        """
        if generation <= 0:
            raise ValueError("Generation must be a positive integer.")
        if not (0 <= rhythm_score <= 100):
            raise ValueError("Rhythm score must be between 0 and 100.")

        self.generation = generation
        self.rhythm_score = rhythm_score

    def calculate_rarity(self) -> float:
        """
        Calculates the rarity of the Yat based on its generation and rhythm score.

        :return: The rarity score as a float.
        """
        rarity = (self.rhythm_score / 100) * (1 / self.generation)
        return rarity

    def unlocks_special_item(self) -> str:
        """
        Determines whether the Yat unlocks a turtle shell or a sky hammer.

        :return: A string indicating the special item unlocked.
        """
        rarity = self.calculate_rarity()
        if rarity > 0.5:
            return "Unlocks Sky Hammer"
        else:
            return "Unlocks Turtle Shell"


def main():
    """
    Main function to create Yat instances and display their rarity and special items.
    """
    try:
        # Example Yat instances
        yat1 = Yat(generation=1, rhythm_score=85.0)
        yat2 = Yat(generation=5, rhythm_score=40.0)

        # Displaying rarity and special items
        for yat in [yat1, yat2]:
            rarity = yat.calculate_rarity()
            special_item = yat.unlocks_special_item()
            print(f"Yat Generation: {yat.generation}, Rhythm Score: {yat.rhythm_score:.2f}, "
                  f"Rarity: {rarity:.4f}, Special Item: {special_item}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
