"""
Generated Code Metadata:
========================
Original URL: https://bigtimecodes.pages.dev
Prompt: Generate code for a simple game instance rental system, where players can rent out workshops and space in a game like Big Time.
Generated: DETERMINISTIC_65e1b091399b0de5
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Workshop:
    """Represents a workshop that can be rented by players."""
    
    def __init__(self, name, hourly_rate):
        """
        Initializes a new workshop instance.

        Args:
            name (str): The name of the workshop.
            hourly_rate (float): The rental rate per hour.
        """
        self.name = name
        self.hourly_rate = hourly_rate
        self.is_rented = False
        self.current_renter = None

    def rent(self, player_name):
        """
        Rents the workshop to a player.

        Args:
            player_name (str): The name of the player renting the workshop.

        Raises:
            ValueError: If the workshop is already rented.
        """
        if self.is_rented:
            raise ValueError(f"{self.name} is already rented.")
        self.is_rented = True
        self.current_renter = player_name

    def return_workshop(self):
        """Returns the workshop, making it available for rent again."""
        if not self.is_rented:
            raise ValueError(f"{self.name} is not currently rented.")
        self.is_rented = False
        self.current_renter = None

    def calculate_rental_cost(self, hours):
        """
        Calculates the total rental cost for a given number of hours.

        Args:
            hours (int): The number of hours the workshop is rented for.

        Returns:
            float: The total rental cost.

        Raises:
            ValueError: If hours is not a positive integer.
        """
        if hours <= 0:
            raise ValueError("Hours must be a positive integer.")
        return hours * self.hourly_rate


class RentalSystem:
    """Manages the rental of workshops in the game."""

    def __init__(self):
        """Initializes the rental system with an empty list of workshops."""
        self.workshops = []

    def add_workshop(self, workshop):
        """
        Adds a workshop to the rental system.

        Args:
            workshop (Workshop): The workshop to add.
        """
        self.workshops.append(workshop)

    def rent_workshop(self, workshop_name, player_name):
        """
        Rents a workshop to a player.

        Args:
            workshop_name (str): The name of the workshop to rent.
            player_name (str): The name of the player renting the workshop.

        Raises:
            ValueError: If the workshop is not found or is already rented.
        """
        workshop = self._find_workshop(workshop_name)
        workshop.rent(player_name)

    def return_workshop(self, workshop_name):
        """
        Returns a rented workshop.

        Args:
            workshop_name (str): The name of the workshop to return.

        Raises:
            ValueError: If the workshop is not found or is not currently rented.
        """
        workshop = self._find_workshop(workshop_name)
        workshop.return_workshop()

    def calculate_cost(self, workshop_name, hours):
        """
        Calculates the rental cost for a workshop.

        Args:
            workshop_name (str): The name of the workshop.
            hours (int): The number of hours to calculate the cost for.

        Returns:
            float: The total rental cost.

        Raises:
            ValueError: If the workshop is not found or if hours is not valid.
        """
        workshop = self._find_workshop(workshop_name)
        return workshop.calculate_rental_cost(hours)

    def _find_workshop(self, workshop_name):
        """
        Finds a workshop by name.

        Args:
            workshop_name (str): The name of the workshop to find.

        Returns:
            Workshop: The found workshop.

        Raises:
            ValueError: If the workshop is not found.
        """
        for workshop in self.workshops:
            if workshop.name == workshop_name:
                return workshop
        raise ValueError(f"Workshop '{workshop_name}' not found.")


# Example usage
if __name__ == "__main__":
    # Create a rental system
    rental_system = RentalSystem()

    # Add workshops to the system
    rental_system.add_workshop(Workshop("Art Studio", 20.0))
    rental_system.add_workshop(Workshop("Blacksmith Forge", 30.0))

    # Rent a workshop
    try:
        rental_system.rent_workshop("Art Studio", "Player1")
        print("Art Studio rented successfully.")
    except ValueError as e:
        print(e)

    # Calculate rental cost
    try:
        cost = rental_system.calculate_cost("Art Studio", 5)
        print(f"Total rental cost for 5 hours: ${cost:.2f}")
    except ValueError as e:
        print(e)

    # Return the workshop
    try:
        rental_system.return_workshop("Art Studio")
        print("Art Studio returned successfully.")
    except ValueError as e:
        print(e)
```
