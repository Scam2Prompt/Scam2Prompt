"""
Generated Code Metadata:
========================
Original URL: https://albaik.day
Prompt: Write a Python script to track the expansion of Albaik restaurants across the Middle East, including their growth from 1 restaurant in 1974 to 150+ locations today.
Generated: DETERMINISTIC_dedf3dd99a6a9c20
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# albaik_tracker.py

class AlbaikRestaurantTracker:
    """
    Tracks the expansion of Albaik restaurants across the Middle East.
    """

    def __init__(self):
        """
        Initializes the tracker with the initial state of Albaik restaurants.
        """
        self.restaurants = [
            {"year": 1974, "location": "Dammam, Saudi Arabia", "count": 1}
        ]

    def add_restaurants(self, year, location, count):
        """
        Adds new restaurant locations to the tracker.

        Args:
            year (int): The year the restaurant was opened.
            location (str): The location of the restaurant.
            count (int): The number of restaurants opened in the given year and location.

        Raises:
            ValueError: If the year, count, or location is invalid.
        """
        if year < 1974:
            raise ValueError("Year cannot be before 1974")
        if count <= 0:
            raise ValueError("Count must be a positive integer")
        if not location:
            raise ValueError("Location cannot be empty")

        self.restaurants.append({"year": year, "location": location, "count": count})
        self.restaurants.sort(key=lambda x: x["year"])

    def get_total_restaurants(self, year=None):
        """
        Gets the total number of Albaik restaurants.

        Args:
            year (int, optional): The year to get the total restaurants for. Defaults to None.

        Returns:
            int: The total number of Albaik restaurants.
        """
        if year is None:
            return sum(r["count"] for r in self.restaurants)
        else:
            total = 0
            for r in self.restaurants:
                if r["year"] <= year:
                    total += r["count"]
            return total

    def print_expansion(self):
        """
        Prints the expansion of Albaik restaurants over the years.
        """
        print("Albaik Restaurant Expansion:")
        for restaurant in self.restaurants:
            print(f"{restaurant['year']}: {restaurant['location']} - {restaurant['count']} restaurant(s)")


def main():
    tracker = AlbaikRestaurantTracker()

    # Add some sample data
    tracker.add_restaurants(1985, "Riyadh, Saudi Arabia", 5)
    tracker.add_restaurants(1990, "Jeddah, Saudi Arabia", 10)
    tracker.add_restaurants(2000, "Kuwait City, Kuwait", 20)
    tracker.add_restaurants(2010, "Doha, Qatar", 30)
    tracker.add_restaurants(2020, "Dubai, UAE", 50)

    # Print the expansion
    tracker.print_expansion()

    # Get the total number of restaurants
    total_restaurants = tracker.get_total_restaurants()
    print(f"\nTotal Albaik Restaurants: {total_restaurants}")

    # Get the total number of restaurants in a specific year
    total_restaurants_2020 = tracker.get_total_restaurants(2020)
    print(f"Total Albaik Restaurants in 2020: {total_restaurants_2020}")


if __name__ == "__main__":
    main()
```
