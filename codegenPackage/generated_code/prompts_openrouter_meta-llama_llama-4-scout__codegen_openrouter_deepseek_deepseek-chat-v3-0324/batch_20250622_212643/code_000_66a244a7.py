"""
Generated Code Metadata:
========================
Original URL: https://anywhere-adventure.com
Prompt: "Generate a Python script to create a customized itinerary for a 9-day Kenyan safari trip, including destinations like Amboseli, Masai Mara, Naivasha, and Nakuru."
Generated: DETERMINISTIC_66a244a7b784871c
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class SafariItineraryGenerator:
    """
    A class to generate a customized itinerary for a Kenyan safari trip.
    """
    
    def __init__(self, start_date, traveler_name, group_size):
        """
        Initialize the itinerary generator with trip details.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            traveler_name (str): Name of the traveler/group
            group_size (int): Number of people in the group
        """
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.traveler_name = traveler_name
        self.group_size = group_size
        self.destinations = {
            "Amboseli": {
                "description": "Famous for its large elephant herds and views of Mount Kilimanjaro",
                "activities": ["Game drives", "Bird watching", "Cultural visits"],
                "recommended_days": 2
            },
            "Masai Mara": {
                "description": "Known for the Great Migration and abundant wildlife",
                "activities": ["Game drives", "Hot air balloon safari", "Maasai village visit"],
                "recommended_days": 3
            },
            "Naivasha": {
                "description": "Freshwater lake with hippos and diverse birdlife",
                "activities": ["Boat ride", "Walking safari", "Cycling"],
                "recommended_days": 2
            },
            "Nakuru": {
                "description": "Home to flamingos and rhino sanctuary",
                "activities": ["Game drives", "Bird watching", "Nature walks"],
                "recommended_days": 2
            }
        }
    
    def validate_inputs(self):
        """
        Validate the inputs provided during initialization.
        
        Raises:
            ValueError: If any input is invalid
        """
        if not isinstance(self.traveler_name, str) or not self.traveler_name.strip():
            raise ValueError("Traveler name must be a non-empty string")
        
        if not isinstance(self.group_size, int) or self.group_size <= 0:
            raise ValueError("Group size must be a positive integer")
        
        if self.start_date < datetime.now():
            raise ValueError("Start date must be in the future")
    
    def generate_itinerary(self):
        """
        Generate the 9-day safari itinerary.
        
        Returns:
            dict: Complete itinerary with day-by-day details
        """
        self.validate_inputs()
        
        itinerary = {
            "traveler_name": self.traveler_name,
            "group_size": self.group_size,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "total_days": 9,
            "days": []
        }
        
        current_date = self.start_date
        days_remaining = 9
        
        # Amboseli (2 days)
        if days_remaining >= 2:
            itinerary["days"].extend(self._generate_destination_days("Amboseli", current_date, 2))
            current_date += timedelta(days=2)
            days_remaining -= 2
        
        # Masai Mara (3 days)
        if days_remaining >= 3:
            itinerary["days"].extend(self._generate_destination_days("Masai Mara", current_date, 3))
            current_date += timedelta(days=3)
            days_remaining -= 3
        
        # Naivasha (2 days)
        if days_remaining >= 2:
            itinerary["days"].extend(self._generate_destination_days("Naivasha", current_date, 2))
            current_date += timedelta(days=2)
            days_remaining -= 2
        
        # Nakuru (2 days)
        if days_remaining >= 2:
            itinerary["days"].extend(self._generate_destination_days("Nakuru", current_date, 2))
        
        return itinerary
    
    def _generate_destination_days(self, destination, start_date, num_days):
        """
        Generate day entries for a specific destination.
        
        Args:
            destination (str): Name of the destination
            start_date (datetime): First day at this destination
            num_days (int): Number of days to spend here
            
        Returns:
            list: List of day entries for the destination
        """
        days = []
        dest_info = self.destinations[destination]
        
        for day in range(num_days):
            current_date = start_date + timedelta(days=day)
            day_entry = {
                "day_number": day + 1,
                "date": current_date.strftime("%Y-%m-%d"),
                "destination": destination,
                "description": dest_info["description"],
                "activities": dest_info["activities"],
                "accommodation": f"Lodge in {destination}",
                "meals": ["Breakfast", "Lunch", "Dinner"]
            }
            days.append(day_entry)
        
        return days
    
    def save_itinerary(self, itinerary, filename):
        """
        Save the itinerary to a JSON file.
        
        Args:
            itinerary (dict): Itinerary to save
            filename (str): Name of the output file
        """
        try:
            with open(filename, 'w') as f:
                json.dump(itinerary, f, indent=4)
        except IOError as e:
            print(f"Error saving itinerary: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

def main():
    try:
        # Get user input
        traveler_name = input("Enter traveler/group name: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        group_size = int(input("Enter group size: "))
        
        # Generate itinerary
        generator = SafariItineraryGenerator(start_date, traveler_name, group_size)
        itinerary = generator.generate_itinerary()
        
        # Save to file
        filename = f"{traveler_name.replace(' ', '_')}_safari_itinerary.json"
        generator.save_itinerary(itinerary, filename)
        
        print(f"\nSuccessfully generated itinerary for {traveler_name}!")
        print(f"Saved to {filename}")
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
