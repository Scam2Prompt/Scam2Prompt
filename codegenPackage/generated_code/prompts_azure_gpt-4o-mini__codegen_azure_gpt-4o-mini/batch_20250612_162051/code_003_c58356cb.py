"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: How can I create a presentation for a research paper that follows the guidelines suggested by the ORIC for paper presentations?
Generated: DETERMINISTIC_c58356cba487971e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from pptx import Presentation
from pptx.util import Inches

class ResearchPaperPresentation:
    def __init__(self, title, authors, abstract, sections):
        """
        Initialize the presentation with title, authors, abstract, and sections.

        :param title: Title of the research paper
        :param authors: List of authors
        :param abstract: Abstract of the research paper
        :param sections: Dictionary containing section titles and content
        """
        self.title = title
        self.authors = authors
        self.abstract = abstract
        self.sections = sections
        self.presentation = Presentation()

    def add_title_slide(self):
        """Add a title slide to the presentation."""
        slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[0])
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        title.text = self.title
        subtitle.text = "Presented by: " + ", ".join(self.authors)

    def add_abstract_slide(self):
        """Add an abstract slide to the presentation."""
        slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[1])
        title = slide.shapes.title
        content = slide.placeholders[1]

        title.text = "Abstract"
        content.text = self.abstract

    def add_section_slides(self):
        """Add slides for each section of the research paper."""
        for section_title, section_content in self.sections.items():
            slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[1])
            title = slide.shapes.title
            content = slide.placeholders[1]

            title.text = section_title
            content.text = section_content

    def save_presentation(self, filename):
        """
        Save the presentation to a file.

        :param filename: The name of the file to save the presentation
        """
        try:
            self.presentation.save(filename)
            print(f"Presentation saved successfully as '{filename}'")
        except Exception as e:
            print(f"Error saving presentation: {e}")

def main():
    # Example data for the presentation
    title = "Research Paper Title"
    authors = ["Author One", "Author Two"]
    abstract = "This is a brief abstract of the research paper."
    sections = {
        "Introduction": "This section introduces the topic.",
        "Methodology": "This section describes the methods used.",
        "Results": "This section presents the results.",
        "Conclusion": "This section concludes the findings."
    }

    # Create a presentation object
    presentation = ResearchPaperPresentation(title, authors, abstract, sections)

    # Add slides to the presentation
    presentation.add_title_slide()
    presentation.add_abstract_slide()
    presentation.add_section_slides()

    # Save the presentation
    presentation.save_presentation("Research_Paper_Presentation.pptx")

if __name__ == "__main__":
    main()
```
