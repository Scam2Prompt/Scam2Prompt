"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poweredproductions.com.au
Prompt: Write a code snippet for a booking system that manages the hiring of police uniforms and includes a price match guarantee feature.
Generated: DETERMINISTIC_b1adaaaa8b99a4e8
Batch ID: 20250612_164021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class UniformBookingSystem:
    """
    A class to manage the hiring of police uniforms with a price match guarantee.
    """

    def __init__(self):
        # Dictionary to store bookings in the format {booking_id: booking_details}
        self.bookings = {}
        # Price match guarantee enables a customer to get the lowest price
        self.price_match_enabled = True
        # Define base prices for police uniforms
        self.uniform_prices = {
            "standard_uniform": 50,  # Price per day in USD
            "ceremonial_uniform": 100  # Price per day in USD
        }

    def create_booking(self, customer_name, uniform_type, start_date, end_date, competitor_price=None):
        """
        Create a new uniform booking.

        :param customer_name: Name of the customer
        :param uniform_type: Type of uniform ("standard_uniform" or "ceremonial_uniform")
        :param start_date: Start date of booking (YYYY-MM-DD)
        :param end_date: End date of booking (YYYY-MM-DD)
        :param competitor_price: Competitor's price for the same service (optional)
        :return: Booking confirmation details or error message
        """
        try:
            # Validate uniform type
            if uniform_type not in self.uniform_prices:
                return {"error": "Invalid uniform type."}

            # Convert dates to datetime objects
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")

            # Ensure valid date range
            if start_date >= end_date:
                return {"error": "End date must be after start date."}

            # Calculate number of rental days
            rental_days = (end_date - start_date).days

            # Calculate base price
            base_price = rental_days * self.uniform_prices[uniform_type]

            # Apply price match guarantee if competitor price is provided
            if self.price_match_enabled and competitor_price and competitor_price < base_price:
                final_price = competitor_price
            else:
                final_price = base_price

            # Generate a unique booking ID
            booking_id = f"BK{len(self.bookings) + 1:05d}"

            # Store the booking details
            self.bookings[booking_id] = {
                "customer_name": customer_name,
                "uniform_type": uniform_type,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "rental_days": rental_days,
                "base_price": base_price,
                "final_price": final_price
            }

            # Return the booking confirmation
            return {
                "message": "Booking created successfully.",
                "booking_id": booking_id,
                "details": self.bookings[booking_id]
            }

        except ValueError as e:
            # Handle invalid date format
            return {"error": f"Invalid date format: {e}"}

        except Exception as e:
            # Handle other unexpected errors
            return {"error": f"An unexpected error occurred: {e}"}

    def get_booking(self, booking_id):
        """
        Retrieve booking details by booking ID.

        :param booking_id: Unique booking ID
        :return: Booking details or error message
        """
        if booking_id in self.bookings:
            return self.bookings[booking_id]
        else:
            return {"error": "Booking ID not found."}

    def cancel_booking(self, booking_id):
        """
        Cancel a booking by booking ID.

        :param booking_id: Unique booking ID
        :return: Cancellation confirmation or error message
        """
        if booking_id in self.bookings:
            del self.bookings[booking_id]
            return {"message": "Booking canceled successfully."}
        else:
            return {"error": "Booking ID not found."}


# Example Usage
if __name__ == "__main__":
    system = UniformBookingSystem()

    # Create a booking
    response = system.create_booking(
        customer_name="John Doe",
        uniform_type="standard_uniform",
        start_date="2023-11-01",
        end_date="2023-11-05",
        competitor_price=180
    )
    print(response)

    # Fetch booking details
    booking_id = response.get("booking_id")
    if booking_id:
        print(system.get_booking(booking_id))

    # Cancel the booking
    if booking_id:
        print(system.cancel_booking(booking_id))
```
