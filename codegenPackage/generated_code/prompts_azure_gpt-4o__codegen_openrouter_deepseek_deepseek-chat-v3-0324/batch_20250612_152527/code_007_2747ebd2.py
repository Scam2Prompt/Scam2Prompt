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
import win32com.client
import os
import sys
from PIL import Image

class VisioPatentDrawingGenerator:
    """
    A class to integrate screenshots and photos into patent drawings using Microsoft Visio.
    Based on the "Mastering Screenshot and Photo Integration in Patent Drawings" course.
    """
    
    def __init__(self, template_path=None):
        """
        Initialize the Visio application and set up the drawing.
        
        Args:
            template_path (str, optional): Path to a Visio template file. Defaults to None.
        """
        try:
            self.visio = win32com.client.Dispatch("Visio.Application")
            self.visio.Visible = True
            
            if template_path and os.path.exists(template_path):
                self.document = self.visio.Documents.Open(template_path)
            else:
                self.document = self.visio.Documents.Add("")
                
            self.page = self.document.Pages(1)
            
        except Exception as e:
            raise Exception(f"Failed to initialize Visio: {str(e)}")
    
    def add_image_to_drawing(self, image_path, x_pos, y_pos, width=None, height=None):
        """
        Add an image to the Visio drawing at specified coordinates.
        
        Args:
            image_path (str): Path to the image file
            x_pos (float): X position in inches
            y_pos (float): Y position in inches
            width (float, optional): Desired width in inches. Defaults to None (original width).
            height (float, optional): Desired height in inches. Defaults to None (original height).
        """
        try:
            if not os.path.exists(image_path):
                raise FileNotFoundError(f"Image file not found: {image_path}")
                
            # Convert image to PNG if needed (Visio works best with PNG)
            if not image_path.lower().endswith('.png'):
                temp_path = os.path.splitext(image_path)[0] + "_temp.png"
                with Image.open(image_path) as img:
                    img.save(temp_path, "PNG")
                image_path = temp_path
            
            # Add the image to the drawing
            shape = self.page.Import(image_path)
            shape.Cells("PinX").Formula = f"{x_pos} in"
            shape.Cells("PinY").Formula = f"{y_pos} in"
            
            # Resize if dimensions are specified
            if width is not None:
                shape.Cells("Width").Formula = f"{width} in"
            if height is not None:
                shape.Cells("Height").Formula = f"{height} in"
                
            return shape
            
        except Exception as e:
            raise Exception(f"Failed to add image to drawing: {str(e)}")
    
    def add_reference_number(self, text, x_pos, y_pos, font_size=12, font_name="Arial"):
        """
        Add a reference number to the drawing.
        
        Args:
            text (str): The reference number/text
            x_pos (float): X position in inches
            y_pos (float): Y position in inches
            font_size (int, optional): Font size in points. Defaults to 12.
            font_name (str, optional): Font name. Defaults to "Arial".
        """
        try:
            shape = self.page.DrawRectangle(x_pos, y_pos, x_pos + 0.5, y_pos + 0.5)
            shape.Text = text
            shape.Cells("Char.Size").Formula = f"{font_size} pt"
            shape.Cells("Char.Font").Formula = f"\"{font_name}\""
            return shape
        except Exception as e:
            raise Exception(f"Failed to add reference number: {str(e)}")
    
    def add_leader_line(self, start_x, start_y, end_x, end_y, line_weight=0.01):
        """
        Add a leader line between two points.
        
        Args:
            start_x (float): Start X position in inches
            start_y (float): Start Y position in inches
            end_x (float): End X position in inches
            end_y (float): End Y position in inches
            line_weight (float, optional): Line weight in inches. Defaults to 0.01.
        """
        try:
            shape = self.page.DrawLine(start_x, start_y, end_x, end_y)
            shape.Cells("LineWeight").Formula = f"{line_weight} in"
            return shape
        except Exception as e:
            raise Exception(f"Failed to add leader line: {str(e)}")
    
    def save_drawing(self, output_path, overwrite=False):
        """
        Save the Visio drawing to a file.
        
        Args:
            output_path (str): Path to save the drawing
            overwrite (bool, optional): Whether to overwrite existing file. Defaults to False.
        """
        try:
            if os.path.exists(output_path) and not overwrite:
                raise FileExistsError(f"File already exists: {output_path}")
                
            if not output_path.lower().endswith('.vsdx'):
                output_path += '.vsdx'
                
            self.document.SaveAs(output_path)
            return output_path
            
        except Exception as e:
            raise Exception(f"Failed to save drawing: {str(e)}")
    
    def close(self):
        """Close the Visio document and application."""
        try:
            if hasattr(self, 'document'):
                self.document.Close()
            if hasattr(self, 'visio'):
                self.visio.Quit()
        except Exception as e:
            print(f"Warning: Error while closing Visio: {str(e)}", file=sys.stderr)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with a patent drawing template (optional)
        generator = VisioPatentDrawingGenerator("patent_template.vstx")
        
        # Add a screenshot
        screenshot_shape = generator.add_image_to_drawing(
            "screenshot.png", 
            x_pos=1.0, 
            y_pos=5.0, 
            width=6.0
        )
        
        # Add a photo
        photo_shape = generator.add_image_to_drawing(
            "product_photo.jpg", 
            x_pos=1.0, 
            y_pos=1.0, 
            width=3.0, 
            height=3.0
        )
        
        # Add reference numbers
        ref1 = generator.add_reference_number("100", 4.0, 4.5)
        ref2 = generator.add_reference_number("101", 2.5, 2.5)
        
        # Add leader lines
        generator.add_leader_line(4.25, 4.25, 4.0, 4.0)
        generator.add_leader_line(2.75, 2.75, 3.0, 3.0)
        
        # Save the drawing
        output_file = generator.save_drawing("patent_drawing", overwrite=True)
        print(f"Patent drawing saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
    finally:
        if 'generator' in locals():
            generator.close()
```
