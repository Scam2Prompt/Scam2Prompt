"""
Generated Code Metadata:
========================
Original URL: https://graffian.com
Prompt: Write a Python script to curate a collection of cooking oils based on their taste, aroma, and quality, similar to Authentic Oil's selection process.
Generated: DETERMINISTIC_a55c6e9b8a356f6f
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class CookingOil:
    """
    Represents a cooking oil with attributes for taste, aroma, and quality.
    """
    def __init__(self, name, taste, aroma, quality):
        self.name = name
        self.taste = taste
        self.aroma = aroma
        self.quality = quality

    def __repr__(self):
        return f"CookingOil(name={self.name}, taste={self.taste}, aroma={self.aroma}, quality={self.quality})"


class OilCurator:
    """
    Curates a collection of cooking oils based on taste, aroma, and quality.
    """
    def __init__(self):
        self.oil_collection = []

    def add_oil(self, oil):
        """
        Adds a CookingOil object to the collection.
        :param oil: CookingOil object
        """
        if not isinstance(oil, CookingOil):
            raise TypeError("Only CookingOil objects can be added to the collection.")
        self.oil_collection.append(oil)

    def curate_collection(self, taste_threshold, aroma_threshold, quality_threshold):
        """
        Filters the oil collection based on taste, aroma, and quality thresholds.
        :param taste_threshold: Minimum acceptable taste score
        :param aroma_threshold: Minimum acceptable aroma score
        :param quality_threshold: Minimum acceptable quality score
        :return: List of curated CookingOil objects
        """
        curated = [
            oil for oil in self.oil_collection
            if oil.taste >= taste_threshold and oil.aroma >= aroma_threshold and oil.quality >= quality_threshold
        ]
        return curated

    def save_collection_to_file(self, filename):
        """
        Saves the curated collection to a JSON file.
        :param filename: Name of the file to save the collection
        """
        try:
            with open(filename, 'w') as file:
                json.dump([oil.__dict__ for oil in self.oil_collection], file, indent=4)
        except IOError as e:
            print(f"Error saving collection to file: {e}")

    def load_collection_from_file(self, filename):
        """
        Loads a collection of oils from a JSON file.
        :param filename: Name of the file to load the collection from
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.oil_collection = [CookingOil(**oil) for oil in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading collection from file: {e}")


# Example usage
if __name__ == "__main__":
    # Create an OilCurator instance
    curator = OilCurator()

    # Add some cooking oils to the collection
    curator.add_oil(CookingOil("Olive Oil", taste=8, aroma=9, quality=10))
    curator.add_oil(CookingOil("Coconut Oil", taste=7, aroma=8, quality=9))
    curator.add_oil(CookingOil("Avocado Oil", taste=9, aroma=8, quality=10))
    curator.add_oil(CookingOil("Canola Oil", taste=6, aroma=5, quality=7))

    # Curate the collection based on thresholds
    curated_oils = curator.curate_collection(taste_threshold=7, aroma_threshold=8, quality_threshold=9)
    print("Curated Oils:", curated_oils)

    # Save the curated collection to a file
    curator.save_collection_to_file("oil_collection.json")

    # Load the collection from the file
    curator.load_collection_from_file("oil_collection.json")
    print("Loaded Oils:", curator.oil_collection)
```
