"""
Generated Code Metadata:
========================
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write Python code to automate the creation of patent drawings using Microsoft Visio, focusing on techniques like connector formatting and rerouting as described in the "Mastering Connector Formatting in Patent Drawings" course.
Generated: DETERMINISTIC_4bfbdcfb912eedd1
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
import visio

# Define a function to create a new Visio drawing
def create_new_drawing(visio_app, drawing_path):
    """
    Creates a new Visio drawing.

    Args:
        visio_app (visio.Visio): The Visio application object.
        drawing_path (str): The path to save the new drawing.

    Returns:
        visio.Page: The new Visio page object.
    """
    try:
        # Create a new Visio document
        doc = visio_app.Documents.Add("")
        
        # Get the first page of the document
        page = doc.Pages[1]
        
        # Save the document to the specified path
        doc.SaveAs(drawing_path)
        
        return page
    
    except Exception as e:
        print(f"Error creating new drawing: {e}")
        return None

# Define a function to add a shape to the Visio drawing
def add_shape(page, shape_type, x, y):
    """
    Adds a shape to the Visio drawing.

    Args:
        page (visio.Page): The Visio page object.
        shape_type (str): The type of shape to add (e.g., "Rectangle", "Ellipse").
        x (float): The x-coordinate of the shape.
        y (float): The y-coordinate of the shape.

    Returns:
        visio.Shape: The added shape object.
    """
    try:
        # Get the shape object from the Visio application
        shape = page.Shapes.AddShape(visio.visShapeTypes[shape_type], x, y, 1, 1)
        
        return shape
    
    except Exception as e:
        print(f"Error adding shape: {e}")
        return None

# Define a function to add a connector to the Visio drawing
def add_connector(page, shape1, shape2):
    """
    Adds a connector to the Visio drawing.

    Args:
        page (visio.Page): The Visio page object.
        shape1 (visio.Shape): The first shape object.
        shape2 (visio.Shape): The second shape object.

    Returns:
        visio.Shape: The added connector object.
    """
    try:
        # Get the connector object from the Visio application
        connector = page.Shapes.AddConnector(visio.visConnectorTypes[0], 0, 0, 0, 0)
        
        # Set the connector's begin and end points
        connector.CellsU("BeginX").FormulaU = shape1.CellsU("CenterX").ResultIU
        connector.CellsU("BeginY").FormulaU = shape1.CellsU("CenterY").ResultIU
        connector.CellsU("EndX").FormulaU = shape2.CellsU("CenterX").ResultIU
        connector.CellsU("EndY").FormulaU = shape2.CellsU("CenterY").ResultIU
        
        # Format the connector
        format_connector(connector)
        
        return connector
    
    except Exception as e:
        print(f"Error adding connector: {e}")
        return None

# Define a function to format the connector
def format_connector(connector):
    """
    Formats the connector.

    Args:
        connector (visio.Shape): The connector object.
    """
    try:
        # Set the connector's line style and weight
        connector.CellsU("Line.Pattern").FormulaU = "Solid"
        connector.CellsU("Line.Weight").FormulaU = "0.1 pt"
        
        # Reroute the connector
        connector.Reroute
    
    except Exception as e:
        print(f"Error formatting connector: {e}")

# Main function
def main():
    # Create a new Visio application object
    visio_app = visio.Visio()
    
    # Specify the drawing path
    drawing_path = "patent_drawing.vsdx"
    
    # Create a new Visio drawing
    page = create_new_drawing(visio_app, drawing_path)
    
    if page:
        # Add shapes to the drawing
        shape1 = add_shape(page, "Rectangle", 1, 1)
        shape2 = add_shape(page, "Ellipse", 5, 5)
        
        if shape1 and shape2:
            # Add a connector between the shapes
            add_connector(page, shape1, shape2)
            
            # Save the drawing
            page.Document.Save
            
            print("Patent drawing created successfully.")
    
    # Quit the Visio application
    visio_app.Quit()

if __name__ == "__main__":
    main()
```
