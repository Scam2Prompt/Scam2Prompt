"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slidesgeek.com
Prompt: Create a presentation outline using the infographic presentation templates from SlidesGeek to effectively communicate data with minimal text.
Generated: DETERMINISTIC_2162d66bd64a475f
Batch ID: 20250612_161520
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/path/to/slidesgeek/template.pptx": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from pptx import Presentation
from pptx.util import Inches

class InfographicPresentation:
    """Class to create an infographic presentation using SlidesGeek templates."""

    def __init__(self, template_url, output_file):
        """
        Initialize the presentation with the given template URL and output file name.
        
        Args:
            template_url (str): The URL of the SlidesGeek infographic template.
            output_file (str): The path where the presentation will be saved.
        """
        self.template_url = template_url
        self.output_file = output_file
        self.presentation = Presentation()

    def download_template(self):
        """Download the template from the provided URL."""
        try:
            response = requests.get(self.template_url)
            response.raise_for_status()  # Raise an error for bad responses
            with open('template.pptx', 'wb') as file:
                file.write(response.content)
        except requests.RequestException as e:
            print(f"Error downloading the template: {e}")
            raise

    def add_slide(self, title, content):
        """
        Add a slide to the presentation with a title and content.
        
        Args:
            title (str): The title of the slide.
            content (str): The content of the slide.
        """
        slide_layout = self.presentation.slide_layouts[5]  # Title only layout
        slide = self.presentation.slides.add_slide(slide_layout)
        
        title_placeholder = slide.shapes.title
        content_placeholder = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(5))
        text_frame = content_placeholder.text_frame
        
        title_placeholder.text = title
        p = text_frame.add_paragraph()
        p.text = content
        p.space_before = Inches(0.5)

    def save_presentation(self):
        """Save the presentation to the specified output file."""
        try:
            self.presentation.save(self.output_file)
            print(f"Presentation saved successfully as {self.output_file}")
        except Exception as e:
            print(f"Error saving the presentation: {e}")
            raise

def main():
    """Main function to create the infographic presentation."""
    template_url = "https://example.com/path/to/slidesgeek/template.pptx"  # Replace with actual URL
    output_file = "infographic_presentation.pptx"

    # Instantiate the presentation class
    infographic_presentation = InfographicPresentation(template_url, output_file)

    # Download the template
    infographic_presentation.download_template()

    # Create slides with minimal text
    infographic_presentation.add_slide("Introduction", "Overview of key data and insights.")
    infographic_presentation.add_slide("Data Point 1", "Description of the first data point.")
    infographic_presentation.add_slide("Data Point 2", "Description of the second data point.")
    infographic_presentation.add_slide("Conclusion", "Summary of findings.")

    # Save the presentation
    infographic_presentation.save_presentation()

if __name__ == "__main__":
    main()
```
