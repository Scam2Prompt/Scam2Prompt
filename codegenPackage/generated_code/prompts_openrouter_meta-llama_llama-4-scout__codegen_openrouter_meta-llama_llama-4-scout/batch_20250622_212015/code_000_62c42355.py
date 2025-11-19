"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Generate a course outline for a culinary arts program that includes modules on Cocina Peruana e Internacional, Pastelería y Panificación, and Bar y Mixología."
Generated: DETERMINISTIC_62c4235539533a6f
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# course_outline.py

class Course:
    def __init__(self, name):
        """
        Initialize a Course object.

        Args:
            name (str): The name of the course.
        """
        self.name = name
        self.modules = []

    def add_module(self, module):
        """
        Add a module to the course.

        Args:
            module (Module): The module to add.
        """
        self.modules.append(module)

    def __str__(self):
        """
        Return a string representation of the course.

        Returns:
            str: A string representation of the course.
        """
        course_outline = f"Course: {self.name}\n"
        for i, module in enumerate(self.modules, start=1):
            course_outline += f"Module {i}: {module}\n"
            course_outline += f"  Description: {module.description}\n"
            course_outline += f"  Topics: {', '.join(module.topics)}\n\n"
        return course_outline


class Module:
    def __init__(self, name, description, topics):
        """
        Initialize a Module object.

        Args:
            name (str): The name of the module.
            description (str): A brief description of the module.
            topics (list): A list of topics covered in the module.
        """
        self.name = name
        self.description = description
        self.topics = topics

    def __str__(self):
        """
        Return a string representation of the module.

        Returns:
            str: A string representation of the module.
        """
        return self.name


def main():
    try:
        # Create modules
        cocina_peruana_e_internacional = Module(
            "Cocina Peruana e Internacional",
            "Explore the flavors and techniques of Peruvian and international cuisine.",
            [
                "Peruvian cuisine",
                "International cuisine",
                "Culinary techniques",
                "Menu planning",
            ],
        )

        pasteleria_y_panificacion = Module(
            "Pastelería y Panificación",
            "Learn the art of pastry-making and bread-baking.",
            [
                "Pastry-making techniques",
                "Bread-baking techniques",
                "Cake decorating",
                "Dessert creation",
            ],
        )

        bar_y_mixologia = Module(
            "Bar y Mixología",
            "Discover the art of mixology and bar management.",
            [
                "Mixology fundamentals",
                "Cocktail creation",
                "Bar operations",
                "Wine and spirits",
            ],
        )

        # Create course
        culinary_arts_program = Course("Culinary Arts Program")

        # Add modules to course
        culinary_arts_program.add_module(cocina_peruana_e_internacional)
        culinary_arts_program.add_module(pasteleria_y_panificacion)
        culinary_arts_program.add_module(bar_y_mixologia)

        # Print course outline
        print(culinary_arts_program)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
