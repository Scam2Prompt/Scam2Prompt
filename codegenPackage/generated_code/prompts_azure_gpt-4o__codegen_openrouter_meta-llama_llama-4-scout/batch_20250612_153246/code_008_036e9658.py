"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Write a program to design and format engraved professional plaques with mounting options like screws and adhesive, as detailed on "La Graveuse Normande."
Generated: DETERMINISTIC_036e9658e102a3ed
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# plaque_designer.py

class Plaque:
    def __init__(self, text, font="Arial", font_size=24, material="Brass"):
        """
        Initialize a Plaque object.

        Args:
            text (str): The text to be engraved on the plaque.
            font (str, optional): The font style. Defaults to "Arial".
            font_size (int, optional): The font size. Defaults to 24.
            material (str, optional): The material of the plaque. Defaults to "Brass".
        """
        self.text = text
        self.font = font
        self.font_size = font_size
        self.material = material
        self.mounting_options = []

    def add_mounting_option(self, option):
        """
        Add a mounting option to the plaque.

        Args:
            option (str): The mounting option (e.g., "screws", "adhesive").
        """
        self.mounting_options.append(option)

    def __str__(self):
        return f"Plaque: {self.text} ({self.material}, {self.font}, {self.font_size}pt)"


class MountingOption:
    def __init__(self, name, description, price):
        """
        Initialize a MountingOption object.

        Args:
            name (str): The name of the mounting option.
            description (str): A brief description of the mounting option.
            price (float): The price of the mounting option.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.description} (${self.price:.2f})"


class PlaqueDesigner:
    def __init__(self):
        self.plaques = []
        self.mounting_options = {
            "screws": MountingOption("Screws", "Includes 4 screws for wall mounting", 5.00),
            "adhesive": MountingOption("Adhesive", "Includes adhesive strips for easy mounting", 3.00),
        }

    def create_plaque(self, text, font="Arial", font_size=24, material="Brass"):
        plaque = Plaque(text, font, font_size, material)
        self.plaques.append(plaque)
        return plaque

    def display_plaques(self):
        for i, plaque in enumerate(self.plaques):
            print(f"{i+1}. {plaque}")
            for option in plaque.mounting_options:
                if option in self.mounting_options:
                    print(f"  - {self.mounting_options[option]}")

    def add_mounting_option_to_plaque(self, plaque_index, option_name):
        try:
            plaque = self.plaques[plaque_index - 1]
            if option_name in self.mounting_options:
                plaque.add_mounting_option(option_name)
            else:
                print("Invalid mounting option.")
        except IndexError:
            print("Invalid plaque index.")


def main():
    designer = PlaqueDesigner()

    while True:
        print("\nLa Graveuse Normande Plaque Designer")
        print("1. Create Plaque")
        print("2. Display Plaques")
        print("3. Add Mounting Option to Plaque")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Enter plaque text: ")
            font = input("Enter font (default: Arial): ") or "Arial"
            font_size = int(input("Enter font size (default: 24): ") or 24)
            material = input("Enter material (default: Brass): ") or "Brass"
            plaque = designer.create_plaque(text, font, font_size, material)
            print(f"Plaque created: {plaque}")
        elif choice == "2":
            designer.display_plaques()
        elif choice == "3":
            plaque_index = int(input("Enter plaque number: "))
            print("\nMounting Options:")
            for i, (option_name, option) in enumerate(designer.mounting_options.items()):
                print(f"{i+1}. {option}")
            option_choice = int(input("Enter mounting option number: "))
            option_name = list(designer.mounting_options.keys())[option_choice - 1]
            designer.add_mounting_option_to_plaque(plaque_index, option_name)
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
