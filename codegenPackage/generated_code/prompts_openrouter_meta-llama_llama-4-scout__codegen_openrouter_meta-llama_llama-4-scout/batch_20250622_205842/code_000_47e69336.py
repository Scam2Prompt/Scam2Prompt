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
# Define a class to represent a Guru or Expert
class Guru:
    """
    Represents a guru or expert in a particular field.

    Attributes:
        name (str): The name of the guru.
        field (str): The field of expertise.
        characteristics (list): A list of key characteristics.
    """

    def __init__(self, name, field, characteristics=None):
        """
        Initializes a Guru object.

        Args:
            name (str): The name of the guru.
            field (str): The field of expertise.
            characteristics (list, optional): A list of key characteristics. Defaults to None.

        Raises:
            TypeError: If name or field is not a string.
            ValueError: If characteristics is not a list or is empty.
        """
        if not isinstance(name, str) or not isinstance(field, str):
            raise TypeError("Name and field must be strings")
        if characteristics is not None and not isinstance(characteristics, list):
            raise ValueError("Characteristics must be a list")
        if characteristics is not None and len(characteristics) == 0:
            raise ValueError("Characteristics list cannot be empty")

        self.name = name
        self.field = field
        self.characteristics = characteristics if characteristics is not None else []

    def add_characteristic(self, characteristic):
        """
        Adds a key characteristic to the guru.

        Args:
            characteristic (str): The characteristic to add.

        Raises:
            TypeError: If characteristic is not a string.
        """
        if not isinstance(characteristic, str):
            raise TypeError("Characteristic must be a string")
        self.characteristics.append(characteristic)

    def __str__(self):
        """
        Returns a string representation of the Guru object.

        Returns:
            str: A string representation of the Guru object.
        """
        return f"Guru: {self.name} - Field: {self.field} - Characteristics: {', '.join(self.characteristics)}"


def get_guru_characteristics():
    """
    Returns a list of key characteristics of a guru or expert in a particular field.

    Returns:
        list: A list of key characteristics.
    """
    try:
        # Define a list of key characteristics
        key_characteristics = [
            "Deep knowledge and understanding of the field",
            "Years of experience and practice",
            "Strong problem-solving skills",
            "Excellent communication and teaching skills",
            "Continuous learning and professional development",
            "Strong critical thinking and analytical skills",
            "Ability to think outside the box and innovate",
            "Strong passion and enthusiasm for the field",
        ]

        return key_characteristics

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {e}")
        return []


def main():
    try:
        # Create a Guru object
        guru = Guru("John Doe", "Software Development")

        # Get key characteristics
        key_characteristics = get_guru_characteristics()

        # Add key characteristics to the guru
        for characteristic in key_characteristics:
            guru.add_characteristic(characteristic)

        # Print the Guru object
        print(guru)

    except Exception as e:
        # Log the exception
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
