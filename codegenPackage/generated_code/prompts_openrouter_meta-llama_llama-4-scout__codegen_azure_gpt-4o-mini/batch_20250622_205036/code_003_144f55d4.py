"""
Generated Code Metadata:
========================
Original URL: https://worldiscoveryperu.com
Prompt: "Compare and contrast the 'Perú Andino 1' and 'Perú Ancestral 1' travel packages offered by World Discovery Perù, highlighting their unique features and experiences."
Generated: DETERMINISTIC_144f55d4906a9a61
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TravelPackage:
    """
    A class to represent a travel package.

    Attributes:
        name (str): The name of the travel package.
        description (str): A brief description of the travel package.
        unique_features (list): A list of unique features of the travel package.
        experiences (list): A list of experiences included in the travel package.
    """

    def __init__(self, name, description, unique_features, experiences):
        """
        Initializes a TravelPackage instance.

        Args:
            name (str): The name of the travel package.
            description (str): A brief description of the travel package.
            unique_features (list): A list of unique features of the travel package.
            experiences (list): A list of experiences included in the travel package.
        """
        self.name = name
        self.description = description
        self.unique_features = unique_features
        self.experiences = experiences

    def display_info(self):
        """Displays the information of the travel package."""
        print(f"Package Name: {self.name}")
        print(f"Description: {self.description}")
        print("Unique Features:")
        for feature in self.unique_features:
            print(f"- {feature}")
        print("Experiences Included:")
        for experience in self.experiences:
            print(f"- {experience}")
        print("\n")


def compare_packages(package1, package2):
    """
    Compares two travel packages and displays their information.

    Args:
        package1 (TravelPackage): The first travel package to compare.
        package2 (TravelPackage): The second travel package to compare.
    """
    print("Comparing Travel Packages:\n")
    package1.display_info()
    package2.display_info()


def main():
    """
    Main function to create travel packages and compare them.
    """
    try:
        # Define the 'Perú Andino 1' travel package
        peru_andino_1 = TravelPackage(
            name="Perú Andino 1",
            description="Explore the majestic Andes mountains and their rich culture.",
            unique_features=[
                "Guided tours of ancient Incan ruins",
                "Scenic hikes through breathtaking landscapes",
                "Cultural immersion with local communities"
            ],
            experiences=[
                "Visit Machu Picchu",
                "Explore the Sacred Valley",
                "Experience traditional Andean music and dance"
            ]
        )

        # Define the 'Perú Ancestral 1' travel package
        peru_ancestral_1 = TravelPackage(
            name="Perú Ancestral 1",
            description="Discover the ancestral heritage of Peru through its history and traditions.",
            unique_features=[
                "Focus on ancient civilizations and their legacies",
                "Workshops on traditional crafts and cooking",
                "Visits to archaeological sites off the beaten path"
            ],
            experiences=[
                "Tour of the Nazca Lines",
                "Visit to the ancient city of Cusco",
                "Participate in a traditional Peruvian cooking class"
            ]
        )

        # Compare the two travel packages
        compare_packages(peru_andino_1, peru_ancestral_1)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
