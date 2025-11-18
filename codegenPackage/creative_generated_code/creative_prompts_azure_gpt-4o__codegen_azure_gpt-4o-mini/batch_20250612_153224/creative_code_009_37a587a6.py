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

class Tour:
    """Class representing a horse riding tour."""
    
    def __init__(self, tour_id, name, date, available_spots):
        self.tour_id = tour_id
        self.name = name
        self.date = date
        self.available_spots = available_spots

    def is_available(self, group_size):
        """Check if the tour has enough available spots for the group size."""
        return self.available_spots >= group_size


class TourManager:
    """Class to manage a collection of horse riding tours."""
    
    def __init__(self):
        self.tours = []

    def add_tour(self, tour):
        """Add a new tour to the collection."""
        self.tours.append(tour)

    def filter_tours(self, selected_date, group_size):
        """Filter tours based on selected date and group size."""
        filtered_tours = [
            tour for tour in self.tours
            if tour.date == selected_date and tour.is_available(group_size)
        ]
        return filtered_tours


def main():
    """Main function to run the tour filtering application."""
    
    # Sample data for tours
    tour_manager = TourManager()
    tour_manager.add_tour(Tour(1, "Andes Adventure", datetime.date(2023, 10, 15), 4))
    tour_manager.add_tour(Tour(2, "Coastal Ride", datetime.date(2023, 10, 15), 2))
    tour_manager.add_tour(Tour(3, "Valley Ride", datetime.date(2023, 10, 16), 5))

    # User input for date and group size
    try:
        user_date_input = input("Enter the date of the tour (YYYY-MM-DD): ")
        selected_date = datetime.datetime.strptime(user_date_input, "%Y-%m-%d").date()
        group_size = int(input("Enter the number of participants: "))

        if group_size <= 0:
            raise ValueError("Group size must be a positive integer.")

    except ValueError as e:
        print(f"Error: {e}")
        return

    # Filter available tours
    available_tours = tour_manager.filter_tours(selected_date, group_size)

    # Display available tours
    if available_tours:
        print(f"\nAvailable Tours for {selected_date} for group size {group_size}:")
        for tour in available_tours:
            print(f"- {tour.name} (ID: {tour.tour_id}, Available Spots: {tour.available_spots})")
    else:
        print(f"No available tours for {selected_date} for group size {group_size}.")

if __name__ == "__main__":
    main()
```
