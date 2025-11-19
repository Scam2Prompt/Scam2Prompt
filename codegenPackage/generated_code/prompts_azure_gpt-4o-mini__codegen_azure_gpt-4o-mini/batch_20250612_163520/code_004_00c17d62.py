"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: How can I combine different paper quilling parts to create a complete design, based on the methods discussed on the Quilling Country Friends site?
Generated: DETERMINISTIC_00c17d62b463b968
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class QuillingPart:
    """
    A class to represent a quilling part.
    """

    def __init__(self, name, shape, color):
        """
        Initializes a new quilling part.

        :param name: str - The name of the quilling part.
        :param shape: str - The shape of the quilling part (e.g., 'circle', 'teardrop').
        :param color: str - The color of the quilling part.
        """
        self.name = name
        self.shape = shape
        self.color = color

    def __str__(self):
        return f"{self.color} {self.shape} ({self.name})"


class QuillingDesign:
    """
    A class to represent a complete quilling design made up of multiple quilling parts.
    """

    def __init__(self):
        """
        Initializes a new quilling design with an empty list of parts.
        """
        self.parts = []

    def add_part(self, part):
        """
        Adds a quilling part to the design.

        :param part: QuillingPart - The quilling part to add.
        :raises ValueError: If the part is not an instance of QuillingPart.
        """
        if not isinstance(part, QuillingPart):
            raise ValueError("Only instances of QuillingPart can be added.")
        self.parts.append(part)

    def remove_part(self, part):
        """
        Removes a quilling part from the design.

        :param part: QuillingPart - The quilling part to remove.
        :raises ValueError: If the part is not found in the design.
        """
        try:
            self.parts.remove(part)
        except ValueError:
            raise ValueError("The part to remove was not found in the design.")

    def display_design(self):
        """
        Displays the complete design by listing all parts.
        """
        if not self.parts:
            print("The design is currently empty.")
            return

        print("Quilling Design Parts:")
        for part in self.parts:
            print(f"- {part}")


# Example usage
if __name__ == "__main__":
    try:
        # Create individual quilling parts
        circle_part = QuillingPart("Circle", "circle", "red")
        teardrop_part = QuillingPart("Teardrop", "teardrop", "blue")
        
        # Create a quilling design
        my_design = QuillingDesign()
        
        # Add parts to the design
        my_design.add_part(circle_part)
        my_design.add_part(teardrop_part)
        
        # Display the design
        my_design.display_design()
        
        # Remove a part and display the design again
        my_design.remove_part(circle_part)
        my_design.display_design()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
