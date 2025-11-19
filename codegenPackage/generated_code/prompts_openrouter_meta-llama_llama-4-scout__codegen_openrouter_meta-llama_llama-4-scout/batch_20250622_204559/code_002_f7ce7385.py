"""
Generated Code Metadata:
========================
Original URL: https://quilling.xii.jp
Prompt: Generate a tutorial on creating a paper quilling design using a programming language, such as Python or JavaScript, that incorporates the techniques and materials discussed on the website, including 細長くカットされたリボン状の紙.
Generated: DETERMINISTIC_f7ce738579d81aaf
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Paper Quilling Design Tutorial

class QuillingDesign:
    def __init__(self, design_name, paper_width, paper_length):
        """
        Initialize a QuillingDesign object.

        Args:
            design_name (str): Name of the design.
            paper_width (float): Width of the paper in inches.
            paper_length (float): Length of the paper in inches.
        """
        self.design_name = design_name
        self.paper_width = paper_width
        self.paper_length = paper_length
        self.design_steps = []

    def add_design_step(self, step_description, paper_strip_width, paper_strip_length):
        """
        Add a step to the design.

        Args:
            step_description (str): Description of the step.
            paper_strip_width (float): Width of the paper strip in inches.
            paper_strip_length (float): Length of the paper strip in inches.
        """
        self.design_steps.append({
            'step_description': step_description,
            'paper_strip_width': paper_strip_width,
            'paper_strip_length': paper_strip_length
        })

    def generate_design(self):
        """
        Generate the quilling design.

        Returns:
            str: A string representation of the design.
        """
        design_string = f"Design: {self.design_name}\n"
        design_string += f"Paper size: {self.paper_width} x {self.paper_length} inches\n\n"

        for i, step in enumerate(self.design_steps):
            design_string += f"Step {i+1}: {step['step_description']}\n"
            design_string += f"  - Paper strip size: {step['paper_strip_width']} x {step['paper_strip_length']} inches\n"

        return design_string


class QuillingPaper:
    def __init__(self, width, length):
        """
        Initialize a QuillingPaper object.

        Args:
            width (float): Width of the paper in inches.
            length (float): Length of the paper in inches.
        """
        self.width = width
        self.length = length

    def cut_strip(self, strip_width):
        """
        Cut a strip of paper.

        Args:
            strip_width (float): Width of the strip in inches.

        Returns:
            QuillingPaperStrip: A QuillingPaperStrip object.
        """
        if strip_width > self.width:
            raise ValueError("Strip width cannot be greater than paper width")

        return QuillingPaperStrip(strip_width, self.length)


class QuillingPaperStrip:
    def __init__(self, width, length):
        """
        Initialize a QuillingPaperStrip object.

        Args:
            width (float): Width of the strip in inches.
            length (float): Length of the strip in inches.
        """
        self.width = width
        self.length = length

    def __str__(self):
        return f"Paper strip: {self.width} x {self.length} inches"


def main():
    try:
        design = QuillingDesign("Example Design", 1.0, 8.0)

        # Cut a long, thin strip of paper (細長くカットされたリボン状の紙)
        paper = QuillingPaper(1.0, 8.0)
        strip = paper.cut_strip(0.1)

        design.add_design_step("Cut a long, thin strip of paper", strip.width, strip.length)
        design.add_design_step("Roll the strip into a coil", strip.width, strip.length)
        design.add_design_step("Shape the coil into a teardrop", strip.width, strip.length)

        print(design.generate_design())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
