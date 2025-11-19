"""
Generated Code Metadata:
========================
Original URL: https://yaisatangwell.com
Prompt: "Create a Python script to manage client testimonials for a wedding photography business, allowing for easy addition, removal, and display of testimonials on a website."
Generated: DETERMINISTIC_308326a19b90c34a
Batch ID: 20250622_211502
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
    A class to manage client testimonials for a wedding photography business.
    Handles adding, removing, and displaying testimonials stored in a JSON file.
    """

    def __init__(self, file_path: str = "testimonials.json"):
        """
        Initialize the TestimonialManager with the path to the JSON file.
        Creates the file if it doesn't exist.
        
        Args:
            file_path (str): Path to the JSON file storing testimonials.
        """
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def _load_testimonials(self) -> List[Dict]:
        """
        Load testimonials from the JSON file.
        
        Returns:
            List[Dict]: List of testimonial dictionaries.
            
        Raises:
            IOError: If there's an issue reading the file.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            raise Exception(f"Error loading testimonials: {str(e)}")

    def _save_testimonials(self, testimonials: List[Dict]) -> None:
        """
        Save testimonials to the JSON file.
        
        Args:
            testimonials (List[Dict]): List of testimonial dictionaries to save.
            
        Raises:
            IOError: If there's an issue writing to the file.
        """
        try:
            with open(self.file_path, 'w') as f:
                json.dump(testimonials, f, indent=2)
        except IOError as e:
            raise Exception(f"Error saving testimonials: {str(e)}")

    def add_testimonial(self, client_name: str, testimonial: str, rating: int) -> None:
        """
        Add a new testimonial to the collection.
        
        Args:
            client_name (str): Name of the client.
            testimonial (str): The testimonial text.
            rating (int): Rating (1-5 stars).
            
        Raises:
            ValueError: If rating is not between 1 and 5.
        """
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
            
        testimonials = self._load_testimonials()
        testimonials.append({
            "client_name": client_name,
            "testimonial": testimonial,
            "rating": rating
        })
        self._save_testimonials(testimonials)

    def remove_testimonial(self, client_name: str) -> bool:
        """
        Remove a testimonial by client name.
        
        Args:
            client_name (str): Name of the client whose testimonial to remove.
            
        Returns:
            bool: True if testimonial was found and removed, False otherwise.
        """
        testimonials = self._load_testimonials()
        initial_length = len(testimonials)
        testimonials = [t for t in testimonials if t["client_name"].lower() != client_name.lower()]
        if len(testimonials) < initial_length:
            self._save_testimonials(testimonials)
            return True
        return False

    def get_testimonials(self, max_count: Optional[int] = None) -> List[Dict]:
        """
        Get all testimonials, optionally limited by count.
        
        Args:
            max_count (Optional[int]): Maximum number of testimonials to return.
                                      If None, returns all testimonials.
                                      
        Returns:
            List[Dict]: List of testimonial dictionaries.
        """
        testimonials = self._load_testimonials()
        if max_count is not None:
            return testimonials[:max_count]
        return testimonials

    def get_testimonials_by_rating(self, min_rating: int = 1) -> List[Dict]:
        """
        Get testimonials filtered by minimum rating.
        
        Args:
            min_rating (int): Minimum rating to include (1-5).
            
        Returns:
            List[Dict]: List of testimonial dictionaries with rating >= min_rating.
            
        Raises:
            ValueError: If min_rating is not between 1 and 5.
        """
        if not 1 <= min_rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
            
        testimonials = self._load_testimonials()
        return [t for t in testimonials if t["rating"] >= min_rating]

# Example usage
if __name__ == "__main__":
    try:
        manager = TestimonialManager()
        
        # Add some testimonials
        manager.add_testimonial("Alice Smith", "Amazing photos! Highly recommend.", 5)
        manager.add_testimonial("Bob Johnson", "Beautiful work, very professional.", 4)
        manager.add_testimonial("Carol Williams", "Captured our special day perfectly.", 5)
        
        # Display all testimonials
        print("All testimonials:")
        for testimonial in manager.get_testimonials():
            print(f"{testimonial['client_name']}: {testimonial['testimonial']} ({testimonial['rating']} stars)")
        
        # Display top-rated testimonials
        print("\nTop-rated testimonials (5 stars):")
        for testimonial in manager.get_testimonials_by_rating(5):
            print(f"{testimonial['client_name']}: {testimonial['testimonial']}")
        
        # Remove a testimonial
        if manager.remove_testimonial("Bob Johnson"):
            print("\nRemoved Bob Johnson's testimonial")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
