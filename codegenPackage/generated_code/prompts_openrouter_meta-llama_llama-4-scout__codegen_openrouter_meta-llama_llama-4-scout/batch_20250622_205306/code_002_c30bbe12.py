"""
Generated Code Metadata:
========================
Original URL: https://secondcitysummers.com
Prompt: Generate a list of potential comedy class offerings for kids and teens at The Second City, including improv, acting, and comedy writing.
Generated: DETERMINISTIC_c30bbe123094356d
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# comedy_classes.py

class ComedyClass:
    """Represents a comedy class offering."""

    def __init__(self, name, description, age_range, duration):
        """
        Initializes a ComedyClass object.

        Args:
            name (str): The name of the class.
            description (str): A brief description of the class.
            age_range (str): The age range for the class (e.g., "kids", "teens").
            duration (str): The duration of the class (e.g., "6 weeks", "1 day").
        """
        self.name = name
        self.description = description
        self.age_range = age_range
        self.duration = duration

    def __str__(self):
        return f"{self.name} ({self.age_range}) - {self.description} ({self.duration})"


class ComedyClassCatalog:
    """Represents a catalog of comedy class offerings."""

    def __init__(self):
        self.classes = []

    def add_class(self, comedy_class):
        """Adds a comedy class to the catalog."""
        self.classes.append(comedy_class)

    def get_classes(self, age_range=None):
        """
        Retrieves a list of comedy classes.

        Args:
            age_range (str, optional): Filters classes by age range. Defaults to None.

        Returns:
            list: A list of ComedyClass objects.
        """
        if age_range:
            return [cls for cls in self.classes if cls.age_range == age_range]
        return self.classes


def main():
    # Create a catalog of comedy classes
    catalog = ComedyClassCatalog()

    # Add classes for kids
    catalog.add_class(ComedyClass("Improv for Kids", "Learn the basics of improv comedy", "kids", "6 weeks"))
    catalog.add_class(ComedyClass("Kids' Comedy Writing", "Write and perform your own comedy sketches", "kids", "8 weeks"))
    catalog.add_class(ComedyClass("Acting for Kids", "Develop acting skills with a comedic twist", "kids", "6 weeks"))

    # Add classes for teens
    catalog.add_class(ComedyClass("Improv for Teens", "Take your improv skills to the next level", "teens", "8 weeks"))
    catalog.add_class(ComedyClass("Teens' Comedy Writing", "Write and perform your own comedy scripts", "teens", "10 weeks"))
    catalog.add_class(ComedyClass("Comedy Acting for Teens", "Hone your acting skills with a focus on comedy", "teens", "8 weeks"))

    # Retrieve and print classes for kids and teens
    try:
        kids_classes = catalog.get_classes("kids")
        teens_classes = catalog.get_classes("teens")

        print("Kids' Classes:")
        for cls in kids_classes:
            print(cls)

        print("\nTeens' Classes:")
        for cls in teens_classes:
            print(cls)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
