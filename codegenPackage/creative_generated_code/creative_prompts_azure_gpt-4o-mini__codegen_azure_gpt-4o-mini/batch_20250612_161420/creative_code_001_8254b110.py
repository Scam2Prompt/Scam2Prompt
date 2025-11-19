"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://del-pinar.com.ar
Prompt: Write a Python function that integrates with a hotel management library to display amenities like a heated pool and gym for an apart hotel.
Generated: DETERMINISTIC_8254b110b0d3de93
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# hotel_management.py

class Hotel:
    """A class representing a hotel with various amenities."""

    def __init__(self, name):
        """Initializes a new Hotel instance with a given name."""
        self.name = name
        self.amenities = []

    def add_amenity(self, amenity):
        """Adds an amenity to the hotel's list of amenities.

        Args:
            amenity (str): The amenity to be added.
        """
        if amenity and isinstance(amenity, str):
            self.amenities.append(amenity)
        else:
            raise ValueError("Amenity must be a non-empty string.")

    def display_amenities(self):
        """Displays the list of amenities available in the hotel."""
        if not self.amenities:
            print(f"{self.name} has no amenities available.")
        else:
            print(f"Amenities available at {self.name}:")
            for amenity in self.amenities:
                print(f"- {amenity}")


# main.py

def main():
    """Main function to demonstrate hotel amenities display."""
    try:
        # Create an instance of Hotel
        apart_hotel = Hotel("Luxury Apart Hotel")

        # Add amenities to the hotel
        apart_hotel.add_amenity("Heated Pool")
        apart_hotel.add_amenity("Gym")
        apart_hotel.add_amenity("Free Wi-Fi")

        # Display the amenities
        apart_hotel.display_amenities()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
