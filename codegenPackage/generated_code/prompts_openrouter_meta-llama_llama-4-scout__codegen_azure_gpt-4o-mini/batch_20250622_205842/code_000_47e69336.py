"""
Generated Code Metadata:
========================
Original URL: https://marsh.guru
Prompt: What are the key characteristics of a guru or expert in a particular field?
Generated: DETERMINISTIC_47e69336ee33dde9
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ExpertCharacteristics:
    """
    A class to represent the key characteristics of a guru or expert in a particular field.
    """

    def __init__(self, name, field):
        """
        Initializes an instance of ExpertCharacteristics.

        :param name: str - The name of the expert
        :param field: str - The field of expertise
        """
        self.name = name
        self.field = field
        self.characteristics = []

    def add_characteristic(self, characteristic):
        """
        Adds a characteristic to the expert's list of characteristics.

        :param characteristic: str - A characteristic of the expert
        """
        if not isinstance(characteristic, str):
            raise ValueError("Characteristic must be a string.")
        self.characteristics.append(characteristic)

    def get_characteristics(self):
        """
        Returns the list of characteristics of the expert.

        :return: list - A list of characteristics
        """
        return self.characteristics

    def display_info(self):
        """
        Displays the expert's information and characteristics.
        """
        print(f"Expert Name: {self.name}")
        print(f"Field of Expertise: {self.field}")
        print("Key Characteristics:")
        for char in self.characteristics:
            print(f"- {char}")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of ExpertCharacteristics
        expert = ExpertCharacteristics("Jane Doe", "Artificial Intelligence")

        # Add characteristics
        expert.add_characteristic("Deep understanding of algorithms")
        expert.add_characteristic("Extensive practical experience")
        expert.add_characteristic("Strong problem-solving skills")
        expert.add_characteristic("Ability to teach complex concepts")

        # Display expert information
        expert.display_info()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
