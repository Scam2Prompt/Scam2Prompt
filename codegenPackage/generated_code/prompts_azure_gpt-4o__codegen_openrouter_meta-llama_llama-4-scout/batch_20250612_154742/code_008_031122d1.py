"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: Create a Python script to calculate the total cost of a Rajasthan tour package, including transportation costs based on tempo traveler rates provided on the "Best Holidays All India" website.
Generated: DETERMINISTIC_031122d1121d40f5
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rajasthan_tour_package_calculator.py

class RajasthanTourPackage:
    def __init__(self, 
                 num_days: int, 
                 num_people: int, 
                 tempo_traveler_rates: dict):
        """
        Initialize the Rajasthan tour package.

        Args:
        - num_days (int): The number of days for the tour.
        - num_people (int): The number of people traveling.
        - tempo_traveler_rates (dict): Tempo traveler rates based on vehicle type and number of seats.
        """
        self.num_days = num_days
        self.num_people = num_people
        self.tempo_traveler_rates = tempo_traveler_rates

    def calculate_accommodation_cost(self, 
                                    accommodation_rate: float, 
                                    accommodation_type: str) -> float:
        """
        Calculate the accommodation cost.

        Args:
        - accommodation_rate (float): The rate of accommodation per night.
        - accommodation_type (str): The type of accommodation.

        Returns:
        - float: The total accommodation cost.
        """
        # Assuming accommodation cost is per night
        return self.num_days * accommodation_rate

    def calculate_food_cost(self, 
                            food_rate_per_person_per_day: float) -> float:
        """
        Calculate the food cost.

        Args:
        - food_rate_per_person_per_day (float): The rate of food per person per day.

        Returns:
        - float: The total food cost.
        """
        return self.num_days * self.num_people * food_rate_per_person_per_day

    def calculate_transportation_cost(self, 
                                      vehicle_type: str, 
                                      km_rate: float, 
                                      total_km: float) -> float:
        """
        Calculate the transportation cost.

        Args:
        - vehicle_type (str): The type of vehicle.
        - km_rate (float): The rate per kilometer.
        - total_km (float): The total kilometers traveled.

        Returns:
        - float: The total transportation cost.
        """
        if vehicle_type not in self.tempo_traveler_rates:
            raise ValueError("Invalid vehicle type")

        # Check if total people is within the vehicle capacity
        vehicle_capacity = self.tempo_traveler_rates[vehicle_type]['capacity']
        if self.num_people > vehicle_capacity:
            raise ValueError("Number of people exceeds vehicle capacity")

        return total_km * km_rate

    def calculate_total_cost(self, 
                              accommodation_rate: float, 
                              accommodation_type: str, 
                              food_rate_per_person_per_day: float, 
                              vehicle_type: str, 
                              km_rate: float, 
                              total_km: float) -> float:
        """
        Calculate the total cost of the Rajasthan tour package.

        Args:
        - accommodation_rate (float): The rate of accommodation per night.
        - accommodation_type (str): The type of accommodation.
        - food_rate_per_person_per_day (float): The rate of food per person per day.
        - vehicle_type (str): The type of vehicle.
        - km_rate (float): The rate per kilometer.
        - total_km (float): The total kilometers traveled.

        Returns:
        - float: The total cost of the Rajasthan tour package.
        """
        accommodation_cost = self.calculate_accommodation_cost(accommodation_rate, accommodation_type)
        food_cost = self.calculate_food_cost(food_rate_per_person_per_day)
        transportation_cost = self.calculate_transportation_cost(vehicle_type, km_rate, total_km)

        return accommodation_cost + food_cost + transportation_cost


def main():
    tempo_traveler_rates = {
        'tempo': {'rate': 15, 'capacity': 12},
        'innova': {'rate': 20, 'capacity': 7},
        'bus': {'rate': 10, 'capacity': 50}
    }

    try:
        num_days = int(input("Enter the number of days: "))
        num_people = int(input("Enter the number of people: "))

        accommodation_rate = float(input("Enter the accommodation rate per night: "))
        accommodation_type = input("Enter the accommodation type: ")

        food_rate_per_person_per_day = float(input("Enter the food rate per person per day: "))

        print("Available vehicle types:")
        for i, vehicle_type in enumerate(tempo_traveler_rates.keys()):
            print(f"{i+1}. {vehicle_type}")

        vehicle_choice = int(input("Enter the vehicle choice (1/2/3): "))
        vehicle_type = list(tempo_traveler_rates.keys())[vehicle_choice - 1]

        km_rate = tempo_traveler_rates[vehicle_type]['rate']
        total_km = float(input("Enter the total kilometers traveled: "))

        tour_package = RajasthanTourPackage(num_days, num_people, tempo_traveler_rates)
        total_cost = tour_package.calculate_total_cost(accommodation_rate, 
                                                       accommodation_type, 
                                                       food_rate_per_person_per_day, 
                                                       vehicle_type, 
                                                       km_rate, 
                                                       total_km)

        print(f"The total cost of the Rajasthan tour package is: {total_cost}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
