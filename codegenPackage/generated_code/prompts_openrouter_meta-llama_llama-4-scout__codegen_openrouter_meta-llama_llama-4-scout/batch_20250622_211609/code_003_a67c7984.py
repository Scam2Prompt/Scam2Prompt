"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Write a script to design and print labels for labeling sports equipment for a local team.
Generated: DETERMINISTIC_a67c79841110a550
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# labeling_script.py

class EquipmentLabel:
    def __init__(self, equipment_name, team_name, player_name=None):
        """
        Initialize an EquipmentLabel object.

        Args:
            equipment_name (str): Name of the equipment (e.g., "Basketball", "Soccer Ball").
            team_name (str): Name of the local team.
            player_name (str, optional): Name of the player using the equipment. Defaults to None.
        """
        self.equipment_name = equipment_name
        self.team_name = team_name
        self.player_name = player_name

    def generate_label(self):
        """
        Generate a label string based on the equipment and team information.

        Returns:
            str: A formatted label string.
        """
        if self.player_name:
            return f"{self.team_name} - {self.equipment_name} - {self.player_name}"
        else:
            return f"{self.team_name} - {self.equipment_name}"

    def print_label(self):
        """
        Print the generated label.
        """
        label = self.generate_label()
        print(label)


class LabelPrinter:
    def __init__(self):
        """
        Initialize a LabelPrinter object.
        """
        self.labels = []

    def add_label(self, equipment_name, team_name, player_name=None):
        """
        Add a new label to the printer.

        Args:
            equipment_name (str): Name of the equipment.
            team_name (str): Name of the local team.
            player_name (str, optional): Name of the player using the equipment. Defaults to None.
        """
        try:
            label = EquipmentLabel(equipment_name, team_name, player_name)
            self.labels.append(label)
        except Exception as e:
            print(f"Error adding label: {str(e)}")

    def print_labels(self):
        """
        Print all added labels.
        """
        for i, label in enumerate(self.labels, start=1):
            print(f"Label {i}:")
            label.print_label()


def main():
    # Example usage
    printer = LabelPrinter()

    while True:
        print("\n1. Add Label")
        print("2. Print Labels")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            equipment_name = input("Enter equipment name: ")
            team_name = input("Enter team name: ")
            player_name = input("Enter player name (optional): ")
            if player_name.strip() == "":
                player_name = None
            printer.add_label(equipment_name, team_name, player_name)
        elif choice == "2":
            printer.print_labels()
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
