"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a program to rent out Workshops and SPACE in Big Time, including a feature to calculate rental fees based on user-defined parameters.
Generated: DETERMINISTIC_c5509d7ca66b7c74
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Workshop:
    """
    A class to represent a workshop available for rent.
    
    Attributes
    ----------
    name : str
        The name of the workshop.
    base_rate : float
        The base rental rate per hour.
    capacity : int
        The maximum number of participants allowed in the workshop.
    """

    def __init__(self, name, base_rate, capacity):
        """
        Constructs all the necessary attributes for the workshop object.

        Parameters
        ----------
        name : str
            The name of the workshop.
        base_rate : float
            The base rental rate per hour.
        capacity : int
            The maximum number of participants allowed.
        """
        self.name = name
        self.base_rate = base_rate
        self.capacity = capacity

    def calculate_rental_fee(self, hours, participants):
        """
        Calculate the rental fee based on hours and number of participants.

        Parameters
        ----------
        hours : float
            Number of hours the workshop is rented for.
        participants : int
            Number of participants attending the workshop.

        Returns
        -------
        fee : float
            Total rental fee.
        """
        if hours <= 0 or participants <= 0:
            raise ValueError("Hours and participants must be greater than zero.")
        if participants > self.capacity:
            raise ValueError("Number of participants exceeds workshop capacity.")

        fee = self.base_rate * hours
        return fee


class Space:
    """
    A class to represent a space available for rent.

    Attributes
    ----------
    name : str
        The name of the space.
    base_rate : float
        The base rental rate per hour.
    size : float
        The size of the space in square meters.
    """

    def __init__(self, name, base_rate, size):
        """
        Constructs all the necessary attributes for the space object.

        Parameters
        ----------
        name : str
            The name of the space.
        base_rate : float
            The base rental rate per hour.
        size : float
            The size of the space in square meters.
        """
        self.name = name
        self.base_rate = base_rate
        self.size = size

    def calculate_rental_fee(self, hours):
        """
        Calculate the rental fee based on hours rented.

        Parameters
        ----------
        hours : float
            Number of hours the space is rented for.

        Returns
        -------
        fee : float
            Total rental fee.
        """
        if hours <= 0:
            raise ValueError("Hours must be greater than zero.")

        fee = self.base_rate * hours
        return fee


def main():
    """
    Main function to demonstrate the rental fee calculation for workshops and spaces.
    """
    try:
        # Create instances of Workshop and Space
        workshop = Workshop(name="Creative Writing Workshop", base_rate=50.0, capacity=20)
        space = Space(name="Conference Room A", base_rate=100.0, size=50.0)
        
        # Example rental calculations
        workshop_hours = 3
        workshop_participants = 15
        space_hours = 2

        # Calculate and print rental fees
        workshop_fee = workshop.calculate_rental_fee(workshop_hours, workshop_participants)
        print(f"Workshop Rental Fee: ${workshop_fee:.2f}")

        space_fee = space.calculate_rental_fee(space_hours)
        print(f"Space Rental Fee: ${space_fee:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
