"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Write a Python script to recommend Spanish language classes for foreigners based on their proficiency level, using the structure described on the "Clases de Español para Extranjeros" page of SpanishUpdate.com.
Generated: DETERMINISTIC_a6f3296c7ad0a1e3
Batch ID: 20250612_152340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# spanish_language_classes.py

class SpanishLanguageClass:
    """Represents a Spanish language class for foreigners."""

    def __init__(self, name, description, level):
        """
        Initializes a SpanishLanguageClass object.

        Args:
            name (str): The name of the class.
            description (str): A brief description of the class.
            level (str): The proficiency level of the class (A1, A2, B1, B2, C1, C2).
        """
        self.name = name
        self.description = description
        self.level = level

    def __str__(self):
        return f"{self.name} ({self.level}) - {self.description}"


class LanguageClassRecommender:
    """Recommends Spanish language classes based on proficiency level."""

    def __init__(self):
        """
        Initializes a LanguageClassRecommender object.

        The classes are structured according to the "Clases de Español para Extranjeros" page of SpanishUpdate.com.
        """
        self.classes = [
            SpanishLanguageClass("Beginner", "For those with little to no Spanish knowledge.", "A1"),
            SpanishLanguageClass("Elementary", "For those who can understand and communicate basic phrases.", "A2"),
            SpanishLanguageClass("Intermediate", "For those who can hold conversations and understand various topics.", "B1"),
            SpanishLanguageClass("Upper-Intermediate", "For those who can express themselves fluently and accurately.", "B2"),
            SpanishLanguageClass("Advanced", "For those who can understand complex texts and conversations.", "C1"),
            SpanishLanguageClass("Proficient", "For those who can communicate with native-like fluency and accuracy.", "C2"),
        ]

    def recommend_classes(self, level):
        """
        Recommends Spanish language classes based on the given proficiency level.

        Args:
            level (str): The proficiency level (A1, A2, B1, B2, C1, C2).

        Returns:
            list[SpanishLanguageClass]: A list of recommended language classes.

        Raises:
            ValueError: If the given level is not valid.
        """
        if level not in ["A1", "A2", "B1", "B2", "C1", "C2"]:
            raise ValueError("Invalid level. Please choose from A1, A2, B1, B2, C1, or C2.")

        recommended_classes = [cls for cls in self.classes if cls.level == level]
        return recommended_classes


def main():
    try:
        recommender = LanguageClassRecommender()
        level = input("Enter your Spanish proficiency level (A1, A2, B1, B2, C1, C2): ")
        recommended_classes = recommender.recommend_classes(level)

        if recommended_classes:
            print("Recommended classes:")
            for cls in recommended_classes:
                print(cls)
        else:
            print("No classes found for the given level.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
