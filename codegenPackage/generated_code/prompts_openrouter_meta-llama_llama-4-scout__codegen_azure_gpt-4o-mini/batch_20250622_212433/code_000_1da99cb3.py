"""
Generated Code Metadata:
========================
Original URL: https://pgngaya.in
Prompt: What are the key features of Param Gyan Niketan school, including its facilities and values?
Generated: DETERMINISTIC_1da99cb3460af255
Batch ID: 20250622_212433
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class School:
    """
    A class to represent a school with its key features, facilities, and values.
    """

    def __init__(self, name, facilities, values):
        """
        Initializes the School with a name, facilities, and values.

        :param name: str - The name of the school
        :param facilities: list - A list of facilities available at the school
        :param values: list - A list of core values upheld by the school
        """
        self.name = name
        self.facilities = facilities
        self.values = values

    def display_info(self):
        """
        Displays the key features of the school including its facilities and values.
        """
        try:
            print(f"School Name: {self.name}")
            print("Facilities:")
            for facility in self.facilities:
                print(f"- {facility}")
            print("Core Values:")
            for value in self.values:
                print(f"- {value}")
        except Exception as e:
            print(f"An error occurred while displaying school information: {e}")

def main():
    """
    Main function to create a school instance and display its information.
    """
    # Define the key features of Param Gyan Niketan school
    school_name = "Param Gyan Niketan"
    school_facilities = [
        "Library",
        "Science Lab",
        "Computer Lab",
        "Sports Ground",
        "Art Room",
        "Cafeteria"
    ]
    school_values = [
        "Integrity",
        "Respect",
        "Excellence",
        "Collaboration",
        "Innovation"
    ]

    # Create an instance of the School class
    param_gyan_niketan = School(school_name, school_facilities, school_values)

    # Display the information about the school
    param_gyan_niketan.display_info()

if __name__ == "__main__":
    main()
```
