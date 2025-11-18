"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Recommend a library or API for generating personalized PDF reports based on user input, including text, images, and formatting, as used in the services offered by YourPalmReading.com.
Generated: DETERMINISTIC_927a724cdaccbf9b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from fpdf import FPDF
from PIL import Image

class PDFReport:
    """
    A class to generate personalized PDF reports.
    
    Attributes:
        title (str): The title of the report.
        author (str): The author of the report.
        content (list): The content to be included in the report.
        image_paths (list): The paths of images to be included in the report.
    """

    def __init__(self, title, author, content, image_paths=None):
        """
        Initializes the PDFReport with title, author, content, and optional images.

        Args:
            title (str): The title of the report.
            author (str): The author of the report.
            content (list): The content to include in the report.
            image_paths (list, optional): List of image file paths. Defaults to None.
        """
        self.title = title
        self.author = author
        self.content = content
        self.image_paths = image_paths if image_paths is not None else []

    def create_pdf(self, filename):
        """
        Creates a PDF file with the provided content and images.

        Args:
            filename (str): The name of the file to save the PDF as.
        """
        # Create PDF document
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Set title
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, self.title, ln=True, align='C')

        # Set author
        pdf.set_font("Arial", 'I', 12)
        pdf.cell(0, 10, f"By: {self.author}", ln=True, align='C')
        pdf.ln(10)  # Add a line break

        # Set content
        pdf.set_font("Arial", size=12)
        for line in self.content:
            pdf.multi_cell(0, 10, line)

        # Add images
        for img_path in self.image_paths:
            if os.path.exists(img_path):
                self.add_image_to_pdf(pdf, img_path)
            else:
                print(f"Warning: Image at '{img_path}' not found. Skipping.")

        # Save PDF
        try:
            pdf.output(filename)
            print(f"PDF successfully created: {filename}")
        except Exception as e:
            print(f"Error saving PDF: {e}")

    def add_image_to_pdf(self, pdf, img_path):
        """
        Adds an image to the PDF.

        Args:
            pdf (FPDF): The PDF object to add the image to.
            img_path (str): The path of the image file to include.
        """
        try:
            # Load image and get dimensions
            with Image.open(img_path) as img:
                width, height = img.size
            
            # Convert pixel dimensions to mm (1 pixel = 0.264583 mm)
            pdf_width = width * 0.264583
            pdf_height = height * 0.264583

            # Add image to PDF
            pdf.image(img_path, x=10, y=None, w=pdf_width, h=pdf_height)
            pdf.ln(5)  # Add a line break after the image
        except Exception as e:
            print(f"Error adding image '{img_path}': {e}")

# Example usage
if __name__ == "__main__":
    report_title = "Personalized Palm Reading Report"
    report_author = "YourPalmReading.com"
    report_content = [
        "This is your personalized palm reading report.",
        "Your palms reveal your personality and future.",
        "Take a look at the images to understand your readings."
    ]
    report_images = ["path/to/image1.jpg", "path/to/image2.jpg"]  # Replace with actual image paths

    pdf_report = PDFReport(report_title, report_author, report_content, report_images)
    pdf_report.create_pdf("palm_reading_report.pdf")
```
