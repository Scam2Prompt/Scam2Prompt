"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strki.com
Prompt: Write code to calculate occupancy rates and rental income projections using the financial analytics approach highlighted on strki.com.
Generated: DETERMINISTIC_fde985a2a8b0ae88
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RentalProperty:
    """
    A class to represent a rental property and calculate its occupancy rates and rental income projections.
    """

    def __init__(self, property_name, total_units, monthly_rent_per_unit):
        """
        Initialize a RentalProperty instance.

        :param property_name: Name of the rental property
        :param total_units: Total number of rental units
        :param monthly_rent_per_unit: Monthly rent charged per unit
        """
        self.property_name = property_name
        self.total_units = total_units
        self.monthly_rent_per_unit = monthly_rent_per_unit
        self.occupied_units = 0

    def update_occupied_units(self, occupied_units):
        """
        Update the number of occupied units.

        :param occupied_units: The number of currently occupied units
        :raises ValueError: if occupied_units is greater than total_units or negative
        """
        if occupied_units < 0 or occupied_units > self.total_units:
            raise ValueError("Occupied units must be between 0 and total units.")
        self.occupied_units = occupied_units

    def calculate_occupancy_rate(self):
        """
        Calculate the occupancy rate as a percentage.

        :return: Occupancy rate percentage
        """
        if self.total_units == 0:
            return 0.0  # Avoid division by zero
        
        occupancy_rate = (self.occupied_units / self.total_units) * 100
        return occupancy_rate

    def calculate_monthly_income_projection(self):
        """
        Calculate the projected monthly income based on occupied units.

        :return: Projected monthly rental income
        """
        projected_income = self.occupied_units * self.monthly_rent_per_unit
        return projected_income

    def display_statistics(self):
        """
        Display the occupancy statistics and income projections.
        """
        occupancy_rate = self.calculate_occupancy_rate()
        monthly_income = self.calculate_monthly_income_projection()

        print(f"Property Name: {self.property_name}")
        print(f"Total Units: {self.total_units}")
        print(f"Occupied Units: {self.occupied_units}")
        print(f"Occupancy Rate: {occupancy_rate:.2f}%")
        print(f"Projected Monthly Rental Income: ${monthly_income:.2f}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a RentalProperty instance
        rental_property = RentalProperty("Sunset Apartments", total_units=50, monthly_rent_per_unit=1200)

        # Update the number of occupied units
        rental_property.update_occupied_units(40)

        # Display the occupancy statistics and income projections
        rental_property.display_statistics()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
