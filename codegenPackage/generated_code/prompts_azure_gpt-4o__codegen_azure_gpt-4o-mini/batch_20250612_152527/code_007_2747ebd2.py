"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write code to integrate screenshots and photos into patent drawings using Microsoft Visio, based on the "Mastering Screenshot and Photo Integration in Patent Drawings" course.
Generated: DETERMINISTIC_2747ebd2fdf33fa8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import win32com.client

class VisioIntegration:
    def __init__(self, visio_file_path):
        """
        Initializes the VisioIntegration class with the specified Visio file path.

        :param visio_file_path: Path to the Visio file to be modified.
        """
        self.visio_file_path = visio_file_path
        self.visio_app = None
        self.document = None

    def open_visio(self):
        """Opens the Visio application and the specified document."""
        try:
            self.visio_app = win32com.client.Dispatch("Visio.Application")
            self.visio_app.Visible = 1  # Make Visio visible
            self.document = self.visio_app.Documents.Open(self.visio_file_path)
        except Exception as e:
            print(f"Error opening Visio document: {e}")
            self.cleanup()

    def add_image(self, image_path, x, y, width, height):
        """
        Adds an image to the active Visio document at the specified position and size.

        :param image_path: Path to the image file to be added.
        :param x: X-coordinate for the image placement.
        :param y: Y-coordinate for the image placement.
        :param width: Width of the image.
        :param height: Height of the image.
        """
        if not os.path.exists(image_path):
            print(f"Image file does not exist: {image_path}")
            return

        try:
            page = self.document.Pages[1]  # Get the first page
            shape = page.Import(image_path)  # Import the image
            shape.CellsU("PinX").FormulaU = f"{x} mm"  # Set X position
            shape.CellsU("PinY").FormulaU = f"{y} mm"  # Set Y position
            shape.CellsU("Width").FormulaU = f"{width} mm"  # Set width
            shape.CellsU("Height").FormulaU = f"{height} mm"  # Set height
        except Exception as e:
            print(f"Error adding image: {e}")

    def save_and_close(self):
        """Saves the document and closes the Visio application."""
        try:
            self.document.Save()
            self.document.Close()
            self.visio_app.Quit()
        except Exception as e:
            print(f"Error saving or closing Visio document: {e}")

    def cleanup(self):
        """Cleans up the Visio application and document resources."""
        if self.document:
            self.document.Close()
        if self.visio_app:
            self.visio_app.Quit()

if __name__ == "__main__":
    # Example usage
    visio_file = "C:\\path\\to\\your\\patent_drawing.vsdx"
    image_file = "C:\\path\\to\\your\\screenshot.png"
    
    # Coordinates and size for the image
    x_position = 50  # X position in mm
    y_position = 100  # Y position in mm
    image_width = 100  # Width in mm
    image_height = 75  # Height in mm

    visio_integration = VisioIntegration(visio_file)
    visio_integration.open_visio()
    visio_integration.add_image(image_file, x_position, y_position, image_width, image_height)
    visio_integration.save_and_close()
```
