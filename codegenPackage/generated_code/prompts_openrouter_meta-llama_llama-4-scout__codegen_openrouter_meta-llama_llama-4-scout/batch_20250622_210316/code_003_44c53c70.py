"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: Compare the features of the different campuses of Universidad Tecnológico Cuicalli, including Naucalpan, Huixquilucan, Ecatepec, and Arboledas.
Generated: DETERMINISTIC_44c53c7024ff8ede
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# campus_comparator.py

class Campus:
    """Represents a campus of Universidad Tecnológico Cuicalli."""

    def __init__(self, name, location, features):
        """
        Initializes a Campus object.

        Args:
            name (str): Name of the campus.
            location (str): Location of the campus.
            features (list): List of features of the campus.
        """
        self.name = name
        self.location = location
        self.features = features

    def __str__(self):
        return f"{self.name} ({self.location})"


class CampusComparator:
    """Compares the features of different campuses."""

    def __init__(self):
        self.campuses = []

    def add_campus(self, campus):
        """
        Adds a campus to the comparator.

        Args:
            campus (Campus): Campus object to add.
        """
        self.campuses.append(campus)

    def compare_features(self):
        """
        Compares the features of the campuses.

        Returns:
            dict: Dictionary with campus names as keys and their features as values.
        """
        features_comparison = {}
        for campus in self.campuses:
            features_comparison[campus.name] = campus.features
        return features_comparison

    def print_comparison(self):
        """
        Prints the comparison of features in a readable format.
        """
        features_comparison = self.compare_features()
        for campus, features in features_comparison.items():
            print(f"Features of {campus}:")
            for feature in features:
                print(f"- {feature}")
            print()


def main():
    try:
        comparator = CampusComparator()

        naucalpan_campus = Campus(
            "Naucalpan",
            "Naucalpan de Juárez",
            [
                "Library",
                "Computer Labs",
                "Auditorium",
                "Sports Facilities",
                "Cafeteria",
            ],
        )

        huixquilucan_campus = Campus(
            "Huixquilucan",
            "Huixquilucan de Degollado",
            [
                "Library",
                "Computer Labs",
                "Auditorium",
                "Sports Facilities",
                "Cafeteria",
                "Research Center",
            ],
        )

        ecatepec_campus = Campus(
            "Ecatepec",
            "Ecatepec de Morelos",
            [
                "Library",
                "Computer Labs",
                "Auditorium",
                "Sports Facilities",
            ],
        )

        arboledas_campus = Campus(
            "Arboledas",
            "Ciudad de México",
            [
                "Library",
                "Computer Labs",
                "Auditorium",
                "Sports Facilities",
                "Cafeteria",
                "Language Center",
            ],
        )

        comparator.add_campus(naucalpan_campus)
        comparator.add_campus(huixquilucan_campus)
        comparator.add_campus(ecatepec_campus)
        comparator.add_campus(arboledas_campus)

        comparator.print_comparison()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
