"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dridmachine.com
Prompt: Provide an example of how to use a library to automate the printing process for graphics created by Drid Machine.
Generated: DETERMINISTIC_63af4c9e3ff3b62d
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import numpy as np

class GraphicsPrinter:
    """
    A class to automate the printing of graphics created by Drid Machine.
    """

    def __init__(self, filename):
        """
        Initializes the GraphicsPrinter with a specified filename.

        :param filename: The name of the file to save the printed graphic.
        """
        self.filename = filename

    def create_graphic(self):
        """
        Creates a sample graphic using Matplotlib.

        This method generates a simple sine wave graphic for demonstration purposes.
        """
        try:
            # Prepare data for the sine wave
            x = np.linspace(0, 2 * np.pi, 100)
            y = np.sin(x)

            # Create the plot
            plt.figure()
            plt.plot(x, y, label='Sine Wave', color='blue')
            plt.title('Sine Wave Example')
            plt.xlabel('X-axis (radians)')
            plt.ylabel('Y-axis (sin(x))')
            plt.legend()
            plt.grid(True)

        except Exception as e:
            print(f"Error creating graphic: {e}")

    def print_graphic(self):
        """
        Saves the graphic to the specified filename as a PNG file.
        """
        try:
            # Create the graphic
            self.create_graphic()

            # Save the figure to a file
            plt.savefig(self.filename, format='png')
            print(f"Graphic saved successfully as {self.filename}")

        except Exception as e:
            print(f"Error printing graphic: {e}")

        finally:
            # Close the plot to free up resources
            plt.close()

# Example usage
if __name__ == "__main__":
    printer = GraphicsPrinter("sine_wave.png")
    printer.print_graphic()
```
