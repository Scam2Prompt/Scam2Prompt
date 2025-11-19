"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roc-remi.com
Prompt: Generate a booking request code for a stay at Chalet Roc Remi in Les Gets, including options for B&B and full chalet rental.
Generated: DETERMINISTIC_0e7f216edc055df8
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ChaletBooking:
    def __init__(self, chalet_name: str):
        """Initialize the booking system for the specified chalet."""
        self.chalet_name = chalet_name
        self.bookings = []

    def book(self, guest_name: str, stay_dates: list, option: str):
        """Book a stay at the chalet.

        Args:
            guest_name (str): The name of the guest making the booking.
            stay_dates (list): A list of dates for the stay (start and end).
            option (str): The booking option, either 'B&B' or 'Full Chalet Rental'.

        Raises:
            ValueError: If the booking option is not valid or if stay_dates are invalid.
        """
        # Validate input parameters
        if option not in ['B&B', 'Full Chalet Rental']:
            raise ValueError("Invalid booking option. Choose 'B&B' or 'Full Chalet Rental'.")
        
        if len(stay_dates) != 2 or stay_dates[0] >= stay_dates[1]:
            raise ValueError("Invalid stay dates. Provide a start and end date.")

        # Create a booking record
        booking = {
            'guest_name': guest_name,
            'stay_dates': stay_dates,
            'option': option,
        }
        self.bookings.append(booking)
        return booking

    def show_bookings(self):
        """Display all current bookings."""
        if not self.bookings:
            print("No current bookings for", self.chalet_name)
        else:
            print("Current bookings for", self.chalet_name)
            for booking in self.bookings:
                print(f"Guest: {booking['guest_name']}, Dates: {booking['stay_dates']}, Option: {booking['option']}")

def main():
    """Main function to demonstrate booking functionality."""
    try:
        # Initialize the booking system for Chalet Roc Remi
        chalet = ChaletBooking("Chalet Roc Remi")
        
        # Example bookings
        chalet.book("Alice Smith", ["2023-12-01", "2023-12-05"], "B&B")
        chalet.book("Bob Johnson", ["2023-12-10", "2023-12-15"], "Full Chalet Rental")

        # Show all bookings
        chalet.show_bookings()

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
```
