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
# iconic_trails.py

class IconicTrail:
    """Represents an iconic 100-mile trail for ultra-runners and hikers."""

    def __init__(self, name, distance, elevation_gain, location):
        """
        Initializes an IconicTrail object.

        Args:
            name (str): The name of the trail.
            distance (int): The distance of the trail in miles.
            elevation_gain (int): The elevation gain of the trail in feet.
            location (str): The location of the trail.
        """
        self.name = name
        self.distance = distance
        self.elevation_gain = elevation_gain
        self.location = location

    def __str__(self):
        return f"{self.name} - {self.distance} miles, {self.elevation_gain} ft elevation gain, {self.location}"


class TrailGuide:
    """Provides information and advice on iconic 100-mile trails."""

    def __init__(self):
        self.trails = []

    def add_trail(self, trail):
        """
        Adds an iconic trail to the guide.

        Args:
            trail (IconicTrail): The trail to add.
        """
        self.trails.append(trail)

    def get_trails(self):
        """
        Returns a list of iconic trails.

        Returns:
            list[IconicTrail]: A list of iconic trails.
        """
        return self.trails

    def provide_preparation_advice(self):
        """
        Provides general advice on preparation and safety for ultra-runners and hikers.

        Returns:
            str: Advice on preparation and safety.
        """
        advice = (
            "To prepare for an iconic 100-mile trail, make sure to:\n"
            "- Train regularly and build up your endurance\n"
            "- Pack essential gear, including food, water, and a first aid kit\n"
            "- Check the weather forecast and trail conditions before heading out\n"
            "- Let someone know your itinerary and expected return time\n"
            "- Bring a map and compass or GPS device\n"
            "- Be prepared for emergencies and know basic first aid\n"
        )
        return advice


def main():
    try:
        guide = TrailGuide()

        # Add iconic trails
        wilderness_trail = IconicTrail(
            "100 Mile Wilderness",
            100,
            13100,
            "Maine, USA",
        )
        wonderland_trail = IconicTrail(
            "Wonderland Trail",
            93,
            13000,
            "Washington, USA",
        )
        muir_trail = IconicTrail(
            "John Muir Trail",
            211,
            22000,
            "California, USA",
        )

        guide.add_trail(wilderness_trail)
        guide.add_trail(wonderland_trail)
        guide.add_trail(muir_trail)

        # Print iconic trails
        print("Iconic 100-Mile Trails:")
        for i, trail in enumerate(guide.get_trails()):
            print(f"{i+1}. {trail}")

        # Provide preparation advice
        print("\nPreparation and Safety Advice:")
        print(guide.provide_preparation_advice())

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
