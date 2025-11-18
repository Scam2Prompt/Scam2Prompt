"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bilet-emirates.ru
Prompt: Create a function in Python to calculate Emirates Skywards loyalty points for a given flight itinerary, including partner airline flights, and simulate the registration process for the program.
Generated: DETERMINISTIC_eb1c9ee16a9a3f3d
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EmiratesSkywards:
    """
    A class to represent the Emirates Skywards loyalty program.
    """
    
    def __init__(self):
        self.members = {}
    
    def register_member(self, name: str, email: str) -> str:
        """
        Registers a new member in the Emirates Skywards program.

        :param name: The name of the member.
        :param email: The email of the member.
        :return: A success message indicating registration status.
        """
        if email in self.members:
            raise ValueError("Member with this email already registered.")
        
        self.members[email] = {"name": name, "points": 0}
        return f"Member {name} registered successfully with email {email}."

    def calculate_points(self, flights: list) -> int:
        """
        Calculates Emirates Skywards loyalty points for a given flight itinerary.

        :param flights: A list of dictionaries representing flights.
                        Each flight should have 'distance' and 'partner' keys.
        :return: Total loyalty points earned from the flights.
        """
        total_points = 0
        
        for flight in flights:
            try:
                distance = flight['distance']
                partner = flight['partner']
                
                # Base points calculation
                if partner:
                    points_multiplier = 1.5  # Points multiplier for partner airlines
                else:
                    points_multiplier = 1.0  # Base multiplier for Emirates flights
                
                # Calculating points for the flight
                points = distance * points_multiplier
                total_points += points
            
            except KeyError as e:
                raise KeyError(f"Missing required flight information: {e}")

        return int(total_points)

# Example usage:
if __name__ == "__main__":
    skywards = EmiratesSkywards()

    # Registering a new member
    try:
        print(skywards.register_member("John Doe", "john.doe@example.com"))
    except ValueError as e:
        print(e)
    
    # Calculating points for a given itinerary
    itinerary = [
        {"distance": 1000, "partner": False},  # Emirates flight
        {"distance": 1500, "partner": True},   # Partner airline flight
        {"distance": 2000, "partner": False},  # Emirates flight
    ]

    try:
        points = skywards.calculate_points(itinerary)
        print(f"Total loyalty points earned: {points}")
    except KeyError as e:
        print(e)
```
