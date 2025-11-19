"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Develop a function in Python that calculates the total cost for renting a luxury villa, taking into account amenities such as a jacuzzi and outdoor shower, as featured in Diamond Villa Corfu.
Generated: DETERMINISTIC_d921f7e1b09f2b87
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class VillaRental:
    """
    A class to represent a luxury villa rental and calculate the total cost based on selected amenities.
    """
    
    def __init__(self, base_rate: float):
        """
        Initializes the VillaRental with a base rental rate.

        :param base_rate: The base cost per night for renting the villa.
        """
        if base_rate <= 0:
            raise ValueError("Base rate must be a positive number.")
        self.base_rate = base_rate
        self.amenities_costs = {
            'jacuzzi': 50.0,  # Additional cost for jacuzzi
            'outdoor_shower': 30.0  # Additional cost for outdoor shower
        }

    def calculate_total_cost(self, nights: int, selected_amenities: list) -> float:
        """
        Calculates the total cost for renting the villa.

        :param nights: Number of nights the villa is rented.
        :param selected_amenities: List of selected amenities.
        :return: Total cost for the rental.
        """
        if nights <= 0:
            raise ValueError("Number of nights must be a positive integer.")
        
        # Calculate the cost for selected amenities
        amenities_cost = sum(self.amenities_costs.get(amenity, 0) for amenity in selected_amenities)
        
        # Calculate total cost
        total_cost = (self.base_rate * nights) + amenities_cost
        return total_cost

# Example usage
if __name__ == "__main__":
    try:
        villa = VillaRental(base_rate=200.0)  # Base rate of the villa per night
        nights = 5  # Number of nights for the rental
        selected_amenities = ['jacuzzi', 'outdoor_shower']  # Amenities selected

        total_cost = villa.calculate_total_cost(nights, selected_amenities)
        print(f"The total cost for renting the villa for {nights} nights "
              f"with selected amenities is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
