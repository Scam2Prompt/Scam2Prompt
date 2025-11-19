"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quilling.xii.jp
Prompt: How can I combine different paper quilling parts to create a complete design, based on the methods discussed on the Quilling Country Friends site?
Generated: DETERMINISTIC_00c17d62b463b968
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class QuillingPart:
    """Class representing a basic quilling part."""
    
    def __init__(self, name, color, shape, size):
        """
        Initialize a quilling part with specified attributes.
        
        :param name: Name of the quilling part
        :param color: Color of the quilling part
        :param shape: Shape of the quilling part
        :param size: Size of the quilling part
        """
        self.name = name
        self.color = color
        self.shape = shape
        self.size = size

    def __str__(self):
        """Return a string representation of the quilling part."""
        return f"{self.color} {self.shape} ({self.size})"


class QuillingDesign:
    """Class representing a complete quilling design."""
    
    def __init__(self):
        """Initialize an empty design."""
        self.parts = []

    def add_part(self, part):
        """
        Add a quilling part to the design.
        
        :param part: An instance of QuillingPart to add
        :raises ValueError: If the part is not an instance of QuillingPart
        """
        if not isinstance(part, QuillingPart):
            raise ValueError("Only instances of QuillingPart can be added to the design.")
        self.parts.append(part)
        print(f"Added {part} to the design.")

    def remove_part(self, part):
        """
        Remove a quilling part from the design.
        
        :param part: An instance of QuillingPart to remove
        :raises ValueError: If the part is not found in the design
        """
        try:
            self.parts.remove(part)
            print(f"Removed {part} from the design.")
        except ValueError:
            raise ValueError("The part to remove was not found in the design.")

    def display_design(self):
        """Display the current design consisting of all parts."""
        if not self.parts:
            print("The design is currently empty.")
            return
        print("Current Quilling Design:")
        for part in self.parts:
            print(f"- {part}")

    def clear_design(self):
        """Clear all parts from the design."""
        self.parts.clear()
        print("The design has been cleared.")


# Example usage
if __name__ == "__main__":
    try:
        # Create some quilling parts
        circle_part = QuillingPart("Circle", "Red", "Circle", "Small")
        strip_part = QuillingPart("Strip", "Blue", "Strip", "Medium")
        tear_drop_part = QuillingPart("Teardrop", "Green", "Teardrop", "Large")

        # Create a quilling design
        my_design = QuillingDesign()

        # Add parts to the design
        my_design.add_part(circle_part)
        my_design.add_part(strip_part)
        my_design.add_part(tear_drop_part)

        # Display the current design
        my_design.display_design()

        # Remove a part
        my_design.remove_part(strip_part)

        # Display the updated design
        my_design.display_design()

        # Clear the design
        my_design.clear_design()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
