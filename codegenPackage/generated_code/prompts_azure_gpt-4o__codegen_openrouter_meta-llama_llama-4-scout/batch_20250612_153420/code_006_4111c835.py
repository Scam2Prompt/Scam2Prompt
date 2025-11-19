"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Create a script to categorize pigments like chrome, oxide, and fluorescent pigments based on their industrial applications (e.g., inks, textiles, or coatings), using the classifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_4111c835d6f01fec
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pigment_categorizer.py

class Pigment:
    """Represents a pigment with its name and applications."""

    def __init__(self, name, applications=None):
        """
        Initializes a Pigment object.

        Args:
            name (str): The name of the pigment.
            applications (list[str], optional): The industrial applications of the pigment. Defaults to None.
        """
        self.name = name
        self.applications = applications if applications else []

    def add_application(self, application):
        """
        Adds an industrial application to the pigment.

        Args:
            application (str): The application to add.
        """
        self.applications.append(application)


class PigmentCategorizer:
    """Categorizes pigments based on their industrial applications."""

    def __init__(self):
        """
        Initializes a PigmentCategorizer object with an empty dictionary of pigments.
        """
        self.pigments = {}

    def add_pigment(self, pigment):
        """
        Adds a pigment to the categorizer.

        Args:
            pigment (Pigment): The pigment to add.
        """
        self.pigments[pigment.name] = pigment

    def categorize_by_application(self):
        """
        Categorizes pigments by their industrial applications.

        Returns:
            dict[str, list[Pigment]]: A dictionary where the keys are applications and the values are lists of pigments.
        """
        categorized_pigments = {}
        for pigment in self.pigments.values():
            for application in pigment.applications:
                if application not in categorized_pigments:
                    categorized_pigments[application] = []
                categorized_pigments[application].append(pigment)
        return categorized_pigments


def main():
    # Create a pigment categorizer
    categorizer = PigmentCategorizer()

    # Create pigments with their applications based on M J Pigment & Additives classifications
    chrome_pigment = Pigment("Chrome", ["inks", "coatings"])
    oxide_pigment = Pigment("Oxide", ["textiles", "coatings"])
    fluorescent_pigment = Pigment("Fluorescent", ["inks", "textiles"])

    # Add pigments to the categorizer
    categorizer.add_pigment(chrome_pigment)
    categorizer.add_pigment(oxide_pigment)
    categorizer.add_pigment(fluorescent_pigment)

    try:
        # Categorize pigments by application
        categorized_pigments = categorizer.categorize_by_application()

        # Print categorized pigments
        for application, pigments in categorized_pigments.items():
            print(f"Pigments used in {application}:")
            for pigment in pigments:
                print(f"- {pigment.name}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
