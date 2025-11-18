"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Write a Python script to generate a list of art course categories, including "aquarela," "mangá," and "desenho realista," as described on Ânima's website.
Generated: DETERMINISTIC_82623bdb4e297f82
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# art_course_categories.py

class ArtCourseCategories:
    """
    A class to represent a collection of art course categories.
    """

    def __init__(self):
        """
        Initializes the ArtCourseCategories with predefined categories.
        """
        self.categories = self.generate_categories()

    def generate_categories(self):
        """
        Generates a list of art course categories.
        
        Returns:
            list: A list containing the names of art course categories.
        """
        return [
            "aquarela",      # Watercolor painting
            "mangá",         # Manga drawing
            "desenho realista"  # Realistic drawing
        ]

    def get_categories(self):
        """
        Returns the list of art course categories.

        Returns:
            list: A list of art course categories.
        """
        return self.categories

def main():
    """
    Main function to execute the script.
    """
    try:
        art_categories = ArtCourseCategories()
        categories = art_categories.get_categories()
        
        # Display the categories
        print("Art Course Categories:")
        for category in categories:
            print(f"- {category}")
    
    except Exception as e:
        print(f"An error occurred while retrieving art course categories: {e}")

if __name__ == "__main__":
    main()
```
