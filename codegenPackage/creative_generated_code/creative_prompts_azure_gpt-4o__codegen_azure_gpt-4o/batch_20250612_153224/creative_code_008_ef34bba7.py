"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Generate a script to calculate the rental cost of Yanmar mini excavators based on daily rates and rental duration, including a feature for automatic reservation confirmation.
Generated: DETERMINISTIC_ef34bba787a5fe10
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class MiniExcavatorRental:
    def __init__(self):
        """
        Initialize the rental system with excavator inventory and rates.
        """
        self.excavators = {
            "Yanmar VIO17": 150,  # Daily rate in USD
            "Yanmar VIO35": 200,
            "Yanmar VIO50": 250
        }
        self.reservations = []  # List to store reservation details

    def calculate_rental_cost(self, model, days):
        """
        Calculate the rental cost for a given excavator model and rental duration.

        Parameters:
        model (str): Excavator model name
        days (int): Number of rental days

        Returns:
        float: Total rental cost
        """
        if model not in self.excavators:
            raise ValueError(f"Model '{model}' not available in inventory.")
        if days <= 0:
            raise ValueError("Rental duration must be a positive integer.")
        
        daily_rate = self.excavators[model]
        return daily_rate * days

    def reserve_excavator(self, model, start_date, days):
        """
        Reserve an excavator for a specific duration.

        Parameters:
        model (str): Excavator model name
        start_date (str): Start date in 'YYYY-MM-DD' format
        days (int): Number of rental days

        Returns:
        dict: Reservation details
        """
        try:
            # Validate input
            if model not in self.excavators:
                raise ValueError(f"Model '{model}' not available.")
            
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            if days <= 0:
                raise ValueError("Rental duration must be a positive integer.")
            
            end_date_obj = start_date_obj + datetime.timedelta(days=days)
            total_cost = self.calculate_rental_cost(model, days)

            # Create reservation entry
            reservation = {
                "model": model,
                "start_date": start_date_obj.date(),
                "end_date": end_date_obj.date(),
                "days": days,
                "total_cost": total_cost,
                "confirmation_id": self.generate_confirmation_id()
            }
            self.reservations.append(reservation)
            return reservation

        except ValueError as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None

    def generate_confirmation_id(self):
        """
        Generate a unique confirmation ID for a reservation.

        Returns:
        str: Unique confirmation ID
        """
        return f"RES-{len(self.reservations) + 1:04d}"

    def list_reservations(self):
        """
        List all reservations.

        Returns:
        list: List of reservation details
        """
        return self.reservations

# Example usage (uncomment to test)
# rental_service = MiniExcavatorRental()
# try:
#     reservation = rental_service.reserve_excavator("Yanmar VIO35", "2023-10-01", 3)
#     if reservation:
#         print("Reservation confirmed!")
#         print(reservation)
# except Exception as e:
#     print(f"An error occurred: {e}")

# print("All reservations:")
# print(rental_service.list_reservations())
```
