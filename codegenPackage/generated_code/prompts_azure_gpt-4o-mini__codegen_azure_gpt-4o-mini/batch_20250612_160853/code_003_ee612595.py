"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Develop a function that lists the areas of expertise for Dr. S. Nagendra Boopathy, including interventional cardiology and structural heart disease, as highlighted on the Ask a Cardiologist webpage.
Generated: DETERMINISTIC_ee6125952b68e73f
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Cardiologist:
    """
    A class to represent a cardiologist and their areas of expertise.
    """

    def __init__(self, name):
        """
        Initializes the Cardiologist with a name and an empty list of expertise areas.

        :param name: str - The name of the cardiologist
        """
        self.name = name
        self.expertise_areas = []

    def add_expertise(self, area):
        """
        Adds an area of expertise to the cardiologist's list.

        :param area: str - The area of expertise to be added
        :raises ValueError: If the area is empty or already exists in the list
        """
        if not area:
            raise ValueError("Expertise area cannot be empty.")
        if area in self.expertise_areas:
            raise ValueError(f"Expertise area '{area}' already exists.")
        self.expertise_areas.append(area)

    def list_expertise(self):
        """
        Returns a list of the cardiologist's areas of expertise.

        :return: list - A list of expertise areas
        """
        return self.expertise_areas


def main():
    """
    Main function to demonstrate the usage of the Cardiologist class.
    """
    try:
        # Create an instance of Cardiologist for Dr. S. Nagendra Boopathy
        dr_nagendra = Cardiologist("Dr. S. Nagendra Boopathy")

        # Adding areas of expertise
        dr_nagendra.add_expertise("Interventional Cardiology")
        dr_nagendra.add_expertise("Structural Heart Disease")

        # List and print the areas of expertise
        expertise_list = dr_nagendra.list_expertise()
        print(f"Areas of expertise for {dr_nagendra.name}:")
        for area in expertise_list:
            print(f"- {area}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
