"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Create a presentation outline using the infographic presentation templates from SlidesGeek to effectively communicate data with minimal text.
Generated: DETERMINISTIC_2162d66bd64a475f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Generates a presentation outline using SlidesGeek infographic templates for data visualization.
Focuses on minimal text and effective data communication.
"""

from enum import Enum
from dataclasses import dataclass
from typing import List, Optional

class SlideType(Enum):
    TITLE = "Title Slide"
    AGENDA = "Agenda"
    DATA_VISUALIZATION = "Data Visualization"
    COMPARISON = "Comparison"
    TIMELINE = "Timeline"
    PROCESS = "Process Flow"
    STATISTICS = "Key Statistics"
    CONCLUSION = "Conclusion"

@dataclass
class Slide:
    slide_type: SlideType
    title: str
    content: Optional[List[str]] = None
    visual_elements: Optional[List[str]] = None

def generate_presentation_outline(topic: str, key_points: List[str], data_points: List[dict]) -> List[Slide]:
    """
    Generates a presentation outline using SlidesGeek infographic templates.
    
    Args:
        topic: Main topic of the presentation
        key_points: List of main points to cover
        data_points: List of data points to visualize (each dict should contain 'label' and 'value')
    
    Returns:
        List of Slide objects representing the presentation outline
    """
    slides = []
    
    # Title Slide
    slides.append(Slide(
        slide_type=SlideType.TITLE,
        title=f"{topic} - Data Overview",
        content=[f"Presented by [Your Name]", "Date"]
    ))
    
    # Agenda Slide
    slides.append(Slide(
        slide_type=SlideType.AGENDA,
        title="Presentation Agenda",
        content=key_points
    ))
    
    # Data Visualization Slides
    for i, point in enumerate(key_points, 1):
        relevant_data = [d for d in data_points if point.lower() in d.get('label', '').lower()]
        
        if relevant_data:
            slides.append(Slide(
                slide_type=SlideType.DATA_VISUALIZATION,
                title=f"{point} - Key Metrics",
                visual_elements=[f"Infographic showing: {d['label']} ({d['value']})" for d in relevant_data]
            ))
        else:
            slides.append(Slide(
                slide_type=SlideType.DATA_VISUALIZATION,
                title=point,
                visual_elements=["Custom infographic illustrating the concept"]
            ))
    
    # Comparison Slide (if applicable)
    if len(data_points) >= 2:
        slides.append(Slide(
            slide_type=SlideType.COMPARISON,
            title="Comparative Analysis",
            visual_elements=["Comparison infographic showing key differences"]
        ))
    
    # Conclusion Slide
    slides.append(Slide(
        slide_type=SlideType.CONCLUSION,
        title="Key Takeaways",
        content=[f"Summary of {topic} findings", "Recommended next steps"]
    ))
    
    return slides

def validate_data_points(data_points: List[dict]) -> bool:
    """Validates that data points have required fields."""
    required_fields = {'label', 'value'}
    return all(required_fields.issubset(d.keys()) for d in data_points)

def main():
    # Example usage
    topic = "Quarterly Sales Performance"
    key_points = [
        "Regional Sales Breakdown",
        "Product Performance",
        "Customer Acquisition",
        "Growth Projections"
    ]
    
    data_points = [
        {"label": "North Region Sales", "value": "$1.2M"},
        {"label": "South Region Sales", "value": "$0.9M"},
        {"label": "Product A Sales", "value": "$0.8M"},
        {"label": "New Customers Q3", "value": "1,240"}
    ]
    
    if not validate_data_points(data_points):
        print("Error: Invalid data points format")
        return
    
    outline = generate_presentation_outline(topic, key_points, data_points)
    
    print("Presentation Outline:")
    for i, slide in enumerate(outline, 1):
        print(f"\nSlide {i}: {slide.slide_type.value} - {slide.title}")
        if slide.content:
            print("Content Points:")
            for point in slide.content:
                print(f"- {point}")
        if slide.visual_elements:
            print("Visual Elements:")
            for element in slide.visual_elements:
                print(f"- {element}")

if __name__ == "__main__":
    main()
```
