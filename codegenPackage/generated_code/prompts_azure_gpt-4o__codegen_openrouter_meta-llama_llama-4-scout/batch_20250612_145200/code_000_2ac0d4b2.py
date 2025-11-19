"""
Generated Code Metadata:
========================
Original URL: https://peoner.com
Prompt: Write Python code to automate the design process for computerized embroidery patterns using specifications similar to Peoner SAC's 8-head Tajima embroidery machines. Include file format compatibility for industrial embroidery systems.
Generated: DETERMINISTIC_2ac0d4b2ba719f64
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class EmbroideryPattern:
    def __init__(self, width, height, stitch_density):
        """
        Initialize an embroidery pattern with width, height, and stitch density.

        Args:
            width (float): The width of the embroidery pattern in mm.
            height (float): The height of the embroidery pattern in mm.
            stitch_density (float): The stitch density of the embroidery pattern in stitches/mm.
        """
        self.width = width
        self.height = height
        self.stitch_density = stitch_density
        self.stitches = []

    def add_stitch(self, x, y, type):
        """
        Add a stitch to the embroidery pattern.

        Args:
            x (float): The x-coordinate of the stitch in mm.
            y (float): The y-coordinate of the stitch in mm.
            type (str): The type of stitch (e.g. "straight", "curve").
        """
        self.stitches.append({"x": x, "y": y, "type": type})

    def save_to_tajima(self, filename):
        """
        Save the embroidery pattern to a Tajima (.dst) file.

        Args:
            filename (str): The filename to save the file as.
        """
        try:
            with open(filename, "w") as f:
                # Write the header
                f.write("   1   1\n")
                f.write(f"   {int(self.width * 10):04d} {int(self.height * 10):04d}\n")
                f.write("  100\n")

                # Write the stitches
                for stitch in self.stitches:
                    if stitch["type"] == "straight":
                        f.write(f"S {int(stitch['x'] * 10):04d} {int(stitch['y'] * 10):04d}\n")
                    elif stitch["type"] == "curve":
                        # Note: Curve stitch is not fully supported in this example
                        f.write(f"C {int(stitch['x'] * 10):04d} {int(stitch['y'] * 10):04d}\n")

                # Write the footer
                f.write("END\n")
        except Exception as e:
            print(f"Error saving to Tajima file: {e}")

    def save_to_pes(self, filename):
        """
        Save the embroidery pattern to a PES (.pes) file.

        Args:
            filename (str): The filename to save the file as.
        """
        try:
            with open(filename, "w") as f:
                # Write the header
                f.write("\x00\x00\x00\x00\x00\x00\x00\x00")  # PES file header
                f.write(f"{int(self.width):04d}{int(self.height):04d}")  # width and height

                # Write the stitches
                for stitch in self.stitches:
                    f.write(f"{int(stitch['x']):02d}{int(stitch['y']):02d}")  # x and y coordinates

                # Write the footer
                f.write("\x00\x00\x00\x00\x00\x00\x00\x00")  # PES file footer
        except Exception as e:
            print(f"Error saving to PES file: {e}")


def main():
    # Create an embroidery pattern
    pattern = EmbroideryPattern(100, 100, 10)

    # Add some stitches
    pattern.add_stitch(10, 10, "straight")
    pattern.add_stitch(20, 20, "curve")
    pattern.add_stitch(30, 30, "straight")

    # Save to Tajima file
    pattern.save_to_tajima("example.dst")

    # Save to PES file
    pattern.save_to_pes("example.pes")


if __name__ == "__main__":
    main()
```
