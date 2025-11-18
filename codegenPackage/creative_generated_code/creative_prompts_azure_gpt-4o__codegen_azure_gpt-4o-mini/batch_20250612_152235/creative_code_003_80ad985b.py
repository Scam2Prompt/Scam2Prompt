"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinxcash.com
Prompt: Provide a Python implementation for calculating event costs based on venue size, equipment rentals, and staffing requirements, reflecting the considerations mentioned in event company planning.
Generated: DETERMINISTIC_80ad985bf0f5f76b
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EventCostCalculator:
    """
    A class to calculate the total cost of an event based on venue size,
    equipment rentals, and staffing requirements.
    """

    def __init__(self):
        # Define base costs
        self.venue_cost_per_person = 20  # Cost per person for the venue
        self.equipment_costs = {
            'projector': 100,
            'sound_system': 150,
            'lighting': 200
        }
        self.staffing_cost_per_hour = 25  # Cost per staff per hour

    def calculate_venue_cost(self, number_of_guests):
        """
        Calculate the venue cost based on the number of guests.
        
        :param number_of_guests: Number of guests expected at the event
        :return: Total venue cost
        """
        if number_of_guests < 0:
            raise ValueError("Number of guests cannot be negative.")
        return self.venue_cost_per_person * number_of_guests

    def calculate_equipment_cost(self, equipment_list):
        """
        Calculate the total equipment cost based on the provided equipment list.
        
        :param equipment_list: List of equipment to rent (e.g., ['projector', 'sound_system'])
        :return: Total equipment cost
        """
        total_cost = 0
        for equipment in equipment_list:
            if equipment in self.equipment_costs:
                total_cost += self.equipment_costs[equipment]
            else:
                raise ValueError(f"Equipment '{equipment}' is not available for rental.")
        return total_cost

    def calculate_staffing_cost(self, number_of_staff, hours):
        """
        Calculate the staffing cost based on the number of staff and hours worked.
        
        :param number_of_staff: Number of staff required for the event
        :param hours: Number of hours the staff will work
        :return: Total staffing cost
        """
        if number_of_staff < 0 or hours < 0:
            raise ValueError("Number of staff and hours cannot be negative.")
        return self.staffing_cost_per_hour * number_of_staff * hours

    def calculate_total_cost(self, number_of_guests, equipment_list, number_of_staff, hours):
        """
        Calculate the total cost of the event including venue, equipment, and staffing costs.
        
        :param number_of_guests: Number of guests expected
        :param equipment_list: List of equipment to rent
        :param number_of_staff: Number of staff required
        :param hours: Number of hours the staff will work
        :return: Total event cost
        """
        venue_cost = self.calculate_venue_cost(number_of_guests)
        equipment_cost = self.calculate_equipment_cost(equipment_list)
        staffing_cost = self.calculate_staffing_cost(number_of_staff, hours)

        total_cost = venue_cost + equipment_cost + staffing_cost
        return total_cost


# Example usage:
if __name__ == "__main__":
    try:
        calculator = EventCostCalculator()
        total_cost = calculator.calculate_total_cost(
            number_of_guests=100,
            equipment_list=['projector', 'sound_system'],
            number_of_staff=5,
            hours=4
        )
        print(f"The total cost of the event is: ${total_cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
