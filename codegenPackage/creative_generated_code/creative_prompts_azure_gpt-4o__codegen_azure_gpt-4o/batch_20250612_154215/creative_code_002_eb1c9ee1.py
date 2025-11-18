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
import re

class EmiratesSkywards:
    """
    A class to simulate Emirates Skywards loyalty points calculation and program registration.
    """

    def __init__(self):
        # Base point multiplier for Emirates flights
        self.base_multiplier = 1.0
        
        # Multipliers for partner airlines, where key is airline code and value is multiplier
        self.partner_multipliers = {
            "QF": 0.8,   # Qantas
            "BA": 0.7,   # British Airways
            "AA": 0.6    # American Airlines
        }

    def register_user(self, full_name, email, phone):
        """
        Simulates user registration for the Emirates Skywards program.

        Parameters:
        full_name (str): Full name of the user.
        email (str): Email address of the user.
        phone (str): Phone number of the user.

        Returns:
        dict: A confirmation dictionary containing user details.
        """
        # Validate input
        if not full_name or not isinstance(full_name, str):
            raise ValueError("Full name must be a non-empty string.")
        
        # Simple email validation
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        
        # Simple phone validation (must be numeric and of reasonable length)
        if not phone.isdigit() or len(phone) < 7:
            raise ValueError("Invalid phone number format.")
        
        return {
            "message": "Registration successful!",
            "name": full_name,
            "email": email,
            "phone": phone
        }

    def calculate_loyalty_points(self, airline_code, distance):
        """
        Calculates Emirates Skywards loyalty points for a given flight itinerary.

        Parameters:
        airline_code (str): Airline code (e.g., "EK" for Emirates, "BA" for British Airways).
        distance (float): Flight distance in miles.

        Returns:
        float: Calculated loyalty points.
        """
        if distance <= 0:
            raise ValueError("Distance must be a positive number.")
        
        multiplier = self.partner_multipliers.get(airline_code.upper(), self.base_multiplier)
        return distance * multiplier

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of EmiratesSkywards class
        skywards = EmiratesSkywards()

        # Simulate user registration
        user_details = skywards.register_user(
            full_name="John Doe",
            email="john.doe@example.com",
            phone="1234567890"
        )
        print(user_details)

        # Calculate loyalty points for Emirates flight
        points_emirates = skywards.calculate_loyalty_points(airline_code="EK", distance=5000)
        print(f"Loyalty Points for Emirates flight: {points_emirates}")

        # Calculate loyalty points for a partner airline flight
        points_partner = skywards.calculate_loyalty_points(airline_code="BA", distance=3000)
        print(f"Loyalty Points for British Airways flight: {points_partner}")

    except Exception as e:
        print(f"Error: {e}")
```
