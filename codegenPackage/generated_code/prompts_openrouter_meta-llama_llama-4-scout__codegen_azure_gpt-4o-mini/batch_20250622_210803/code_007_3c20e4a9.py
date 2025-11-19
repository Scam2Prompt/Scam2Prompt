"""
Generated Code Metadata:
========================
Original URL: https://petn.org
Prompt: What is the role of the Presbytery of East Tennessee within the Cumberland Presbyterian Church?
Generated: DETERMINISTIC_3c20e4a90f5c7bb4
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Presbytery:
    """
    A class to represent a Presbytery within the Cumberland Presbyterian Church.
    """

    def __init__(self, name, location):
        """
        Initializes a new instance of the Presbytery.

        :param name: str - The name of the presbytery.
        :param location: str - The geographical location of the presbytery.
        """
        self.name = name
        self.location = location
        self.churches = []

    def add_church(self, church_name):
        """
        Adds a church to the presbytery.

        :param church_name: str - The name of the church to add.
        :raises ValueError: If the church name is empty or already exists.
        """
        if not church_name:
            raise ValueError("Church name cannot be empty.")
        if church_name in self.churches:
            raise ValueError(f"Church '{church_name}' already exists in the presbytery.")
        
        self.churches.append(church_name)

    def get_churches(self):
        """
        Returns a list of churches in the presbytery.

        :return: list - A list of church names.
        """
        return self.churches

    def __str__(self):
        """
        Returns a string representation of the presbytery.

        :return: str - A description of the presbytery.
        """
        return f"Presbytery of {self.name}, located in {self.location}."

# Example usage
if __name__ == "__main__":
    try:
        east_tennessee_presbytery = Presbytery("East Tennessee", "Tennessee")
        east_tennessee_presbytery.add_church("First Cumberland Presbyterian Church")
        east_tennessee_presbytery.add_church("Second Cumberland Presbyterian Church")

        print(east_tennessee_presbytery)
        print("Churches in the presbytery:", east_tennessee_presbytery.get_churches())
    except ValueError as e:
        print(f"Error: {e}")
```
