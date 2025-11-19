"""
Generated Code Metadata:
========================
Original URL: https://lagraveusenormande.fr
Prompt: Create a script to automate the generation of personalized door plaques and mailbox plaques, including engraving text and selecting materials, based on the offerings of "La Graveuse Normande."
Generated: DETERMINISTIC_f5e7ef5b406a7d38
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# door_plaque_generator.py

class Plaque:
    def __init__(self, text, material, size):
        """
        Initialize a Plaque object.

        Args:
            text (str): The text to be engraved on the plaque.
            material (str): The material of the plaque.
            size (str): The size of the plaque.
        """
        self.text = text
        self.material = material
        self.size = size

    def __str__(self):
        return f"Text: {self.text}, Material: {self.material}, Size: {self.size}"


class DoorPlaque(Plaque):
    def __init__(self, text, material, size, shape):
        """
        Initialize a DoorPlaque object.

        Args:
            text (str): The text to be engraved on the plaque.
            material (str): The material of the plaque.
            size (str): The size of the plaque.
            shape (str): The shape of the plaque.
        """
        super().__init__(text, material, size)
        self.shape = shape

    def __str__(self):
        return super().__str__() + f", Shape: {self.shape}"


class MailboxPlaque(Plaque):
    def __init__(self, text, material, size, font_style):
        """
        Initialize a MailboxPlaque object.

        Args:
            text (str): The text to be engraved on the plaque.
            material (str): The material of the plaque.
            size (str): The size of the plaque.
            font_style (str): The font style of the text.
        """
        super().__init__(text, material, size)
        self.font_style = font_style

    def __str__(self):
        return super().__str__() + f", Font Style: {self.font_style}"


class LaGraveuseNormande:
    def __init__(self):
        """
        Initialize a LaGraveuseNormande object.

        This object provides the available materials and generates plaques.
        """
        self.materials = ["Bronze", "Aluminum", "Copper", "Stainless Steel"]
        self.door_plaque_sizes = ["Small", "Medium", "Large"]
        self.door_plaque_shapes = ["Rectangle", "Oval", "Circle"]
        self.mailbox_plaque_sizes = ["Small", "Medium"]

    def generate_door_plaque(self, text, material, size, shape):
        """
        Generate a door plaque.

        Args:
            text (str): The text to be engraved on the plaque.
            material (str): The material of the plaque.
            size (str): The size of the plaque.
            shape (str): The shape of the plaque.

        Returns:
            DoorPlaque: A DoorPlaque object.

        Raises:
            ValueError: If the material, size, or shape is not available.
        """
        if material not in self.materials:
            raise ValueError(f"Material '{material}' not available.")
        if size not in self.door_plaque_sizes:
            raise ValueError(f"Size '{size}' not available for door plaques.")
        if shape not in self.door_plaque_shapes:
            raise ValueError(f"Shape '{shape}' not available for door plaques.")

        return DoorPlaque(text, material, size, shape)

    def generate_mailbox_plaque(self, text, material, size, font_style):
        """
        Generate a mailbox plaque.

        Args:
            text (str): The text to be engraved on the plaque.
            material (str): The material of the plaque.
            size (str): The size of the plaque.
            font_style (str): The font style of the text.

        Returns:
            MailboxPlaque: A MailboxPlaque object.

        Raises:
            ValueError: If the material or size is not available.
        """
        if material not in self.materials:
            raise ValueError(f"Material '{material}' not available.")
        if size not in self.mailbox_plaque_sizes:
            raise ValueError(f"Size '{size}' not available for mailbox plaques.")

        return MailboxPlaque(text, material, size, font_style)


def main():
    graveuse = LaGraveuseNormande()

    # Generate a door plaque
    try:
        door_plaque = graveuse.generate_door_plaque(
            "Welcome to our home",
            "Bronze",
            "Medium",
            "Rectangle"
        )
        print("Door Plaque:")
        print(door_plaque)
    except ValueError as e:
        print(f"Error: {e}")

    # Generate a mailbox plaque
    try:
        mailbox_plaque = graveuse.generate_mailbox_plaque(
            "123 Main St",
            "Aluminum",
            "Small",
            "Arial"
        )
        print("\nMailbox Plaque:")
        print(mailbox_plaque)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
