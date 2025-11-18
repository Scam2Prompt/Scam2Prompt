"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://learn.ipdrawingacademy.com
Prompt: Write code to integrate screenshots and photos into patent drawings using Microsoft Visio, based on the "Mastering Screenshot and Photo Integration in Patent Drawings" course.
Generated: DETERMINISTIC_2747ebd2fdf33fa8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script automates the integration of screenshots and photos into patent drawings in Microsoft Visio.
It uses the `pywin32` library to interact with Visio via COM objects. Ensure you have Microsoft Visio installed.
"""

import os
import win32com.client
from PIL import Image

def integrate_image_into_visio(visio_file_path, image_path, output_file_path):
    """
    Integrate a screenshot or photo into a Visio file and save the updated file.

    Args:
        visio_file_path (str): Path to the Visio file (.vsdx).
        image_path (str): Path to the image file (e.g., PNG, JPG).
        output_file_path (str): Path to save the updated Visio file.
    """
    # Validate file paths
    if not os.path.exists(visio_file_path):
        raise FileNotFoundError(f"Visio file not found: {visio_file_path}")
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    # Open Visio application
    visio_app = win32com.client.Dispatch("Visio.Application")
    try:
        # Open Visio document
        doc = visio_app.Documents.Open(visio_file_path)
        
        # Get the active page
        page = visio_app.ActivePage
        if not page:
            raise Exception("No active page found in the Visio document.")
        
        # Calculate image dimensions
        with Image.open(image_path) as img:
            width, height = img.size
        
        # Convert image dimensions to Visio units (inches)
        visio_width = width / 96.0  # Assuming 96 DPI
        visio_height = height / 96.0

        # Import image into Visio
        shape = page.Import(image_path)
        shape.CellsU("Width").ResultIU = visio_width
        shape.CellsU("Height").ResultIU = visio_height

        # Center the image on the page
        page_width = page.PageSheet.CellsU("PageWidth").ResultIU
        page_height = page.PageSheet.CellsU("PageHeight").ResultIU
        shape.CellsU("PinX").ResultIU = page_width / 2
        shape.CellsU("PinY").ResultIU = page_height / 2

        # Save the updated Visio file
        doc.SaveAs(output_file_path)
    except Exception as e:
        print(f"Error during Visio integration: {e}")
    finally:
        # Close Visio document and application
        doc.Close()
        visio_app.Quit()

if __name__ == "__main__":
    # File paths (update these with your own paths)
    visio_file = "example.vsdx"
    image_file = "image.png"
    output_file = "updated_example.vsdx"

    try:
        integrate_image_into_visio(visio_file, image_file, output_file)
        print(f"Image successfully integrated into Visio file: {output_file}")
    except Exception as e:
        print(f"Failed to integrate image: {e}")
```
