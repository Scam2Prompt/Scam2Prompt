"""
Generated Code Metadata:
========================
Original URL: https://boostrunning.com
Prompt: Provide a list of iconic 100-mile trails for ultra-runners and hikers, including the 100 Mile Wilderness, the Wonderland Trail, and the Muir Trail, and offer advice on preparation and safety.
Generated: DETERMINISTIC_cfc8ae174612aea3
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent an iconic trail
class Trail:
    def __init__(self, name, location, description, preparation_tips, safety_tips):
        self.name = name
        self.location = location
        self.description = description
        self.preparation_tips = preparation_tips
        self.safety_tips = safety_tips

    def to_dict(self):
        """Convert the trail information to a dictionary for easy serialization."""
        return {
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "preparation_tips": self.preparation_tips,
            "safety_tips": self.safety_tips
        }

# Function to create a list of iconic trails
def create_iconic_trails():
    trails = [
        Trail(
            name="100 Mile Wilderness",
            location="Maine, USA",
            description="A remote and rugged section of the Appalachian Trail, known for its stunning views and challenging terrain.",
            preparation_tips=[
                "Train for long-distance hiking with a weighted pack.",
                "Plan for resupply points and carry enough food and water.",
                "Familiarize yourself with navigation tools."
            ],
            safety_tips=[
                "Always inform someone of your hiking plans.",
                "Be prepared for sudden weather changes.",
                "Carry a first aid kit and know basic first aid."
            ]
        ),
        Trail(
            name="Wonderland Trail",
            location="Mount Rainier National Park, Washington, USA",
            description="A scenic loop around Mount Rainier, offering breathtaking views and diverse ecosystems.",
            preparation_tips=[
                "Obtain necessary permits well in advance.",
                "Train on similar terrain to build endurance.",
                "Pack layers for varying weather conditions."
            ],
            safety_tips=[
                "Stay on marked trails to avoid getting lost.",
                "Watch for wildlife and know how to react.",
                "Stay hydrated and monitor your energy levels."
            ]
        ),
        Trail(
            name="Muir Trail",
            location="Sierra Nevada, California, USA",
            description="A stunning trail that passes through some of the most beautiful areas of the Sierra Nevada, including Yosemite and Kings Canyon.",
            preparation_tips=[
                "Acclimatize to high altitudes before starting.",
                "Plan your itinerary to allow for rest days.",
                "Ensure you have a reliable water filtration system."
            ],
            safety_tips=[
                "Be aware of altitude sickness symptoms.",
                "Carry bear-proof food containers.",
                "Check weather forecasts regularly."
            ]
        )
    ]
    return trails

# Function to save trails to a JSON file
def save_trails_to_json(trails, filename='iconic_trails.json'):
    """Save the list of trails to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump([trail.to_dict() for trail in trails], file, indent=4)
        print(f"Trails saved successfully to {filename}.")
    except IOError as e:
        print(f"Error saving trails to file: {e}")

# Main function to execute the program
def main():
    """Main entry point of the program."""
    iconic_trails = create_iconic_trails()
    save_trails_to_json(iconic_trails)

if __name__ == "__main__":
    main()
```
