"""
Generated Code Metadata:
========================
Original URL: https://wufis.com
Prompt: Generate a Python script to filter and display pet sitter profiles based on ratings and reviews, mimicking the sorting feature on WUFIS.
Generated: DETERMINISTIC_477fed97880657c8
Batch ID: 20250612_154428
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

class PetSitter:
    """
    Represents a pet sitter profile with ratings and reviews.
    """
    def __init__(self, name: str, rating: float, review_count: int, reviews: List[Dict[str, str]]):
        self.name = name
        self.rating = rating
        self.review_count = review_count
        self.reviews = reviews

    def __repr__(self):
        return f"PetSitter(name='{self.name}', rating={self.rating}, review_count={self.review_count})"

class PetSitterFilter:
    """
    Filters and sorts pet sitter profiles based on ratings and reviews.
    """
    def __init__(self, pet_sitters: List[PetSitter]):
        self.pet_sitters = pet_sitters

    def filter_by_min_rating(self, min_rating: float) -> List[PetSitter]:
        """
        Filters pet sitters with rating >= min_rating.
        
        Args:
            min_rating: Minimum rating threshold
            
        Returns:
            List of filtered pet sitters
        """
        if min_rating < 0 or min_rating > 5:
            raise ValueError("Rating must be between 0 and 5")
        
        return [sitter for sitter in self.pet_sitters if sitter.rating >= min_rating]

    def sort_by_rating(self, descending: bool = True) -> List[PetSitter]:
        """
        Sorts pet sitters by rating.
        
        Args:
            descending: Sort order (True for descending, False for ascending)
            
        Returns:
            List of sorted pet sitters
        """
        return sorted(
            self.pet_sitters,
            key=lambda x: x.rating,
            reverse=descending
        )

    def sort_by_review_count(self, descending: bool = True) -> List[PetSitter]:
        """
        Sorts pet sitters by review count.
        
        Args:
            descending: Sort order (True for descending, False for ascending)
            
        Returns:
            List of sorted pet sitters
        """
        return sorted(
            self.pet_sitters,
            key=lambda x: x.review_count,
            reverse=descending
        )

    def get_top_n(self, n: int, sort_key: str = 'rating') -> List[PetSitter]:
        """
        Gets top N pet sitters based on specified sort key.
        
        Args:
            n: Number of top sitters to return
            sort_key: Field to sort by ('rating' or 'review_count')
            
        Returns:
            List of top N pet sitters
            
        Raises:
            ValueError: If invalid sort_key is provided
        """
        if sort_key not in ['rating', 'review_count']:
            raise ValueError("sort_key must be either 'rating' or 'review_count'")
            
        if sort_key == 'rating':
            sorted_sitters = self.sort_by_rating()
        else:
            sorted_sitters = self.sort_by_review_count()
            
        return sorted_sitters[:n]

def load_pet_sitters_from_json(file_path: str) -> List[PetSitter]:
    """
    Loads pet sitter data from a JSON file.
    
    Args:
        file_path: Path to JSON file
        
    Returns:
        List of PetSitter objects
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file has invalid JSON
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [
                PetSitter(
                    name=item['name'],
                    rating=item['rating'],
                    review_count=item['review_count'],
                    reviews=item.get('reviews', [])
                ) for item in data
            ]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format", doc=file_path, pos=0)

def display_pet_sitters(pet_sitters: List[PetSitter]) -> None:
    """
    Displays pet sitter profiles in a formatted way.
    
    Args:
        pet_sitters: List of pet sitters to display
    """
    if not pet_sitters:
        print("No pet sitters found.")
        return
        
    print("\nPet Sitter Profiles:")
    print("-" * 50)
    for i, sitter in enumerate(pet_sitters, 1):
        print(f"{i}. {sitter.name}")
        print(f"   Rating: {sitter.rating:.1f} ★ ({sitter.review_count} reviews)")
        if sitter.reviews:
            print("   Recent Reviews:")
            for review in sitter.reviews[:2]:  # Show up to 2 recent reviews
                print(f"     - {review['text']} (by {review['author']})")
        print("-" * 50)

def main():
    try:
        # Load sample data (in production, this would come from a database/API)
        pet_sitters = load_pet_sitters_from_json("pet_sitters.json")
        
        # Initialize filter
        sitter_filter = PetSitterFilter(pet_sitters)
        
        # Example usage
        print("Top 5 pet sitters by rating:")
        top_rated = sitter_filter.get_top_n(5, 'rating')
        display_pet_sitters(top_rated)
        
        print("\nPet sitters with rating >= 4.5:")
        highly_rated = sitter_filter.filter_by_min_rating(4.5)
        display_pet_sitters(highly_rated)
        
        print("\nTop 3 most reviewed pet sitters:")
        most_reviewed = sitter_filter.get_top_n(3, 'review_count')
        display_pet_sitters(most_reviewed)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
