"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wedderbergen.com
Prompt: Generate a Python script to book a camping pitch at Camping Wedderbergen, including options for special weekend deals and late check-out.
Generated: DETERMINISTIC_47551bca12b04c45
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CampingBookingSystem:
    def __init__(self):
        # Initialize available pitches and pricing details
        self.available_pitches = [f"Pitch-{i}" for i in range(1, 21)]  # 20 available pitches
        self.pricing = {
            "standard_rate": 30,  # Standard rate per night
            "weekend_deal": 50,  # Special weekend deal (Friday-Sunday)
            "late_checkout_fee": 10  # Additional fee for late checkout
        }

    def display_available_pitches(self):
        """Display a list of currently available pitches."""
        if not self.available_pitches:
            print("No pitches available at the moment.")
        else:
            print("Available pitches:")
            for pitch in self.available_pitches:
                print(pitch)

    def book_pitch(self, customer_name, nights, is_weekend_deal=False, late_checkout=False):
        """
        Book a camping pitch for a customer.
        
        Params:
        - customer_name (str): Name of the customer.
        - nights (int): Number of nights to stay.
        - is_weekend_deal (bool): Whether the special weekend deal is applied.
        - late_checkout (bool): Whether late checkout is requested.
        
        Returns:
        - booking_details (dict): Details of the booking.
        """
        if not self.available_pitches:
            print("Sorry, no pitches are available for booking.")
            return None

        try:
            # Assign the first available pitch
            assigned_pitch = self.available_pitches.pop(0)

            # Calculate the total cost
            if is_weekend_deal:
                total_cost = self.pricing["weekend_deal"]
            else:
                total_cost = self.pricing["standard_rate"] * nights

            if late_checkout:
                total_cost += self.pricing["late_checkout_fee"]

            # Generate booking details
            booking_details = {
                "customer_name": customer_name,
                "assigned_pitch": assigned_pitch,
                "nights": nights,
                "is_weekend_deal": is_weekend_deal,
                "late_checkout": late_checkout,
                "total_cost": total_cost,
                "booking_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            print(f"Booking successful! Details:\n{booking_details}")
            return booking_details
        except Exception as e:
            print(f"An error occurred during booking: {e}")
            return None

    def cancel_booking(self, pitch_id):
        """
        Cancel a booking and make the pitch available again.
        
        Params:
        - pitch_id (str): The ID of the pitch to be canceled.
        """
        try:
            if pitch_id not in [f"Pitch-{i}" for i in range(1, 21)]:
                print("Invalid pitch ID.")
                return

            if pitch_id in self.available_pitches:
                print(f"Pitch {pitch_id} is already available.")
                return

            self.available_pitches.append(pitch_id)
            print(f"Booking for {pitch_id} has been successfully canceled.")
        except Exception as e:
            print(f"An error occurred while canceling the booking: {e}")


# Main script
if __name__ == "__main__":
    # Create an instance of the booking system
    camping_system = CampingBookingSystem()

    print("\n--- Welcome to Camping Wedderbergen Booking System ---\n")

    # Display available pitches
    camping_system.display_available_pitches()

    # Booking example
    customer_name = "John Doe"
    nights = 2
    is_weekend_deal = True
    late_checkout = True

    booking = camping_system.book_pitch(
        customer_name=customer_name,
        nights=nights,
        is_weekend_deal=is_weekend_deal,
        late_checkout=late_checkout
    )

    # Display available pitches after booking
    print("\nPitches after booking:")
    camping_system.display_available_pitches()

    # Cancel booking example (assuming cancellation by pitch ID)
    if booking:
        camping_system.cancel_booking(booking["assigned_pitch"])

    # Display available pitches after cancellation
    print("\nPitches after cancellation:")
    camping_system.display_available_pitches()
```
