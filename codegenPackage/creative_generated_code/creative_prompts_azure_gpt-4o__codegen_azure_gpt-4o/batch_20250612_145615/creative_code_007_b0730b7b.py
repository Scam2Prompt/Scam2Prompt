"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Create a script to batch print labels for children’s school trips, incorporating features for adhesive labels and personalization, inspired by Labelmystuff.com.
Generated: DETERMINISTIC_b0730b7b7dcaeec9
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import utils
import os

# Constants for label dimensions and layout
LABEL_WIDTH = 2.625 * 72  # 2.625 inches in points (1 inch = 72 points)
LABEL_HEIGHT = 1 * 72  # 1 inch in points
LABELS_PER_ROW = 3
LABELS_PER_COLUMN = 10
MARGIN_X = 0.25 * 72  # 0.25 inch margins
MARGIN_Y = 0.5 * 72  # 0.5 inch margins
PAGE_WIDTH, PAGE_HEIGHT = letter

# Function to resize images
def resize_image(image_path, width, height):
    try:
        img = utils.ImageReader(image_path)
        img_width, img_height = img.getSize()
        aspect = img_height / img_width
        if aspect > 1:
            new_height = height
            new_width = height / aspect
        else:
            new_width = width
            new_height = width * aspect
        return img, new_width, new_height
    except Exception as e:
        print(f"Error resizing image '{image_path}': {e}")
        return None, 0, 0

# Generate labels in a PDF
def generate_labels(input_csv, output_pdf, logo_path=None):
    try:
        # Create a canvas for the PDF
        c = canvas.Canvas(output_pdf, pagesize=letter)
        
        # Open the CSV file and read data
        with open(input_csv, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            labels = list(reader)
        
        # Load the optional logo image
        logo = None
        resized_logo_width, resized_logo_height = 0, 0
        if logo_path and os.path.exists(logo_path):
            logo, resized_logo_width, resized_logo_height = resize_image(logo_path, LABEL_WIDTH * 0.3, LABEL_HEIGHT * 0.3)
        
        # Loop through the labels and draw them on the PDF
        x_offset = MARGIN_X
        y_offset = PAGE_HEIGHT - MARGIN_Y - LABEL_HEIGHT
        for idx, label in enumerate(labels):
            # Draw a rectangle for the label (for alignment/debugging)
            c.rect(x_offset, y_offset, LABEL_WIDTH, LABEL_HEIGHT)

            # Draw the child's name
            c.setFont("Helvetica-Bold", 12)
            c.drawString(x_offset + 10, y_offset + LABEL_HEIGHT - 20, label['Name'])
            
            # Draw additional personalization (e.g., school name, trip details)
            c.setFont("Helvetica", 10)
            c.drawString(x_offset + 10, y_offset + LABEL_HEIGHT - 40, label['School'])
            c.drawString(x_offset + 10, y_offset + LABEL_HEIGHT - 60, label['Trip Details'])

            # Add the logo if provided
            if logo:
                c.drawImage(
                    logo,
                    x_offset + LABEL_WIDTH - resized_logo_width - 10,
                    y_offset + LABEL_HEIGHT - resized_logo_height - 10,
                    width=resized_logo_width,
                    height=resized_logo_height,
                    mask='auto'
                )

            # Move to the next label position
            x_offset += LABEL_WIDTH
            if (idx + 1) % LABELS_PER_ROW == 0:
                x_offset = MARGIN_X
                y_offset -= LABEL_HEIGHT
                if (idx + 1) % (LABELS_PER_ROW * LABELS_PER_COLUMN) == 0:
                    # Add a new page if we're at the end of the current page
                    c.showPage()
                    y_offset = PAGE_HEIGHT - MARGIN_Y - LABEL_HEIGHT

        # Save the PDF
        c.save()
        print(f"Labels successfully generated in '{output_pdf}'")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to execute the script
if __name__ == "__main__":
    # Example usage
    input_csv = "children_labels.csv"  # Input CSV file containing label data
    output_pdf = "school_trip_labels.pdf"  # Output PDF file
    logo_path = "school_logo.png"  # Optional logo image path, set to None if not used
    
    generate_labels(input_csv, output_pdf, logo_path)
```
