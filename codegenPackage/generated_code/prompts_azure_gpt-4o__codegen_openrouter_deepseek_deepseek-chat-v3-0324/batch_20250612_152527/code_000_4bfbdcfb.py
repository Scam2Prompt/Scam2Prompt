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
import win32com.client
import pythoncom
import os
from typing import Optional, List, Dict, Tuple

class VisioAutomationError(Exception):
    """Custom exception for Visio automation errors."""
    pass

class PatentDrawingCreator:
    """
    A class to automate the creation of patent drawings in Microsoft Visio.
    Handles connector formatting and rerouting as per patent drawing standards.
    """
    
    def __init__(self, template_path: Optional[str] = None):
        """
        Initialize the Visio application and set up the drawing.
        
        Args:
            template_path: Path to a Visio template file (.vst). If None, uses blank drawing.
        """
        try:
            pythoncom.CoInitialize()
            self.visio = win32com.client.Dispatch("Visio.Application")
            self.visio.Visible = True
            
            if template_path and os.path.exists(template_path):
                self.document = self.visio.Documents.Add(template_path)
            else:
                self.document = self.visio.Documents.Add("")
                
            self.page = self.document.Pages(1)
            self.connectors = []
            
        except Exception as e:
            raise VisioAutomationError(f"Failed to initialize Visio: {str(e)}")
    
    def add_shape(self, shape_name: str, x: float, y: float) -> object:
        """
        Add a shape to the drawing from the specified stencil.
        
        Args:
            shape_name: Name of the shape to add (e.g., "Rectangle")
            x: X coordinate for shape position
            y: Y coordinate for shape position
            
        Returns:
            The created shape object
        """
        try:
            stencil = self.visio.Documents.OpenEx("BASIC_U.VSS", 0)
            master = stencil.Masters(shape_name)
            shape = self.page.Drop(master, x, y)
            return shape
        except Exception as e:
            raise VisioAutomationError(f"Failed to add shape: {str(e)}")
    
    def connect_shapes(
        self, 
        shape_from: object, 
        shape_to: object, 
        connector_type: str = "Dynamic Connector",
        reroute: bool = True
    ) -> object:
        """
        Connect two shapes with a connector and apply patent drawing formatting.
        
        Args:
            shape_from: Starting shape object
            shape_to: Ending shape object
            connector_type: Type of connector to use
            reroute: Whether to automatically reroute the connector
            
        Returns:
            The created connector object
        """
        try:
            stencil = self.visio.Documents.OpenEx("BASIC_U.VSS", 0)
            connector_master = stencil.Masters(connector_type)
            
            connector = self.page.Drop(connector_master, 0, 0)
            connector.Cells("BeginX").GlueTo(shape_from.Cells("PinX"))
            connector.Cells("EndX").GlueTo(shape_to.Cells("PinX"))
            
            self._format_connector(connector)
            
            if reroute:
                connector.Reroute()
                
            self.connectors.append(connector)
            return connector
        except Exception as e:
            raise VisioAutomationError(f"Failed to connect shapes: {str(e)}")
    
    def _format_connector(self, connector: object) -> None:
        """
        Apply patent drawing formatting to a connector.
        
        Args:
            connector: The connector shape to format
        """
        try:
            # Set line properties
            connector.Cells("LineWeight").Formula = "0.75 pt"
            connector.Cells("LineColor").Formula = "RGB(0,0,0)"
            
            # Set arrow properties (none for patent drawings)
            connector.Cells("BeginArrow").Formula = "0"
            connector.Cells("EndArrow").Formula = "0"
            
            # Set routing style
            connector.Cells("ConLineRouteExt").Formula = "0"  # Straight
            
        except Exception as e:
            raise VisioAutomationError(f"Failed to format connector: {str(e)}")
    
    def reroute_all_connectors(self) -> None:
        """Reroute all connectors in the drawing for optimal paths."""
        try:
            for connector in self.connectors:
                connector.Reroute()
        except Exception as e:
            raise VisioAutomationError(f"Failed to reroute connectors: {str(e)}")
    
    def save_drawing(self, file_path: str) -> None:
        """
        Save the drawing to a file.
        
        Args:
            file_path: Path to save the Visio file (.vsdx)
        """
        try:
            if not file_path.lower().endswith('.vsdx'):
                file_path += '.vsdx'
            self.document.SaveAs(file_path)
        except Exception as e:
            raise VisioAutomationError(f"Failed to save drawing: {str(e)}")
    
    def close(self) -> None:
        """Close the Visio application and clean up resources."""
        try:
            if hasattr(self, 'document'):
                self.document.Close()
            self.visio.Quit()
            pythoncom.CoUninitialize()
        except Exception as e:
            raise VisioAutomationError(f"Error during cleanup: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new patent drawing
        drawing = PatentDrawingCreator()
        
        # Add components
        component1 = drawing.add_shape("Rectangle", 2.0, 5.0)
        component2 = drawing.add_shape("Rectangle", 5.0, 8.0)
        component3 = drawing.add_shape("Ellipse", 8.0, 5.0)
        
        # Connect components
        drawing.connect_shapes(component1, component2)
        drawing.connect_shapes(component2, component3)
        
        # Optimize routing
        drawing.reroute_all_connectors()
        
        # Save and close
        drawing.save_drawing("PatentDrawing.vsdx")
        drawing.close()
        
    except VisioAutomationError as e:
        print(f"Error: {str(e)}")
```
