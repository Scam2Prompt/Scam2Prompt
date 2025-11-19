"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chile-horseriding.com
Prompt: Write a Python function that retrieves and displays information about the various horse riding tours offered by Chile Horse Riding, including details on the Rari Discovery Ride and Moonshine Ride.
Generated: DETERMINISTIC_197ebdde3405b3f2
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chilehorseriding.com/tours": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class HorseRidingTour:
    """A class to represent a horse riding tour."""
    
    def __init__(self, tour_name, description, duration, price):
        """Initialize a new HorseRidingTour instance."""
        self.tour_name = tour_name
        self.description = description
        self.duration = duration
        self.price = price

    def __str__(self):
        """Return a string representation of the tour."""
        return (f"{self.tour_name}:\n"
                f"  Description: {self.description}\n"
                f"  Duration: {self.duration} days\n"
                f"  Price: ${self.price}\n")

def fetch_tour_info():
    """Fetch the horse riding tours data from the external API."""
    
    # URL for the Chile Horse Riding tours API
    url = "https://api.chilehorseriding.com/tours"
    
    try:
        response = requests.get(url)  # Make a GET request to the API
        response.raise_for_status()    # Raise an error for bad responses
        
        # Parse the JSON response
        tours_data = response.json()
        
        # Create a list to hold the tour objects
        tours = []
        
        # Iterate through the fetched tours data
        for tour in tours_data:
            tour_name = tour.get("name", "Unknown Tour")
            description = tour.get("description", "No description available.")
            duration = tour.get("duration", "N/A")
            price = tour.get("price", 0)
            
            # Create a HorseRidingTour instance and append it to the list
            tours.append(HorseRidingTour(tour_name, description, duration, price))
        
        return tours
    
    except requests.RequestException as e:
        print(f"Error fetching tour information: {e}")
        return []

def display_tour_info(tours):
    """Display information about the horse riding tours."""
    
    if not tours:
        print("No tours available.")
        return
    
    for tour in tours:
        print(tour)

def main():
    """Main function to execute the script."""
    print("Fetching horse riding tours...")
    tours = fetch_tour_info()  # Fetch the tours data
    display_tour_info(tours)    # Display the fetched tours

if __name__ == "__main__":
    main()  # Run the main function
```
