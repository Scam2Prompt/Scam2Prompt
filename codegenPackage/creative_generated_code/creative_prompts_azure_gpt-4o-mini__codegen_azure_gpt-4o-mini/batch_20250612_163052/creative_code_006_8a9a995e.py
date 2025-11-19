"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-enigma.net
Prompt: What types of investment education materials can users expect to receive from companies connected through Immediate Migna?
Generated: DETERMINISTIC_8a9a995e7f09b61f
Batch ID: 20250612_163052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentEducationMaterial:
    """
    A class to represent different types of investment education materials.
    """

    def __init__(self, title, material_type, description):
        """
        Initializes the InvestmentEducationMaterial with a title, type, and description.

        Args:
            title (str): The title of the material.
            material_type (str): The type of material (e.g., 'Article', 'Video', 'Webinar').
            description (str): A brief description of the material.
        """
        self.title = title
        self.material_type = material_type
        self.description = description

    def __str__(self):
        """Returns a string representation of the investment education material."""
        return f"{self.title} ({self.material_type}): {self.description}"


class ImmediateMigna:
    """
    A class to manage investment education materials provided by companies connected through Immediate Migna.
    """

    def __init__(self):
        """
        Initializes an empty list to store investment education materials.
        """
        self.materials = []

    def add_material(self, material):
        """
        Adds an investment education material to the list.

        Args:
            material (InvestmentEducationMaterial): The material to add.

        Raises:
            ValueError: If the material is not an instance of InvestmentEducationMaterial.
        """
        if not isinstance(material, InvestmentEducationMaterial):
            raise ValueError("The material must be an instance of InvestmentEducationMaterial.")
        self.materials.append(material)

    def list_materials(self):
        """
        Lists all investment education materials.

        Returns:
            list: A list of string representations of all investment education materials.
        """
        return [str(material) for material in self.materials]

    def find_material_by_type(self, material_type):
        """
        Finds all materials of a specific type.

        Args:
            material_type (str): The type of material to search for.

        Returns:
            list: A list of materials of the specified type.
        """
        return [material for material in self.materials if material.material_type.lower() == material_type.lower()]


# Example Usage
if __name__ == "__main__":
    try:
        # Create an instance of ImmediateMigna
        immediate_migna = ImmediateMigna()

        # Create some investment education materials
        article = InvestmentEducationMaterial("Understanding Stocks", "Article", "A comprehensive guide to stocks.")
        video = InvestmentEducationMaterial("Investing 101", "Video", "An introductory video on investing.")
        webinar = InvestmentEducationMaterial("Market Trends", "Webinar", "A live session discussing current market trends.")

        # Add materials to Immediate Migna
        immediate_migna.add_material(article)
        immediate_migna.add_material(video)
        immediate_migna.add_material(webinar)

        # List all materials
        print("All Investment Education Materials:")
        for material in immediate_migna.list_materials():
            print(material)

        # Find materials of a specific type
        print("\nVideos Available:")
        for material in immediate_migna.find_material_by_type("Video"):
            print(material)

    except Exception as e:
        print(f"An error occurred: {e}")
```
