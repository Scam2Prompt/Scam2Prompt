"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Write a script to automate the creation of a wine pairing menu for a 6-course dinner, using the FestiVin Caraquet's concept of pairing each course with a specific wine.
Generated: DETERMINISTIC_6d919946c1211bf2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define classes for Course and Wine
class Course:
    """Represents a single course in the dinner menu."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Wine:
    """Represents a wine that will be paired with a course."""
    def __init__(self, name, varietal, region):
        self.name = name
        self.varietal = varietal
        self.region = region

    def __str__(self):
        return f"{self.name} ({self.varietal}, {self.region})"


class WinePairingMenu:
    """Handles the creation and display of a wine pairing menu for a multi-course dinner."""
    def __init__(self):
        self.menu = []

    def add_pairing(self, course, wine):
        """
        Adds a course and wine pairing to the menu.

        :param course: Course object to be paired with wine.
        :param wine: Wine object to be paired with the course.
        """
        self.menu.append({"course": course, "wine": wine})

    def display_menu(self):
        """Displays the wine pairing menu."""
        for index, pairing in enumerate(self.menu, start=1):
            course = pairing['course']
            wine = pairing['wine']
            print(f"Course {index}:")
            print(f"  {course}")
            print(f"  Paired with: {wine}")
            print("-" * 40)

    def save_menu_to_file(self, filename):
        """
        Saves the wine pairing menu to a JSON file.

        :param filename: Name of the file where the menu will be saved.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(
                    [
                        {
                            "course": {"name": pairing["course"].name, "description": pairing["course"].description},
                            "wine": {"name": pairing["wine"].name, "varietal": pairing["wine"].varietal, "region": pairing["wine"].region}
                        }
                        for pairing in self.menu
                    ],
                    file,
                    indent=4
                )
            print(f"Menu successfully saved to {filename}")
        except IOError as e:
            print(f"Error saving menu to file: {e}")


# Main script execution
if __name__ == "__main__":
    # Create a WinePairingMenu instance
    menu = WinePairingMenu()

    # Define 6 courses and pair them with wines
    courses = [
        Course("Appetizer", "Fresh oysters served with a mignonette sauce."),
        Course("Salad", "Arugula salad with goat cheese and dried cranberries."),
        Course("Soup", "Creamy butternut squash soup."),
        Course("Main Course", "Grilled lamb chops with rosemary reduction."),
        Course("Cheese Plate", "Selection of aged cheeses."),
        Course("Dessert", "Dark chocolate mousse.")
    ]

    wines = [
        Wine("Chablis", "Chardonnay", "France"),
        Wine("Pinot Noir", "Pinot Noir", "California"),
        Wine("Riesling", "Riesling", "Germany"),
        Wine("Cabernet Sauvignon", "Cabernet Sauvignon", "Argentina"),
        Wine("Sauternes", "Semillon", "France"),
        Wine("Ruby Port", "Port", "Portugal")
    ]

    # Add pairings to the menu
    for course, wine in zip(courses, wines):
        menu.add_pairing(course, wine)

    # Display the menu
    print("Wine Pairing Menu:")
    print("=" * 40)
    menu.display_menu()

    # Save the menu to a file
    menu.save_menu_to_file("wine_pairing_menu.json")
```
