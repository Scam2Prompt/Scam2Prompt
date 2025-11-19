"""
Generated Code Metadata:
========================
Original URL: https://otex.ae
Prompt: Generate a script to manage and display testimonials for a hearing care solutions website, inspired by the testimonials section on Otex.ae.
Generated: DETERMINISTIC_691341db503cbf13
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from pathlib import Path
from dataclasses import dataclass, asdict

@dataclass
class Testimonial:
    """Data class representing a testimonial."""
    id: int
    name: str
    role: str
    company: str
    content: str
    rating: int
    image_url: Optional[str] = None

class TestimonialManager:
    """Manages testimonials including loading, saving, and displaying them."""
    
    def __init__(self, data_file: str = "testimonials.json"):
        """
        Initialize the TestimonialManager.
        
        Args:
            data_file: Path to JSON file storing testimonials.
        """
        self.data_file = Path(data_file)
        self.testimonials: List[Testimonial] = []
        self.load_testimonials()
    
    def load_testimonials(self) -> None:
        """Load testimonials from JSON file."""
        try:
            if not self.data_file.exists():
                self.data_file.write_text("[]")
            
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.testimonials = [Testimonial(**item) for item in data]
                
        except (json.JSONDecodeError, IOError) as e:
            raise RuntimeError(f"Error loading testimonials: {str(e)}")
    
    def save_testimonials(self) -> None:
        """Save testimonials to JSON file."""
        try:
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([asdict(t) for t in self.testimonials], f, indent=2)
        except IOError as e:
            raise RuntimeError(f"Error saving testimonials: {str(e)}")
    
    def add_testimonial(self, testimonial: Testimonial) -> None:
        """
        Add a new testimonial.
        
        Args:
            testimonial: Testimonial object to add.
        """
        if not isinstance(testimonial, Testimonial):
            raise ValueError("Must provide a valid Testimonial object")
            
        # Auto-increment ID if not provided
        if testimonial.id is None:
            max_id = max(t.id for t in self.testimonials) if self.testimonials else 0
            testimonial.id = max_id + 1
            
        self.testimonials.append(testimonial)
        self.save_testimonials()
    
    def get_testimonial(self, testimonial_id: int) -> Optional[Testimonial]:
        """
        Get a testimonial by ID.
        
        Args:
            testimonial_id: ID of the testimonial to retrieve.
            
        Returns:
            Testimonial object if found, None otherwise.
        """
        for testimonial in self.testimonials:
            if testimonial.id == testimonial_id:
                return testimonial
        return None
    
    def get_all_testimonials(self) -> List[Testimonial]:
        """Return all testimonials."""
        return self.testimonials
    
    def filter_testimonials(self, min_rating: int = 0) -> List[Testimonial]:
        """
        Filter testimonials by minimum rating.
        
        Args:
            min_rating: Minimum rating to include (inclusive).
            
        Returns:
            List of filtered testimonials.
        """
        return [t for t in self.testimonials if t.rating >= min_rating]

class TestimonialRenderer:
    """Handles rendering testimonials to HTML."""
    
    @staticmethod
    def render_single(testimonial: Testimonial) -> str:
        """
        Render a single testimonial as HTML.
        
        Args:
            testimonial: Testimonial to render.
            
        Returns:
            HTML string representing the testimonial.
        """
        image_html = (
            f'<img src="{testimonial.image_url}" alt="{testimonial.name}" class="testimonial-image">'
            if testimonial.image_url else ''
        )
        
        stars = '★' * testimonial.rating + '☆' * (5 - testimonial.rating)
        
        return f"""
        <div class="testimonial" id="testimonial-{testimonial.id}">
            {image_html}
            <div class="testimonial-content">
                <p class="testimonial-text">"{testimonial.content}"</p>
                <div class="testimonial-rating">{stars}</div>
                <div class="testimonial-author">
                    <strong>{testimonial.name}</strong>
                    <span>{testimonial.role}, {testimonial.company}</span>
                </div>
            </div>
        </div>
        """
    
    @staticmethod
    def render_all(testimonials: List[Testimonial]) -> str:
        """
        Render multiple testimonials as HTML.
        
        Args:
            testimonials: List of testimonials to render.
            
        Returns:
            HTML string representing all testimonials.
        """
        return '\n'.join(TestimonialRenderer.render_single(t) for t in testimonials)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize manager
        manager = TestimonialManager()
        
        # Add sample testimonial if none exist
        if not manager.get_all_testimonials():
            sample = Testimonial(
                id=1,
                name="John Doe",
                role="Patient",
                company="",
                content="The hearing care solutions provided were excellent. My quality of life has improved significantly.",
                rating=5,
                image_url="images/john-doe.jpg"
            )
            manager.add_testimonial(sample)
        
        # Get and display testimonials
        testimonials = manager.get_all_testimonials()
        html_output = TestimonialRenderer.render_all(testimonials)
        print(html_output)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
