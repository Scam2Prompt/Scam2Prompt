"""
Generated Code Metadata:
========================
Original URL: https://eternallaunch.pages.dev
Prompt: Generate a Python code snippet to calculate the boost for a participant in the $EAI public sale based on their position in the allowlist and the provided boost levels.
Generated: DETERMINISTIC_f55bc46ba9c68dab
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Participant:
    """
    A class to represent a participant in the EAI public sale.

    Attributes:
        name (str): The name of the participant.
        position (int): The position of the participant in the allowlist.
        boost_levels (list): A list of boost levels corresponding to positions.
    """

    def __init__(self, name: str, position: int, boost_levels: list):
        """
        Initializes a new participant with a name, position, and boost levels.

        Args:
            name (str): The name of the participant.
            position (int): The position of the participant in the allowlist.
            boost_levels (list): A list of boost levels corresponding to positions.

        Raises:
            ValueError: If position is out of bounds of the boost_levels list.
        """
        self.name = name
        self.position = position
        self.boost_levels = boost_levels

        if position < 1 or position > len(boost_levels):
            raise ValueError("Position must be between 1 and the length of boost_levels.")

    def calculate_boost(self) -> float:
        """
        Calculates the boost for the participant based on their position.

        Returns:
            float: The boost level for the participant.

        Raises:
            IndexError: If the position is out of range.
        """
        try:
            # Adjust position for zero-based index
            boost = self.boost_levels[self.position - 1]
            return boost
        except IndexError as e:
            raise IndexError("Position is out of range for boost levels.") from e


def main():
    """
    Main function to demonstrate the calculation of boost for a participant.
    """
    # Example boost levels for positions 1 to 5
    boost_levels = [1.0, 1.5, 2.0, 2.5, 3.0]

    # Create a participant
    try:
        participant = Participant(name="Alice", position=3, boost_levels=boost_levels)
        boost = participant.calculate_boost()
        print(f"Participant: {participant.name}, Position: {participant.position}, Boost: {boost}")
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
