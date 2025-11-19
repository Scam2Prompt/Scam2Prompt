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
# travel_packages.py

class TravelPackage:
    def __init__(self, name, description, features, experiences):
        """
        Initialize a TravelPackage object.

        Args:
            name (str): The name of the travel package.
            description (str): A brief description of the travel package.
            features (list): A list of unique features of the travel package.
            experiences (list): A list of experiences offered by the travel package.
        """
        self.name = name
        self.description = description
        self.features = features
        self.experiences = experiences

    def __str__(self):
        return f"{self.name}: {self.description}"

    def print_details(self):
        print(f"**{self.name}**")
        print(self.description)
        print("\n**Unique Features:**")
        for feature in self.features:
            print(f"- {feature}")
        print("\n**Experiences:**")
        for experience in self.experiences:
            print(f"- {experience}")


class WorldDiscoveryPeru:
    def __init__(self):
        """
        Initialize a WorldDiscoveryPeru object with travel packages.
        """
        self.packages = {
            "Perú Andino1": TravelPackage(
                "Perú Andino1",
                "Explore the Andean highlands and discover the rich cultural heritage of Peru.",
                [
                    "Visit Machuigenicchu, one of the Seven Wonders of the World",
                    "Experience the vibrant city of Cusco",
                    "Hike to the Sun Gate for breathtaking views",
                ],
                [
                    "Guided tours of historic sites",
                    "Traditional Andean lunch",
                    "Free time to explore local markets",
                ],
            ),
            "Perú Ancestral1": TravelPackage(
                "Perú Ancestral1",
                "Uncover the ancient secrets of Peru and immerse yourself in its rich history.",
                [
                    "Visit the ancient city of Chan Chan",
                    "Explore the mysterious Nazca Lines",
                    "Discover the traditional textiles of the Andean communities",
                ],
                [
                    "Guided tours of archaeological sites",
                    "Private audience with a local shaman",
                    "Traditional Andean dinner",
                ],
            ),
        }

    def compare_packages(self, package1_name, package2_name):
        """
        Compare and contrast two travel packages.

        Args:
            package1_name (str): The name of the first travel package.
            package2_name (str): The name of the second travel package.
        """
        if package1_name not in self.packages or package2_name not in self.packages:
            raise ValueError("Invalid package name")

        package1 = self.packages[package1_name]
        package2 = self.packages[package2_name]

        print("# Travel Package Comparison")
        print(f"## {package1_name} vs {package2_name}\n")

        package1.print_details()
        print("\n---\n")
        package2.print_details()

        print("\n# Comparison Highlights")
        print(f"## Unique Features of {package1_name}:")
        for feature in package1.features:
            print(f"- {feature}")
        print(f"\n## Unique Features of {package2_name}:")
        for feature in package2.features:
            if feature not in package1.features:
                print(f"- {feature}")

        print(f"\n## Shared Experiences:")
        shared_experiences = set(package1.experiences).intersection(set(package2.experiences))
        for experience in shared_experiences:
            print(f"- {experience}")


if __name__ == "__main__":
    peru = WorldDiscoveryPeru()
    peru.compare_packages("Perú Andino1", "Perú Ancestral1")
```
