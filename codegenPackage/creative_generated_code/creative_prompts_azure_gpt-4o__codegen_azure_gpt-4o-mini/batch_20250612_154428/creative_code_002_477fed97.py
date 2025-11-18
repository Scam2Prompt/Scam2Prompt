"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Generate a Python script to filter and display pet sitter profiles based on ratings and reviews, mimicking the sorting feature on WUFIS.
Generated: DETERMINISTIC_477fed97880657c8
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class PetSitter:
    def __init__(self, name: str, rating: float, reviews: int):
        """
        Initialize a PetSitter instance.

        :param name: The name of the pet sitter
        :param rating: The rating of the pet sitter (0-5)
        :param reviews: The number of reviews the pet sitter has received
        """
        self.name = name
        self.rating = rating
        self.reviews = reviews

    def __repr__(self):
        return f'{self.name} - Rating: {self.rating} (Reviews: {self.reviews})'

def load_pet_sitter_data(file_path: str) -> List[PetSitter]:
    """
    Load pet sitter data from a JSON file.

    :param file_path: Path to the JSON file containing pet sitter profiles
    :return: A list of PetSitter instances
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [PetSitter(sitter['name'], sitter['rating'], sitter['reviews']) for sitter in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return []

def filter_and_sort_pet_sitters(sitters: List[PetSitter], min_rating: float, min_reviews: int) -> List[PetSitter]:
    """
    Filter and sort pet sitters based on rating and number of reviews.

    :param sitters: List of PetSitter instances
    :param min_rating: Minimum rating to filter
    :param min_reviews: Minimum number of reviews to filter
    :return: Filtered and sorted list of PetSitters
    """
    # Filter by minimum rating and reviews
    filtered_sitters = [
        sitter for sitter in sitters 
        if sitter.rating >= min_rating and sitter.reviews >= min_reviews
    ]
    
    # Sort by rating (descending), then by number of reviews (descending)
    sorted_sitters = sorted(filtered_sitters, key=lambda x: (-x.rating, -x.reviews))
    return sorted_sitters

def display_pet_sitters(sitters: List[PetSitter]):
    """
    Display the list of pet sitters.

    :param sitters: List of PetSitter instances to display
    """
    if not sitters:
        print("No pet sitters found based on the provided filters.")
        return
    
    print("Filtered and Sorted Pet Sitters:")
    for sitter in sitters:
        print(sitter)

def main():
    # Load pet sitter data from a JSON file
    file_path = 'pet_sitters.json'
    pet_sitters = load_pet_sitter_data(file_path)

    # Define filtering criteria
    min_rating = 4.0
    min_reviews = 10

    # Filter and sort pet sitters
    filtered_sitters = filter_and_sort_pet_sitters(pet_sitters, min_rating, min_reviews)

    # Display the filtered pet sitters
    display_pet_sitters(filtered_sitters)

if __name__ == "__main__":
    main()
```

Make sure to create a `pet_sitters.json` file in the same directory with the appropriate structure for the script to run correctly.
