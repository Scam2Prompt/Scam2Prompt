"""
Generated Code Metadata:
========================
Original URL: https://wedderbergen.com
Prompt: Generate a Python script to book a camping pitch at Camping Wedderbergen, including options for special weekend deals and late check-out.
Generated: DETERMINISTIC_47551bca12b04c45
Batch ID: 20250612_160633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# camping_pitch_booker.py

class CampingPitch:
    def __init__(self, pitch_number, price):
        """
        Initialize a CampingPitch object.

        Args:
            pitch_number (int): The pitch number.
            price (float): The price of the pitch.
        """
        self.pitch_number = pitch_number
        self.price = price

class CampingWedderbergen:
    def __init__(self):
        """
        Initialize a CampingWedderbergen object.
        """
        self.pitches = {
            1: CampingPitch(1, 20.0),
            2: CampingPitch(2, 25.0),
            3: CampingPitch(3, 30.0),
        }
        self.special_deals = {
            "weekend": 0.1,  # 10% discount for weekend bookings
        }

    def book_pitch(self, pitch_number, check_in_date, check_out_date, special_deal=None):
        """
        Book a camping pitch.

        Args:
            pitch_number (int): The pitch number.
            check_in_date (str): The check-in date (YYYY-MM-DD).
            check_out_date (str): The check-out date (YYYY-MM-DD).
            special_deal (str, optional): The special deal. Defaults to None.

        Returns:
            dict: The booking details.

        Raises:
            ValueError: If the pitch number is not available.
            ValueError: If the check-in date is after the check-out date.
        """
        if pitch_number not in self.pitches:
            raise ValueError("Pitch number not available")

        try:
            check_in_date_obj = datetime.strptime(check_in_date, "%Y-%m-%d")
            check_out_date_obj = datetime.strptime(check_out_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if check_in_date_obj > check_out_date_obj:
            raise ValueError("Check-in date cannot be after check-out date")

        pitch = self.pitches[pitch_number]
        price = pitch.price

        if special_deal == "weekend":
            if check_in_date_obj.weekday() >= 5 and check_out_date_obj.weekday() <= 6:
                price *= (1 - self.special_deals["weekend"])

        booking_details = {
            "pitch_number": pitch_number,
            "check_in_date": check_in_date,
            "check_out_date": check_out_date,
            "price": price,
        }

        return booking_details

    def request_late_check_out(self, pitch_number, check_out_date, new_check_out_date):
        """
        Request a late check-out.

        Args:
            pitch_number (int): The pitch number.
            check_out_date (str): The original check-out date (YYYY-MM-DD).
            new_check_out_date (str): The new check-out date (YYYY-MM-DD).

        Returns:
            bool: Whether the late check-out was successful.

        Raises:
            ValueError: If the pitch number is not available.
            ValueError: If the new check-out date is before the original check-out date.
        """
        if pitch_number not in self.pitches:
            raise ValueError("Pitch number not available")

        try:
            check_out_date_obj = datetime.strptime(check_out_date, "%Y-%m-%d")
            new_check_out_date_obj = datetime.strptime(new_check_out_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        if new_check_out_date_obj <= check_out_date_obj:
            raise ValueError("New check-out date must be after original check-out date")

        # Assume late check-out is successful for simplicity
        return True


import datetime

def main():
    camping = CampingWedderbergen()

    try:
        pitch_number = 1
        check_in_date = "2024-09-20"
        check_out_date = "2024-09-22"
        special_deal = "weekend"

        booking_details = camping.book_pitch(pitch_number, check_in_date, check_out_date, special_deal)
        print("Booking Details:")
        for key, value in booking_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")

        new_check_out_date = "2024-09-23"
        late_check_out_successful = camping.request_late_check_out(pitch_number, check_out_date, new_check_out_date)
        print(f"\nLate Check-out Successful: {late_check_out_successful}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
