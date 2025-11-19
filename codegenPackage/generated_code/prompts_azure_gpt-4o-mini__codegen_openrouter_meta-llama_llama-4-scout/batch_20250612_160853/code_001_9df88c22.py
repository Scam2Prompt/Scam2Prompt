"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.ilmaweb.com
Prompt: Write a function that calculates the total cost for a group tour package to Gunung Bromo, incorporating Jeep rental, catering, and accommodation from Budi Bromo Tour.
Generated: DETERMINISTIC_9df88c22918818e4
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GunungBromoTourPackage:
    """
    Represents a group tour package to Gunung Bromo.

    Attributes:
        jeep_rental_cost (float): The cost of Jeep rental per person.
        catering_cost (float): The cost of catering per person.
        accommodation_cost (float): The cost of accommodation per person.
        num_participants (int): The number of participants in the tour.
    """

    def __init__(self, jeep_rental_cost, catering_cost, accommodation_cost, num_participants):
        """
        Initializes a GunungBromoTourPackage.

        Args:
            jeep_rental_cost (float): The cost of Jeep rental per person.
            catering_cost (float): The cost of catering per person.
            accommodation_cost (float): The cost of accommodation per person.
            num_participants (int): The number of participants in the tour.

        Raises:
            ValueError: If the number of participants is not a positive integer.
            TypeError: If the costs are not numbers.
        """
        if not isinstance(jeep_rental_cost, (int, float)) or not isinstance(catering_cost, (int, float)) or not isinstance(accommodation_cost, (int, float)):
            raise TypeError("Costs must be numbers")
        if not isinstance(num_participants, int) or num_participants <= 0:
            raise ValueError("Number of participants must be a positive integer")

        self.jeep_rental_cost = jeep_rental_cost
        self.catering_cost = catering_cost
        self.accommodation_cost = accommodation_cost
        self.num_participants = num_participants

    def calculate_total_cost(self):
        """
        Calculates the total cost for the tour package.

        Returns:
            float: The total cost for the tour package.
        """
        # Calculate the total cost by summing up the individual costs per person and multiplying by the number of participants
        total_cost = (self.jeep_rental_cost + self.catering_cost + self.accommodation_cost) * self.num_participants
        return total_cost


class BudiBromoTour:
    """
    Represents Budi Bromo Tour's packages.

    Attributes:
        package_name (str): The name of the package.
    """

    def __init__(self, package_name):
        """
        Initializes a BudiBromoTour.

        Args:
            package_name (str): The name of the package.
        """
        self.package_name = package_name

    def get_package_details(self):
        """
        Returns the package details.

        Returns:
            dict: A dictionary containing the package details.
        """
        # For demonstration purposes, assume we have the following package details
        package_details = {
            "Budi Bromo Tour Package": {
                "jeep_rental_cost": 150000,  # in IDR
                "catering_cost": 50000,      # in IDR
                "accommodation_cost": 200000 # in IDR
            }
        }
        return package_details.get(self.package_name, {})


def main():
    try:
        # Create a Budi Bromo Tour package
        budi_bromo_tour = BudiBromoTour("Budi Bromo Tour Package")
        package_details = budi_bromo_tour.get_package_details()

        if package_details:
            # Create a Gunung Bromo tour package
            gunung_bromo_tour_package = GunungBromoTourPackage(
                jeep_rental_cost=package_details["jeep_rental_cost"],
                catering_cost=package_details["catering_cost"],
                accommodation_cost=package_details["accommodation_cost"],
                num_participants=10
            )

            # Calculate the total cost
            total_cost = gunung_bromo_tour_package.calculate_total_cost()
            print(f"Total cost for {gunung_bromo_tour_package.num_participants} participants: IDR {total_cost}")
        else:
            print("Package details not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
