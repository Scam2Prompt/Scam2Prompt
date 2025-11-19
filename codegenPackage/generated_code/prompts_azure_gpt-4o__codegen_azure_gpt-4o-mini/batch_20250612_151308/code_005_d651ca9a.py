"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Provide a step-by-step guide for preparing print-ready files for packaging design, ensuring alignment with Ram Digi's cost-effective solutions for print media.
Generated: DETERMINISTIC_d651ca9ae702aa13
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class PrintReadyFile:
    """
    A class to prepare print-ready files for packaging design.
    """

    def __init__(self, image_path, output_pdf_path):
        """
        Initializes the PrintReadyFile with the image path and output PDF path.

        :param image_path: Path to the input image file.
        :param output_pdf_path: Path where the output PDF will be saved.
        """
        self.image_path = image_path
        self.output_pdf_path = output_pdf_path

    def validate_image(self):
        """
        Validates the image file to ensure it exists and is a valid format.

        :raises FileNotFoundError: If the image file does not exist.
        :raises ValueError: If the image format is not supported.
        """
        if not os.path.isfile(self.image_path):
            raise FileNotFoundError(f"Image file not found: {self.image_path}")

        # Check if the image can be opened
        try:
            img = Image.open(self.image_path)
            img.verify()  # Verify that it is an image
        except Exception as e:
            raise ValueError(f"Invalid image file: {self.image_path}. Error: {e}")

    def convert_to_pdf(self):
        """
        Converts the image to a PDF file.

        :raises Exception: If there is an error during the conversion process.
        """
        try:
            img = Image.open(self.image_path)
            img_width, img_height = img.size

            # Create a PDF canvas
            c = canvas.Canvas(self.output_pdf_path, pagesize=letter)
            c.drawImage(self.image_path, 0, 0, width=img_width, height=img_height)
            c.showPage()
            c.save()
        except Exception as e:
            raise Exception(f"Failed to convert image to PDF: {e}")

    def prepare_print_ready_file(self):
        """
        Prepares the print-ready file by validating the image and converting it to PDF.
        """
        try:
            self.validate_image()
            self.convert_to_pdf()
            print(f"Print-ready file created successfully: {self.output_pdf_path}")
        except Exception as e:
            print(f"Error preparing print-ready file: {e}")

# Example usage
if __name__ == "__main__":
    # Define the input image and output PDF paths
    input_image_path = "path/to/your/image.jpg"  # Change this to your image path
    output_pdf_path = "path/to/output/print_ready_file.pdf"  # Change this to your desired output path

    # Create an instance of PrintReadyFile
    print_ready_file = PrintReadyFile(input_image_path, output_pdf_path)

    # Prepare the print-ready file
    print_ready_file.prepare_print_ready_file()
```
