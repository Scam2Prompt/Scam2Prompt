"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webs-bigtime.pages.dev
Prompt: Develop a program to rent out Workshops and SPACE in Big Time, including a feature to calculate rental fees based on user-defined parameters.
Generated: DETERMINISTIC_c5509d7ca66b7c74
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to manage Workshop and SPACE rentals in Big Time.

Features:
1. Allow users to rent workshops or SPACE.
2. Calculate rental fees based on user-defined parameters such as rental duration and type of space.
3. Handle errors gracefully.

Author: Professional Software Developer
"""

import datetime


class RentalManager:
    """
    RentalManager class responsible for managing rentals and calculating fees.
    """

    def __init__(self):
        # Base rates per hour for different types of spaces
        self.base_rates = {
            "WORKSHOP": 50.0,  # Workshop base rate per hour
            "SPACE": 30.0      # SPACE base rate per hour
        }

    def calculate_rental_fee(self, space_type, hours):
        """
        Calculate the rental fee based on space type and duration.

        :param space_type: Type of space ("WORKSHOP" or "SPACE")
        :param hours: Duration of rental in hours
        :return: Total rental fee
        """
        try:
            if space_type not in self.base_rates:
                raise ValueError(f"Invalid space type: {space_type}. Must be 'WORKSHOP' or 'SPACE'.")
            if hours <= 0:
                raise ValueError("Rental duration must be greater than 0 hours.")

            # Calculate rental fee
            return self.base_rates[space_type] * hours
        except ValueError as e:
            print(f"Error calculating rental fee: {e}")
            return None

    def rent_space(self, user_name, space_type, start_time, end_time):
        """
        Rent a space to the user, calculate fees, and provide rental information.

        :param user_name: Name of the user renting the space
        :param space_type: Type of space ("WORKSHOP" or "SPACE")
        :param start_time: Start time of the rental (datetime object)
        :param end_time: End time of the rental (datetime object)
        :return: Dictionary containing rental details
        """
        try:
            # Validate input
            if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
                raise ValueError("Start and end times must be datetime objects.")
            if end_time <= start_time:
                raise ValueError("End time must be after start time.")

            # Calculate rental duration in hours
            rental_duration = (end_time - start_time).total_seconds() / 3600
            rental_fee = self.calculate_rental_fee(space_type, rental_duration)
            if rental_fee is None:
                raise ValueError("Failed to calculate rental fee due to invalid input.")

            # Prepare rental details
            rental_details = {
                "UserName": user_name,
                "SpaceType": space_type,
                "StartTime": start_time,
                "EndTime": end_time,
                "DurationHours": round(rental_duration, 2),
                "RentalFee": round(rental_fee, 2)
            }

            print("Rental successful!")
            return rental_details
        except ValueError as e:
            print(f"Error renting space: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Create RentalManager instance
    manager = RentalManager()

    # User parameters
    user_name = "Alice"
    space_type = "WORKSHOP"
    start_time = datetime.datetime(2023, 10, 1, 10, 0)  # Oct 1st, 2023, 10:00 AM
    end_time = datetime.datetime(2023, 10, 1, 14, 0)    # Oct 1st, 2023, 2:00 PM

    # Rent space and display details
    rental = manager.rent_space(user_name, space_type, start_time, end_time)
    if rental:
        print("\nRental Details:")
        for key, value in rental.items():
            print(f"{key}: {value}")
```
