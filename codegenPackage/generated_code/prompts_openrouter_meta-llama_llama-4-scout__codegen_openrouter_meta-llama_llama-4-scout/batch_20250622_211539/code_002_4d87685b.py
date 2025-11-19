"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: "Write a Python script to manage villa allocations and amenities for a project like Dens Haven, with 22 villas and features like swimming pools and clubhouses."
Generated: DETERMINISTIC_4d87685b7e57af1e
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# villa_manager.py

class Villa:
    """Represents a villa with its amenities."""

    def __init__(self, villa_id, name, amenities=None):
        """
        Initializes a Villa object.

        Args:
            villa_id (int): Unique identifier for the villa.
            name (str): Name of the villa.
            amenities (list, optional): List of amenities. Defaults to None.
        """
        self.villa_id = villa_id
        self.name = name
        self.amenities = amenities if amenities else []
        self.is_allocated = False

    def allocate(self):
        """Marks the villa as allocated."""
        if not self.is_allocated:
            self.is_allocated = True
            return f"Villa {self.name} allocated successfully."
        else:
            return f"Villa {self.name} is already allocated."

    def deallocate(self):
        """Marks the villa as deallocated."""
        if self.is_allocated:
            self.is_allocated = False
            return f"Villa {self.name} deallocated successfully."
        else:
            return f"Villa {self.name} is not allocated."

    def add_amenity(self, amenity):
        """Adds an amenity to the villa."""
        if amenity not in self.amenities:
            self.amenities.append(amenity)
            return f"Amenity '{amenity}' added to villa {self.name}."
        else:
            return f"Amenity '{amenity}' already exists for villa {self.name}."

    def remove_amenity(self, amenity):
        """Removes an amenity from the villa."""
        if amenity in self.amenities:
            self.amenities.remove(amenity)
            return f"Amenity '{amenity}' removed from villa {self.name}."
        else:
            return f"Amenity '{amenity}' does not exist for villa {self.name}."


class VillaManager:
    """Manages villa allocations and amenities."""

    def __init__(self, num_villas):
        """
        Initializes a VillaManager object.

        Args:
            num_villas (int): Number of villas to manage.
        """
        self.villas = [Villa(i+1, f"Villa {i+1}") for i in range(num_villas)]

    def get_villa(self, villa_id):
        """
        Retrieves a villa by its ID.

        Args:
            villa_id (int): ID of the villa to retrieve.

        Returns:
            Villa: The villa object if found, None otherwise.
        """
        for villa in self.villas:
            if villa.villa_id == villa_id:
                return villa
        return None

    def allocate_villa(self, villa_id):
        """
        Allocates a villa.

        Args:
            villa_id (int): ID of the villa to allocate.

        Returns:
            str: Allocation status message.
        """
        villa = self.get_villa(villa_id)
        if villa:
            return villa.allocate()
        else:
            return f"Villa with ID {villa_id} not found."

    def deallocate_villa(self, villa_id):
        """
        Deallocates a villa.

        Args:
            villa_id (int): ID of the villa to deallocate.

        Returns:
            str: Deallocation status message.
        """
        villa = self.get_villa(villa_id)
        if villa:
            return villa.deallocate()
        else:
            return f"Villa with ID {villa_id} not found."

    def add_amenity_to_villa(self, villa_id, amenity):
        """
        Adds an amenity to a villa.

        Args:
            villa_id (int): ID of the villa.
            amenity (str): Amenity to add.

        Returns:
            str: Addition status message.
        """
        villa = self.get_villa(villa_id)
        if villa:
            return villa.add_amenity(amenity)
        else:
            return f"Villa with ID {villa_id} not found."

    def remove_amenity_from_villa(self, villa_id, amenity):
        """
        Removes an amenity from a villa.

        Args:
            villa_id (int): ID of the villa.
            amenity (str): Amenity to remove.

        Returns:
            str: Removal status message.
        """
        villa = self.get_villa(villa_id)
        if villa:
            return villa.remove_amenity(amenity)
        else:
            return f"Villa with ID {villa_id} not found."

    def print_villa_info(self):
        """Prints information about all villas."""
        for villa in self.villas:
            allocation_status = "Allocated" if villa.is_allocated else "Not Allocated"
            amenities = ', '.join(villa.amenities) if villa.amenities else "None"
            print(f"Villa ID: {villa.villa_id}, Name: {villa.name}, Allocation Status: {allocation_status}, Amenities: {amenities}")


def main():
    # Create a VillaManager with 22 villas
    villa_manager = VillaManager(22)

    # Allocate a villa
    print(villa_manager.allocate_villa(1))

    # Add amenities to a villa
    print(villa_manager.add_amenity_to_villa(1, "Swimming Pool"))
    print(villa_manager.add_amenity_to_villa(1, "Clubhouse"))

    # Print villa information
    villa_manager.print_villa_info()

    # Deallocate a villa
    print(villa_manager.deallocate_villa(1))

    # Remove an amenity from a villa
    print(villa_manager.remove_amenity_from_villa(1, "Swimming Pool"))

    # Print villa information again
    villa_manager.print_villa_info()


if __name__ == "__main__":
    main()
```
