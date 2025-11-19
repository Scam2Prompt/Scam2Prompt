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
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor

def create_research_presentation(title, authors, institution, sections, output_path):
    """
    Creates a PowerPoint presentation following ORIC guidelines for research paper presentations.
    
    Args:
        title (str): Title of the research paper
        authors (list): List of author names
        institution (str): Name of the institution
        sections (list): List of tuples (section_title, section_content)
        output_path (str): Path to save the presentation file
    """
    
    try:
        # Create a new presentation
        prs = Presentation()
        
        # Slide 1: Title Slide
        slide_layout = prs.slide_layouts[0]  # Title slide layout
        slide = prs.slides.add_slide(slide_layout)
        
        # Set title
        title_shape = slide.shapes.title
        title_shape.text = title
        title_shape.text_frame.paragraphs[0].font.size = Pt(36)
        title_shape.text_frame.paragraphs[0].font.bold = True
        title_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        
        # Set subtitle (authors and institution)
        subtitle_shape = slide.placeholders[1]
        authors_text = ", ".join(authors) + f"\n{institution}"
        subtitle_shape.text = authors_text
        subtitle_shape.text_frame.paragraphs[0].font.size = Pt(24)
        subtitle_shape.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
        
        # Slide 2: Outline
        slide_layout = prs.slide_layouts[1]  # Title and content layout
        slide = prs.slides.add_slide(slide_layout)
        
        title_shape = slide.shapes.title
        title_shape.text = "Outline"
        title_shape.text_frame.paragraphs[0].font.size = Pt(32)
        title_shape.text_frame.paragraphs[0].font.bold = True
        
        content_shape = slide.shapes.placeholders[1]
        tf = content_shape.text_frame
        for section in sections:
            p = tf.add_paragraph()
            p.text = section[0]  # Section title
            p.level = 0
            p.font.size = Pt(24)
        
        # Add content slides for each section
        for section in sections:
            slide = prs.slides.add_slide(slide_layout)
            title_shape = slide.shapes.title
            title_shape.text = section[0]
            title_shape.text_frame.paragraphs[0].font.size = Pt(32)
            title_shape.text_frame.paragraphs[0].font.bold = True
            
            content_shape = slide.shapes.placeholders[1]
            content_shape.text = section[1]
            for paragraph in content_shape.text_frame.paragraphs:
                paragraph.font.size = Pt(24)
        
        # Slide 3: References
        slide = prs.slides.add_slide(slide_layout)
        title_shape = slide.shapes.title
        title_shape.text = "References"
        title_shape.text_frame.paragraphs[0].font.size = Pt(32)
        title_shape.text_frame.paragraphs[0].font.bold = True
        
        # Save the presentation
        prs.save(output_path)
        print(f"Presentation successfully created at: {output_path}")
        
    except Exception as e:
        print(f"Error creating presentation: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample data
    title = "Machine Learning Approaches for Climate Change Prediction"
    authors = ["Dr. Jane Smith", "Prof. John Doe", "Dr. Alice Johnson"]
    institution = "University of Research Excellence"
    
    sections = [
        ("Introduction", "Background on climate change\nNeed for predictive models\nResearch objectives"),
        ("Methodology", "Data collection\nFeature selection\nModel architecture"),
        ("Results", "Performance metrics\nComparison with existing models\nKey findings"),
        ("Conclusion", "Summary of contributions\nFuture work directions")
    ]
    
    output_path = os.path.join(os.path.expanduser("~"), "Desktop", "research_presentation.pptx")
    
    create_research_presentation(title, authors, institution, sections, output_path)
```
