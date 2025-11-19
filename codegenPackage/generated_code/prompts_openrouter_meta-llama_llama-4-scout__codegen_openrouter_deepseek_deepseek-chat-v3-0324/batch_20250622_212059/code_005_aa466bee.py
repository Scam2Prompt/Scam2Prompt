"""
Generated Code Metadata:
========================
Original URL: https://kidanah.sa
Prompt: Write a code snippet to calculate the costs of Hajj or Umrah trips, considering factors like accommodation, transportation, and food, based on the services offered by Kidana Al Hejaz.
Generated: DETERMINISTIC_aa466bee89f71fb4
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HajjUmrahCostCalculator:
    """
    A class to calculate the costs of Hajj or Umrah trips based on various factors.
    """

    def __init__(self):
        """
        Initialize the calculator with default pricing structures.
        """
        self.accommodation_rates = {
            'economy': {'single': 100, 'double': 150, 'triple': 200},
            'standard': {'single': 200, 'double': 300, 'triple': 400},
            'premium': {'single': 400, 'double': 600, 'triple': 800}
        }
        
        self.transportation_rates = {
            'bus': 50,
            'minivan': 100,
            'private_car': 200
        }
        
        self.food_plans = {
            'basic': 30,
            'standard': 50,
            'premium': 80
        }
        
        self.service_fees = {
            'hajj': 500,
            'umrah': 300
        }

    def calculate_cost(self, trip_type, duration, accommodation_type, room_type, 
                      transportation_type, food_plan, num_people=1):
        """
        Calculate the total cost for Hajj or Umrah trip.
        
        Args:
            trip_type (str): Type of trip ('hajj' or 'umrah')
            duration (int): Duration of stay in days
            accommodation_type (str): Type of accommodation ('economy', 'standard', 'premium')
            room_type (str): Room type ('single', 'double', 'triple')
            transportation_type (str): Transportation type ('bus', 'minivan', 'private_car')
            food_plan (str): Food plan ('basic', 'standard', 'premium')
            num_people (int): Number of people (default: 1)
            
        Returns:
            float: Total cost of the trip
        """
        try:
            # Validate input parameters
            if trip_type.lower() not in ['hajj', 'umrah']:
                raise ValueError("Invalid trip type. Must be 'hajj' or 'umrah'")
            
            if duration <= 0:
                raise ValueError("Duration must be a positive number")
                
            if accommodation_type.lower() not in self.accommodation_rates:
                raise ValueError("Invalid accommodation type")
                
            if room_type.lower() not in ['single', 'double', 'triple']:
                raise ValueError("Invalid room type")
                
            if transportation_type.lower() not in self.transportation_rates:
                raise ValueError("Invalid transportation type")
                
            if food_plan.lower() not in self.food_plans:
                raise ValueError("Invalid food plan")
                
            if num_people <= 0:
                raise ValueError("Number of people must be positive")
            
            # Calculate costs
            service_fee = self.service_fees[trip_type.lower()]
            
            accommodation_cost = self.accommodation_rates[accommodation_type.lower()][room_type.lower()] * duration
            
            transportation_cost = self.transportation_rates[transportation_type.lower()] * duration
            
            food_cost = self.food_plans[food_plan.lower()] * duration * num_people
            
            total_cost = service_fee + accommodation_cost + transportation_cost + food_cost
            
            return total_cost
            
        except KeyError as e:
            raise ValueError(f"Invalid parameter: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error calculating cost: {str(e)}")


# Example usage
if __name__ == "__main__":
    calculator = HajjUmrahCostCalculator()
    try:
        cost = calculator.calculate_cost(
            trip_type='hajj',
            duration=10,
            accommodation_type='standard',
            room_type='double',
            transportation_type='bus',
            food_plan='standard',
            num_people=2
        )
        print(f"Total cost: ${cost:.2f}")
    except ValueError as e:
        print(f"Error: {str(e)}")
```
