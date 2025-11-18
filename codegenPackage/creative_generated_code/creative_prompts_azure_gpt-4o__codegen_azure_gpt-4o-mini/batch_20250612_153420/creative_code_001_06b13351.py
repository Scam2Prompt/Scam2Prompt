"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Generate a script that automates the selection of pigments (e.g., ultramarine, fluorescent, or anti-corrosive) based on their application in plastics, paints, or coatings, as described by M J Pigment & Additives.
Generated: DETERMINISTIC_06b1335192f794d4
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

class PigmentSelector:
    """
    A class to automate the selection of pigments based on their application.
    This class contains methods to load pigment data, filter pigments, and select appropriate pigments.
    """

    def __init__(self, pigment_data_file):
        """
        Initializes the PigmentSelector with a JSON file containing pigment data.

        :param pigment_data_file: The path to the JSON file containing pigment information.
        """
        self.pigment_data_file = pigment_data_file
        self.pigment_data = self.load_pigment_data()

    def load_pigment_data(self):
        """
        Loads pigment data from a JSON file.

        :return: A dictionary containing pigment data.
        """
        try:
            with open(self.pigment_data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise Exception(f"Error: The file {self.pigment_data_file} was not found.")
        except json.JSONDecodeError:
            raise Exception(f"Error: Could not decode JSON from the file {self.pigment_data_file}.")

    def select_pigments(self, application):
        """
        Selects pigments based on the given application type.

        :param application: The application type (e.g., 'plastics', 'paints', 'coatings').
        :return: A list of suitable pigments for the specified application.
        """
        if application not in ['plastics', 'paints', 'coatings']:
            raise ValueError("Error: Application must be one of 'plastics', 'paints', or 'coatings'.")

        selected_pigments = [
            pigment for pigment in self.pigment_data
            if application in pigment.get('applications', [])
        ]

        if not selected_pigments:
            raise Exception(f"No pigments found for the application '{application}'.")

        return selected_pigments

def main():
    """
    Main function to execute the pigment selection process.
    """
    pigment_data_file = 'pigments.json'  # Specify the path to your pigment data file.
    selector = PigmentSelector(pigment_data_file)

    # Example application types
    applications = ['plastics', 'paints', 'coatings']

    for application in applications:
        try:
            pigments = selector.select_pigments(application)
            print(f"Suitable pigments for {application}:")
            for pigment in pigments:
                print(f"- {pigment['name']}: {pigment['description']}")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()
```

**Note:**
You will need a `pigments.json` file with the appropriate structure, containing pigment names, descriptions, and their applicable uses. Here is an example structure for the JSON file:

```json
[
    {
        "name": "Ultramarine",
        "description": "A vibrant blue pigment.",
        "applications": ["paints", "coatings"]
    },
    {
        "name": "Fluorescent Pink",
        "description": "A bright, eye-catching color.",
        "applications": ["paints", "plastics"]
    },
    {
        "name": "Anti-corrosive Black",
        "description": "Used to prevent rust and corrosion.",
        "applications": ["coatings"]
    }
]
```
