"""
Generated Code Metadata:
========================
Original URL: https://uniswop.shop
Prompt: Create a function that facilitates in-person meetups for transactions in a college marketplace app, inspired by the UniSwop model.
Generated: DETERMINISTIC_9c17e908dd1342b6
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from geopy.distance import geodesic

class MeetupScheduler:
    """
    A class to facilitate in-person meetups for transactions in a college marketplace app.
    """

    def __init__(self):
        # Store scheduled meetups
        self.meetups = []

    def schedule_meetup(self, buyer, seller, item, buyer_location, seller_location, preferred_time):
        """
        Schedules a meetup between a buyer and a seller.

        Args:
            buyer (str): Name or ID of the buyer.
            seller (str): Name or ID of the seller.
            item (str): Item being transacted.
            buyer_location (tuple): (latitude, longitude) of the buyer.
            seller_location (tuple): (latitude, longitude) of the seller.
            preferred_time (datetime): Preferred time for the meetup.

        Returns:
            dict: Details of the scheduled meetup.
        """
        try:
            # Validate input
            if not isinstance(preferred_time, datetime.datetime):
                raise ValueError("Preferred time must be a datetime object.")

            # Calculate midpoint for the meetup
            midpoint = self._calculate_midpoint(buyer_location, seller_location)

            # Create a meetup record
            meetup = {
                "buyer": buyer,
                "seller": seller,
                "item": item,
                "location": midpoint,
                "time": preferred_time,
                "status": "Scheduled"
            }

            # Store the meetup
            self.meetups.append(meetup)

            return meetup
        except Exception as e:
            # Handle unexpected errors
            return {"error": str(e)}

    def _calculate_midpoint(self, loc1, loc2):
        """
        Calculates the geographic midpoint between two locations.

        Args:
            loc1 (tuple): (latitude, longitude) of the first location.
            loc2 (tuple): (latitude, longitude) of the second location.

        Returns:
            tuple: (latitude, longitude) of the midpoint.
        """
        try:
            lat1, lon1 = loc1
            lat2, lon2 = loc2

            # Calculate the midpoint
            midpoint_lat = (lat1 + lat2) / 2
            midpoint_lon = (lon1 + lon2) / 2

            return (midpoint_lat, midpoint_lon)
        except Exception as e:
            raise ValueError(f"Invalid location data: {e}")

    def list_meetups(self):
        """
        Lists all scheduled meetups.

        Returns:
            list: A list of all meetups.
        """
        return self.meetups

    def cancel_meetup(self, buyer, seller, item):
        """
        Cancels a scheduled meetup.

        Args:
            buyer (str): Name or ID of the buyer.
            seller (str): Name or ID of the seller.
            item (str): Item being transacted.

        Returns:
            str: Confirmation message or error message.
        """
        try:
            for meetup in self.meetups:
                if meetup["buyer"] == buyer and meetup["seller"] == seller and meetup["item"] == item:
                    self.meetups.remove(meetup)
                    return f"Meetup for item '{item}' between {buyer} and {seller} has been canceled."

            return "No matching meetup found to cancel."
        except Exception as e:
            return f"Error while canceling meetup: {e}"


# Example usage
if __name__ == "__main__":
    scheduler = MeetupScheduler()

    # Schedule a meetup
    meetup = scheduler.schedule_meetup(
        buyer="Alice",
        seller="Bob",
        item="Textbook",
        buyer_location=(40.7128, -74.0060),  # New York City
        seller_location=(40.730610, -73.935242),  # Brooklyn
        preferred_time=datetime.datetime(2023, 10, 15, 14, 0)
    )
    print("Scheduled Meetup:", meetup)

    # List all meetups
    print("All Meetups:", scheduler.list_meetups())

    # Cancel a meetup
    cancel_message = scheduler.cancel_meetup(buyer="Alice", seller="Bob", item="Textbook")
    print(cancel_message)

    # List all meetups after cancellation
    print("All Meetups After Cancellation:", scheduler.list_meetups())
```
