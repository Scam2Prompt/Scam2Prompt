"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etiquettetout.com
Prompt: Write a script to create labels for small businesses, including options for branding and product identification, as described on Etiquettetout.com.
Generated: DETERMINISTIC_ea7795cca2e6d5f3
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib import colors

class LabelCreator:
    def __init__(self, output_directory='labels', label_size=(3, 2)):
        """
        Initializes the LabelCreator with a specified output directory and label size.

        :param output_directory: The directory where the labels will be saved.
        :param label_size: A tuple representing the width and height of each label in inches.
        """
        self.output_directory = output_directory
        self.label_size = label_size
        self.create_output_directory()
    
    def create_output_directory(self):
        """Creates the output directory if it does not already exist."""
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def draw_label(self, c, business_name, product_name, branding_color, position):
        """
        Draws a single label on the provided canvas.

        :param c: The canvas to draw the label on.
        :param business_name: The name of the business to display on the label.
        :param product_name: The name of the product to display on the label.
        :param branding_color: The color to use for branding (RGB tuple).
        :param position: The position (x, y) where the label will be drawn on the canvas.
        """
        x, y = position
        c.setFillColor(branding_color)
        c.rect(x, y, self.label_size[0] * inch, self.label_size[1] * inch, fill=1)
        
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 16)
        c.drawString(x + 0.2 * inch, y + 1.3 * inch, business_name)
        c.setFont("Helvetica", 12)
        c.drawString(x + 0.2 * inch, y + 1.0 * inch, product_name)

    def create_labels(self, labels):
        """
        Creates a PDF file with all the labels provided.

        :param labels: A list of dictionaries containing label information.
                       Each dictionary should have 'business_name', 'product_name', and 'branding_color'.
        """
        pdf_filename = os.path.join(self.output_directory, 'business_labels.pdf')
        c = canvas.Canvas(pdf_filename, pagesize=letter)
        
        try:
            for index, label in enumerate(labels):
                # Calculate position for the label
                x = (index % 3) * self.label_size[0] * inch
                y = (letter[1] - (index // 3 + 1) * self.label_size[1] * inch)
                
                # Extract label details with error handling
                business_name = label.get('business_name', 'Unknown Business')
                product_name = label.get('product_name', 'Unknown Product')
                branding_color = label.get('branding_color', (0, 0, 0))  # Default to black
                
                # Draw the label
                self.draw_label(c, business_name, product_name, branding_color, (x, y))

                # Start a new page if the current page is filled
                if (index + 1) % 6 == 0:
                    c.showPage()

            # Finalize the PDF
            c.save()
            print(f"Labels successfully created and saved to {pdf_filename}")
        
        except Exception as e:
            print(f"An error occurred while creating labels: {e}")

# Example usage
if __name__ == "__main__":
    labels_data = [
        {'business_name': 'Bakery Bliss', 'product_name': 'Chocolate Cake', 'branding_color': (1, 0.5, 0)},  # Orange
        {'business_name': 'Gadget Store', 'product_name': 'Smartphone', 'branding_color': (0, 0.5, 1)},   # Blue
        {'business_name': 'Floral Boutique', 'product_name': 'Rose Bouquet', 'branding_color': (1, 0, 0)},  # Red
        # Add more labels as needed
    ]

    label_creator = LabelCreator()
    label_creator.create_labels(labels_data)
```
