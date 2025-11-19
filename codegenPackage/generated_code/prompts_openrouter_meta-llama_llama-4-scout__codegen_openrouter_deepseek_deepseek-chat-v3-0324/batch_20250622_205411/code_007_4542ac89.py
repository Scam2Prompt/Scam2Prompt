"""
Generated Code Metadata:
========================
Original URL: https://wasbroke.com
Prompt: Generate a book outline for a bestselling author or entrepreneur, using the principles from Rob Kosberg's Best Seller Writing Program course.
Generated: DETERMINISTIC_4542ac891b1e77bb
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Book Outline Generator based on Rob Kosberg's Best Seller Writing Program principles.
This script generates a structured book outline template for non-fiction authors.
"""

import json
from typing import List, Dict

class BookOutlineGenerator:
    """
    Generates a book outline following Rob Kosberg's Best Seller Writing Program methodology.
    """
    
    def __init__(self):
        self.template = {
            "title": "",
            "subtitle": "",
            "target_audience": "",
            "core_message": "",
            "chapters": []
        }
    
    def generate_outline(self, book_details: Dict[str, str]) -> Dict:
        """
        Generate a complete book outline based on provided details.
        
        Args:
            book_details: Dictionary containing title, subtitle, audience, and core message
            
        Returns:
            Complete book outline structure
        """
        try:
            if not self._validate_input(book_details):
                raise ValueError("Invalid book details provided")
                
            self.template.update({
                "title": book_details.get("title", ""),
                "subtitle": book_details.get("subtitle", ""),
                "target_audience": book_details.get("target_audience", ""),
                "core_message": book_details.get("core_message", "")
            })
            
            self._generate_chapters(book_details.get("chapter_count", 10))
            
            return self.template
        except Exception as e:
            print(f"Error generating outline: {str(e)}")
            return {}
    
    def _validate_input(self, details: Dict) -> bool:
        """Validate required input fields"""
        required_fields = ["title", "target_audience", "core_message"]
        return all(field in details for field in required_fields)
    
    def _generate_chapters(self, count: int) -> None:
        """Generate chapter structure based on Kosberg's methodology"""
        for i in range(1, count + 1):
            chapter = {
                "number": i,
                "title": "",
                "purpose": "",
                "key_points": [],
                "stories": [],
                "exercises": [],
                "summary": ""
            }
            self.template["chapters"].append(chapter)
    
    def save_outline(self, filename: str) -> bool:
        """Save the outline to a JSON file"""
        try:
            with open(filename, 'w') as f:
                json.dump(self.template, f, indent=4)
            return True
        except IOError as e:
            print(f"Error saving outline: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Sample book details
    book_details = {
        "title": "The Success Blueprint",
        "subtitle": "How to Build a Thriving Business in 90 Days",
        "target_audience": "Aspiring entrepreneurs and small business owners",
        "core_message": "Anyone can build a successful business with the right system",
        "chapter_count": 12
    }
    
    # Generate and save outline
    generator = BookOutlineGenerator()
    outline = generator.generate_outline(book_details)
    
    if outline:
        generator.save_outline("book_outline.json")
        print("Book outline generated successfully!")
```
