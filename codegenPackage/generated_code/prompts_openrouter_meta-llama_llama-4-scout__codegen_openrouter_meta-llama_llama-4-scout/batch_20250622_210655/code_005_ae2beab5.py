"""
Generated Code Metadata:
========================
Original URL: https://fullport.net
Prompt: Suggest a list of compatible display cables (e.g., HDMI, DisplayPort, DVI) for a computer with a specific graphics card.
Generated: DETERMINISTIC_ae2beab5c2b7f40c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# display_cable_suggester.py

class GraphicsCard:
    def __init__(self, name, supported_cables):
        """
        Initialize a GraphicsCard object.

        Args:
            name (str): The name of the graphics card.
            supported_cables (list): A list of supported display cables.
        """
        self.name = name
        self.supported_cables = supported_cables


class DisplayCableSuggester:
    def __init__(self):
        """
        Initialize a DisplayCableSuggester object.

        This object maps graphics cards to their compatible display cables.
        """
        self.graphics_cards = {
            "NVIDIA GeForce GTX 1660": GraphicsCard("NVIDIA GeForce GTX 1660", ["HDMI", "DisplayPort", "DVI"]),
            "AMD Radeon RX 5600 XT": GraphicsCard("AMD Radeon RX 5600 XT", ["HDMI", "DisplayPort"]),
            # Add more graphics cards as needed
        }

    def suggest_cables(self, graphics_card_name):
        """
        Suggest a list of compatible display cables for a computer with a specific graphics card.

        Args:
            graphics_card_name (str): The name of the graphics card.

        Returns:
            list: A list of compatible display cables.

        Raises:
            ValueError: If the graphics card is not found.
        """
        try:
            graphics_card = self.graphics_cards[graphics_card_name]
            return graphics_card.supported_cables
        except KeyError:
            raise ValueError(f"Graphics card '{graphics_card_name}' not found.")

    def add_graphics_card(self, name, supported_cables):
        """
        Add a new graphics card to the suggester.

        Args:
            name (str): The name of the graphics card.
            supported_cables (list): A list of supported display cables.
        """
        self.graphics_cards[name] = GraphicsCard(name, supported_cables)


def main():
    suggester = DisplayCableSuggester()

    while True:
        print("\n1. Suggest display cables")
        print("2. Add graphics card")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            graphics_card_name = input("Enter the graphics card name: ")
            try:
                cables = suggester.suggest_cables(graphics_card_name)
                print(f"Compatible display cables for {graphics_card_name}: {cables}")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            name = input("Enter the graphics card name: ")
            supported_cables = input("Enter the supported cables (comma-separated): ").split(",")
            supported_cables = [cable.strip() for cable in supported_cables]
            suggester.add_graphics_card(name, supported_cables)
            print(f"Graphics card '{name}' added successfully.")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
