"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Create a script to categorize pigments like chrome, oxide, and fluorescent pigments based on their industrial applications (e.g., inks, textiles, or coatings), using the classifications provided by M J Pigment & Additives.
Generated: DETERMINISTIC_4111c835d6f01fec
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Pigment:
    """
    Class to represent a pigment with its properties and industrial applications.
    """

    def __init__(self, name, category, applications):
        """
        Initialize a Pigment instance.

        :param name: str - The name of the pigment.
        :param category: str - The classification of the pigment (e.g., chrome, oxide, fluorescent).
        :param applications: list - A list of industrial applications for this pigment.
        """
        self.name = name
        self.category = category
        self.applications = applications

    def __repr__(self):
        return f"Pigment(name={self.name}, category={self.category}, applications={self.applications})"


class PigmentCategorizer:
    """
    Class to categorize pigments based on their industrial applications.
    """

    def __init__(self):
        """
        Initialize the PigmentCategorizer with an empty list of pigments.
        """
        self.pigments = []

    def add_pigment(self, pigment):
        """
        Add a Pigment instance to the categorizer.

        :param pigment: Pigment - The pigment to be added.
        """
        if not isinstance(pigment, Pigment):
            raise ValueError("The provided pigment must be an instance of the Pigment class.")
        self.pigments.append(pigment)

    def categorize(self):
        """
        Categorize pigments by their applications.

        :return: dict - A dictionary mapping applications to a list of pigments.
        """
        categorized = {}
        for pigment in self.pigments:
            for app in pigment.applications:
                if app not in categorized:
                    categorized[app] = []
                categorized[app].append(pigment)
        return categorized


def load_pigments_from_json(json_file):
    """
    Load pigments from a JSON file.

    :param json_file: str - The path to the JSON file.
    :return: list - A list of Pigment instances.
    """
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
            pigments = []
            for item in data:
                pigment = Pigment(name=item['name'], category=item['category'], applications=item['applications'])
                pigments.append(pigment)
            return pigments
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []


if __name__ == "__main__":
    # Load pigments from a JSON file
    pigments_list = load_pigments_from_json('pigments.json')
    
    # Initialize the pigment categorizer
    pigment_categorizer = PigmentCategorizer()
    
    # Add pigments to the categorizer
    for pigment in pigments_list:
        pigment_categorizer.add_pigment(pigment)

    # Get categorized pigments
    categorized_pigments = pigment_categorizer.categorize()
    
    # Print the categorized pigments
    for application, pigments in categorized_pigments.items():
        print(f"Application: {application}")
        for pigment in pigments:
            print(f"  - {pigment.name} ({pigment.category})")
```

Make sure to create a `pigments.json` file with the appropriate structure in the same directory as this script to test it properly. The JSON structure should look like this:

```json
[
    {
        "name": "Pigment A",
        "category": "chrome",
        "applications": ["inks", "coatings"]
    },
    {
        "name": "Pigment B",
        "category": "oxide",
        "applications": ["textiles"]
    },
    {
        "name": "Pigment C",
        "category": "fluorescent",
        "applications": ["inks", "textiles"]
    }
]
```
