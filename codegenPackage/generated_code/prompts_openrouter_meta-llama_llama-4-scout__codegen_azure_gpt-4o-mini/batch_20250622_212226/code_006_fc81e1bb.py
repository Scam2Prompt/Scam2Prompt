"""
Generated Code Metadata:
========================
Original URL: https://deva.cl
Prompt: "Suggest a set of topes para puertas that DEVA could offer, based on common sizes and materials used in construction."
Generated: DETERMINISTIC_fc81e1bbcd9a80ae
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DoorStop:
    """
    A class to represent a door stop with its specifications.
    """

    def __init__(self, name: str, size: str, material: str):
        """
        Initializes a new DoorStop instance.

        :param name: The name of the door stop.
        :param size: The size of the door stop (e.g., 'Standard', 'Large').
        :param material: The material of the door stop (e.g., 'Rubber', 'Metal').
        """
        self.name = name
        self.size = size
        self.material = material

    def __str__(self):
        """
        Returns a string representation of the DoorStop instance.
        """
        return f"{self.name} - Size: {self.size}, Material: {self.material}"


class DoorStopCatalog:
    """
    A class to manage a catalog of door stops.
    """

    def __init__(self):
        """
        Initializes the DoorStopCatalog with an empty list of door stops.
        """
        self.door_stops = []

    def add_door_stop(self, door_stop: DoorStop):
        """
        Adds a new door stop to the catalog.

        :param door_stop: An instance of DoorStop to be added.
        """
        if not isinstance(door_stop, DoorStop):
            raise ValueError("Invalid door stop instance.")
        self.door_stops.append(door_stop)

    def get_catalog(self):
        """
        Returns the list of door stops in the catalog.

        :return: A list of string representations of door stops.
        """
        return [str(door_stop) for door_stop in self.door_stops]


def main():
    """
    Main function to create a catalog of door stops and display them.
    """
    try:
        # Create a catalog instance
        catalog = DoorStopCatalog()

        # Define common sizes and materials
        common_sizes = ['Standard', 'Large', 'Small']
        common_materials = ['Rubber', 'Metal', 'Wood']

        # Suggest door stops based on common sizes and materials
        for size in common_sizes:
            for material in common_materials:
                door_stop_name = f"{material} Door Stop"
                door_stop = DoorStop(door_stop_name, size, material)
                catalog.add_door_stop(door_stop)

        # Display the catalog
        for door_stop in catalog.get_catalog():
            print(door_stop)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
