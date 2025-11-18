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
import json

class AdvertisementSpace:
    def __init__(self, location, price_per_day):
        """
        Initialize an advertisement space with a location and price per day.
        
        :param location: str - The location of the advertisement space.
        :param price_per_day: float - The price per day for renting the space.
        """
        self.location = location
        self.price_per_day = price_per_day

class Reservation:
    def __init__(self, space, start_date, end_date):
        """
        Initialize a reservation for a given advertisement space and date range.

        :param space: AdvertisementSpace - The advertisement space being reserved.
        :param start_date: datetime.date - The start date of the reservation.
        :param end_date: datetime.date - The end date of the reservation.
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date.")
        
        self.space = space
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        """
        Calculate the total cost of the reservation based on the price per day.

        :return: float - Total cost of the reservation.
        """
        duration = (self.end_date - self.start_date).days
        return duration * self.space.price_per_day

def reserve_ad_space(ad_space, start_date, end_date):
    """
    Reserve an advertisement space for a specified date range.

    :param ad_space: AdvertisementSpace - The advertisement space to reserve.
    :param start_date: str - The start date in 'YYYY-MM-DD' format.
    :param end_date: str - The end date in 'YYYY-MM-DD' format.
    
    :return: dict - Confirmation details of the reservation.
    """
    try:
        # Parse the input date strings into datetime.date objects
        start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

        # Create a reservation
        reservation = Reservation(ad_space, start_date_obj, end_date_obj)

        # Prepare the confirmation details
        confirmation = {
            "location": ad_space.location,
            "start_date": str(reservation.start_date),
            "end_date": str(reservation.end_date),
            "total_cost": reservation.total_cost
        }

        return confirmation

    except ValueError as ve:
        return {"error": str(ve)}
    except Exception as e:
        return {"error": "An unexpected error occurred: " + str(e)}

# Example usage:
if __name__ == "__main__":
    # Create an advertisement space
    ad_space = AdvertisementSpace(location="Downtown Billboard", price_per_day=150.0)

    # Reserve the advertisement space
    result = reserve_ad_space(ad_space, "2023-11-01", "2023-11-10")
    
    # Print the reservation result
    print(json.dumps(result, indent=4))
```
