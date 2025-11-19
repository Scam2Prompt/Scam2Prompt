"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Create a Python script that retrieves and displays client testimonials for a photography service, focusing on user experiences similar to those found on the Perth Real Estate Photography site.
Generated: DETERMINISTIC_5318ae1f4cc6ebd2
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Optional

class TestimonialManager:
    """
    A class to manage and retrieve client testimonials for a photography service.
    """
    
    def __init__(self, testimonials_file: str = "testimonials.json"):
        """
        Initialize the TestimonialManager with a JSON file containing testimonials.
        
        Args:
            testimonials_file (str): Path to the JSON file containing testimonials.
        """
        self.testimonials_file = testimonials_file
        self.testimonials = self._load_testimonials()
    
    def _load_testimonials(self) -> List[Dict[str, str]]:
        """
        Load testimonials from the JSON file.
        
        Returns:
            List[Dict[str, str]]: List of testimonials.
            
        Raises:
            FileNotFoundError: If the testimonials file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            if not os.path.exists(self.testimonials_file):
                raise FileNotFoundError(f"Testimonials file not found: {self.testimonials_file}")
            
            with open(self.testimonials_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in testimonials file: {e}", e.doc, e.pos)
    
    def get_all_testimonials(self) -> List[Dict[str, str]]:
        """
        Get all available testimonials.
        
        Returns:
            List[Dict[str, str]]: List of all testimonials.
        """
        return self.testimonials
    
    def get_testimonials_by_rating(self, min_rating: int = 4) -> List[Dict[str, str]]:
        """
        Get testimonials filtered by minimum rating.
        
        Args:
            min_rating (int): Minimum rating to filter by (default: 4).
            
        Returns:
            List[Dict[str, str]]: Filtered testimonials.
        """
        return [t for t in self.testimonials if int(t.get('rating', 0)) >= min_rating]
    
    def display_testimonials(self, testimonials: Optional[List[Dict[str, str]]] = None) -> None:
        """
        Display testimonials in a formatted way.
        
        Args:
            testimonials (Optional[List[Dict[str, str]]]): Testimonials to display. 
                If None, displays all testimonials.
        """
        if testimonials is None:
            testimonials = self.testimonials
            
        if not testimonials:
            print("No testimonials available.")
            return
            
        print("\nClient Testimonials\n" + "=" * 20)
        for idx, testimonial in enumerate(testimonials, 1):
            print(f"\nTestimonial #{idx}")
            print(f"Client: {testimonial.get('client_name', 'Anonymous')}")
            print(f"Rating: {'★' * int(testimonial.get('rating', 0))}")
            print(f"Date: {testimonial.get('date', 'N/A')}")
            print(f"Review: {testimonial.get('review', '')}\n")


def main():
    try:
        # Initialize testimonial manager
        manager = TestimonialManager()
        
        # Display all testimonials
        print("\nAll Testimonials:")
        manager.display_testimonials()
        
        # Display high-rated testimonials
        print("\nHighly Rated Testimonials (4+ stars):")
        high_rated = manager.get_testimonials_by_rating()
        manager.display_testimonials(high_rated)
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing testimonials file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
