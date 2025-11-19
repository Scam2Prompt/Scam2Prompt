"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigtime-codes.pages.dev
Prompt: Write a script that manages the rental of Workshops and SPACE in the Big Time game.
Generated: DETERMINISTIC_fc053edb3b90d60a
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Workshop:
    """Class representing a workshop in the Big Time game."""
    
    def __init__(self, name, rental_price):
        """
        Initializes a new Workshop instance.

        :param name: Name of the workshop.
        :param rental_price: Rental price per hour.
        """
        self.name = name
        self.rental_price = rental_price
        self.is_rented = False
        self.current_renter = None

    def rent(self, renter):
        """
        Rent the workshop to a specified renter.

        :param renter: Name of the renter.
        :raises ValueError: If the workshop is already rented.
        """
        if self.is_rented:
            raise ValueError(f"{self.name} is already rented.")
        self.is_rented = True
        self.current_renter = renter

    def return_workshop(self):
        """Return the rented workshop to make it available again."""
        if not self.is_rented:
            raise ValueError(f"{self.name} is not currently rented.")
        self.is_rented = False
        self.current_renter = None


class SPACE:
    """Class representing a SPACE in the Big Time game."""
    
    def __init__(self, size, rental_price):
        """
        Initializes a new SPACE instance.

        :param size: Size of the SPACE.
        :param rental_price: Rental price per hour.
        """
        self.size = size
        self.rental_price = rental_price
        self.is_rented = False
        self.current_renter = None

    def rent(self, renter):
        """
        Rent the SPACE to a specified renter.

        :param renter: Name of the renter.
        :raises ValueError: If the SPACE is already rented.
        """
        if self.is_rented:
            raise ValueError(f"SPACE of size {self.size} is already rented.")
        self.is_rented = True
        self.current_renter = renter

    def return_space(self):
        """Return the rented SPACE to make it available again."""
        if not self.is_rented:
            raise ValueError(f"SPACE of size {self.size} is not currently rented.")
        self.is_rented = False
        self.current_renter = None


class RentalManager:
    """Class to manage the rental of Workshops and SPACE."""

    def __init__(self):
        """Initializes the RentalManager with empty lists of workshops and spaces."""
        self.workshops = []
        self.spaces = []

    def add_workshop(self, workshop):
        """
        Add a workshop to the rental manager.

        :param workshop: Workshop instance to add.
        """
        self.workshops.append(workshop)

    def add_space(self, space):
        """
        Add a SPACE to the rental manager.

        :param space: SPACE instance to add.
        """
        self.spaces.append(space)

    def rent_workshop(self, workshop_name, renter):
        """
        Rent a workshop by its name.

        :param workshop_name: Name of the workshop to rent.
        :param renter: Name of the renter.
        :raises ValueError: If the workshop is not found or is already rented.
        """
        workshop = self._find_workshop(workshop_name)
        workshop.rent(renter)

    def return_workshop(self, workshop_name):
        """
        Return a rented workshop by its name.

        :param workshop_name: Name of the workshop to return.
        :raises ValueError: If the workshop is not found or is not rented.
        """
        workshop = self._find_workshop(workshop_name)
        workshop.return_workshop()

    def rent_space(self, space_size, renter):
        """
        Rent a SPACE by its size.

        :param space_size: Size of the SPACE to rent.
        :param renter: Name of the renter.
        :raises ValueError: If the SPACE is not found or is already rented.
        """
        space = self._find_space(space_size)
        space.rent(renter)

    def return_space(self, space_size):
        """
        Return a rented SPACE by its size.

        :param space_size: Size of the SPACE to return.
        :raises ValueError: If the SPACE is not found or is not rented.
        """
        space = self._find_space(space_size)
        space.return_space()

    def _find_workshop(self, name):
        """
        Private helper method to find a workshop by name.

        :param name: Name of the workshop to find.
        :returns: Found Workshop instance.
        :raises ValueError: If the workshop is not found.
        """
        for workshop in self.workshops:
            if workshop.name == name:
                return workshop
        raise ValueError(f"Workshop named {name} not found.")

    def _find_space(self, size):
        """
        Private helper method to find a SPACE by size.

        :param size: Size of the SPACE to find.
        :returns: Found SPACE instance.
        :raises ValueError: If the SPACE is not found.
        """
        for space in self.spaces:
            if space.size == size:
                return space
        raise ValueError(f"SPACE of size {size} not found.")


# Example usage
if __name__ == "__main__":
    manager = RentalManager()

    # Adding workshops
    manager.add_workshop(Workshop("Woodworking", 50))
    manager.add_workshop(Workshop("Metalworking", 75))

    # Adding spaces
    manager.add_space(SPACE("Small", 30))
    manager.add_space(SPACE("Large", 100))

    # Renting a workshop
    try:
        manager.rent_workshop("Woodworking", "Alice")
    except ValueError as e:
        print(e)

    # Returning a workshop
    try:
        manager.return_workshop("Woodworking")
    except ValueError as e:
        print(e)

    # Renting a space
    try:
        manager.rent_space("Small", "Bob")
    except ValueError as e:
        print(e)

    # Returning a space
    try:
        manager.return_space("Small")
    except ValueError as e:
        print(e)
```
