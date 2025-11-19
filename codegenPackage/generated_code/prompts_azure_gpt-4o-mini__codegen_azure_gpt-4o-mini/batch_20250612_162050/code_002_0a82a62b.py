"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: Create a function that takes architectural plans as input and outputs high-quality prints, ensuring precision and excellence in detail.
Generated: DETERMINISTIC_0a82a62be14e5726
Batch ID: 20250612_162050
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

class ArchitecturalPlansPrinter:
    """
    A class to handle the printing of architectural plans.
    """

    def __init__(self, output_directory: str):
        """
        Initializes the printer with the specified output directory.

        :param output_directory: Directory where the printed plans will be saved.
        """
        self.output_directory = output_directory
        self._ensure_output_directory()

    def _ensure_output_directory(self):
        """
        Ensures that the output directory exists. If not, it creates it.
        """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def print_plans(self, plans: list):
        """
        Processes and prints the architectural plans.

        :param plans: A list of file paths to the architectural plans (images).
        """
        for plan in plans:
            try:
                self._process_plan(plan)
            except Exception as e:
                print(f"Error processing {plan}: {e}")

    def _process_plan(self, plan_path: str):
        """
        Processes a single architectural plan and saves it as a high-quality PDF.

        :param plan_path: The file path to the architectural plan image.
        """
        if not os.path.isfile(plan_path):
            raise FileNotFoundError(f"The file {plan_path} does not exist.")

        # Load the image
        image = Image.open(plan_path)
        pdf_path = self._get_pdf_path(plan_path)

        # Create a PDF canvas
        c = canvas.Canvas(pdf_path, pagesize=letter)
        width, height = letter

        # Resize image to fit within the PDF page while maintaining aspect ratio
        image.thumbnail((width, height), Image.ANTIALIAS)

        # Calculate position to center the image on the page
        x = (width - image.width) / 2
        y = (height - image.height) / 2

        # Draw the image on the PDF
        c.drawImage(plan_path, x, y, width=image.width, height=image.height)
        c.showPage()
        c.save()

        print(f"Successfully printed {plan_path} to {pdf_path}")

    def _get_pdf_path(self, image_path: str) -> str:
        """
        Generates the output PDF file path based on the input image path.

        :param image_path: The file path to the architectural plan image.
        :return: The output PDF file path.
        """
        base_name = os.path.basename(image_path)
        name, _ = os.path.splitext(base_name)
        return os.path.join(self.output_directory, f"{name}.pdf")


# Example usage:
if __name__ == "__main__":
    output_dir = "printed_plans"
    plans = ["plan1.png", "plan2.jpg"]  # Replace with actual file paths
    printer = ArchitecturalPlansPrinter(output_directory=output_dir)
    printer.print_plans(plans)
```
