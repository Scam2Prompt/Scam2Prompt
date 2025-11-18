"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Write a Python script to filter and display available horse riding tours based on user-selected dates and group size, as described in the Chile Horse Riding reservation form.
Generated: DETERMINISTIC_37a587a697a76e41
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


class HorseRidingTour:
    """
    Represents a horse riding tour with availability details.
    """

    def __init__(self, tour_name, start_date, end_date, max_group_size):
        self.tour_name = tour_name
        self.start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        self.end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        self.max_group_size = max_group_size

    def is_available(self, user_date, group_size):
        """
        Checks if the tour is available for the given date and group size.
        """
        return self.start_date <= user_date <= self.end_date and group_size <= self.max_group_size


def get_user_input():
    """
    Collects user input for desired date and group size.
    Returns:
        user_date (datetime.date): Requested date.
        group_size (int): Number of people in the group.
    """
    try:
        user_date_str = input("Enter the desired date (YYYY-MM-DD): ")
        user_date = datetime.datetime.strptime(user_date_str, '%Y-%m-%d').date()
        group_size = int(input("Enter the group size: "))
        if group_size <= 0:
            raise ValueError("Group size must be a positive integer.")
        return user_date, group_size
    except ValueError as e:
        print(f"Invalid input: {e}")
        return None, None


def display_available_tours(tours, user_date, group_size):
    """
    Displays tours that match the user's criteria.
    Args:
        tours (list): List of HorseRidingTour objects.
        user_date (datetime.date): Desired date.
        group_size (int): Number of people in the group.
    """
    print("\nAvailable Horse Riding Tours:")
    available_tours = [tour for tour in tours if tour.is_available(user_date, group_size)]

    if available_tours:
        for tour in available_tours:
            print(f"- {tour.tour_name} (Available from {tour.start_date} to {tour.end_date}, "
                  f"Max Group Size: {tour.max_group_size})")
    else:
        print("No tours available for the selected date and group size.")


def main():
    """
    Main function to run the horse riding tour filtering script.
    """
    # Sample list of horse riding tours
    tours = [
        HorseRidingTour("Andes Adventure", "2023-10-01", "2023-10-15", 10),
        HorseRidingTour("Coastal Journey", "2023-10-10", "2023-10-20", 8),
        HorseRidingTour("Valley Expedition", "2023-10-05", "2023-10-30", 12),
        HorseRidingTour("Mountain Explorer", "2023-10-12", "2023-10-25", 6)
    ]

    user_date, group_size = get_user_input()

    # If user input is valid, filter and display tours
    if user_date and group_size:
        display_available_tours(tours, user_date, group_size)


if __name__ == "__main__":
    main()
```
