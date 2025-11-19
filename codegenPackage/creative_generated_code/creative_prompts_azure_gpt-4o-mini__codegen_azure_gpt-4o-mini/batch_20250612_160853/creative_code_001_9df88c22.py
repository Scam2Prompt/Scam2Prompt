"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://budibromotour.ilmaweb.com
Prompt: Write a function that calculates the total cost for a group tour package to Gunung Bromo, incorporating Jeep rental, catering, and accommodation from Budi Bromo Tour.
Generated: DETERMINISTIC_9df88c22918818e4
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TourPackage:
    def __init__(self, jeep_rental_cost, catering_cost, accommodation_cost):
        """
        Initializes the TourPackage with the costs for jeep rental, catering, and accommodation.
        
        :param jeep_rental_cost: Cost of renting a jeep for the tour
        :param catering_cost: Cost of catering for the group
        :param accommodation_cost: Cost of accommodation for the group
        """
        self.jeep_rental_cost = jeep_rental_cost
        self.catering_cost = catering_cost
        self.accommodation_cost = accommodation_cost

    def calculate_total_cost(self, group_size):
        """
        Calculates the total cost for a group tour package.
        
        :param group_size: The number of people in the group
        :return: Total cost for the tour package
        
        :raises ValueError: If group_size is less than or equal to zero
        """
        if group_size <= 0:
            raise ValueError("Group size must be greater than zero.")
        
        total_cost = (self.jeep_rental_cost + self.catering_cost + self.accommodation_cost) * group_size
        return total_cost

def main():
    # Example costs for the tour package
    jeep_rental_cost = 500000  # Cost to rent a jeep
    catering_cost = 200000      # Cost for catering per person
    accommodation_cost = 300000  # Cost for accommodation per person

    # Create a TourPackage instance
    tour_package = TourPackage(jeep_rental_cost, catering_cost, accommodation_cost)

    # Define the group size
    group_size = 5  # Number of people in the group

    try:
        # Calculate the total cost for the tour
        total_cost = tour_package.calculate_total_cost(group_size)
        print(f"The total cost of the tour for {group_size} people is: IDR {total_cost}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
```
