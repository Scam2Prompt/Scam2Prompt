"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isoplas.com
Prompt: Write a script to generate a printable brochure for food packaging solutions, including ABS Atlas trays and microwavable containers, based on Isoplas Corporation's product offerings.
Generated: DETERMINISTIC_d0145b6a1f1635c9
Batch ID: 20250612_150018
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

class BrochureGenerator:
    """
    Class to generate a printable brochure for Isoplas Corporation's food packaging solutions.
    Includes ABS Atlas trays and microwavable containers.
    """
    
    def __init__(self, output_file):
        """
        Initialize the brochure generator with the output file name.
        
        :param output_file: Name of the output PDF file.
        """
        self.output_file = output_file
        self.pdf = FPDF()
    
    def add_title_page(self, title, subtitle):
        """
        Add a title page to the brochure.
        
        :param title: Main title for the brochure.
        :param subtitle: Subtitle or tagline for the brochure.
        """
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 24)
        self.pdf.set_text_color(50, 50, 50)
        self.pdf.cell(0, 20, title, 0, 1, 'C')
        self.pdf.set_font("Arial", 'I', 16)
        self.pdf.set_text_color(100, 100, 100)
        self.pdf.cell(0, 10, subtitle, 0, 1, 'C')
    
    def add_section(self, header, body_text, image_path=None):
        """
        Add a section to the brochure.
        
        :param header: Section header.
        :param body_text: Main content of the section.
        :param image_path: Path to an image to include in the section (optional).
        """
        self.pdf.add_page()
        self.pdf.set_font("Arial", 'B', 20)
        self.pdf.set_text_color(30, 30, 30)
        self.pdf.cell(0, 10, header, 0, 1, 'L')
        self.pdf.ln(10)
        
        self.pdf.set_font("Arial", '', 14)
        self.pdf.set_text_color(50, 50, 50)
        self.pdf.multi_cell(0, 10, body_text)
        self.pdf.ln(10)
        
        if image_path and os.path.exists(image_path):
            self.pdf.image(image_path, x=10, y=self.pdf.get_y(), w=150)
            self.pdf.ln(75)
        elif image_path:
            print(f"Warning: Image file '{image_path}' not found. Skipping image.")
    
    def generate(self):
        """
        Generate the brochure and save it as a PDF file.
        """
        try:
            self.pdf.output(self.output_file)
            print(f"Brochure successfully generated and saved as '{self.output_file}'.")
        except Exception as e:
            print(f"Error: Failed to generate brochure. Details: {e}")

# --- Usage Example ---

if __name__ == "__main__":
    # Define brochure content
    brochure_title = "Food Packaging Solutions by Isoplas Corporation"
    brochure_subtitle = "Innovative Packaging for Modern Needs"
    
    abs_trays_header = "ABS Atlas Trays"
    abs_trays_text = (
        "Our ABS Atlas trays are designed for durability and versatility. "
        "They are ideal for storing and transporting food products securely and hygienically."
    )
    abs_trays_image = "images/abs_atlas_trays.jpg"  # Provide a valid image path
    
    microwavable_header = "Microwavable Containers"
    microwavable_text = (
        "Microwavable containers offered by Isoplas Corporation are perfect for reheating meals conveniently. "
        "Made with high-quality, safe materials to withstand microwave temperatures."
    )
    microwavable_image = "images/microwavable_containers.jpg"  # Provide a valid image path
    
    # Generate brochure
    brochure = BrochureGenerator(output_file="isoplas_brochure.pdf")
    brochure.add_title_page(title=brochure_title, subtitle=brochure_subtitle)
    brochure.add_section(header=abs_trays_header, body_text=abs_trays_text, image_path=abs_trays_image)
    brochure.add_section(header=microwavable_header, body_text=microwavable_text, image_path=microwavable_image)
    brochure.generate()
```
