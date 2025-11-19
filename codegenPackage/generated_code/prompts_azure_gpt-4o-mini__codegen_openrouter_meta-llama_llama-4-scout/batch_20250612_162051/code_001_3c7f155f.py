"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: Write a Python function that calculates the total cost for a family of four booking a VIP Desert Safari, including additional charges for quad biking and henna painting.
Generated: DETERMINISTIC_3c7f155f304d3b27
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# desert_safari_booking.py

class DesertSafariBooking:
    """
    Calculates the total cost for a family of four booking a VIP Desert Safari.
    """

    def __init__(self, 
                 base_cost: float = 1500.0, 
                 quad_biking_cost: float = 50.0, 
                 henna_painting_cost: float = 20.0):
        """
        Initializes the DesertSafariBooking with base costs.

        Args:
        - base_cost (float): The base cost for a family of four. Defaults to 1500.0.
        - quad_biking_cost (float): The cost for quad biking per person. Defaults to 50.0.
        - henna_painting_cost (float): The cost for henna painting per person. Defaults to 20.0.
        """
        self.base_cost = base_cost
        self.quad_biking_cost = quad_biking_cost
        self.henna_painting_cost = henna_painting_cost
        self.num_people = 4  # Default family size

    def calculate_total_cost(self, 
                             include_quad_biking: bool = False, 
                             include_henna_painting: bool = False) -> float:
        """
        Calculates the total cost for the desert safari booking.

        Args:
        - include_quad_biking (bool): Whether to include quad biking. Defaults to False.
        - include_henna_painting (bool): Whether to include henna painting. Defaults to False.

        Returns:
        - float: The total cost for the desert safari booking.

        Raises:
        - ValueError: If the number of people is not a positive integer.
        """
        if not isinstance(self.num_people, int) or self.num_people <= 0:
            raise ValueError("Number of people must be a positive integer.")

        total_cost = self.base_cost

        if include_quad_biking:
            total_cost += self.quad_biking_cost * self.num_people

        if include_henna_painting:
            total_cost += self.henna_painting_cost * self.num_people

        return total_cost


def main():
    try:
        booking = DesertSafariBooking()
        total_cost = booking.calculate_total_cost(include_quad_biking=True, include_henna_painting=True)
        print(f"Total cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
