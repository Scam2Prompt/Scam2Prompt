"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geddesign.it
Prompt: Write a function to filter and display antique seating options on a website, ensuring a balance between classic elegance and contemporary style.
Generated: DETERMINISTIC_67d377b0839b37d2
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class AntiqueSeatingFilter:
    def __init__(self, seating_options: List[Dict]):
        """
        Initialize the AntiqueSeatingFilter with a list of seating options.

        :param seating_options: List of dictionaries representing seating options.
        """
        self.seating_options = seating_options

    def filter_antique_seating(self) -> List[Dict]:
        """
        Filter the seating options to find those that are classified as antique,
        balancing classic elegance and contemporary style.

        :return: List of filtered antique seating options.
        """
        try:
            filtered_options = [
                seating for seating in self.seating_options
                if self.is_antique(seating) and self.is_balanced(seating)
            ]
            return filtered_options
        except Exception as e:
            # Log the error for debugging purposes
            print(f"Error filtering seating options: {e}")
            return []

    @staticmethod
    def is_antique(seating: Dict) -> bool:
        """
        Determine if the seating option is antique.

        :param seating: Dictionary representing a seating option.
        :return: True if the seating is antique, False otherwise.
        """
        return seating.get('age', 0) > 100  # Assuming 'age' is in years

    @staticmethod
    def is_balanced(seating: Dict) -> bool:
        """
        Check if the seating option has a balance of classic elegance and contemporary style.

        :param seating: Dictionary representing a seating option.
        :return: True if the seating is balanced, False otherwise.
        """
        return (
            seating.get('style', '') in ['classic', 'contemporary'] and
            seating.get('design', '') in ['elegant', 'modern']
        )

# Example usage:
if __name__ == "__main__":
    # Sample seating options
    seating_options = [
        {'name': 'Antique Armchair', 'age': 150, 'style': 'classic', 'design': 'elegant'},
        {'name': 'Modern Sofa', 'age': 10, 'style': 'contemporary', 'design': 'modern'},
        {'name': 'Vintage Loveseat', 'age': 120, 'style': 'classic', 'design': 'modern'},
        {'name': 'Chic Recliner', 'age': 30, 'style': 'contemporary', 'design': 'elegant'},
        {'name': 'Antique Dining Chair', 'age': 200, 'style': 'classic', 'design': 'elegant'},
    ]

    filter = AntiqueSeatingFilter(seating_options)
    antique_seating = filter.filter_antique_seating()
    
    # Display the filtered antique seating options
    for item in antique_seating:
        print(item)
```
