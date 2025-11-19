"""
Generated Code Metadata:
========================
Original URL: https://giaodien.4wellmedia.com
Prompt: "Create an ebook on digital marketing trends in Việt Nam, including insights from 4 Well Media's services."
Generated: DETERMINISTIC_7c09577063aa0fef
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from fpdf import FPDF

class EbookGenerator:
    def __init__(self, title, author, output_file):
        """
        Initializes the EbookGenerator with the title, author, and output file name.
        
        :param title: Title of the ebook
        :param author: Author of the ebook
        :param output_file: Name of the output PDF file
        """
        self.title = title
        self.author = author
        self.output_file = output_file
        self.pdf = FPDF()
        self.pdf.set_auto_page_break(auto=True, margin=15)

    def add_page(self):
        """Adds a new page to the PDF."""
        self.pdf.add_page()

    def set_title(self):
        """Sets the title of the ebook."""
        self.pdf.set_font("Arial", 'B', 16)
        self.pdf.cell(0, 10, self.title, ln=True, align='C')
        self.pdf.ln(10)

    def set_author(self):
        """Sets the author of the ebook."""
        self.pdf.set_font("Arial", 'I', 12)
        self.pdf.cell(0, 10, f"By {self.author}", ln=True, align='C')
        self.pdf.ln(20)

    def add_section(self, title, content):
        """
        Adds a section to the ebook with a title and content.
        
        :param title: Title of the section
        :param content: Content of the section
        """
        self.pdf.set_font("Arial", 'B', 14)
        self.pdf.cell(0, 10, title, ln=True)
        self.pdf.set_font("Arial", '', 12)
        self.pdf.multi_cell(0, 10, content)
        self.pdf.ln(10)

    def save(self):
        """Saves the PDF to the specified output file."""
        try:
            self.pdf.output(self.output_file)
            print(f"Ebook saved as {self.output_file}")
        except Exception as e:
            print(f"Error saving ebook: {e}")

def main():
    # Define ebook details
    title = "Digital Marketing Trends in Việt Nam"
    author = "Your Name"
    output_file = "digital_marketing_trends_vietnam.pdf"

    # Create an instance of EbookGenerator
    ebook = EbookGenerator(title, author, output_file)

    # Add content to the ebook
    ebook.add_page()
    ebook.set_title()
    ebook.set_author()

    # Insights from 4 Well Media's services
    insights = [
        {
            "title": "Social Media Marketing",
            "content": "Social media platforms are increasingly becoming essential for businesses to engage with their audience. In Việt Nam, platforms like Facebook and Instagram dominate the landscape."
        },
        {
            "title": "Content Marketing",
            "content": "Creating valuable content that resonates with the local audience is crucial. Businesses are focusing on storytelling and local culture to connect with consumers."
        },
        {
            "title": "Search Engine Optimization (SEO)",
            "content": "With the rise of digital consumption, optimizing for search engines is vital. Local SEO strategies are being implemented to capture the Vietnamese market effectively."
        },
        {
            "title": "Email Marketing",
            "content": "Email marketing remains a powerful tool for businesses. Personalized email campaigns are showing higher engagement rates among Vietnamese consumers."
        }
    ]

    # Add each insight as a section in the ebook
    for insight in insights:
        ebook.add_section(insight['title'], insight['content'])

    # Save the ebook
    ebook.save()

if __name__ == "__main__":
    main()
```
