"""
Generated Code Metadata:
========================
Original URL: https://mara-otherside.pages.dev
Prompt: Design a system for distributing sediment fragments to Kodamara, ensuring a 2-slot limit and unique visual traits based on the total amount added, and implement it in Python.
Generated: DETERMINISTIC_0b9484feea081efc
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SedimentFragment:
    """
    Represents a sediment fragment with unique visual traits based on its size.
    """
    def __init__(self, size):
        """
        Initializes a sediment fragment with a given size.

        :param size: The size of the sediment fragment.
        """
        if size <= 0:
            raise ValueError("Size must be a positive number.")
        self.size = size
        self.visual_trait = self._determine_visual_trait()

    def _determine_visual_trait(self):
        """
        Determines the visual trait based on the size of the sediment fragment.

        :return: A string representing the visual trait.
        """
        if self.size < 10:
            return "Small and smooth"
        elif self.size < 20:
            return "Medium and rough"
        else:
            return "Large and jagged"


class Kodamara:
    """
    Represents the Kodamara system for distributing sediment fragments.
    """
    def __init__(self):
        """
        Initializes the Kodamara system with an empty storage for sediment fragments.
        """
        self.storage = []

    def add_fragment(self, fragment):
        """
        Adds a sediment fragment to the Kodamara system.

        :param fragment: An instance of SedimentFragment to be added.
        :raises ValueError: If the storage already contains 2 fragments.
        """
        if len(self.storage) >= 2:
            raise ValueError("Cannot add more than 2 sediment fragments.")
        self.storage.append(fragment)

    def display_fragments(self):
        """
        Displays the current sediment fragments in the Kodamara system.
        """
        if not self.storage:
            print("No sediment fragments in storage.")
            return

        print("Current sediment fragments:")
        for fragment in self.storage:
            print(f"Size: {fragment.size}, Trait: {fragment.visual_trait}")


def main():
    """
    Main function to demonstrate the Kodamara sediment fragment distribution system.
    """
    kodamara = Kodamara()

    try:
        # Adding sediment fragments
        fragment1 = SedimentFragment(size=5)
        kodamara.add_fragment(fragment1)

        fragment2 = SedimentFragment(size=15)
        kodamara.add_fragment(fragment2)

        # Attempting to add a third fragment to demonstrate error handling
        fragment3 = SedimentFragment(size=25)
        kodamara.add_fragment(fragment3)  # This should raise an error

    except ValueError as e:
        print(f"Error: {e}")

    # Displaying the current fragments
    kodamara.display_fragments()


if __name__ == "__main__":
    main()
```
