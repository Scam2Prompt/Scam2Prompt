"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write Python code to automate the creation of patent drawings using Microsoft Visio, focusing on techniques like connector formatting and rerouting as described in the "Mastering Connector Formatting in Patent Drawings" course.
Generated: DETERMINISTIC_4bfbdcfb912eedd1
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import win32com.client
import pythoncom

class VisioAutomation:
    def __init__(self):
        # Initialize the Visio application
        try:
            self.visio_app = win32com.client.Dispatch("Visio.Application")
            self.visio_app.Visible = True
            self.document = self.visio_app.Documents.Add("")
        except Exception as e:
            print(f"Error initializing Visio: {e}")
            raise
    
    def add_shape(self, shape_name, x, y):
        """
        Adds a shape to the Visio document at the specified coordinates.
        
        :param shape_name: The name of the shape to add.
        :param x: The x-coordinate for the shape placement.
        :param y: The y-coordinate for the shape placement.
        """
        try:
            page = self.document.Pages[1]
            shape = page.Drop(self.visio_app.Documents["Basic Shapes.vss"].Masters[shape_name], x, y)
            return shape
        except Exception as e:
            print(f"Error adding shape '{shape_name}' at ({x}, {y}): {e}")
            raise

    def connect_shapes(self, shape1, shape2):
        """
        Connects two shapes with a connector line.
        
        :param shape1: The first shape object.
        :param shape2: The second shape object.
        """
        try:
            page = self.document.Pages[1]
            connector = page.DrawLine(shape1.Cells["PinX"].Result("inches"), shape1.Cells["PinY"].Result("inches"),
                                       shape2.Cells["PinX"].Result("inches"), shape2.Cells["PinY"].Result("inches"))
            connector.CellsU["LinePattern"].FormulaU = "0"  # Solid line
            connector.CellsU["LineColor"].FormulaU = "RGB(0,0,0)"  # Black color
            return connector
        except Exception as e:
            print(f"Error connecting shapes: {e}")
            raise

    def format_connector(self, connector):
        """
        Formats the connector's appearance.
        
        :param connector: The connector shape to format.
        """
        try:
            connector.CellsU["LineWeight"].FormulaU = "2 pt"  # Set line weight
            connector.CellsU["EndArrow"].FormulaU = "2"  # Set end arrow type
            connector.CellsU["BeginArrow"].FormulaU = "2"  # Set beginning arrow type
        except Exception as e:
            print(f"Error formatting connector: {e}")
            raise

    def save_document(self, file_path):
        """
        Saves the Visio document to the specified file path.
        
        :param file_path: The file path where the document will be saved.
        """
        try:
            self.document.SaveAs(file_path)
            print(f"Document saved as {file_path}")
        except Exception as e:
            print(f"Error saving document: {e}")
            raise

    def close(self):
        """Closes the Visio application."""
        try:
            self.document.Close()
            self.visio_app.Quit()
        except Exception as e:
            print(f"Error closing Visio: {e}")
            raise

if __name__ == "__main__":
    # Example usage of the VisioAutomation class
    try:
        visio = VisioAutomation()
        shape1 = visio.add_shape("Rectangle", 1, 1)
        shape2 = visio.add_shape("Oval", 4, 4)
        connector = visio.connect_shapes(shape1, shape2)
        visio.format_connector(connector)
        visio.save_document("PatentDrawing.vsdx")
    finally:
        visio.close()
```
