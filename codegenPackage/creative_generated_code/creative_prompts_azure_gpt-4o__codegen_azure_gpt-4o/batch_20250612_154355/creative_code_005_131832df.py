"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Write a function to automate the reservation process for advertising spaces, inspired by WOW MEDIA's "Cotizar tu ubicacion favorita desde aqui" feature.
Generated: DETERMINISTIC_131832df7efdf587
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AdvertisingReservationSystem:
    def __init__(self):
        """
        Initializes the reservation system with available spaces.
        """
        self.advertising_spaces = {
            "Billboard-1": {"location": "Downtown", "available": True, "price_per_day": 200},
            "Billboard-2": {"location": "Airport", "available": True, "price_per_day": 300},
            "Billboard-3": {"location": "Highway", "available": True, "price_per_day": 150},
        }

    def check_availability(self, space_id):
        """
        Checks if the given advertising space is available.
        :param space_id: The ID of the advertising space (e.g., "Billboard-1").
        :return: True if available; False otherwise.
        """
        if space_id not in self.advertising_spaces:
            raise ValueError(f"Invalid space ID: {space_id}")
        return self.advertising_spaces[space_id]["available"]

    def reserve_space(self, space_id, start_date, end_date, customer_name):
        """
        Reserves an advertising space for a given date range.
        :param space_id: The ID of the advertising space.
        :param start_date: Reservation start date (YYYY-MM-DD).
        :param end_date: Reservation end date (YYYY-MM-DD).
        :param customer_name: Name of the customer making the reservation.
        :return: A confirmation message if successful.
        """
        try:
            # Convert dates from string to datetime objects
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
            
            # Validate space ID
            if space_id not in self.advertising_spaces:
                raise ValueError(f"Invalid space ID: {space_id}")
            
            # Check availability
            space = self.advertising_spaces[space_id]
            if not space["available"]:
                raise Exception(f"Space '{space_id}' is not available for reservation.")
            
            # Validate date range
            if start_date >= end_date:
                raise ValueError("Reservation end date must be after the start date.")
            
            # Calculate total cost
            days_reserved = (end_date - start_date).days
            total_cost = days_reserved * space["price_per_day"]
            
            # Mark space as unavailable
            space["available"] = False
            
            # Generate reservation details
            reservation_details = {
                "space_id": space_id,
                "location": space["location"],
                "customer_name": customer_name,
                "start_date": start_date,
                "end_date": end_date,
                "total_cost": total_cost,
            }
            
            return f"Reservation confirmed: {reservation_details}"
        
        except Exception as e:
            return f"Error occurred during reservation: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Initialize the reservation system
    system = AdvertisingReservationSystem()
    
    # Reserve an advertising space
    try:
        confirmation = system.reserve_space(
            space_id="Billboard-1",
            start_date="2023-12-01",
            end_date="2023-12-10",
            customer_name="John Doe"
        )
        print(confirmation)
    except Exception as e:
        print(str(e))
```
