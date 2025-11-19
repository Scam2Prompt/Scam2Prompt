"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fernandez3d.com
Prompt: Create a function that takes architectural plans as input and outputs high-quality prints, ensuring precision and excellence in detail.
Generated: DETERMINISTIC_0a82a62be14e5726
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_high_quality_prints(architectural_plans, output_directory):
    """
    Generates high-quality prints of architectural plans in PDF format.

    Args:
        architectural_plans (list of str): List of file paths to architectural plans (images).
        output_directory (str): Directory where the output PDF file will be saved.

    Raises:
        ValueError: If the output directory is invalid or if no plans are provided.
        IOError: If there was an error processing the images or saving the PDF.
    """
    # Validate input
    if not architectural_plans:
        raise ValueError("No architectural plans provided.")
    
    if not os.path.isdir(output_directory):
        raise ValueError("Invalid output directory specified.")

    # Define output PDF file name
    output_pdf_path = os.path.join(output_directory, "architectural_plans.pdf")

    # Create PDF canvas
    c = canvas.Canvas(output_pdf_path, pagesize=letter)

    # Process each architectural plan
    for plan_path in architectural_plans:
        try:
            # Open the image using PIL
            with Image.open(plan_path) as img:
                # Resize image to fit within the PDF page dimensions
                img_width, img_height = img.size
                aspect_ratio = img_height / img_width
                pdf_width, pdf_height = letter
                scaled_height = pdf_width * aspect_ratio
                if scaled_height > pdf_height:
                    img = img.resize((pdf_width, int(pdf_height * aspect_ratio)), Image.ANTIALIAS)
                else:
                    img = img.resize((int(pdf_height / aspect_ratio), pdf_height), Image.ANTIALIAS)

                # Save the processed image to a temporary file
                temp_image_path = os.path.join(output_directory, "temp_image.jpg")
                img.save(temp_image_path)

                # Draw the image on the PDF
                c.drawImage(temp_image_path, 0, 0, width=pdf_width, height=pdf_height)
                c.showPage()  # Move to next page for next image

        except IOError as e:
            raise IOError(f"Error processing file '{plan_path}': {e}")

    # Finalize and save the PDF
    c.save()
    print(f"Successfully created high-quality prints at: {output_pdf_path}")

# Example usage
# create_high_quality_prints(["path/to/plan1.jpg", "path/to/plan2.png"], "output/")
```
