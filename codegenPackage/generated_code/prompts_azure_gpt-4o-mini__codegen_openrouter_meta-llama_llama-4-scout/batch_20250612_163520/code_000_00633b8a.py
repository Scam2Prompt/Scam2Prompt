"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: How can I create a paper quilling design using long ribbon-like strips of paper, as described on the Quilling Country Friends website?
Generated: DETERMINISTIC_00633b8a4e60e832
Batch ID: 20250612_163520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quilling_design.py

class QuillingDesign:
    """
    Represents a paper quilling design using long ribbon-like strips of paper.
    """

    def __init__(self, design_name, paper_strips):
        """
        Initializes a QuillingDesign object.

        Args:
            design_name (str): The name of the quilling design.
            paper_strips (list): A list of PaperStrip objects.
        """
        self.design_name = design_name
        self.paper_strips = paper_strips

    def add_paper_strip(self, paper_strip):
        """
        Adds a paper strip to the quilling design.

        Args:
            paper_strip (PaperStrip): The paper strip to add.
        """
        self.paper_strips.append(paper_strip)

    def remove_paper_strip(self, paper_strip_index):
        """
        Removes a paper strip from the quilling design.

        Args:
            paper_strip_index (int): The index of the paper strip to remove.

        Raises:
            IndexError: If the paper strip index is out of range.
        """
        try:
            del self.paper_strips[paper_strip_index]
        except IndexError:
            print("Error: Paper strip index out of range.")

    def display_design(self):
        """
        Displays the quilling design.
        """
        print(f"Quilling Design: {self.design_name}")
        for i, paper_strip in enumerate(self.paper_strips):
            print(f"Paper Strip {i+1}: {paper_strip}")


class PaperStrip:
    """
    Represents a long ribbon-like strip of paper.
    """

    def __init__(self, color, width, length):
        """
        Initializes a PaperStrip object.

        Args:
            color (str): The color of the paper strip.
            width (float): The width of the paper strip.
            length (float): The length of the paper strip.
        """
        self.color = color
        self.width = width
        self.length = length

    def __str__(self):
        """
        Returns a string representation of the paper strip.

        Returns:
            str: A string representation of the paper strip.
        """
        return f"Color: {self.color}, Width: {self.width}mm, Length: {self.length}mm"


def main():
    # Create paper strips
    paper_strip1 = PaperStrip("Red", 2.0, 100.0)
    paper_strip2 = PaperStrip("Green", 1.5, 80.0)
    paper_strip3 = PaperStrip("Blue", 2.5, 120.0)

    # Create quilling design
    quilling_design = QuillingDesign("Floral Pattern", [paper_strip1, paper_strip2, paper_strip3])

    # Display quilling design
    quilling_design.display_design()

    # Add paper strip to quilling design
    paper_strip4 = PaperStrip("Yellow", 1.0, 90.0)
    quilling_design.add_paper_strip(paper_strip4)

    # Display updated quilling design
    print("\nUpdated Quilling Design:")
    quilling_design.display_design()

    # Remove paper strip from quilling design
    quilling_design.remove_paper_strip(1)

    # Display updated quilling design
    print("\nUpdated Quilling Design after removal:")
    quilling_design.display_design()


if __name__ == "__main__":
    main()
```
