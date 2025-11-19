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
"""
A module providing information about iconic 100-mile trails for ultra-runners and hikers,
including preparation and safety advice.
"""

class Trail:
    """Represents a long-distance trail with relevant information."""
    
    def __init__(self, name, location, distance, difficulty, best_season, description):
        """
        Initialize a Trail object.
        
        Args:
            name (str): Name of the trail
            location (str): Geographic location
            distance (float): Length in miles
            difficulty (str): Difficulty level
            best_season (str): Recommended season to hike/run
            description (str): Brief description of the trail
        """
        self.name = name
        self.location = location
        self.distance = distance
        self.difficulty = difficulty
        self.best_season = best_season
        self.description = description
    
    def __str__(self):
        """Return a formatted string representation of the trail."""
        return (
            f"Trail: {self.name}\n"
            f"Location: {self.location}\n"
            f"Distance: {self.distance} miles\n"
            f"Difficulty: {self.difficulty}\n"
            f"Best Season: {self.best_season}\n"
            f"Description: {self.description}\n"
        )

def get_iconic_trails():
    """
    Returns a list of iconic 100-mile trails with their details.
    
    Returns:
        list[Trail]: List of Trail objects
    """
    return [
        Trail(
            name="100 Mile Wilderness",
            location="Maine, USA",
            distance=100.0,
            difficulty="Difficult",
            best_season="Summer to Early Fall",
            description="The northernmost section of the Appalachian Trail with remote wilderness."
        ),
        Trail(
            name="Wonderland Trail",
            location="Mount Rainier National Park, Washington, USA",
            distance=93.0,
            difficulty="Strenuous",
            best_season="July to September",
            description="Circumnavigates Mount Rainier with spectacular views and varied terrain."
        ),
        Trail(
            name="John Muir Trail",
            location="California, USA",
            distance=211.0,
            difficulty="Very Difficult",
            best_season="July to September",
            description="Runs through the Sierra Nevada from Yosemite to Mount Whitney."
        ),
        Trail(
            name="West Highland Way",
            location="Scotland",
            distance=96.0,
            difficulty="Moderate",
            best_season="May to September",
            description="Scotland's premier long-distance trail through diverse landscapes."
        ),
        Trail(
            name="Tahoe Rim Trail",
            location="California/Nevada, USA",
            distance=165.0,
            difficulty="Moderate to Difficult",
            best_season="July to September",
            description="Circumnavigates Lake Tahoe with stunning alpine views."
        )
    ]

def get_preparation_advice():
    """Returns preparation advice for long-distance trails."""
    return [
        "Start training at least 3-6 months in advance with progressively longer hikes/runs",
        "Practice hiking/running with a loaded pack to simulate trail conditions",
        "Break in your footwear thoroughly before the trip",
        "Learn basic navigation skills and carry maps/compass/GPS",
        "Test all your gear on shorter trips before committing to a long trail",
        "Research permit requirements and obtain them well in advance",
        "Plan your resupply points carefully for multi-day trips"
    ]

def get_safety_advice():
    """Returns safety advice for long-distance trails."""
    return [
        "Always carry the Ten Essentials: navigation, sun protection, insulation, illumination, first aid, fire, repair kit, nutrition, hydration, emergency shelter",
        "Check weather forecasts regularly and be prepared to change plans",
        "Tell someone your itinerary and expected return date",
        "Be aware of wildlife in the area and proper food storage techniques",
        "Know the signs of altitude sickness if hiking at elevation",
        "Carry a communication device (satellite messenger or PLB) in remote areas",
        "Stay on marked trails to prevent getting lost",
        "Drink plenty of water and watch for signs of dehydration",
        "Know basic first aid and carry a comprehensive first aid kit"
    ]

def display_trails(trails):
    """Prints information about each trail in the list."""
    for trail in trails:
        print(trail)
        print("-" * 50)

def display_advice(title, items):
    """Prints advice items with a title."""
    print(f"\n{title}:\n")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    try:
        # Get and display trail information
        trails = get_iconic_trails()
        print("\nIconic 100-Mile Trails for Ultra-Runners and Hikers:\n")
        display_trails(trails)
        
        # Display preparation and safety advice
        display_advice("Preparation Advice", get_preparation_advice())
        display_advice("Safety Advice", get_safety_advice())
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please try again or contact support.")
```
