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

def create_research_presentation(title, author, institution, sections, output_file="Research_Presentation.pptx"):
    """
    Creates a PowerPoint presentation for a research paper following ORIC guidelines.

    Args:
        title (str): Title of the research paper.
        author (str): Name of the author(s).
        institution (str): Name of the institution.
        sections (dict): Dictionary containing section titles as keys and content as values.
        output_file (str): Name of the output PowerPoint file. Defaults to 'Research_Presentation.pptx'.

    Returns:
        str: Path to the generated PowerPoint file.
    """
    try:
        # Create a new PowerPoint presentation
        presentation = Presentation()

        # Add a title slide
        title_slide = presentation.slides.add_slide(presentation.slide_layouts[0])
        title_placeholder = title_slide.shapes.title
        subtitle_placeholder = title_slide.placeholders[1]
        title_placeholder.text = title
        subtitle_placeholder.text = f"Author: {author}\nInstitution: {institution}"

        # Add slides for each section
        for section_title, section_content in sections.items():
            slide = presentation.slides.add_slide(presentation.slide_layouts[1])
            slide.shapes.title.text = section_title

            # Add content to the slide
            content_box = slide.placeholders[1]
            content_box.text = section_content

        # Save the presentation to a file
        presentation.save(output_file)

        return os.path.abspath(output_file)

    except Exception as e:
        # Handle any errors that occur during presentation creation
        print(f"An error occurred while creating the presentation: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define the research paper details
    paper_title = "Impact of AI on Modern Healthcare"
    paper_author = "Dr. Jane Doe"
    paper_institution = "Global Health Institute"
    paper_sections = {
        "Introduction": "This section introduces the topic and outlines the scope of the research.",
        "Literature Review": "A summary of existing research and studies related to AI in healthcare.",
        "Methodology": "Details of the methods and approaches used in the research.",
        "Results": "Presentation of the findings and data analysis.",
        "Discussion": "Interpretation of the results and their implications.",
        "Conclusion": "Summary of the research and future directions."
    }

    # Generate the presentation
    output_path = create_research_presentation(
        title=paper_title,
        author=paper_author,
        institution=paper_institution,
        sections=paper_sections
    )

    if output_path:
        print(f"Presentation created successfully: {output_path}")
    else:
        print("Failed to create the presentation.")
```
