"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Generate a script that automates the selection of pigments (e.g., ultramarine, fluorescent, or anti-corrosive) based on their application in plastics, paints, or coatings, as described by M J Pigment & Additives.
Generated: DETERMINISTIC_06b1335192f794d4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pigment_selector.py

class Pigment:
    def __init__(self, name, applications):
        """
        Initialize a Pigment object.

        Args:
        - name (str): The name of the pigment.
        - applications (list): A list of applications for the pigment.
        """
        self.name = name
        self.applications = applications

class PigmentDatabase:
    def __init__(self):
        """
        Initialize a PigmentDatabase object.
        """
        self.pigments = []

    def add_pigment(self, pigment):
        """
        Add a pigment to the database.

        Args:
        - pigment (Pigment): The pigment to add.
        """
        self.pigments.append(pigment)

    def get_pigments_by_application(self, application):
        """
        Get a list of pigments suitable for a given application.

        Args:
        - application (str): The application to filter by.

        Returns:
        - list: A list of pigments suitable for the application.
        """
        return [pigment for pigment in self.pigments if application.lower() in [app.lower() for app in pigment.applications]]

def main():
    # Create a pigment database
    database = PigmentDatabase()

    # Add pigments to the database
    database.add_pigment(Pigment("Ultramarine", ["plastics", "paints", "coatings"]))
    database.add_pigment(Pigment("Fluorescent", ["plastics", "coatings"]))
    database.add_pigment(Pigment("Anti-Corrosive", ["paints", "coatings"]))

    # Get user input
    application = input("Enter an application (plastics, paints, or coatings): ")

    # Validate user input
    valid_applications = ["plastics", "paints", "coatings"]
    if application.lower() not in valid_applications:
        print("Invalid application. Please try again.")
        return

    # Get suitable pigments
    suitable_pigments = database.get_pigments_by_application(application)

    # Print results
    if suitable_pigments:
        print(f"Pigments suitable for {application}:")
        for pigment in suitable_pigments:
            print(pigment.name)
    else:
        print(f"No pigments found for {application}.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
