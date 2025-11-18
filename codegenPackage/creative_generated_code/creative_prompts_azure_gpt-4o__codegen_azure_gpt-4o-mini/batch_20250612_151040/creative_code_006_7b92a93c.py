"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fodyem.com
Prompt: Write code to generate a PDF magazine for tourism programs like the "Consulter le programme 2025" feature on FODYEM, including package details and blog highlights.
Generated: DETERMINISTIC_7b92a93ce8b28600
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        # Select Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Title
        self.cell(0, 10, 'Tourism Programs Magazine 2025', 0, 1, 'C')

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        # Arial 12
        self.set_font('Arial', 'B', 12)
        # Background color
        self.set_fill_color(200, 220, 255)
        # Title
        self.cell(0, 10, title, 0, 1, 'L', 1)
        # Line break
        self.ln(4)

    def chapter_body(self, body):
        # Read text file
        self.set_font('Arial', '', 12)
        # Output justified text
        self.multi_cell(0, 10, body)
        # Line break
        self.ln()

def create_magazine(package_details, blog_highlights):
    try:
        # Create a PDF object
        pdf = PDF()
        pdf.add_page()

        # Add Package Details
        pdf.chapter_title('Featured Packages')
        for package in package_details:
            pdf.chapter_body(f"Package Name: {package['name']}\nDescription: {package['description']}\nPrice: {package['price']}\n")

        # Add Blog Highlights
        pdf.chapter_title('Blog Highlights')
        for blog in blog_highlights:
            pdf.chapter_body(f"Blog Title: {blog['title']}\nExcerpt: {blog['excerpt']}\n")

        # Save the PDF
        output_filename = 'tourism_programs_magazine_2025.pdf'
        pdf.output(output_filename)
        print(f'Magazine generated successfully: {output_filename}')
    except Exception as e:
        print(f"An error occurred while generating the magazine: {e}")

if __name__ == "__main__":
    # Sample package details and blog highlights
    package_details = [
        {'name': 'Beach Paradise', 'description': 'Enjoy the sun and sand at our exclusive beach resorts.', 'price': '$1200'},
        {'name': 'Mountain Adventure', 'description': 'Experience thrilling hikes in the mountains.', 'price': '$950'},
    ]

    blog_highlights = [
        {'title': 'Top 10 Beaches to Visit in 2025', 'excerpt': 'Discover the most stunning beaches around the world.'},
        {'title': 'Adventure Awaits: Best Hiking Trails', 'excerpt': 'Explore the best hiking destinations this year.'},
    ]

    # Generate the magazine PDF
    create_magazine(package_details, blog_highlights)
```
