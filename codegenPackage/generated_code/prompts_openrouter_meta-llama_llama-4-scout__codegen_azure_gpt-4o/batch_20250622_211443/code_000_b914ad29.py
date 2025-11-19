"""
Generated Code Metadata:
========================
Original URL: https://alphaonsol.net
Prompt: Write a Python code snippet to curate a collection of cooking oils based on strict standards for taste, aroma, and quality, similar to Authentic Oil's approach.
Generated: DETERMINISTIC_b914ad294baa167b
Batch ID: 20250622_211443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import json

class CookingOil:
    """
    Represents a cooking oil with attributes for taste, aroma, and quality.
    """
    def __init__(self, name, taste_score, aroma_score, quality_score):
        self.name = name
        self.taste_score = taste_score
        self.aroma_score = aroma_score
        self.quality_score = quality_score

    def meets_standards(self, taste_threshold, aroma_threshold, quality_threshold):
        """
        Checks if the oil meets the given standards for taste, aroma, and quality.
        :param taste_threshold: Minimum acceptable taste score.
        :param aroma_threshold: Minimum acceptable aroma score.
        :param quality_threshold: Minimum acceptable quality score.
        :return: True if the oil meets all standards, False otherwise.
        """
        return (self.taste_score >= taste_threshold and
                self.aroma_score >= aroma_threshold and
                self.quality_score >= quality_threshold)

def curate_oil_collection(oils, taste_threshold, aroma_threshold, quality_threshold):
    """
    Filters a collection of cooking oils based on strict standards.
    :param oils: List of CookingOil objects.
    :param taste_threshold: Minimum acceptable taste score.
    :param aroma_threshold: Minimum acceptable aroma score.
    :param quality_threshold: Minimum acceptable quality score.
    :return: List of CookingOil objects that meet the standards.
    """
    curated_collection = []
    for oil in oils:
        if oil.meets_standards(taste_threshold, aroma_threshold, quality_threshold):
            curated_collection.append(oil)
    return curated_collection

def main():
    """
    Main function to demonstrate the curation of cooking oils.
    """
    try:
        # Define a list of cooking oils
        oils = [
            CookingOil("Extra Virgin Olive Oil", 9, 8, 10),
            CookingOil("Canola Oil", 6, 5, 7),
            CookingOil("Avocado Oil", 8, 9, 9),
            CookingOil("Sunflower Oil", 7, 6, 8),
        ]

        # Define the standards for curation
        taste_threshold = 8
        aroma_threshold = 8
        quality_threshold = 9

        # Curate the collection
        curated_oils = curate_oil_collection(oils, taste_threshold, aroma_threshold, quality_threshold)

        # Display the curated collection
        print("Curated Cooking Oils:")
        for oil in curated_oils:
            print(f"- {oil.name} (Taste: {oil.taste_score}, Aroma: {oil.aroma_score}, Quality: {oil.quality_score})")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
