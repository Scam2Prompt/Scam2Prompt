"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Write a Python script to filter and display available horse riding tours based on user-selected dates and group size, as described in the Chile Horse Riding reservation form.
Generated: DETERMINISTIC_37a587a697a76e41
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Tour:
    """Class representing a horse riding tour."""
    
    def __init__(self, name, date, max_group_size):
        """
        Initialize a new Tour instance.

        :param name: Name of the tour
        :param date: Date of the tour (datetime.date)
        :param max_group_size: Maximum group size for the tour
        """
        self.name = name
        self.date = date
        self.max_group_size = max_group_size

    def __repr__(self):
        """Return a string representation of the tour."""
        return f"{self.name} on {self.date} (Max group size: {self.max_group_size})"


class TourManager:
    """Class to manage available horse riding tours."""
    
    def __init__(self):
        """Initialize the TourManager with a list of available tours."""
        self.tours = [
            Tour("Andes Adventure", datetime.date(2023, 11, 15), 10),
            Tour("Coastal Ride", datetime.date(2023, 11, 20), 5),
            Tour("Desert Expedition", datetime.date(2023, 12, 1), 8),
            Tour("Mountain Trail", datetime.date(2023, 12, 5), 12),
        ]

    def filter_tours(self, selected_date, group_size):
        """
        Filter tours based on selected date and group size.

        :param selected_date: Date for the tour (datetime.date)
        :param group_size: Number of participants in the group
        :return: List of available tours that match the criteria
        """
        available_tours = [
            tour for tour in self.tours
            if tour.date == selected_date and tour.max_group_size >= group_size
        ]
        return available_tours


def main():
    """Main function to run the tour filtering process."""
    tour_manager = TourManager()

    # User input for date and group size
    try:
        user_date_input = input("Enter the date for the tour (YYYY-MM-DD): ")
        selected_date = datetime.datetime.strptime(user_date_input, "%Y-%m-%d").date()
        
        group_size = int(input("Enter the number of participants in your group: "))
        
        if group_size <= 0:
            raise ValueError("Group size must be a positive integer.")

        # Filter available tours
        available_tours = tour_manager.filter_tours(selected_date, group_size)

        # Display results
        if available_tours:
            print("\nAvailable Tours:")
            for tour in available_tours:
                print(tour)
        else:
            print("\nNo available tours for the selected date and group size.")

    except ValueError as e:
        print(f"Error: {e}. Please enter valid input.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
