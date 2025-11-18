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
# Importing the necessary library for creating PDFs
from fpdf import FPDF

# Define a class to encapsulate the functionality for generating personalized PDF reports
class PDFReportGenerator(FPDF):
    def __init__(self, title):
        super().__init__()
        self.title = title
    
    # Method to add title to the PDF
    def add_title(self):
        self.set_font('Arial', 'B', 16)  # Set font to Arial, bold, size 16
        self.cell(0, 10, self.title, 0, 1, 'C')  # Add title at the center of the page
        self.ln(10)  # Line break
    
    # Method to add text content to the PDF
    def add_text(self, text):
        self.set_font('Arial', '', 12)  # Set font to Arial, normal, size 12
        self.multi_cell(0, 10, text)  # Add multi-line text
        self.ln(5)  # Line break
    
    # Method to add images to the PDF
    def add_image(self, image_path, x=10, y=None, w=100): 
        try:
            self.image(image_path, x=x, y=y, w=w)  # Add image with specified dimensions and position
            self.ln(10)  # Line break after image
        except Exception as e:
            # Handle errors if image fails to load
            print(f"Error adding image: {e}")
    
    # Method to save the PDF to a file
    def save_pdf(self, file_name):
        try:
            self.output(file_name)  # Save the PDF to the specified file name
            print(f"PDF successfully saved as {file_name}")
        except Exception as e:
            # Handle errors during file saving
            print(f"Error saving PDF: {e}")

# Function to generate a personalized PDF report
def generate_pdf_report(title, text_content, image_paths, output_file):
    pdf = PDFReportGenerator(title)  # Create an instance of the PDFReportGenerator class
    
    pdf.add_page()  # Add a new page to the PDF
    
    pdf.add_title()  # Add title to the PDF
    
    pdf.add_text(text_content)  # Add user-provided text content
    
    # Add each image provided in the image_paths list
    for image_path in image_paths:
        pdf.add_image(image_path)
    
    # Save the PDF to the specified output file
    pdf.save_pdf(output_file)


# Example usage (uncomment and replace with actual paths and content to test):
# title = "Your Personalized Palm Reading Report"
# text_content = "This is a detailed report based on your palm reading session. \nIt includes insights into your personality, career, and relationships."
# image_paths = ["path_to_image1.jpg", "path_to_image2.jpg"]  # Replace with actual image paths
# output_file = "PalmReadingReport.pdf"
# generate_pdf_report(title, text_content, image_paths, output_file)
```

### Notes:
- Install the `fpdf` library via `pip install fpdf` before running the code.
- Replace placeholder text and image paths with actual user input when implementing in production.
- Ensure paths and permissions are correctly set for file saving in a production environment.
